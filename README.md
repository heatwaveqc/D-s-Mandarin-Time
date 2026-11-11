# D's Mandarin Time

A grammar-first Mandarin learning wiki, built with [TiddlyWiki](https://tiddlywiki.com/).

**Architecture:** separately stored, UTF-8 TiddlyWiki `.tid` files; GitHub Actions builds a self-contained static `index.html` and publishes it to GitHub Pages. No server or local Node.js installation is required to *read* the site.

This repository is intentionally independent of GATES, while following the same modular tiddler approach. Its standalone CSS theme adapts GATES Kung Fu's oxblood/parchment palette, KaiTi-like typography, dividers, and compact reference-list styling. GATES' privately hosted border images have not been copied.

## Browsing and deployment

- Once GitHub Pages is configured to use **GitHub Actions**, browse `https://heatwaveqc.github.io/D-s-Mandarin-Time/`.
- The wiki is browser-only and **read-only as a canonical source**: browser edits won't be saved back to this repository.
- Each push to `main` checks content integrity and rebuilds the static site. Before Pages is enabled, the workflow uploads the compiled `index.html` as a downloadable Actions artifact. After Pages is enabled, the same workflow publishes the site.
- To build locally (optional): `npx --yes tiddlywiki@5.4.1 . --build index` (output `public/index.html`).

## Lexical curriculum target

The approved target is a **7,000-entry general Mandarin lexicon** (2,000 fundamental, 3,000 high-use, 2,000 high-availability) **plus 1,000–2,000 additional wuxia/xianxia entries**. The 95–98% lexical token coverage goal is to be **measured** separately for conversation, general written Mandarin and genre material; no single vocabulary count guarantees that coverage.

See [Target Vocabulary Standard](docs/VOCABULARY_TARGET_STANDARD.md) and [Candidate Source Survey](docs/VOCABULARY_SOURCE_SURVEY.md). Use mixed-register frequency evidence, SUBTLEX-CH, the 2025 HSK syllabus, and native high-availability/genre validation. Do not import entire proprietary dictionaries or novel texts into this public repository.

## Content model

- `tiddlers/Navigation`: front page, indexes, course map, study instructions.
- `tiddlers/Grammar`: independently linked grammatical concepts and prerequisites.
- `tiddlers/Vocabulary`: independently stored word-level entries with hanzi, pinyin, POS, gloss, usage, and examples; lesson membership is optional.
- `tiddlers/Characters`: character-level semantic/phonetic decomposition with an etymology-confidence note.
- `tiddlers/Lessons`: reusable lesson assemblies, learning objectives, dependencies.
- `tiddlers/Readings`: controlled reading passages with pinyin and gloss.
- `tiddlers/Exercises`: written assessments and answer keys.
- `tiddlers/System`: wiki title, default tab, helper templates.

All *course* records use `mandarin-kind` and `mandarin-level`. Published vocabulary requires a stable `mandarin-lexeme-id`, `mandarin-hanzi`, `mandarin-pinyin`, `mandarin-gloss`, and `mandarin-pos`; the candidate survey and provenance/frequency/HSK evidence are maintained in the **separate research layer**, not in vocabulary tiddlers. Every existing entry has been backfilled with a unique opaque ID; IDs are allocated by the [Lexical Data Contract](docs/LEXICAL_DATA_CONTRACT.md), not by spelling, POS or lesson. Grammar and lessons can specify `mandarin-prerequisites` as a TiddlyWiki title list, e.g. `[[Grammar/SVO Word Order]] [[Grammar/Predicate Negation]]`. Field names use the `mandarin-` prefix to avoid conflicts with TiddlyWiki internals.

Use real grammatical descriptions, give pinyin on all new Chinese example sentences, and avoid presenting character-component mnemonics as guaranteed etymologies.

Vocabulary exists independently of lesson planning. Omit `mandarin-lessons` on unassigned entries; use `mandarin-lessons: L01 L03` only when a word is assigned to one or more existing lesson-vocabulary indexes. All words remain searchable, while lesson-scoped pages show only assigned words instead of rendering 7,000 entries at once. A short human-recorded, credited Mandarin audio sample is included as an asset-publishing pilot; see `docs/AUDIO_ASSETS.md`.

The wiki holds shared course material. **Do not commit sensitive personal speech recordings, private student data, or individually identifying assessment results to this public repository.** Learner progress can be maintained locally or in an access-controlled Drive sheet.

## Adding material

1. Add one `.tid` file under the appropriate content directory with a unique `title`, `type: text/vnd.tiddlywiki`, `tags`, and canonical metadata.
2. Link using tiddler titles; prefer linking to concepts rather than copying their explanations.
3. Run `python3 scripts/validate_wiki.py` and (optionally) the TiddlyWiki build.
4. Commit to `main`; deployment runs automatically when Pages is enabled.

See [[Wiki Guide]] in the published site for the browsing workflow and links among content types.

Vocabulary research is now **survey first, prune and freeze the selected lexicon, then publish entries**. See [Survey-first Lexicon Standard](docs/LEXICON_SURVEY_STANDARD.md), [Lexical Data Contract](docs/LEXICAL_DATA_CONTRACT.md), and [Work handoff](docs/WORK_POPULATION_GUIDE.md). Research-selected words can hold planned IDs without any wiki pages. Work leaves import PRs in draft for independent editorial review; no mass production is authorized yet.
