# Mandarin Target Vocabulary Standard — v1.0

Status: **approved curriculum target; candidate lexical data not yet ingested or coverage-validated**  
Adopted: 2026-11-11  
Owner: D's Mandarin Time  
Companion: [Source Survey](VOCABULARY_SOURCE_SURVEY.md), [Work population guide](WORK_POPULATION_GUIDE.md).

## Goal and precedent

Model the general-purpose lexical curriculum on the **three functions** of Tullio De Mauro's Italian *Vocabolario di base* (historically approximately 2,000 fundamental, 2,750 high-use, and 2,300 high-availability lexical items). The Mandarin numeric curriculum target rounds the bands to **2,000 + 3,000 + 2,000 = 7,000**. Add a **separate 1,000–2,000 specialized wuxia/xianxia targets**, for a planned **8,000–9,000 unique lexical-entry goal** *before overlap reconciliation*.

The Italian corpus percentages sometimes associated with this model (roughly 86% from fundamental and another ~6% from high-use) are **Italian empirical claims**, not assumptions or predicted coverage for Chinese.

### General layer (7,000 unique lexical units)

| Band | New target | Selection criterion | What the tier is *not* |
| --- | ---: | --- | --- |
| **Fundamental** | 2,000 | Core frequent words across conversation and written discourse; pronouns, particles, auxiliaries, function words, common verbs, classifiers | The first 2,000 HSK entries or simply top 2,000 subtitles without review |
| **High-use** | 3,000 | Broader, frequently encountered words across spoken media, contemporary print, fiction, service and social contexts | All words of intermediate exam grades |
| **High-availability** | 2,000 | Well-known, cognitively available concepts despite low textual frequency: everyday objects, practical life, culturally familiar items, public services, common actions | The next 2,000 *rarest* entries in a corpus |

### Specialization layer (1,000–2,000 distinct additional lexical units)

Mandarin literary / wuxia / xianxia / historical drama vocabulary, including sect/lineage hierarchy, weapons and techniques, training/cultivation, honorifics, kinship/address, martial society, historical institutions, idiomatic/literary formulae, and common genre verbs/adjectives.

These specialized targets are chosen by **genre corpus frequency + educational salience**, not fantasy imagery or literal-English translation alone. Distinguish actual wuxia usages from xianxia/xuanhuan cultivation conventions. Do not fabricate pseudo-Chinese lexical items.

A general word that also matters in wuxia counts **once** toward general vocabulary and receives a topic/genre tag; only *additional unique lexical units* count toward the 1–2k specialized allocation. Consequently, 8–9k is a planning target, not a fixed number of entries guaranteed by concatenating candidate lists.

## What “word” means

Count **segmented lexical units (lexemes/lexical entries)**, not Chinese characters, pinyin syllables, English glosses, or sentence-token occurrences. A two-character compound may be a word; individual characters may also be lexical words. Do not count a compositional phrase twice as a word without a lexical basis.

Disambiguate homographs and multiple readings/senses where a learner would need separate grammatical/phonological knowledge. Keep a stable lexical ID for the entry, optional sense IDs, and explicitly document decisions about multiword expressions, separable verbs, particle combinations, proper nouns, and inflected/transliterated variants.

Keep characters (graph records), words (lexical records), senses (optional future linked records), and lessons (instructional records) conceptually separate.

## Coverage standard: measurement, not a promise

**Desired endpoint: 95–98% lexical token coverage in specified target corpora.** Report percentiles **separately** for:
1. **Everyday spoken Mandarin:** conversation transcripts and dialogue/subtitles (with register flags).
2. **General written Mandarin:** balanced written materials, narrative, public writing/news.
3. **Wuxia/Xianxia:** genre fiction and dialogue, measured with and without specialized vocabulary.

**Never claim that 7,000 words guarantee 95–98% for all genres.** The 2013 comparative Taiwan Mandarin study found that the top 7,000 types covered **96.95%** of its conversational corpus but only **82.55%** of its balanced written corpus. These are corpus-specific rankings, not predictions for Mainland dialogue or modern web novels. A higher reading vocabulary ceiling may be required.

95% is an operational coverage milestone; 98% is a stretch target for extensive reading/listening. Neither assures understanding: syntax, idioms, discourse, and the importance of unfamiliar content words matter.

### Coverage measurement protocol

- Select **held-out**, copyright-compliant, representative samples for each register and period. Do not evaluate only against the same corpus used to rank the words.
- Fix a segmentation standard (e.g. Jieba plus a vetted custom lexical dictionary) before comparing lists; perform manual checks for separable verbs, proper names, four-character expressions, and genre terms.
- Report numerator / denominator of **word tokens**; calculate coverage after and before segmentation sensitivity checks.
- Report recognized vs unrecognized proper nouns and numbers separately; never silently remove hard words to inflate coverage.
- Compare top 2k / 5k / 7k / 8k / 9k milestones using the **same** held-out corpora and segmentation rules.
- Retain coverage by register and by genre plus unknown-word density (e.g., unfamiliar words per 100 tokens), and a separate learner comprehension test.
- Preserve source date/version, access rights, corpus mixture, sampling method, and code/procedures to reproduce the coverage figure.

## Candidate-source strategy

**Use a blend, not a single list**:

- **SUBTLEX-CH** — Cai & Brysbaert (2010), 33.5m segmented subtitle words; ideal conversational frequency candidate and PoS-aware measures. Research use and redistribution rights must be checked before copying raw tables into a public repository.
- **wordfreq** (`zh`) — freely available, cross-domain rank estimator (subtitles, books, Wikipedia, news, web, etc.), usable as a secondary ordering and written-register check. Review data notices and give upstream attribution when reusing rankings.
- **HSK 2025 exam syllabus** — 11,000 numbered entries including pinyin/PoS and 593 grammar items in one independent TSV transcription; use for proficiency grading and syllabic/grammatical coverage, **not** as a frequency-ranked substitute. Do not mix with the different 2021 grading-standard list.
- **Xiao's 5k Frequency Dictionary** — paid, 50m-word, multi-register reference: useful for manual comparison, not for wholesale extraction.
- **High-availability band** — curate categories of things familiar to native speakers and validate with reliable dictionaries/native speakers; raw corpus frequency cannot select this band by itself.
- **Wuxia/xianxia** — independently build or license a genre-specific lexicon using ethically sourced, legal-text corpora and genre-focused expertise. A 2020 corpus study demonstrates feasibility; it is not an available ready-made licensed list.

Additional comparisons are documented in [Vocabulary Source Survey](VOCABULARY_SOURCE_SURVEY.md).

## Data model / future ingestion

Existing pilot word tiddlers have `mandarin-hanzi`, `mandarin-pinyin`, `mandarin-gloss`, and `mandarin-pos`; some also have `mandarin-lessons`. The `mandarin-lessons` field is **optional** for a master-lexicon entry and should be added only when the word is intentionally linked to a lesson. Vocabulary selection/ingestion and curricular lesson creation are independent workstreams.

Optional curated metadata for new records:
- `mandarin-lexical-band`: `fundamental` | `high-use` | `high-availability` | `wuxia-specialist`. Leave blank for provisional pilot vocabulary awaiting ranking.
- `mandarin-registers`: list such as `spoken written fiction literary`.
- `mandarin-topics`: list such as `wuxia weapons` (overlap does not create duplicate records).
- `mandarin-frequency-source`, `mandarin-frequency-rank`: source/version-specific, not fabricated global “true frequency.”
- `mandarin-hsk-edition`, `mandarin-hsk-level`: optional crosswalk.
- `mandarin-source-notes`, `mandarin-review-status`: provenance and review status, e.g. `unreviewed`, `checked`, `verified`.

Choose a source and freeze a version; calculate source-specific ranks and compare before assigning the bands at scale. **Do not classify the existing 31-word pilot as a validated frequency sample.**

Each lesson has a bounded vocabulary page, ideally 15–30 newly introduced words; known words can be linked for review. No single 7k listing in the browser. Do not publish raw copyrighted corpora, licensed dictionaries, personal scores, or learner speech data to this public repo.

## Selection decisions / open work

1. Choose and record primary sources with clear reuse permissions; see the survey for a recommended order.
2. Normalize forms and syllable readings; adjudicate segmentation and duplicated lexemes.
3. Build a small pilot ranked pool (~100–200 candidates), with documented explicit exclusions.
4. Curate high-availability topics and wuxia overlaps separately.
5. Measure independent held-out **spoken, written, wuxia** lexical token coverage.
6. Partition accepted words into lessons using *grammar prerequisites* and contextualized readings, not alphabetical or raw frequency order.

The numeric targets are fixed as above; **the resulting unique entries, coverage outcomes, and exact ranking weights remain empirical questions**.

## Principal references

- De Mauro categories (historical Italian model): https://unora.unior.it/bitstream/11574/198716/1/2013_Maffia_ILMONDO%28in%29CUCINA.pdf
- Tseng, Shu-Chuan (2013), *Lexical Coverage in Taiwan Mandarin Conversation*: https://aclanthology.org/O13-2001.pdf — Table 4, pp. 10–11.
- Cai & Brysbaert (2010), *SUBTLEX-CH*: https://doi.org/10.1371/journal.pone.0010729
- University of Ghent resource: https://www.ugent.be/pp/experimentele-psychologie/en/research/documents/subtlexch
- Robyn Speer's wordfreq: https://github.com/rspeer/wordfreq
- HSK 2025 dataset/edition provenance: https://github.com/uranbekanarbaev/hsk-3.0-vocabulary-dataset
- Zhang, Liu, Zhang (2020), *Wuxia vs. Xianxia corpus*: https://aclanthology.org/2020.ccl-1.2/
