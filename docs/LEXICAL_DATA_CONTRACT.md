# Lexical identity, selection and provenance contract — v2.0

Adopted 2026-11-11. Read alongside [Survey-first Lexicon Standard](LEXICON_SURVEY_STANDARD.md), [Vocabulary Target Standard](VOCABULARY_TARGET_STANDARD.md) and [Work Population Guide](WORK_POPULATION_GUIDE.md).

## Design boundary

**Lexicon selection is research; TiddlyWiki publication is production; lessons are curriculum.** These are separate stages and must not force one another. Source provenance, frequency/prevalence measurements, HSK mappings, research review status, band/category selection, and genre-selection evidence belong in the **research layer**, not inside learner-facing vocabulary tiddlers. Rights-required attribution for adapted material must remain accessible to the user under the relevant license; do not confuse external research provenance with the legal requirements for published reuse.

The already-published 76 vocabulary tiddlers remain in the wiki. They are not assumed to have passed the eventual full-corpus selection process. Research candidates may be collected and rejected without minting permanent lexical IDs or publishing pages.

## Immutable identity and registry states

A permanent lexical ID is an opaque `lx-NNNNNN` (six decimal digits) that **never encodes Hanzi, Pinyin, POS, band, frequency, lesson, or sense**. The 76 existing published records hold IDs `lx-000001` through `lx-000076`. Their numerical order is arbitrary, not a rank. IDs are allocated sequentially and never recycled.

`research/lexeme-id-registry.csv` is the authoritative lifecycle registry:

- `planned`: an accepted lexical item with an immutable ID, a **blank** `tiddler_path`, and a corresponding `research/lexical-selection.csv` row. No wiki page is required.
- `active`: a published `Vocabulary/*.tid` exists and its `mandarin-lexeme-id` matches exactly one active registry row and path.
- `retired`: the ID is reserved forever, the path must be empty and the retirement documented. Never reassign it or restore it to active.

A `planned → active` transition preserves the ID, records a `published:` note in the registry and creates one new vocabulary tiddler. An active file rename retains its ID and requires a `moved:` audit note. An active record cannot revert to planned; a retired ID never returns. The PR history check compares the new registry with `main` to prevent silent ID recycling, deletions and unreviewed lifecycle changes.

The existing 200-candidate survey's `candidate_key` values (e.g. `cmn:我:pronoun`) are **temporary research keys, not permanent lexical IDs**. Reanalyze lexical identity before allocating planned IDs. Heteronyms, unrelated homographs, polyfunctional verbs, separable verbs, lexicalized expressions, regional variants, proper names, and genre-specific meanings require explicit decisions. Do not split ordinary polysemy merely because several English glosses exist.

## Accepted lexical selection records

`research/lexical-selection.csv` describes reserved planned lexical items separately from wiki pages. Its columns are:

```csv
lexeme_id,simplified,traditional,pinyin,pos,gloss,selection_band,candidate_key,review_status,notes
```

Every planned ID must have exactly one row with meaningful form/Pinyin/POS/gloss, a candidate key and a `selected` or `needs-review` status. `selection_band` may be left empty until the classification is adjudicated, otherwise it must match the four approved band names. Research review notes must distinguish editorial selection from independent native-language verification. Existing active legacy entries may be added to the roster, but that is not required merely to retain their ID and existing wiki entry.

The full survey may be larger and use a separate candidate table/ledger. [Survey-first Lexicon Standard](LEXICON_SURVEY_STANDARD.md) sets the intended overcomplete scope, deduplication process, independent coverage measurements, and accepted-roster freeze.

## Source registry and evidence

`research/lexical-sources.json` holds stable source IDs, kind, URL, licensing/reuse status, version, checksum and acquisition date. The current named resources (wordfreq zh, SUBTLEX-CH, HSK 2025 and CC-CEDICT) remain reference/pending rather than approved bulk redistribution sources unless explicitly upgraded with the exact licensed dataset and SHA-256.

`research/lexical-evidence.csv` stores research claims with fields `evidence_id,lexeme_id,source_id,claim_type,claim_value,review_status,reviewed_by,reviewed_on,notes`. Evidence may attach to **planned or active** IDs. A verified editorial review includes reviewer/date but does **not** imply independent native-speaker adjudication. Permission-restricted frequency/HSK tables must remain in appropriate private research storage unless their public reuse rights are explicitly confirmed. Public source-derived numerical frequency or HSK values still require an approved, frozen source in the evidence validator.

Lexical band assignments are **research decisions**, not intrinsic properties of a word. Triangulate spoken/written frequency, validate high-availability judgments independently of rank, distinguish genuinely additional wuxia terminology from ordinary vocabulary, and evaluate held-out token coverage independently by domain. Do not fabricate rankings or treat a 7,000-word target as a guaranteed coverage percentage.

## Published vocabulary format

The wiki-facing record stays focused on the language:

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
mandarin-lessons: L01 L03
```

This is an **existing** ID and must not be copied to new entries. Include useful contextual Hanzi–tone-marked-Pinyin–English examples, collocations, grammatical behavior and any relevant register/sense distinctions. Traditional forms are allowed as linguistic metadata. **Omit `mandarin-source-ids`, `mandarin-lexical-band`, `mandarin-review-status`, `mandarin-hsk-*`, `mandarin-frequency-*` and `mandarin-*-evidence-id` fields from `.tid` files.** Tiddler `mandarin-lessons` remains optional. The validator enforces this research/presentation boundary.

For a new word lacking a reserved ID, `python3 scripts/register_lexeme.py tiddlers/Vocabulary/<file>.tid --batch <batch>` may allocate one. **Preferred after surveying:** use `--lexeme-id lx-NNNNNN` to publish an existing planned item without allocating another ID. The script confirms its Hanzi and Pinyin agree with the accepted selection roster, inserts the ID into the tiddler and updates the lifecycle registry. `--dry-run` previews without writing.

## Division of labor and scale gates

1. Build an intentionally broad, copyright-compliant research candidate pool; do not publish it as vocabulary tiddlers.
2. Review segmentation, identity, sources, bands and domain coverage; prune and freeze a selected roster using planned IDs.
3. Only after the selection stabilizes, generate learner-facing tiddlers in small reviewed batches; create grammatical lessons independently.
4. Work creates a **draft PR** for research or production, never self-merges a vocabulary import. The designated assistant reviews language, rights and validation; only then marks ready/merges. GitHub Actions automatically builds/deploys merged content.
5. Before producing thousands of wiki pages, benchmark 8–9k tiddlers for static build size, search performance and mobile usability. Preserve the offline/static TiddlyWiki design if practical.

A passing validator enforces referential integrity and stated source permissions. It does **not** establish lexical accuracy, naturalness, corpus rankings or held-out coverage.
