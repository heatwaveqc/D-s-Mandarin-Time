# Vocabulary import pilot — batch 2 (everyday concrete vocabulary)

Date: 2026-11-11. This is a second, 20-entry test batch drawn from the existing 200-entry candidate pool. It tests familiar objects, services, transport, food, and weather terms, especially traditional-form mapping and neutral-tone notation. Every entry remains unassigned to lessons.

## Provenance and rights

Candidate selection came from the existing editorial pool; this pass does not claim to have used a frozen lexical dataset. The CC-CEDICT editor describes the data as CC BY-SA 4.0 and exposes a current searchable database (editor: <https://cc-cedict.org/editor/editor.php?handler=Main>; license/download: <https://cc-cedict.org/editor/editor.php?handler=Download>). Its latest online edition was considered as a reference for spot checks, but the database was not downloaded or hashed, and per-entry source citations are not asserted. This batch's definitions and examples are original editorial text; no CC-CEDICT definitions, examples, or ranking data were copied. Future source-derived tables must preserve the edition, date, attribution, and ShareAlike obligations.

The candidate pool remains editorially selected; no wordfreq or SUBTLEX ranks and no HSK classification were added. This is not a frequency-ranked list. Exact source-specific frequency values remain blank.

## Language review

The batch passed a manual Mandarin review for simplified/traditional correspondence, Pinyin, broad POS, sense boundary, and example naturalness. Notes:
- 衣服, 钥匙, 鞋, 饭馆, 面条 and 眼睛 commonly have a neutral-tone final syllable in ordinary Mainland pronunciation. Pinyin shows the lexical neutral tone rather than inventing tone-sandhi spellings.
- 雨伞 has underlying third-third tones; the written Pinyin remains yǔsǎn. In ordinary connected speech the first syllable is subject to third-tone sandhi.
- 眼镜 “glasses” and 眼睛 “eyes” are near-form neighbors but distinct lexical entries; only 眼镜 is in this batch. The pilot separates body-part and object senses.
- 电话 may denote a telephone or a phone call; both are noted. 地址 is a location/postal address. 饭馆 means restaurant; it is not conflated with 饭店, whose regional/contextual use may include “hotel.”
- Traditional forms are separately recorded even where they match simplified characters.

## Records and decisions

The accompanying CSV is the entry-level provenance and uncertainty ledger. All 20 are candidate-pool matches, all unassigned, and all still reviewable. No duplicate headword exists in the repository as of the branch base. Band values are tentative candidate strata only; they are not supported by frequency counts.

## Validator and scaling

No validator/schema change is required. Entries omit `mandarin-lessons`, which is allowed by the existing contract. The batch PR is intended to run the repository's validator, unit tests, and static build. The single-file wiki architecture remains unbenchmarked at 8–9k records; keep the earlier scale benchmark as a gate before mass import.
