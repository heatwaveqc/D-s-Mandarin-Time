# Lexical identity, provenance, and evidence contract — v1.0

Adopted: 2026-11-11. Canonical repository: \`heatwaveqc/D-s-Mandarin-Time\`.

This contract concerns the **independent lexical inventory**, not the lesson prerequisite graph. Every public vocabulary record now has an immutable ID, explicit editorial/source attribution, and validated research references. The validator establishes **data integrity**, not the correctness of its linguistic claims.

## Lexeme identity

- Each \`mandarin-kind: vocabulary\` tiddler requires a unique \`mandarin-lexeme-id: lx-NNNNNN\`, using six decimal digits. The opaque number **never encodes Hanzi, Pinyin, part of speech, sense, lesson, or frequency band**. Examples: \`lx-000020\` belongs to the already-existing 师父 record; it must never be reassigned.
- IDs are allocated sequentially from the highest ever reserved ID. The 76 pre-infrastructure entries were backfilled \`lx-000001\` through \`lx-000076\` on 2026-11-11; the next new entry is \`lx-000077\`. The backfill order is an arbitrary migration order, **not a rank or lesson order**.
- \`research/lexeme-id-registry.csv\` binds each ID to one active source tiddler path. New IDs require **both** a \`.tid\` metadata addition and a registry row in the same PR. The PR history check disallows removal/reuse of previously allocated IDs and nonsequential allocation.
- An editorial change to pronunciation, traditional/simplified form, gloss, POS, register, or lesson assignments **does not change the existing ID**. If a file is renamed/moved, retain the ID and update its registry path with a \`moved:\` note explaining the migration. Reviewers must assess whether the same lexeme is still represented.
- If a record must be permanently discontinued, reserve the old ID as \`retired\` with an empty tiddler path, and document why in \`notes\`. Its ID cannot be reused. For a genuine split into two lexical entries, retain one identity only where justified, allocate a **new** ID for the new lexical entity, and record the editorial reasoning.
- \`research/vocabulary-candidate-pool-200.csv\` contains historical experimental \`cmn:<form>:<POS>\` **candidate keys**; **they are not registered lexeme IDs**, must not be copied into \`mandarin-lexeme-id\`, and should not be used as stable references. When promoting a candidate to the wiki, first search existing records by simplified/traditional/Pinyin/sense and reconcile duplicates.
- Orthographic homographs need not share an ID: e.g. a genuinely unrelated reading/sense or POS-separated lexical item may require its own, but do not split ordinary polysemy simply because one headword has multiple dictionary glosses. Review heteronyms, separable verbs, productive compounds, and proper names explicitly. One lexeme may occur in multiple registers or genres without duplicate IDs.

## Metadata required for every vocabulary tiddler

\`\`\`text
title: Vocabulary/师父
type: text/vnd.tiddlywiki
tags: [[Mandarin Vocabulary]]
mandarin-kind: vocabulary
mandarin-level: beginner
mandarin-lexeme-id: lx-000020
mandarin-source-ids: curriculum-editorial
mandarin-hanzi: 师父
mandarin-pinyin: shīfu
mandarin-gloss: master; respected mentor
mandarin-pos: noun
mandarin-lessons: L01 L03
\`\`\`

This is an **existing-entry example**, not a template ID to reuse. New unsequenced vocabulary typically uses \`mandarin-level: reference\` and **omits \`mandarin-lessons\`**. Preserve existing lesson links; a lexicon entry may exist indefinitely without any.

\`mandarin-source-ids\` is a whitespace-separated list of known IDs from the source registry. \`curriculum-editorial\` identifies an independently written **editorial text provenance**, not a claim that source frequency, syllable tones, or senses have been externally verified. Credit human-produced audio and quoted source materials separately under their applicable license.

## Source registry and reuse decisions

\`research/lexical-sources.json\` contains versioned sources with stable \`id\`, \`kind\`, \`source_url\`, \`license\`, \`reuse_status\`, \`release\`, \`sha256\` and \`accessed\` fields. Public research records may cite sources without copying their data.

Allowed \`reuse_status\` values:

- \`editorial-original\`: content authored for this project; no outside frequency/HSK authority implied.
- \`reference-only\`: consulted for checking facts, with no copied entries/tables.
- \`research-reference-only\`: accessible for analysis, but public data reuse unconfirmed.
- \`not-yet-approved\`: rights/release verification outstanding.
- \`redistribution-approved\`: public data reuse explicitly assessed; exact release and 64-character SHA-256 are required.

Before marking any third-party source \`redistribution-approved\`, retain the exact downloaded release, acquisition date, checksum, license, upstream NOTICE, transformation code, and required attribution. A license on a **paper**, **software**, or **third-party transcription** does not automatically license an upstream table or fiction corpus. If permission is unclear, do not reproduce source-derived rank/HSK data in this public repository.

The initial manifest deliberately lists **wordfreq zh, SUBTLEX-CH, November 2025 HSK, and CC-CEDICT as reference/pending sources, not frozen approved datasets**. No frequencies or HSK levels have been imported from them. Reusing CC BY-SA data may impose attribution/ShareAlike obligations on the resulting derivative; obtain a compatible licensing decision first.

## Entry-level evidence ledger

\`research/lexical-evidence.csv\` is an append-and-review ledger, separate from published definitions. Its columns are:

\`\`\`csv
evidence_id,lexeme_id,source_id,claim_type,claim_value,review_status,reviewed_by,reviewed_on,notes
\`\`\`

Claim types include \`form\`, \`pronunciation\`, \`sense\`, \`register\`, \`frequency\`, \`hsk\`, \`availability\`, \`genre\`, and \`band\`. States: \`candidate\`, \`checked\`, \`verified\`. A \`verified\` record needs a reviewer and review date; that attests to a recorded editorial review, **not necessarily independent native-speaker adjudication**. Distinguish review methods and sources in notes.

A published \`mandarin-lexical-band\` now requires \`mandarin-band-evidence-id\` pointing to a **verified** \`band\` claim for the same lexeme and matching value. Likewise, \`mandarin-frequency-rank\` requires \`mandarin-frequency-evidence-id\` and \`mandarin-hsk-level\` requires \`mandarin-hsk-evidence-id\`, each matching a verified claim. Actual public frequency/HSK values require an approved, versioned, hashed source. This is a **technical minimum**; substantive category assignment must also follow [Vocabulary Target Standard](VOCABULARY_TARGET_STANDARD.md):

- Fundamental/high-use: triangulate corpus ranks, register mixture, and lexical identity; record source editions.
- High-availability: collect real native-availability/usefulness judgments; **low frequency alone is not evidence**.
- Wuxia-specialist: test that an item is genuinely additional to the general 7k rather than a common word with a genre context.
- Coverage: test held-out **spoken, written, and genre** corpora independently, with fixed segmentation rules.

The historical pilot CSVs contain **tentative candidate bands**, not \`mandarin-lexical-band\` field values. Leave that metadata absent until the evidence standard is met.

## Workflow and review roles

1. Work imports a small batch on a branch and opens a **draft PR**. **Work must not mark its own vocabulary PR ready or merge it**, even when technical checks pass, unless the user explicitly changes this instruction.
2. Work updates \`.tid\` records and the ID registry together; creates research evidence/source rows only when actually justified; never fabricates ranks, levels, citations or native review.
3. The GitHub PR workflow runs metadata/DAG validation, lexical registry/evidence validation, non-reuse checks against \`main\`, unit tests and the TiddlyWiki build with a read-only token.
4. The designated reviewer (assistant acting on the user's review request) inspects the linguistic claims, source provenance, rights and examples; corrects issues and reruns checks. **Only that reviewer** marks the draft ready and merges if satisfactory.
5. The existing \`main\` workflow automatically builds and deploys after merge. GitHub deletes merged branches when the repository setting is enabled; branch protection is not required for this agreement.

## Scale gates

This infrastructure is **not** a mass-import authorization. Before expanding from tens to thousands of records, settle the source versions/reuse rights and actual frequency lookup pipeline, adjudicate homographs and sense identity, create a documented sampling protocol for native review, and benchmark 8k–9k tiddlers for static build size and browser-side search. Accept technical validations as necessary, not sufficient.

The next test batch should concentrate on **heteronyms, polysemy, separable verbs, particles, and real wuxia/xianxia usage**, explicitly documenting disambiguation and register rather than repeating simple concrete nouns.
