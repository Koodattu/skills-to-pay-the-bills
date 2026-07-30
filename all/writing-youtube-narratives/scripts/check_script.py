#!/usr/bin/env python3
"""Measure a Markdown voiceover draft and flag common script problems.

Examples:
    python scripts/check_script.py draft.md --target-seconds 600 --wpm 145
    python scripts/check_script.py short.md --target-seconds 55 --wpm 155 --strict

The tool prefers text between <!-- VO_START --> and <!-- VO_END --> markers.
Otherwise it extracts the Markdown section headed "Voiceover". If neither exists,
it analyzes the entire file.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

WORD_RE = re.compile(r"[0-9A-Za-zÀ-ÖØ-öø-ÿĀ-ž]+(?:[’'\-][0-9A-Za-zÀ-ÖØ-öø-ÿĀ-ž]+)*", re.UNICODE)
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
TIMECODE_RE = re.compile(
    r"^\s*(?:\[|\()?\d{1,2}:\d{2}(?::\d{2})?\s*(?:[-–—]\s*\d{1,2}:\d{2}(?::\d{2})?)?(?:\]|\))?\s*(?:[-–—|:]\s*.*)?$"
)
LABEL_RE = re.compile(r"^\s*\[(?:hook|cold open|setup|context|beat|payoff|ending|button|pause|section)[^\]]*\]\s*$", re.I)

FLAG_PHRASES = [
    "hey guys",
    "welcome back",
    "in today's video",
    "in todays video",
    "have you ever wondered",
    "stop scrolling",
    "buckle up",
    "what happened next changed everything",
    "little did they know",
    "let that sink in",
    "the answer may surprise you",
    "and the rest is history",
    "but here's the thing",
    "but heres the thing",
]


def extract_voiceover(text: str) -> str:
    marker = re.search(r"<!--\s*VO_START\s*-->(.*?)<!--\s*VO_END\s*-->", text, re.I | re.S)
    if marker:
        return marker.group(1)

    lines = text.splitlines()
    start: int | None = None
    level: int | None = None
    collected: list[str] = []

    for index, line in enumerate(lines):
        match = HEADING_RE.match(line)
        if start is None:
            if match and match.group(2).strip().lower() in {"voiceover", "voice-over", "narration", "script"}:
                start = index + 1
                level = len(match.group(1))
            continue

        if match and len(match.group(1)) <= (level or 6):
            break
        collected.append(line)

    if start is not None:
        return "\n".join(collected)
    return text


def clean_spoken_text(text: str) -> tuple[str, str]:
    spoken_lines: list[str] = []
    first_line = ""
    in_fence = False

    for raw_line in text.splitlines():
        line = raw_line.strip()
        if line.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence or not line:
            continue
        if HEADING_RE.match(line) or TIMECODE_RE.match(line) or LABEL_RE.match(line):
            continue
        if line.startswith(("**Format:**", "**Target duration:**", "**Estimated spoken words:**", "**Viewer promise:**")):
            continue
        line = re.sub(r"^[-*+]\s+", "", line)
        line = re.sub(r"^>\s?", "", line)
        line = re.sub(r"\[(?:\d{1,2}:\d{2}(?::\d{2})?[^\]]*|pause|beat)\]", "", line, flags=re.I).strip()
        if not line:
            continue
        if not first_line:
            first_line = line
        spoken_lines.append(line)

    return "\n".join(spoken_lines), first_line


def sentence_count(text: str) -> int:
    parts = [part for part in re.split(r"(?<=[.!?])\s+|\n+", text) if WORD_RE.search(part)]
    return max(len(parts), 1 if WORD_RE.search(text) else 0)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path, help="Markdown or plain-text script")
    parser.add_argument("--target-seconds", type=float, help="Requested spoken duration")
    parser.add_argument("--wpm", type=float, default=145.0, help="Assumed spoken words per minute (default: 145)")
    parser.add_argument("--tolerance", type=float, default=0.08, help="Allowed duration delta as a fraction (default: 0.08)")
    parser.add_argument("--strict", action="store_true", help="Exit non-zero when timing is outside tolerance or a generic opener is found")
    args = parser.parse_args()

    if not args.path.is_file():
        parser.error(f"File not found: {args.path}")
    if args.wpm <= 0:
        parser.error("--wpm must be greater than zero")
    if args.target_seconds is not None and args.target_seconds <= 0:
        parser.error("--target-seconds must be greater than zero")

    raw = args.path.read_text(encoding="utf-8")
    voiceover = extract_voiceover(raw)
    spoken, first_line = clean_spoken_text(voiceover)
    words = WORD_RE.findall(spoken)
    word_count = len(words)
    sentences = sentence_count(spoken)
    estimated_seconds = (word_count / args.wpm) * 60 if word_count else 0.0
    lower = spoken.lower()
    first_80 = " ".join(words[:80]).lower()

    flags_all = [phrase for phrase in FLAG_PHRASES if phrase in lower]
    flags_opening = [phrase for phrase in FLAG_PHRASES if phrase in first_80]
    question_count = spoken.count("?")
    not_but_count = len(re.findall(r"\b(?:not|isn't|wasn't|aren't|weren't)\b[^.!?\n]{0,90}\bbut\b", lower))

    rounded_seconds = int(round(estimated_seconds))
    estimated_minutes, estimated_remainder = divmod(rounded_seconds, 60)

    result: dict[str, object] = {
        "file": str(args.path),
        "word_count": word_count,
        "sentence_count": sentences,
        "average_words_per_sentence": round(word_count / sentences, 2) if sentences else 0.0,
        "first_spoken_line": first_line,
        "first_line_word_count": len(WORD_RE.findall(first_line)),
        "assumed_wpm": args.wpm,
        "estimated_seconds": round(estimated_seconds, 1),
        "estimated_timestamp": f"{estimated_minutes}:{estimated_remainder:02d}",
        "question_count": question_count,
        "questions_per_100_words": round((question_count / word_count) * 100, 2) if word_count else 0.0,
        "not_x_but_y_like_patterns": not_but_count,
        "flagged_phrases_in_opening": flags_opening,
        "flagged_phrases_anywhere": flags_all,
    }

    timing_pass: bool | None = None
    if args.target_seconds is not None:
        delta_seconds = estimated_seconds - args.target_seconds
        delta_fraction = delta_seconds / args.target_seconds
        timing_pass = abs(delta_fraction) <= args.tolerance
        result.update(
            {
                "target_seconds": args.target_seconds,
                "delta_seconds": round(delta_seconds, 1),
                "delta_percent": round(delta_fraction * 100, 1),
                "timing_tolerance_percent": round(args.tolerance * 100, 1),
                "timing_pass": timing_pass,
            }
        )

    print(json.dumps(result, indent=2, ensure_ascii=False))

    if args.strict and (flags_opening or timing_pass is False):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
