# Candidate Mandarin Lexical Sources — research survey (2026-11-11)

Status: **desk review only**. No datasets imported or merged into curriculum.

Purpose: identify an existing foundation for a three-tier 7,000-word general Mandarin list, plus 1,000–2,000 additional wuxia/xianxia entries. See [Target Vocabulary Standard](VOCABULARY_TARGET_STANDARD.md) for binding criteria.

## Candidate sources, in recommended order

| Resource | Scope | Why it helps | Limitation / rights | Verdict |
| --- | --- | --- | --- | --- |
| **wordfreq (zh)** | Multiregister estimate from subtitles, books, Wikipedia, news and web | Cross-domain ranks, redistributable package/data with notices | Aggregate not speech-only; Chinese segmentation and opaque mixed-source weighting require scrutiny; cites imperfectly sourced Jieba wordlist | **Preferred general-rank backbone** |
| **SUBTLEX-CH** (Cai & Brysbaert 2010) | 33.5m words / 46.8m characters of film/TV subtitles; PoS and character data | Conversational word frequency, contextual diversity; freely downloadable integrated PoS/pinyin/English edition | Media from ~2010, subtitle register bias; paper says freely available for research: check conditions for reposting frequency tables | **Primary conversational benchmark** |
| **HSK 2025 exam syllabus** | 11,000 numbered entries, Pinyin, PoS, HSK levels; a public TSV also gives ~593 grammar points | Definitive independent pedagogical crosswalk for curriculum; far wider than 7k | **Not** a frequency list. Distinguish the 2025 examination syllabus from 2021 grading standard (~11,092) and legacy 2.0 list. Transcriber acknowledges underlying source rights | **Required overlay, not ordering** |
| **Richard Xiao (2009), A Frequency Dictionary of Mandarin Chinese** | 5,000 most frequent words and 2,000 characters from ~50m-word corpus of speech, fiction, nonfiction, news | Excellent multisource control and sample sentences | Commercial publication; don't bulk scrape/reproduce | **Manual audit / triangulation** |
| **Sinica Chinese Core Vocabulary 1.0** | 1,121 words shared by top-2k written and top-2k Taiwan conversation lists | Strong spoken/written core concept with POS and examples | **Paid application** to ACLCLP; research-only license; dialectal/register differences | **Methodology reference, not ingestion source** |
| **Sense-aware Chinese Vocabulary Resource (2026)** | 7,542 word entries; 24,394 senses; 37-textbook and People's Daily samples | Unusually close to target count; sense frequency and educational focus | Not a balanced everyday/general corpus; rights to original dictionary and news content **not conveyed by MIT license on code** | **Interesting experimental corroboration** |
| **Wuxia/xianxia corpus study** (Zhang/Liu/Zhang 2020) | Academic comparison of two literary genres using corpus frequency/style/topic methods | Validates necessity of a specific genre supplement | Study is not an openly licensed 1–2k word list; no evidence sampled corpus may be redistributed | **Method for genre candidate generation** |

## Hard empirical finding: coverage is register-sensitive

Shu-Chuan Tseng (2013) measured 405,435 tokens of Taiwan conversational Mandarin and 4,767,048 tokens in the Sinica written balanced corpus. With **separate rank lists**:

| Top N types | Conversation token coverage | Written corpus token coverage |
| ---: | ---: | ---: |
| 1,000 | 84.43% | 59.78% |
| 2,000 | 89.87% | 68.69% |
| 3,000 | 92.53% | 73.53% |
| 5,000 | 95.34% | 79.17% |
| 7,000 | 96.95% | 82.55% |
| 9,000 | 97.94% | 84.92% |
| 10,000 | 98.35% | 85.87% |

Source: https://aclanthology.org/O13-2001.pdf Table 4, page 10. **Do not transfer these figures to the planned mixed 7k list without evaluating it**, and do not treat the Taiwanese data as an exact modern Mainland benchmark.

The freely available 1,121-item Sinica core intersects the written and spoken top-2k lists and covers 57.6% of its written corpus and 86.1% of its conversational corpus; however, its license is paid and research-restricted: https://www.aclclp.org.tw/use_sccv.php.

## Data / license links to check before importing

**wordfreq**  
https://github.com/rspeer/wordfreq  
https://github.com/rspeer/wordfreq/blob/master/NOTICE.md  
Its code license is Apache, and data may include CC BY-SA 4.0; the author documents special permission for redistributing SUBTLEX-based data, with attribution requirements. Preserve attribution if rankings are reused.

**SUBTLEX-CH**  
https://www.ugent.be/pp/experimentele-psychologie/en/research/documents/subtlexch  
https://doi.org/10.1371/journal.pone.0010729  
Integrated release supplies word frequencies, PoS, Pinyin and frequent English translations. Citation required; rights statement checked before public bulk rehosting. Useful as independent evidence even if not republished.

**HSK examination edition 2025**  
https://github.com/uranbekanarbaev/hsk-3.0-vocabulary-dataset/blob/main/SOURCES.md  
https://github.com/chelsea6502/hsk-2025-data  
The first project has the original 11,000-numbering and PDF page IDs; the second provides grammar TSV too. Both are third-party transcriptions; consult source rights before copying all entries. Official content and exam publication schedules are distinct.

**Sense-aware 7,542-word resource**  
https://github.com/fulan233/Sense-aware-chinese-vocabulary-resource  
Description: 7,542 lexical entries and 24,394 candidate senses, based largely on 2021 Chinese proficiency standard plus frequency extensions; 37 textbooks and a stratified sample from People's Daily. The authors restrict original dictionary/news corpora and disclaim third-party redistribution rights. Treat as research/analysis rather than a ready-to-republish master dictionary.

**Wuxia/Xianxia genre study**  
https://aclanthology.org/2020.ccl-1.2/  
Sanle Zhang, Pengyuan Liu, and Hu Zhang (2020). *A Corpus-based Contrastive Analysis of Style, Vocabulary and Theme of Wuxia and Xianxia Internet Novels.* Demonstrates genres share and differ in lexicon. Not a published 1k-2k open list.

**Paid comparison**  
https://www.routledge.com/x/x/p/book/9780415455862  
Richard Xiao (2009). A Frequency Dictionary of Mandarin Chinese: Core Vocabulary for Learners, based on a 50m-word balanced corpus with 5,000 words.

## Conclusion

**Do not start from a blank slate. Do not simply import the first 7,000 HSK entries.** There are enough suitable pre-existing candidates to seed the general tiers. The missing deliverable is a **curated, multi-register, license-aware, deduplicated Mandarin “De Mauro style” list**, especially the nonfrequency high-availability band and the specialized wuxia/xianxia layer.

## Next proposed work package (Work)

1. Rights/provenance audit of wordfreq + SUBTLEX-CH + HSK 2025, plus source version hashes and date.
2. Build one candidate pool of 200 entries with columns: simplified, traditional (optional), Pinyin, part of speech, unique lexical ID, subtlex rank, wordfreq rank/Zipf, HSK 2025 level, tentative band, high-availability flag, wuxia relevance, confidence/provenance.
3. Apply deduplication and segmentation review; compare sampled ranks against Xiao (manual reference only).
4. Hold out samples across spontaneous speech, contemporary written, and wuxia material. Establish reproducible coverage method before claiming any achieved percentage.
5. After review, expand to 7k + 1–2k and partition into grammar-led lessons (see Work guide).

The curriculum standard is fixed; list membership, coverage claims and distribution across settings **must be measured**.
