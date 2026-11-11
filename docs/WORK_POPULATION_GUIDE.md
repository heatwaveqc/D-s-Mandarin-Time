# Work handoff — Vocabulary ingestion (v1.0)

Use this contract when populating the Mandarin course through ChatGPT Work or an equivalent batch process.

## Scope and source of truth

The course is a standalone, public **static TiddlyWiki**, not a Node server. **One lexical entry = one vocabulary tiddler**. Never create one monolithic 7,000-word tiddler or an unbounded page that renders all word records. The approved target is **7,000 general Mandarin lexical entries (2k fundamental + 3k high-use + 2k high-availability) plus 1–2k additional unique wuxia/xianxia lexical entries**. Desired 95–98% token coverage must be measured independently for spoken, general written, and genre corpora; the target does not guarantee that percentage. See [VOCABULARY_TARGET_STANDARD.md](VOCABULARY_TARGET_STANDARD.md) and [VOCABULARY_SOURCE_SURVEY.md](VOCABULARY_SOURCE_SURVEY.md).

Before bulk ingestion, perform a small source and rights audit. Prefer **wordfreq zh** as mixed-register candidate frequency backbone, **SUBTLEX-CH** as spoken/subtitle reference, and the **November 2025 HSK syllabus** as pedagogical crosswalk (not frequency order). The 2k high-availability tier and 1–2k wuxia-specific layer require additional curated evaluation; raw frequency alone cannot select these. Select a source vocabulary list, its version, and reuse terms (e.g. an appropriately licensed frequency/HSK list). Record bibliographic provenance. Do not assume that a third-party website's 7k list is the official exam list.

## Content format

Each record is a UTF-8 `tiddlers/Vocabulary/<safe-slug>.tid` file. Required fields:

```
title: Vocabulary/师父
type: text/vnd.tiddlywiki
tags: [[Mandarin Vocabulary]]
mandarin-kind: vocabulary
mandarin-level: beginner
mandarin-hanzi: 师父
mandarin-pinyin: shīfu
mandarin-gloss: master; respected mentor
mandarin-pos: noun
mandarin-lessons: L03
# Optional after frequency/genre review:
# mandarin-lexical-band: wuxia-specialist
# mandarin-registers: spoken fiction literary
# mandarin-topics: wuxia martial-arts
```

After one blank line, include a short definition, at least one example with **Hanzi, tone-marked Pinyin and English**, and links to grammatical or character notes. Never invent a word's pronunciation from its component characters. For heteronyms, alternate readings, proper names, tone sandhi and polysemy, explicitly document when/why a reading is used. Where practical track traditional form and regional usage as optional metadata.

A word can belong to multiple lessons: `mandarin-lessons: L03 L07`.

## Lesson partition

Create/verify `Lesson Vocabulary/LNN` before adding words tagged with its ID. New lesson pages should use the pilot's dynamic filter for bounded lists:

```
[tag[Mandarin Vocabulary]contains:mandarin-lessons[L03]sort[mandarin-pinyin]]
```

The `Vocabulary Index` should link to lesson indexes only; it must never render thousands of words simultaneously. Keep separate curricular sequencing (`Lesson/...`) and lexical organization (`Lesson Vocabulary/...`).

Suggested initial lesson size: 15–30 *new* items, fewer in foundational lessons; larger groups may be appropriate later. Use review links in subsequent units without duplicating lexemes. If more than ~50 new entries are required, split into smaller units.

## Batch workflow

1. Start with an adjudicated, appropriately reusable source/version and a pilot of 20–50 words; explicitly flag ambiguous or suspicious entries. Do not bulk copy proprietary dictionaries, news corpora, or copyrighted fiction into this public repo.
2. Group by grammatical dependencies, character/sound families, frequency, usefulness, and recurring wuxia settings. Do not group solely by alphabetic Pinyin order.
3. Add lesson index before its vocabulary. Populate **one word per tiddler**, and update `mandarin-lessons` on shared words.
4. Commit small, reviewable batches (e.g. <=100 entries per commit).
5. Run `python3 scripts/validate_wiki.py` and confirm GitHub Actions build/deploy. Repair duplicates, missing references, and broken lesson IDs before the next batch.
6. Report real counts, source/version, tentative lexical bands, overlap with wuxia, newly introduced lesson IDs, and any uncertainties. Do not claim that all words have been reviewed solely because CI passes.

## Audio

Audio is optional and reference-based: `mandarin-audio: audio/<slug>.ogg`, plus `mandarin-audio-status` and `mandarin-audio-license`. Human audio or independently reviewed TTS is preferred. The `你好` pilot is a licensed original Ogg recording. The available local eSpeak Mandarin output was **not** deemed adequate for pronunciation teaching. Do not bulk-generate unverified tone examples.

## Privacy

This repository is public. Only curriculum material belongs here. Put personal scores, conversations, recorded speech, and schedules in a private Google Sheet/Drive location, not under GitHub.
