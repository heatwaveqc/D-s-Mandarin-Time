# Work handoff — Mandarin lexical selection and production (v1.3)

Use this contract for ChatGPT Work and equivalent import tasks. **Read [Survey-first Lexicon Standard](LEXICON_SURVEY_STANDARD.md), [Lexical Data Contract](LEXICAL_DATA_CONTRACT.md) and [Vocabulary Target Standard](VOCABULARY_TARGET_STANDARD.md)** before editing the public repository.

## Two separate goals

1. **Choose the library.** Survey deliberately more words than needed; normalize, deduplicate, adjudicate segmentation/Pinyin/senses/register, evaluate evidence and prune to an approved inventory. The target remains 2,000 fundamental + 3,000 high-use + 2,000 high-availability general words plus **1,000–2,000 genuinely additional** wuxia/xianxia words. The current 76 published entries are not proof of final selection. Do not create additional wiki vocabulary pages during survey-only assignments.
2. **Build and teach the library.** After the selection is frozen, produce lexical `.tid` entries in validated batches. Later, assign pedagogically meaningful lesson memberships based on grammar dependencies and contextual material. The selected list, constructed wiki library and course sequencing must remain independent.

A general vocabulary item also useful in wuxia counts once toward general vocabulary. The 95–98% token-coverage objective must be **measured independently** in spontaneous/dialogue Mandarin, general writing and actual genre fiction; raw list size does not establish coverage.

## Survey phase (the next Work assignment)

Start with the existing 200-row candidate research pool and the source survey. Aim provisionally for **~14k–18k general candidate units plus ~3k–5k genre candidates**, before overlap reconciliation and pruning; the size is a research planning parameter, not a frequency threshold. Use manageable research batches and preserve auditability.

- Record original candidate keys (not permanent `lx-` IDs), simplified/traditional forms, tone-marked Pinyin, grammatical class, original succinct gloss, register/genre tags, proposed identity boundaries and review state.
- Keep evidence about frequency, HSK, native high-availability judgments, subgenre occurrence, source licensing and methods **in research files**, linked through candidate keys or eventually stable IDs. Keep unlicensed/restricted source tables in appropriately private storage and publish only legally reusable data/editorial findings.
- Explicitly log duplicates, polysemy/heteronyms, variable readings, separable verbs, compounds, proper names, classical expressions, Taiwan/Mainland distinctions and genre overlap. Mark uncertainty honestly; do not silently invent ranks, dictionary senses or native review.
- Record selection outcomes as `selected`, `needs-review`, `deferred` or `rejected` with reasons; **do not force an exact band quota at the cost of lexical quality**.
- Freeze and version the accepted list, with a license and pronunciation review ledger and evaluation plan for **held-out** spoken/written/genre token coverage. The research survey may require multiple Work tasks. Do not write thousands of `.tid` records during this phase.

When selecting words as a stable inventory (not yet publishing), reserve immutable `lx-NNNNNN` IDs in `research/lexeme-id-registry.csv` with status `planned` and empty path; create matching `research/lexical-selection.csv` rows. A planned ID is a real accepted lexical identity but does **not** require any lesson or TiddlyWiki file. IDs must be sequential, unique and never reused.

## Publication phase (only after survey selection review)

For each finished lexical entry, produce one UTF-8 `tiddlers/Vocabulary/<safe-slug>.tid` file. A minimal source file looks like:

```text
title: Vocabulary/师父
type: text/vnd.tiddlywiki
tags: [[Mandarin Vocabulary]]
mandarin-kind: vocabulary
mandarin-level: beginner
mandarin-lexeme-id: lx-000020
mandarin-hanzi: 师父
mandarin-pinyin: shīfu
mandarin-gloss: master; respected mentor
mandarin-pos: noun
```

`lx-000020` is **already assigned** to 师父; never copy it into a new record. To activate an approved planned word, write its tiddler *without* the ID header then run:

```bash
python3 scripts/register_lexeme.py tiddlers/Vocabulary/<file>.tid --batch publish-01 --lexeme-id lx-NNNNNN
```

This promotes the planned entry to active while retaining its ID and checking Hanzi/Pinyin against the selection roster. For exceptional newly accepted words not in the roster, the tool can allocate the next new ID without `--lexeme-id` once their identity is adjudicated.

Include clear Hanzi–Pinyin–English contextual sentences, useful collocations and learner-facing linguistic distinctions. Only include traditional form, register, audio attribution and lesson membership where relevant to learning; **do not put selection bands, frequency ranks, HSK crosswalks, provenance source IDs, evidence IDs or internal research review status into the vocabulary tiddler**. Keep copyright-required attribution available where licenses demand it.

`mandarin-lessons` is optional. If set (e.g. `L03 L07`), its lesson vocabulary indexes must already exist. Don't invent lessons to satisfy the vocabulary validator. Prefer 15–30 newly introduced items per lesson when appropriate, though grammar dictates actual scope. The vocabulary index must not render the entire ~8k–9k lexicon on one page.

## Checks and review/merge policy

- Run `python3 scripts/validate_wiki.py`, `python3 -m unittest discover -s scripts -p 'test_*.py' -v`, the PR lexical history check, and the pinned TiddlyWiki static build.
- The validator checks unique IDs and lifecycle registry, planned-selection rows, evidence/source permissions, optional lesson memberships and links. Tests do **not** establish native linguistic correctness.
- **Work must open a draft PR and never self-merge** survey or vocabulary production PRs. A separate reviewing assistant verifies source rights, sample quality, identity choices and CI on the latest head, corrects defects and makes the editorial merge decision.
- The `main` workflow automatically validates, builds and deploys after merge; GitHub automatically deletes merged branches if that repository setting is enabled. No ruleset is required by the collaboration policy.
- Report candidate and accepted counts, ID ranges, selected/deferred/rejected statuses, domain breakdowns, duplicate/overlap cases, review uncertainties, source versions/rights and held-out coverage **only when actually measured**.

## Audio, privacy and scale

Audio is optional. Use credited human pronunciation audio or independently checked speech synthesis; do not bulk-generate unreviewed tonal audio. See [Audio Assets](AUDIO_ASSETS.md).

This is a **public** repository. Private learner scores, recordings and conversations belong in private Drive/Sheets, not the published repo. Source licensing may also require keeping restricted analytical tables in private research storage.

Before the 8k–9k production run, benchmark full-size static TiddlyWiki rendering, HTML size, search latency and representative mobile browsers. Preserve offline access and avoid a single huge rendered vocabulary index.
