# AI Tells: The Full Catalogue

Compiled from Wikipedia's "Signs of AI writing" (WikiProject AI Cleanup), the StoryScope study (Russell et al., 2026), and observed LLM defaults. Ordered by importance: structural tells are the hardest to fix and the strongest signal; vocabulary is the weakest signal and the easiest to fix. A de-slopped word list on top of AI structure still reads as AI.

None of these is proof by itself. Humans use em dashes and triads. The pattern is density: several tells co-occurring, consistently, regardless of topic.

## Tier 1: Structural tells (fix these first)

**Over-explaining the point.** AI states a fact, then explains what the fact means, then explains why that matters. In the StoryScope data, AI narrators explicitly state the theme 77% of the time vs 52% for humans. In nonfiction this appears as: the analysis sentence after every data point, the "this matters because" paragraph, the recap before the reader could possibly have forgotten. Fix: state the fact and move on. If significance isn't obvious, the evidence is weak; improve the evidence, not the explanation.

**Sanding specifics into generics (regression to the mean).** AI replaces rare, specific, checkable facts with statistically safe generic statements. "The Statistical Institute of Catalonia was officially established in 1989" becomes "has long played a vital role in the region's data landscape." Any sentence that could be pasted into an article about a different subject is this tell. Fix: restore names, numbers, dates, places, versions.

**Fake balance / no verdict.** Equal weight to every consideration, "both approaches have merits," no conclusion the author owns. Humans present morally and practically ambivalent material but still commit (StoryScope: humans favor ambiguity in material, not in judgment). Fix: pick a side, scope it ("for teams under ten people, X wins"), keep the honest caveat.

**Tidy symmetric structure.** Sections of equal length, everything resolved, an intro that previews all sections and a conclusion that repeats them, a "Challenges" section that begins "Despite..." and ends optimistic. Human structure is asymmetric: sized by importance, comfortable leaving minor threads open. Fix: cut the preview/recap scaffolding; let the important section be long.

**The essay template.** Hook question ("Have you ever wondered...?"), definition of the obvious, three body sections, summary conclusion beginning "In summary" / "In conclusion" / "Overall." Fix: open inside the problem; end on an implication, decision, or sharpened claim.

**Repeating the point under different headings.** Same idea restated with new topic sentences. Fix: merge or cut; each section must advance the argument.

**Headings that label topics instead of advancing arguments.** "Benefits of X" / "Considerations" / "Conclusion." Fix: headings that carry a claim or at least a specific noun ("Why the cache invalidation bug survived three audits").

**No outside world.** AI avoids naming real brands, texts, people, and events; humans reference specific named sources at nearly double the AI rate (47% vs 24%) and address the reader directly far more often (28% vs 7%). Fix: cite the actual paper, name the actual competitor, link the actual doc.

## Tier 2: Sentence-pattern tells

**Negative parallelism ("not X, but Y").** "It's not just a tool; it's a paradigm shift." Also the multi-sentence version and the inverted version. One of the most reliable single tells. Fix: state Y directly. If the contrast genuinely matters, earn it with evidence, not the formula.

**Rule-of-three filler.** "Innovative, scalable, and robust." "Politicians, citizens, and stakeholders." Triads deployed to make thin analysis look comprehensive. Test: remove the triad. If nothing is lost, it was filler. Sometimes the true count is two, or four, or one.

**Superficial -ing analysis clauses.** Facts trailed by a present-participle interpretation: "...highlighting the company's commitment to innovation," "...underscoring the need for reform," "...reflecting broader trends." Adds fictional opinion, states no fact. Fix: end the sentence at the fact.

**Puffery / importance inflation.** "Stands as a testament to," "plays a vital role in," "rich cultural heritage," "solidified its position as," "marked a significant milestone." Fix: state what the thing did; let the reader rank its importance.

**Weasel attribution.** "Has been described as," "experts believe," "is widely regarded as": opinions assigned to a vague authority, often supported by zero or one source. Fix: name who said it, or own the claim yourself.

**Editorializing interjections.** "It's important to note," "It is worth remembering," "Notably," "Crucially," "No discussion would be complete without." The machine announcing what matters. Fix: delete the frame; if it matters, its position and evidence show that.

**False ranges.** "From intimate gatherings to global movements," "from beginners to seasoned professionals": spectrum syntax with no actual spectrum. Fix: name the actual cases.

**Formulaic transition rotation.** Moreover / Furthermore / Additionally / In addition, cycled at paragraph heads, making text feel assembled. Fix: most paragraphs need no transition word; logical sequence does the work. When needed, use plain ones (But, So, And, Still).

**Hedge stacking.** Might, could, perhaps, generally, somewhat, often, in many cases, several per paragraph, blurring every claim. Fix: one calibrated hedge where uncertainty is real; delete the rest.

**Uniform sentence rhythm.** Every sentence 15–25 words, subject-verb-object, medium clauses. Reads smooth and dead. Fix: vary hard. Fragments allowed. One long sentence that earns its length, then a short one.

## Tier 3: Lexical and formatting tells

**Em dashes.** LLMs use them more often than nonprofessional human writing, in formulaic punchy-emphasis positions where a comma, colon, or parentheses fit better. This skill's default: zero em dashes.

**Slop vocabulary.** Words that spiked in post-2022 text and co-occur in clusters: delve, tapestry, leverage, unlock, unleash, seamless, robust, pivotal, intricate, crucial, foster, harness, elevate, navigate/navigating, landscape, realm, testament, underscore, boast, vibrant, dynamic, comprehensive, holistic, game-changer, cutting-edge, groundbreaking, revolutionize, transformative, ever-evolving, in today's fast-paced world, dive deep, embark, journey (metaphorical), elucidate, shed light, glimpse into, remains to be seen. One instance is fine in a human draft; clusters are the tell. Prefer the plain word: use, build, improve, important, complex, big.

**Filler intensifiers and softeners.** very, really, literally, actually, certainly, basically, just (as minimizer). Almost always deletable.

**Formatting overkill.** Bolded key terms scattered through prose, bullet lists where prose would argue better, Title Case Headings, emoji section markers, a heading for every 100 words. Fix: sentence case headings, bold reserved for UI labels or true warnings, bullets only for list-shaped content.

**Chatbot artifacts.** "As an AI," "I hope this helps," "Certainly!", stray markdown asterisks in plain-text contexts, "Sources:" blocks with broken or invented links, curly-quote/straight-quote inconsistency from pasted output.

**Summary endings.** Final paragraph beginning "In summary," "In conclusion," "Ultimately," "Overall," restating the piece. Also the closing platitude: "Only time will tell," "The future looks bright," "one thing is certain."

## The de-slop pass, in order

1. Read the piece once asking only: what does it claim, and where? Fix Tier 1 problems structurally. This usually means deleting explanation paragraphs, merging sections, and restoring specifics. Expect to cut 15–30%.
2. Sweep for Tier 2 patterns. Rewrite sentences, don't decorate them: the fix for "not just X but Y" is a different sentence, not a synonym swap.
3. Sweep Tier 3 mechanically: em dashes, slop words, intensifiers, formatting.
4. Read aloud (mentally) for rhythm. Break up any run of three same-shaped sentences.
5. Verify nothing generic survived: any sentence transplantable to another topic gets specified or cut.

## Calibration warnings

- Don't over-correct into a new uniformity. A text with zero hedges, zero transitions, and all six-word sentences is its own robot voice. The goal is variance and intent, not a different set of rules mechanically applied.
- Preserve deliberate choices. If the author repeats a word for effect, keeps an ambiguity on purpose, or uses a triad that's genuinely three things, leave it. Catch unchosen defaults, not chosen style.
- Humans influenced by LLMs increasingly write with some of these patterns. When critiquing someone's text, flag patterns as "reads as AI" risks, not accusations.