# Writing YouTube Narratives

A portable Agent Skills package for creating narrative voiceover scripts for:

- long-form YouTube videos, especially around 10 minutes;
- short-form videos under 60 seconds;
- angle generation, beat maps, hooks, rewrites, critiques, and format adaptations.

The package follows progressive disclosure: `SKILL.md` contains the operating workflow, while format-specific structures, examples, voice guidance, and validation live in separate files.

## Package structure

```text
writing-youtube-narratives/
├── SKILL.md
├── README.md
├── references/
│   ├── examples.md
│   ├── long-form.md
│   ├── quality-rubric.md
│   ├── short-form.md
│   ├── story-engines.md
│   └── voice-and-style.md
├── templates/
│   └── channel-profile.md
├── scripts/
│   └── check_script.py
└── evals/
    └── evals.json
```

## Installation

Place the entire directory in the skills location supported by the target Agent Skills-compatible runtime. Keep the directory name and relative paths intact.

## Typical requests

```text
Use writing-youtube-narratives. Give me five differentiated 10-minute video angles about [topic], then stop.
```

```text
Use writing-youtube-narratives. Write a 10-minute investigative voiceover from these sources. The audience is [audience], the tone is [tone], and the payoff should be [endpoint].
```

```text
Use writing-youtube-narratives. Write a 50-second Short about [topic]. One idea, one turn, one payoff. Voiceover only.
```

```text
Use writing-youtube-narratives. Diagnose why this opening loses attention, then rewrite only the first 45 seconds without changing the facts.
```

```text
Use writing-youtube-narratives. Adapt this long-form script into three Shorts, each built around a different self-contained moment rather than a summary.
```

## Timing validator

The included script extracts the `Voiceover` section of a Markdown draft, counts spoken words, estimates duration, and flags several generic opener patterns.

```bash
python scripts/check_script.py draft.md --target-seconds 600 --wpm 145
```

Use `--strict` to return a non-zero exit code when timing falls outside the default 8% tolerance or a flagged generic phrase appears in the opening.

Word-count timing is an estimate. A performed or synthesized timed read remains the final check.

## Customization

Create a persistent channel profile from `templates/channel-profile.md`. Keep it concise and evidence-based. Derive transferable traits from sample scripts; do not copy creator-specific phrases or recurring bits.

The default skill deliberately avoids prescribing a universal genre voice. Tone, humor, pacing, and evidence standards should come from the request or channel profile.
