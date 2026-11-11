# D's Mandarin Time

A grammar-first Mandarin learning wiki, built with [TiddlyWiki](https://tiddlywiki.com/).

**Architecture:** separately stored, UTF-8 TiddlyWiki `.tid` files; GitHub Actions builds a self-contained static `index.html` and publishes it to GitHub Pages. No server or local Node.js installation is required to *read* the site.

This repository is intentionally independent of GATES, while following the same modular tiddler approach.

## Browsing and deployment

- Once GitHub Pages is configured to use **GitHub Actions**, browse `https://heatwaveqc.github.io/D-s-Mandarin-Time/`.
- The wiki is browser-only and **read-only as a canonical source**: browser edits won't be saved back to this repository.
- Each push to `main` checks content integrity and rebuilds the static site.
- To build locally (optional): `npx --yes tiddlywiki@5.4.1 . --build index` (output `public/index.html`).

## Content model

- `tiddlers/Navigation`: front page, indexes, course map, study instructions.
- `tiddlers/Grammar`: independently linked grammatical concepts and prerequisites.
- `tiddlers/Vocabulary`: word-level entries with hanzi, pinyin, POS, gloss, usage and example.
- `tiddlers/Characters`: character-level semantic/phonetic decomposition with an etymology-confidence note.
- `tiddlers/Lessons`: reusable lesson assemblies, learning objectives, dependencies.
- `tiddlers/Readings`: controlled reading passages with pinyin and gloss.
- `tiddlers/Exercises`: written assessments and answer keys.
- `tiddlers/System`: wiki title, default tab, helper templates.

All *course* records use `mandarin-kind` and `mandarin-level`. Vocabulary has `mandarin-hanzi`, `mandarin-pinyin`, `mandarin-gloss`, and `mandarin-pos`. Grammar and lessons can specify `mandarin-prerequisites` as a TiddlyWiki title list, e.g. `[[Grammar/SVO Word Order]] [[Grammar/Predicate Negation]]`. Field names use the `mandarin-` prefix to avoid conflicts with TiddlyWiki internals.

Use real grammatical descriptions, give pinyin on all new Chinese example sentences, and avoid presenting character-component mnemonics as guaranteed etymologies.

The wiki holds shared course material. **Do not commit sensitive personal speech recordings, private student data, or individually identifying assessment results to this public repository.** Learner progress can be maintained locally or in an access-controlled Drive sheet.

## Adding material

1. Add one `.tid` file under the appropriate content directory with a unique `title`, `type: text/vnd.tiddlywiki`, `tags`, and canonical metadata.
2. Link using tiddler titles; prefer linking to concepts rather than copying their explanations.
3. Run `python3 scripts/validate_wiki.py` and (optionally) the TiddlyWiki build.
4. Commit to `main`; deployment runs automatically when Pages is enabled.

See [[Wiki Guide]] in the published site for the browsing workflow and links among content types.
