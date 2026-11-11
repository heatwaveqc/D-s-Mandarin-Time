# Survey-first Mandarin lexicon selection — v1.0

Adopted 2026-11-11. This document governs **word selection**, not page production or lesson sequencing. Read with [Vocabulary Target Standard](VOCABULARY_TARGET_STANDARD.md), [Lexical Data Contract](LEXICAL_DATA_CONTRACT.md), and [Work Population Guide](WORK_POPULATION_GUIDE.md).

## Principle

**Select the library first; publish and teach it later.** Do not make another piecemeal `Vocabulary/*.tid` import just to increase the tiddler count. Research records may exist without wiki pages and may remain unassigned to lessons indefinitely. The existing 76 vocabulary tiddlers are an early pilot, not an irrevocably approved sample of the final ranked lexicon.

Selection evidence (frequency/prevalence, corpus and dictionary provenance, licensing, HSK mappings, availability judgments, review history) belongs in the **research layer**, connected by candidate keys and eventually by opaque IDs. A published `.tid` is a learner-facing language entry; it does not need source-frequency rankings or research-provenance fields. Retain any required attribution for adapted content in the wiki's appropriate shared attribution materials; research-only metadata is not a substitute for satisfying licenses.

## Stage A — deliberately overcomplete survey

Plan an initial **roughly 14,000–18,000 general Mandarin candidates plus 3,000–5,000 genre candidates**, before deduplication and overlap reconciliation. These are research sizing ranges, **not evidence-derived corpus thresholds, quotas, or a promise that a particular list reaches a coverage percentage**. Adjust the pool if coverage or native-salience review identifies systematic gaps.

Use independently compatible and permission-cleared resources or original editorial candidate generation. Different evidence streams serve different purposes:

- Frequency/dispersion across conversation, general writing, subtitles and books; do not equate television subtitle dialogue with spontaneous speech.
- Pedagogical knownness and general native availability, deliberately including familiar low-frequency items.
- Wuxia, xianxia, historical and fantasy fiction, with distinct genre tags and copyright-compliant text access; do not count common general words a second time.
- HSK and learner dictionaries **only as crosswalks/verification**, never as a substitute for corpus frequency.

Keep the **candidate survey** as research data, not as TiddlyWiki records. The 200-row pilot is the seed; its normalized first survey batch is `research/candidate-survey.csv`. It assigns opaque stable keys `cand-NNNNNN`, preserving the prior word/POS-derived key only as `seed_candidate_key`. These candidate keys are not permanent lexeme IDs. The seed has 200 `needs-review` records; 44 exact-form overlaps link to active lexeme IDs for reuse review and must not be duplicated. Each candidate should have simplified and traditional forms, normalized Pinyin, proposed POS/lexical unit, concise original gloss, optional regional/register flags, provenance reference and selection notes, duplicate/heteronym flags, and unresolved questions. Source ranks or texts may be held in a separate permission-appropriate **private** research workspace where public redistribution is not authorized. Never transfer restricted tables into the public GitHub repository merely because the corresponding program is open source.

## Stage B — normalize, adjudicate, and prune

Process in audited sub-batches **within the research survey**, not by creating teaching tiddlers. Deduplicate lexical identities rather than just Hanzi strings. Handle heteronyms (行 xíng/háng), homographs, grammatical particles, classifier uses, separable verbs, lexicalized compounds, proper nouns, regional forms, classical/genre senses and everyday-versus-genre overlaps explicitly.

For each candidate, record `surveyed`, `needs-review`, `selected`, `deferred`, or `rejected` and an editorial reason. A provisional frequency rank, HSK level or genre occurrence is not an adjudicated selection decision. Reviewers should examine high-impact ambiguities, disputed wordhood, atypical spelling/tones, and a statistically useful random sample of ordinary records. Do not label an automatically checked entry as independently linguistically verified.

Select toward the approved objective of **2,000 fundamental + 3,000 high-use + 2,000 high-availability general lexical entries, plus 1,000–2,000 genuinely additional specialist entries**. These bands are selection decisions to be justified **outside the tiddler**, not attributes inherently possessed by words. Measure held-out token coverage separately for spoken Mandarin, general writing and wuxia/xianxia. If the targets do not deliver the desired coverage, show the result and revise the plan; do not invent percentages.

## Stage C — freeze an approved selection roster

After pruning, reserve immutable `lx-NNNNNN` IDs for the accepted inventory as **planned** records in `research/lexeme-id-registry.csv`, without requiring a TiddlyWiki file. Populate `research/lexical-selection.csv` for these planned IDs. This roster is the versioned editorial bridge from research to publication. IDs are never reused; changes to spelling/POS/band do not create a fresh ID unless a genuine lexical split warrants one.

The selection roster has one row per **planned** lexeme (active legacy entries may be added but do not require duplicate data). It records `lexeme_id`, normalized simplified/traditional/Pinyin/POS/gloss, editorial selection band if chosen, original candidate key, review status, and adjudication notes. The ID registry records lifecycle (`planned`, `active`, `retired`), not a frequency rank. Marking a lexical record `selected` is **not** proof of independent native review.

Freeze the accepted roster with a dated version, review ledger and unresolved-question list. **Do not generate 8,000–9,000 tiddlers during this stage.** Maintain a written licensing decision and distinguish public editorial metadata from private/restricted source data.

## Stage D — construct the TiddlyWiki library

Once an approved selection roster exists, publish words in small validated production batches. Promote a planned ID to `active` using `scripts/register_lexeme.py --lexeme-id lx-NNNNNN --batch ...` when its finished `.tid` is created; do not mint another ID for the same word. A published entry contains the lexical ID, Hanzi, Pinyin, gloss, POS, useful usage and collocations, and original contextual examples. Traditional forms and linguistically relevant register/sense notes are welcome.

All research selection, source/rights, HSK and frequency evidence remain external to the `.tid` by default. **No frequency rank, lexical band, HSK level or research provenance ID belongs in the content tiddler.** Lesson IDs remain optional and are added only when a lesson deliberately introduces the word. Production PRs stay draft until a separate linguistic reviewer approves them; tests are necessary but not proof of accurate language.

Before mass production, benchmark static HTML size, build time and browser-side search for a synthetic 8–9k lexicon; keep offline/static use available. Preserve the pilot tiddlers and their ID history.

## Immediate next deliverable

A **large survey work package**, not a third `.tid` batch: research candidate acquisition plan, source/rights manifest, versioned candidate pool, normalization/duplicate audit, review queue, pruning criteria and initial coverage sampling methodology. Do this in manageable validated **research** sub-batches, retaining candidate uncertainty; do not claim a frozen final list or perform bulk publication in that Work run.
