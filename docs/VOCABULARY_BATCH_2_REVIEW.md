# Vocabulary import pilot — batch 2 (everyday concrete vocabulary)

Date: 2026-11-11. This is a second, 20-entry test batch drawn from the existing 200-entry candidate pool. It tests familiar objects, services, transport, food, and weather terms, especially traditional-form mapping and neutral-tone notation. Every entry remains unassigned to lessons.

## Provenance and rights

Candidate selection came from the existing editorial pool; this pass does not claim to have used a frozen lexical dataset. The CC-CEDICT editor describes the data as CC BY-SA 4.0 and exposes a current searchable database (editor: <https://cc-cedict.org/editor/editor.php?handler=Main>; license/download: <https://cc-cedict.org/editor/editor.php?handler=Download>). Its latest online edition was considered as a reference for spot checks, but the database was not downloaded or hashed, and per-entry source citations are not asserted. This batch's definitions and examples are original editorial text; no CC-CEDICT definitions, examples, or ranking data were copied. Future source-derived tables must preserve the edition, date, attribution, and ShareAlike obligations.

The candidate pool remains editorially selected; no wordfreq or SUBTLEX ranks and no HSK classification were added. This is not a frequency-ranked list. Exact source-specific frequency values remain blank.

## Language review

The batch received a manual Mandarin review for simplified/traditional correspondence, Pinyin, broad POS, sense boundaries, and example naturalness. This review is editorial, not a two-linguist adjudication. Notes:
- 衣服 (yīfu) and 钥匙 (yàoshi) commonly have a neutral-tone final syllable in Mainland speech. 饭馆 (fànguǎn), 面条 (miàntiáo), and 眼镜 (yǎnjìng) retain full lexical tones.
- 雨伞 has underlying third-third tones; the written Pinyin remains yǔsǎn. In ordinary connected speech the first syllable is subject to third-tone sandhi.
- 眼镜 “glasses” and 眼睛 “eyes” are near-form neighbors but distinct lexical entries; only 眼镜 is in this batch.
- 电话 may denote a telephone or a phone call; both are noted. 地址 is a location/postal address. 饭馆 means restaurant; it is not conflated with 饭店, whose regional/contextual use may include “hotel.”
- Traditional forms are separately recorded even where they match simplified characters.

## Records and decisions

The accompanying CSV is the entry-level provenance and uncertainty ledger. All 20 are candidate-pool matches, all unassigned, and all still reviewable. No duplicate headword exists in the repository as of the branch base. Band values are tentative candidate strata only; they are not supported by frequency counts.

## Validator and scaling

No validator/schema change is required. Entries omit `mandarin-lessons`, which is allowed by the existing contract. The batch PR is intended to run the repository's validator, unit tests, and static build. The single-file wiki architecture remains unbenchmarked at 8–9k records; keep the earlier scale benchmark as a gate before mass import.

## Follow-up editorial audit (2026-11-11)

The second batch was merged through PR #4 and its GitHub Actions validation and deployment passed. A subsequent 20/20 tiddler review confirmed the simplified/traditional forms, primary Pinyin readings, glosses, and example alignment were broadly sound. We identified **10** boilerplate usage notes that did not teach a word-specific contrast or collocation; all ten were replaced with targeted notes in a separate review PR. The duplicated hospital/doctor example was differentiated, and the two examples depicting a supermarket purchase of cooked rice (`米饭`) were replaced with more ordinary contexts for `超市` and `鸡蛋`. The `米饭` entry itself correctly uses an eating context and remains unchanged.

The accompanying 20-row CSV continues to label all source-frequency bands as **tentative**; none of the tiddlers asserts a final band or individual HSK level. CC-CEDICT officially publishes its data under CC BY-SA 4.0 and recommends downloading a release through MDBG for a reproducible snapshot (<https://cc-cedict.org/editor/editor.php?handler=Download>). No CC-CEDICT tables, definitions, or example text were copied into this batch. Future ingestion must record a dated source version/hash, per-record review evidence, and license notices when actual data are reused.

**Follow-up disposition:** Linguistically acceptable for a limited pilot after these editorial corrections, but this still does not satisfy the scale gates: immutable lexical IDs; fully versioned, license-safe frequency evidence; adjudicated band assignment; and independent pronunciation/sense/regional review remain unresolved. Do not count tentative high-availability strata as proven native-availability categories.
