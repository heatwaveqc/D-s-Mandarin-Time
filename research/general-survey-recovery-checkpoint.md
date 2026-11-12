# General survey recovery checkpoint (2026-11-12)

## State

The lost Work chat's reported general survey file could not be recovered. We reconstructed a reproducible candidate pool from pinned, licensed source snapshots and saved it in the project's private survey Drive folder as nine CSV shards. The data is intentionally not committed to this public repository while source and linguistic review remain open.

- Existing public PR seed: 230 candidates.
- Reconstructed general source candidates: 16,122, keys `cand-000231`–`cand-016352`.
- Combined general survey: 16,352 candidates, within the initial 14k–18k planning range.
- Checkpoints: eight 2,000-row batches and one 122-row batch.
- All reconstructed rows are `needs-review`; no new tiddlers, lesson assignments, or permanent lexeme IDs were created.
- Existing private genre supplement remains separate; general/genre overlap has not yet been reconciled.

## Source and method

- `wordfreq` 3.1.1 `zh` top-N ordering; source file hash and attribution are recorded in `research/lexical-sources.json`.
- MDBG CC-CEDICT snapshot dated 2026-11-11; source Pinyin/gloss fields are identified in the private batch records.
- Each candidate is a 2–8 Han-character form with an exact simplified-form match in CC-CEDICT, after deduplicating against the existing PR seed. The final included wordfreq rank is 22,185.
- Pinyin was converted from numbered notation to tone marks. POS labels are provisional mappings from the packaged Jieba tags; underlying Jieba list provenance is not fully known, so that source remains marked not-yet-approved.
- The survey is a mixed-source candidate pool, not independent speech/writing/genre frequency lists. No HSK mapping, native-speaker audit, or held-out coverage evaluation is claimed.

The source registry now records pinned releases, hashes, permissions, required attribution and remaining provenance limits. The private Drive checkpoint includes the batch files, generator, source snapshot files, method note and count/checksum manifest.

## Next review work

1. Review the Jieba POS source provenance and whether those provisional tags should remain in the survey.
2. Reconcile the genre candidates against the general pool and document overlap.
3. Run a stratified linguistic review for wordhood, segmentation, Pinyin, POS, gloss and proper-name handling.
4. Keep all records provisional until adjudicated; prune and freeze a separate accepted roster before allocating permanent lexeme IDs.
