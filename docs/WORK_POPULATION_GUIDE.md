# Work handoff — Vocabulary ingestion (v1.2)

Use this contract when populating the Mandarin course through ChatGPT Work or an equivalent batch process. **Read [LEXICAL_DATA_CONTRACT.md](LEXICAL_DATA_CONTRACT.md) first**; it defines required immutable IDs, source/evidence registries, and two-pass review. Do not merge an import PR within the same Work session.

## Scope and source of truth

The course is a standalone, public **static TiddlyWiki**, not a Node server. **One lexical entry = one vocabulary tiddler**. The master lexicon is independent of lessons: an entry may exist permanently without lesson membership, and importing words must not force creation of placeholder lessons. Never create one monolithic 7,000-word tiddler or an unbounded page that renders all word records. The approved target is **7,000 general Mandarin lexical entries (2k fundamental + 3k high-use + 2k high-availability) plus 1–2k additional unique wuxia/xianxia lexical entries**. Desired 95–98% token coverage must be measured independently for spoken, general written, and genre corpora; the target does not guarantee that percentage. See [VOCABULARY_TARGET_STANDARD.md](VOCABULARY_TARGET_STANDARD.md) and [VOCABULARY_SOURCE_SURVEY.md](VOCABULARY_SOURCE_SURVEY.md).

Before bulk ingestion, perform a small source and rights audit. Prefer **wordfreq zh** as mixed-register candidate frequency backbone, **SUBTLEX-CH** as spoken/subtitle reference, and the **November 2025 HSK syllabus** as pedagogical crosswalk (not frequency order). The 2k high-availability tier and 1–2k wuxia-specific layer require additional curated evaluation; raw frequency alone cannot select these. Select a source vocabulary list, its version, and reuse terms (e.g. an appropriately licensed frequency/HSK list). Record bibliographic provenance. Do not assume that a third-party website's 7k list is the official exam list.

## Content format

Each record is a UTF-8 `tiddlers/Vocabulary/<safe-slug>.tid` file. Required fields:

```
title: Vocabulary/师父
type: text/vnd.tiddlywiki
tags: [[Mandarin Vocabulary]]
mandarin-kind: vocabulary
mandarin-level: beginner
mandarin-lexeme-id: lx-000020
mandarin-source-ids: curriculum-editorial
mandarin-hanzi: 师父
mandarin-pinyin: shīfu
mandarin-gloss: master; respected mentor
mandarin-pos: noun
```

The displayed ID `lx-000020` belongs to the **existing** 师父 tiddler; never copy it into a new record. For new imports, allocate the next never-used ID from `research/lexeme-id-registry.csv` and add a matching registry row in the same PR. `mandarin-source-ids` must reference one or more entries in `research/lexical-sources.json`; `curriculum-editorial` signals original editorial writing, **not** externally validated linguistic correctness.

Optional metadata includes `mandarin-lessons: L03` (only after assigning a lesson), `mandarin-lexical-band`, `mandarin-registers`, and `mandarin-topics`. For unsequenced reference entries, `mandarin-level: reference` is acceptable; this field does not imply lesson membership. The optional fields should be added as actual `.tid` header fields, not as comment lines.

After one blank line, include a short definition, at least one example with **Hanzi, tone-marked Pinyin and English**, and links to grammatical or character notes. Never invent a word's pronunciation from its component characters. For heteronyms, alternate readings, proper names, tone sandhi and polysemy, explicitly document when/why a reading is used. Where practical track traditional form and regional usage as optional metadata.

A word can belong to multiple lessons: `mandarin-lessons: L03 L07`. For words not yet assigned to lessons, **omit** `mandarin-lessons` entirely. If any lesson IDs are specified, all must resolve to existing `Lesson Vocabulary/LNN` indexes.

## Lesson partition

Only create/verify `Lesson Vocabulary/LNN` when a pedagogical lesson actually uses a group of words. Before assigning `mandarin-lessons: LNN`, create its corresponding index. New lesson pages should use the pilot's dynamic filter for bounded lists:

```
[tag[Mandarin Vocabulary]contains:mandarin-lessons[L03]sort[mandarin-pinyin]]
```

The `Vocabulary Index` may link to lesson indexes and explain how to find any lexical entry using search; it must never render thousands of words simultaneously. Unassigned words remain searchable and count toward the lexicon inventory, but do not appear in lesson filters. Keep separate curricular sequencing (`Lesson/...`) from the independent master lexicon (`Vocabulary/...`).

Suggested initial lesson size: 15–30 *new* items, fewer in foundational lessons; larger groups may be appropriate later. Use review links in subsequent units without duplicating lexemes. If more than ~50 new entries are required, split into smaller units.

## Batch workflow

1. Start with an adjudicated, appropriately reusable source/version and a pilot of 20–50 words; explicitly flag ambiguous or suspicious entries. Do not bulk copy proprietary dictionaries, news corpora, or copyrighted fiction into this public repo.
2. Build and adjudicate the **independent lexical inventory** first. Track duplicate forms, segmentation, source provenance, uncertainty, and optional lexical bands. Do not create artificial lessons to make new words pass validation.
3. Populate **one word per tiddler**. For the small subset chosen for instruction, group by grammatical dependencies, character/sound families, frequency, usefulness, and recurring wuxia settings—not alphabetic Pinyin order. Create each lesson index before assigning its ID to any word; leave all other words unassigned.
4. Allocate **one immutable lexeme ID per new lexical entry**; update `research/lexeme-id-registry.csv` atomically with tiddlers. Add evidence to `research/lexical-evidence.csv` only if independently documented. Candidate CSV IDs based on form/POS are research keys and must not be promoted as stable lexeme IDs. Commit small, reviewable batches (e.g. <=100 entries per commit).
5. Run `python3 scripts/validate_wiki.py`, the unit tests and the PR GitHub Actions check, including lexeme-history validation. Repair duplicates, missing references, invalid source references and broken lesson IDs before the next batch. Do not change previously allocated IDs on lexical reanalysis.
6. Report real counts, **assigned versus unassigned** entries, source/version and licensing status, tentative lexical bands, overlap with wuxia, newly introduced lesson IDs, lexical-ID range, evidence references, and any uncertainties. Do not claim that all words have been reviewed solely because CI passes.

## Pull-request review and merge policy

The default collaboration policy is **draft import PRs, automatic validation, independent editorial merge decisions**. **A Work import session must leave its vocabulary PR in draft and must not self-merge.** The designated reviewing assistant may mark it ready and merge after checking that:

1. PR validation has completed successfully on the current head commit, including the metadata validator, regression tests, TiddlyWiki build, and output checks.
2. New lexical entries have been reviewed for Hanzi/traditional forms, tone-marked Pinyin and neutral tones, segmentation and lexical identity, POS, glosses, register, and natural original example sentences. An automated pass alone is insufficient.
3. Source provenance and redistribution rights are documented; ranks, corpus coverage, HSK crosswalks, and band placement are not portrayed as verified unless their supporting evidence exists.
4. No unresolved systemic blocker or likely substantive linguistic error remains. Unverified but explicitly labeled research candidates may be committed as research candidates, not as final classified vocabulary.
5. The branch is up to date enough to merge safely, and the latest CI results apply to the mergeable changes.

Work leaves the PR in draft even if its technical checks pass. The independent reviewing assistant marks it ready and merges when the checks and linguistic review are satisfied. The existing `main` push workflow builds/deploys the static site after merge. Automatic deletion of merged branches is a **repository setting**, not a workflow guarantee; do not require an additional branch-protection ruleset for the collaboration process. Agents should never bypass a failed check simply because GitHub does not enforce it.

## Audio

Audio is optional and reference-based: `mandarin-audio: audio/<slug>.ogg`, plus `mandarin-audio-status` and `mandarin-audio-license`. Human audio or independently reviewed TTS is preferred. The `你好` pilot is a licensed original Ogg recording. The available local eSpeak Mandarin output was **not** deemed adequate for pronunciation teaching. Do not bulk-generate unverified tone examples.

## Privacy

This repository is public. Only curriculum material belongs here. Put personal scores, conversations, recorded speech, and schedules in a private Google Sheet/Drive location, not under GitHub.
