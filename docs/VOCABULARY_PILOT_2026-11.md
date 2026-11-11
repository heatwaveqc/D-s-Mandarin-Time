# Mandarin vocabulary pilot — 2026-11

Status: **editorially reviewed 25-entry repository pilot** and **provisional 200-entry candidate pool**; not a corpus coverage study, source-ranked frequency list, or independent native-linguist adjudication. Frequency ranks are intentionally blank in this release because the source datasets were not downloaded and frozen for this run. HSK membership and level are likewise not asserted record-by-record. All 200 candidates are manually curated research candidates, not a licensed-source transcription. Each remains subject to review.

## Source and rights assessment

| Source | Finding | Reuse decision |
|---|---|---|
| wordfreq `zh` | Mixed-source frequency estimate assembled from web, subtitles, books and other text. The upstream project documents Apache-2.0 code and CC BY-SA 4.0 data, with source notices and attribution requirements. Its Chinese segmentation is a candidate-generation aid; list membership and Zipf values are not a linguistically adjudicated lexicon. Package version and data hash must be frozen before deriving public ranks. | Suitable for private candidate comparison and, after exact version/notice review, potentially reusable derived frequency metadata with attribution and ShareAlike compliance. This pilot republishes no wordfreq rank or copied data. |
| SUBTLEX-CH | Cai & Brysbaert subtitle corpus; published study reports 33.5 million word tokens / 46.8 million characters and word/POS and character frequency tables. This is a subtitle/media register proxy, not spontaneous conversation. Data access is described as free for research; the pilot has not verified a blanket public redistribution grant for the downloadable tables. | Cite and consult as a separate benchmark. Do not republish its tables or rankings until the specific download terms and rights are confirmed. Source paper is open access under CC BY. |
| November 2025 HSK syllabus | Examination syllabus / pedagogical crosswalk, not frequency order. Official ChineseTest describes the new three stages/nine levels and syllabus components. Third-party transcriptions do not convey rights to the underlying standard. | Use only to map entries to an edition/level after record-level verification. No HSK claims are made in this candidate pool or pilot. |
| Dictionaries and curated resources | Open resources such as CC BY-SA Wiktionary may support independent sense and pronunciation checks with attribution and compatible terms. Commercial learner dictionaries, paid corpora and copyrighted frequency dictionaries are research references only unless their terms explicitly permit reuse. | Definitions/examples here are short original editorial text. Review specific license and notice before importing metadata or wording. |
| Wuxia/xianxia | Academic genre-comparison work can guide methodology and candidate discovery; published novels and scraped web fiction remain copyrighted absent permission or a suitable license. | Use public-domain/explicitly licensed texts, author-authorized corpora, or independently authored texts. Record text-level provenance and rights; never ingest novel passages or scrape-derived word lists by default. |

### Version and reproducibility notes

Checked 2026-11-11. References: wordfreq project README and NOTICE (<https://github.com/rspeer/wordfreq>); SUBTLEX-CH article (Cai & Brysbaert 2010, <https://doi.org/10.1371/journal.pone.0010729>) and project page (<https://www.ugent.be/pp/experimentele-psychologie/en/research/documents/subtlexch>); official HSK information (<https://www.chinesetest.cn/HSK?lang=en>); wuxia/xianxia corpus study (<https://aclanthology.org/2020.ccl-1.2/>). The upstream wordfreq documentation currently identifies the research citation as v3.0.2 (Zenodo DOI 10.5281/zenodo.7199437); that is a package citation, not proof that a particular local data file was used here. SUBTLEX-CH is the 2010 release described in the cited paper; the November 2025 HSK syllabus is the relevant edition. The actual wordfreq and SUBTLEX data files were not downloaded or hashed for this pilot, so no dataset-specific values are claimed. Before using source ranks, record the exact download URL, retrieval date, release/version, file hash, license text, and transformation script.

Research access is not redistribution permission. In particular, a research download, a paper's open-access license, and a permissive license on third-party code are not interchangeable with rights to republish the underlying lexical tables or source fiction.

## Identity and candidate protocol

**The CSV's `cmn:<simplified-form>:<POS>` identifiers are provisional candidate keys, not finalized stable lexeme IDs.** They embed mutable analyses (word class and orthography), which can change during adjudication. For example, 这里/那里 are locatives rather than ordinary nouns, while 安全 has adjectival and nominal uses. Before expanding imports, adopt immutable IDs independent of POS labels and assign them consistently to lexical tiddlers and the source ledger; preserve previously assigned IDs on future metadata edits. Traditional variants should map to the same lexical record when appropriate; POS-distinct or unrelated homographs may warrant separate entries, while polysemous senses can share an entry when their grammar/teaching behavior is shared. Heteronyms need clear reading-specific treatment; separable verbs need construction notes; productive phrases should not be counted automatically. The revised ID convention must be specified and tested before scale.

The attached CSV has 200 unique simplified-form candidates across four provisional strata: 50 fundamental, 47 high-use, 53 high-availability, and 50 wuxia/xianxia. Cross-category duplicates were counted once and assigned to the first applicable stratum. Repeated occurrences across genres are one candidate, not multiple counts. “Provisional” is deliberate: source ranks, HSK editions/levels, frequency bands and coverage are not fabricated. Review confidence is a triage estimate, not a claim of corpus verification.

## Pilot import

Twenty-five new entries were prepared as independent vocabulary tiddlers, each with an original example and no lesson assignment. The existing 30 vocabulary entries were checked for exact-form duplicates before selecting the pilot. Existing lesson assignments and lesson indexes were not changed. The validator accepts omitted `mandarin-lessons` while rejecting unresolved supplied IDs.

After editorial audit, **all 25 imported records have their `mandarin-lexical-band` field omitted** until their corpus and availability evidence is reviewed. Each carries `mandarin-review-status: editorial-reviewed; band-unverified`. The source candidate pool retains its clearly marked *provisional* band proposals. An entry's lack of lesson assignment does not make it incomplete.

## Second test batch

A second 20-entry batch has been added in a separate pull request for review. Its records are editorially reviewed, unassigned to lessons, and marked `band-unverified`; the batch ledger retains provisional candidate strata without asserting frequency or HSK status. Across both pilot batches, the working repository contains **45 imported entries**, **45 unassigned**, **0 lesson-assigned**, and **0 with a verified lexical-band field**. No coverage claim is made.

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

The initial Work session had no local clone or runnable Node/TiddlyWiki environment, so it could not run local tests. Subsequently, PR validation was added in `.github/workflows/validate-pr.yml` and successfully ran `python3 scripts/validate_wiki.py`, unit tests, the pinned TiddlyWiki static build, and output checks against the proposed branch. See [PR #2](https://github.com/heatwaveqc/D-s-Mandarin-Time/pull/2) for the latest check result. These automated checks establish technical consistency, not native-level linguistic verification.

## Editorial linguistic audit and provenance disposition — 2026-11-11

Scope: individually inspected all 25 new `Vocabulary/*.tid` records for simplified/traditional orthography, displayed Pinyin and neutral-tone/sandhi treatment, POS and sense glosses, the Hanzi–Pinyin–English correspondence of examples, register, and usage guidance. This is an **editorial/linguistic audit, not independent native-speaker verification or full independent dictionary crosschecking of every sense**. Representative externally checked questions included the distinct traditional graph 幾 for 几 (jǐ), the restaurant/hotel senses of 饭店, and wordfreq/SUBTLEX provenance. Original examples were retained or revised; dictionary wording was not reproduced.

| Item(s) | Editorial outcome |
|---|---|
| 休息、学生、早上、晚上、朋友、谢谢 | Kept common neutral-tone readings; clarified word-specific usage rather than generic boilerplate. |
| 再见 | Replaced stilted contextual example with a conventional direct farewell. |
| 写、同学、老师、茶、问 | Readings and example correspondences acceptable; clarified collocation and syntactic behavior. |
| 几 | Distinguished interrogative/quantifying use and traditional 幾 from 几 (jī, 'small table'); marked numeral function as well as interrogative. |
| 多少 | Clarified quantitative versus price questions and the contrast with 几. |
| 家、工作、请 | Added specific notes on classifier, noun/verb, and polite-verb uses, respectively. |
| 对不起 | Narrowed 'excuse me' to the apologetic use, distinguishing 请问 for attracting attention. |
| 忙 | Clarified stative adjectival predicates and the non-intensifying use of 很. |
| 明天、昨天 | Clarified time-adverbial syntax and lack of verbal tense inflection. |
| 水 | Clarified measure phrase 一杯 and tone-sandhi transcription. |
| 没关系 | Distinguished conversational reassurance from literal 'no relation'. |
| 读 | Corrected misleading 'study aloud': 读 is 'read; study' contextually; 朗读 explicitly means read aloud. |
| 饭店 | Retained both restaurant and hotel senses; revised example to naturally foreground restaurant meaning. |

Every imported record is **unassigned to lessons**. No frequency band is currently asserted as final in any of these 25 tiddlers. This is deliberate: the pilot's originally proposed 14 fundamental, 10 high-use, and 1 high-availability labels were not supported by verified source ranks or an adjudicated high-availability procedure. They may be reconsidered when source evidence is available.

### Additional checks on the 200-entry candidate inventory

- Fixed five clear traditional-form transcription errors: 我们 → 我們, 听 → 聽, 会 → 會, 门 → 門, 规矩 → 規矩.
- Improved the candidate glosses for 比武 (verbal use), 山庄 (broader estate/guesthouse sense), and 心法 (method/principles, not only cultivation).
- Marked locative POS concerns for 这里 and 那里, and adjectival/nominal polyfunctionality for 安全. Their old POS-derived candidate IDs demonstrate why immutable lexeme IDs are a prerequisite for scale.
- The pool's 50 / 47 / 53 / 50 candidate strata and 200 distinct simplified forms are **editorial sampling**, not a frequency- or uniqueness-adjudicated 200-lexeme selection. It overlaps intentionally with existing textbook entries and with the 25 pilot entries; overlaps must never produce second lexeme records.
- Common words placed under the wuxia stratum (e.g., 剑, 刀, 毒药, 决斗, 报仇) require general-versus-genre band reassessment. Wuxia relevance is not evidence that a word belongs to the **additional** specialist quota. Proper names such as 武当, 少林, and 峨眉 need a separate explicit policy before counting toward lexical targets. 长剑 requires lexicalization review rather than automatic inclusion as a compound. The broad 'high-availability' group likewise contains likely high-frequency items and needs its own selection evidence.

### Source and licensing result

- **This pilot's public content:** provisional original editorial candidate metadata and example sentences. No downloaded wordfreq or SUBTLEX-CH frequency rows, HSK standard tables, or novel excerpts are redistributed. The immediate public pilot therefore does not depend on an unverified right to republish those source datasets.
- **Future use of wordfreq:** the upstream [NOTICE](https://github.com/rspeer/wordfreq/blob/master/NOTICE.md) requires explicit credit to Robyn Speer, source acknowledgments including SUBTLEX authors, and compliance with applicable CC BY-SA 4.0 data terms. Freeze the exact code/data release, notice and transformation script before committing frequency-derived metadata.
- **Future direct use of SUBTLEX-CH:** the [Ghent resource page](https://www.ugent.be/plone_portal/pp/experimentele-psychologie/en/research/documents/subtlexch/overview.htm) and [Cai & Brysbaert (2010)](https://doi.org/10.1371/journal.pone.0010729) authorize/reference research access and citation, not a clearly documented blanket redistribution grant for direct table rehosting. Seek explicit terms or publish independently authored conclusions without copied tables.
- **HSK and genre resources:** HSK mappings remain blank pending edition-specific entry checks. Third-party transcriptions and copyrighted fiction are not import-ready redistribution sources merely because readable online.

**Decision:** GO for merging this **bounded, editorially reviewed infrastructure/content pilot** after successful branch CI. **CONDITIONAL GO** only for further small curated batches. **NO-GO for the full 7,000 + 1,000–2,000 import** until immutable lexical IDs, per-source licensing/provenance manifests, reproducible ranking and held-out segmentation/coverage methods, and a native/independent adjudication process are established.
