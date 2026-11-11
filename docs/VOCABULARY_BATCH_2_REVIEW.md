# Vocabulary import pilot — batch 2 (everyday concrete vocabulary)

Date: 2026-11-11. This is a second, 20-entry test batch drawn from the existing 200-entry candidate pool. It tests familiar objects, services, transport, food, and weather terms, especially traditional-form mapping and neutral-tone notation. Every entry remains unassigned to lessons.

## Provenance and rights

For orthographic/traditional-form, pronunciation, broad part-of-speech, and sense checks, consult the current searchable CC-CEDICT editor/database (CC BY-SA 4.0; <https://cc-cedict.org/editor/editor.php?handler=Main>, license/download page <https://cc-cedict.org/editor/editor.php?handler=Download>), accessed 2026-11-11. The public site describes its search as the latest version, but this pass did not download or hash a dated release snapshot. Thus this ledger records date and licensing but cannot claim an immutable version/hash. The glossary and examples in tiddlers are original editorial text; no CC-CEDICT example sentence or extended definition is reproduced. CC-CEDICT license and attribution details are recorded so a later source-derived table can be handled separately.

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
