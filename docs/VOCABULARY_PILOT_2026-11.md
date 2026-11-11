# Mandarin vocabulary pilot — 2026-11

Status: pilot candidate pool and repository implementation; not a coverage study. Frequency ranks are intentionally blank in this release because the source datasets were not downloaded and frozen for this run. HSK membership and level are likewise not asserted record-by-record. All 200 candidates are manually curated research candidates, not a licensed-source transcription. Each remains subject to review.

## Source and rights assessment

| Source | Finding | Reuse decision |
|---|---|---|
| wordfreq `zh` | Mixed-source frequency estimate assembled from web, subtitles, books and other text. The upstream project documents Apache-2.0 code and CC BY-SA 4.0 data, with source notices and attribution requirements. Its Chinese segmentation is a candidate-generation aid; list membership and Zipf values are not a linguistically adjudicated lexicon. Package version and data hash must be frozen before deriving public ranks. | Suitable for private candidate comparison and, after exact version/notice review, potentially reusable derived frequency metadata with attribution and ShareAlike compliance. This pilot republishes no wordfreq rank or copied data. |
| SUBTLEX-CH | Cai & Brysbaert subtitle corpus; published study reports 33.5 million word tokens / 46.8 million characters and word/POS and character frequency tables. This is a subtitle/media register proxy, not spontaneous conversation. Data access is described as free for research; the pilot has not verified a blanket public redistribution grant for the downloadable tables. | Cite and consult as a separate benchmark. Do not republish its tables or rankings until the specific download terms and rights are confirmed. Source paper is open access under CC BY. |
| November 2025 HSK syllabus | Examination syllabus / pedagogical crosswalk, not frequency order. Official ChineseTest describes the new three stages/nine levels and syllabus components. Third-party transcriptions do not convey rights to the underlying standard. | Use only to map entries to an edition/level after record-level verification. No HSK claims are made in this candidate pool or pilot. |
| Dictionaries and curated resources | Open resources such as CC BY-SA Wiktionary may support independent sense and pronunciation checks with attribution and compatible terms. Commercial learner dictionaries, paid corpora and copyrighted frequency dictionaries are research references only unless their terms explicitly permit reuse. | Definitions/examples here are short original editorial text. Review specific license and notice before importing metadata or wording. |
| Wuxia/xianxia | Academic genre-comparison work can guide methodology and candidate discovery; published novels and scraped web fiction remain copyrighted absent permission or a suitable license. | Use public-domain/explicitly licensed texts, author-authorized corpora, or independently authored texts. Record text-level provenance and rights; never ingest novel passages or scrape-derived word lists by default. |

### Version and reproducibility notes

Checked 2026-11-11. References: wordfreq project README and NOTICE (<https://github.com/rspeer/wordfreq>); SUBTLEX-CH article (Cai & Brysbaert 2010, <https://doi.org/10.1371/journal.pone.0010729>) and project page (<https://www.ugent.be/pp/experimentele-psychologie/en/research/documents/subtlexch>); official HSK information (<https://www.chinesetest.cn/HSK?lang=en>); wuxia/xianxia corpus study (<https://aclanthology.org/2020.ccl-1.2/>). The source files themselves were not fetched or hashed for this pilot; no exact dataset release/version is claimed. The next data run should record download URL, retrieval date, release/version, file hash, license text, and transformation script.

Research access is not redistribution permission. In particular, a research download, a paper's open-access license, and a permissive license on third-party code are not interchangeable with rights to republish the underlying lexical tables or source fiction.

## Identity and candidate protocol

Candidate IDs use `cmn:<simplified-form>:<POS>` for a headword/POS unit; add a stable sense suffix only when senses require independent curriculum treatment (for example `cmn:打:verb:s01`). The display form is not itself the identity: traditional variants map to the same lexeme; POS-distinct or unrelated homographs may have separate records; polysemous senses stay together when their grammar/teaching behavior is shared. Heteronyms require sense/pronunciation-specific records or explicit reading notes. Separable verbs are lexicalized as the conventional verb but retain a note on separable syntax; productive phrases are not added as lexical items. This is a proposed convention, not yet enforced by the validator.

The attached CSV has 200 unique simplified-form candidates (50 each, across four provisional strata). Repeated occurrences across genres are one candidate, not multiple counts. “Provisional” is deliberate: source ranks, HSK editions/levels, frequency bands and coverage are not fabricated. Review confidence is a triage estimate, not a claim of corpus verification.

## Pilot import

Twenty-five new entries are imported as independent vocabulary tiddlers with original examples and no lesson assignments. The existing 30 vocabulary entries were checked for exact-form duplicates; pilot forms were selected to avoid them. Existing lesson assignments and lesson indexes were not changed. The validator already allows omitted `mandarin-lessons` and rejects unresolved supplied IDs; the repository's existing tests cover both cases.

## Review ledger

- **Unresolved:** all 200 candidates need multi-source frequency lookup, official HSK crosswalk, and native-level sense/register review before band membership is finalized.
- **Literary uncertainty:** wuxia terms have cross-period and subgenre variation; prioritize modern genre corpora with rights cleared and mark archaic/classical readings separately.
- **Potentially ambiguous:** 打, 行, 还, 得, 着, 了, 看, 过 and several classifiers/coverbs are polyfunctional or heteronymous. Keep sense/POS notes together unless separate learning behavior requires stable sense records.
- **Rejected from pool:** no proprietary rank lists, dictionary definitions copied verbatim, or fiction excerpts. Candidate phrases that are merely compositional were excluded.
- **No duplicates observed** within the 200 simplified headword candidates; this is string-level deduplication, not a full synonym/sense identity adjudication.

## Held-out coverage protocol

1. Freeze three independent licensed or permission-cleared test corpora: spontaneous/conversational speech with transcripts; contemporary general writing sampled across news, essays, public information and prose; and wuxia/xianxia fiction with source-level permission. Keep source documents disjoint from candidate-generation data.
2. Publish sampling strata, dates, inclusion rules, transcript normalization, Chinese text segmentation, tokenization version/configuration, and exclusions. Preserve original text; normalize only documented orthographic variants.
3. Have two Mandarin linguists independently adjudicate word segmentation and lexical identity on a stratified sample; resolve disagreements and publish the adjudication guide. Count out-of-vocabulary names and productive compounds consistently.
4. Match corpus tokens to lexeme IDs, reporting token coverage, type coverage, OOV rate, and coverage by genre/domain. Report confidence intervals by document-level bootstrap, not token bootstrap. Publish no corpus text or restricted wordlist.
5. Evaluate candidate list without tuning on held-out data; if revised, use a new held-out set or nested evaluation. Report each corpus independently and distinguish surface coverage from learner-known vocabulary.

## Scale and build assessment

The source architecture stores one small tiddler per lexical record and uses bounded lesson views; this is a sound ingestion model for 8–9k records. The current static build embeds all tiddlers in a single HTML artifact, so total payload and browser-side search/index memory are the main scale risks. No 8–9k benchmark was run in this environment. Before full import, generate a synthetic/licensed-size benchmark matching expected median and high-percentile tiddler sizes, record build time and HTML size, then test search responsiveness on representative desktop/mobile browsers. If needed, split delivery by corpus or add server-side search only after preserving offline/static use as an explicit design choice.

## Execution limitation

This checkout session did not provide a local clone or runnable Node/TiddlyWiki environment. Repository file writes are proposed on a review branch. Therefore local validator, unittest, and static-build results are **not claimed** here. Run the existing GitHub Actions checks on the pull request before merge; the workflow currently triggers for main pushes and manual dispatch, not ordinary pull-request events.
