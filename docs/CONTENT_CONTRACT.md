# Mandarin content contract (v1.2)

## General structure

This is a **public, static** TiddlyWiki. `.tid` text files are the canonical source. Do not store private learner records in it. GitHub Actions compiles the file set into one browsable `index.html`; editing in the browser will not create a Git commit.

The content is organized by **kind**, not by rigid lesson order. The course order is a *view* over interconnected concepts.

| Kind | Responsibility | Required fields |
| --- | --- | --- |
| `navigation` | Indexes, home and reference guides | `title`, `mandarin-kind`, `mandarin-level` |
| `grammar` | A single reusable grammatical concept | common fields; `mandarin-prerequisites` where appropriate |
| `vocabulary` | Learner-facing lexical item | `mandarin-lexeme-id`, `mandarin-hanzi`, `mandarin-pinyin`, `mandarin-gloss`, `mandarin-pos` |
| `character` | Individual graph and its composition | `mandarin-hanzi`, `mandarin-pinyin`, `mandarin-gloss` |
| `lesson` | Objectives, guided explanations and tasks | `mandarin-summary`, `mandarin-prerequisites` |
| `reading` | Text with hideable pronunciation/meaning | prerequisites, controls on introduced vocabulary |
| `exercise` | Challenge + key or rubric | prerequisites |
| `roadmap` | Program-level map (future) | common fields |

All regular content records need `tags`, `type: text/vnd.tiddlywiki`, `mandarin-kind` and `mandarin-level`.

## Curriculum lexical standard

The binding [vocabulary target standard](VOCABULARY_TARGET_STANDARD.md) is **2k fundamental + 3k high-use + 2k high-availability (7k general), plus 1k–2k genuinely additional wuxia/xianxia lexical entries**. The 95–98% token-coverage target is a separately measured objective for spoken Mandarin, general writing and genre fiction, never a guarantee from word count.

**Selection is now a distinct research stage before vocabulary publication.** Follow [Survey-first Lexicon Standard](LEXICON_SURVEY_STANDARD.md). Overcomplete candidates are adjudicated/pruned into an accepted roster; accepted items may have a permanent ID with registry status `planned` and **no corresponding .tid file**. Published wiki entries use status `active` and their stable ID. Keep the source/provenance ledger, frequency rankings, HSK crosswalks, review status and lexical selection bands outside the tiddlers. Original content is required; preserve any licensing/attribution obligations for actually adapted or redistributed material.

See [Lexical Data Contract](LEXICAL_DATA_CONTRACT.md) and [Work Population Guide](WORK_POPULATION_GUIDE.md). The validation system checks both research registry integrity and wiki content without forcing research candidates into lessons or pages.

## Dependencies

**Vocabulary is a standalone lexicon, independent of lesson sequencing.** `mandarin-lessons` is optional and may be omitted for unassigned words. When a word is deliberately introduced or reviewed in lessons, assign `mandarin-lessons: L01 L03`; every specified ID must have an existing `Lesson Vocabulary/LNN` index. The validator checks supplied IDs but does not require any. Do not invent lessons merely to make vocabulary records valid. A word can be introduced or revisited in multiple lessons without duplicating its lexical record.

The vocabulary index and sidebar search can reach entries regardless of lesson membership. Lesson pages may use bounded `contains:mandarin-lessons[Lxx]` filters, which intentionally exclude unassigned words. Do not put the full target vocabulary in a single tiddler or an unbounded auto-rendered list.

Audio fields are `mandarin-audio`, `mandarin-audio-status`, and `mandarin-audio-license`. See `docs/AUDIO_ASSETS.md`; the first sample is a credited human recording, not neural TTS.

In `mandarin-prerequisites`, use **exact** existing tiddler titles in TiddlyWiki list notation:

```
mandarin-prerequisites: [[Grammar/SVO Word Order]] [[Grammar/Classifiers]]
```

Treat this as a *hard prerequisite*, not an optional topical link. Content may link to other material without declaring a prerequisite. The validator rejects missing prerequisite targets, self-dependencies, cycles, duplicate titles, broken ordinary wiki links and missing vocabulary metadata.

This is currently a **conceptual progression**, not an automatic per-learner gate. Future dashboards may overlay learner-specific mastery scores from a private source without committing those scores publicly.

## Language policy

- Use simplified Chinese and **tone-marked Hanyu Pinyin** for every new Chinese phrase and sentence.
- If a token has neutral tone, show its Pinyin without a tone mark.
- Distinguish phonemic tone from sandhi realizations, and mark notable sandhi (e.g. `yì běn` for 一本).
- Distinguish grammatical aspect from tense. Avoid “了 is the past tense.”
- Character pages should separately describe semantic components, phonetic clues, and known historical simplifications; don't invent graphical etymologies.
- Include at least one contextualized example for each vocabulary entry. Where possible, reuse known vocabulary before introducing new words.
- Mark deliberately limited / constructed readings as pedagogical rather than natural literary excerpts.
- Track frequency / HSK alignment only with a cited reference and reliable edition; the pilot makes no frequency claims.

## Planned additions

1. Audio clips / blind listening cards with playback testing.
2. Mastery taxonomy: recognition, meaning recall, pronunciation, production, listening and transfer.
3. Grammar index by typological features, plus explicit lesson unlocks.
4. Stable per-lexeme IDs and registry validation are implemented; homograph and sense adjudication remain an ongoing content responsibility.
5. More accurate reading-level statistics and graded literary corpus.

## Publishing

`python3 scripts/validate_wiki.py` validates metadata, lexical identity, source registry and evidence consistency. The PR workflow also checks the registry against `main` to prevent reassignment of previously allocated IDs. `tiddlywiki . --build index` builds `public/index.html`, using TiddlyWiki 5.4.1. GitHub Actions always validates, builds, and uploads a portable HTML artifact. If Pages is enabled it also uploads the Pages artifact and deploys. Set Pages to **GitHub Actions** under repository settings, then re-run or dispatch the workflow. No persistent Node service is needed.

For large vocabulary imports and scope-limited progress reporting, see `docs/WORK_POPULATION_GUIDE.md`.
