# Audio asset contract (pilot)

## Demonstrated pipeline

A human Mandarin recording from Wikimedia Commons is copied unchanged as a small Ogg Vorbis file by the GitHub Actions runner, checked by ffprobe and committed once to `assets/audio/nihao.ogg`. The build copies audio files to `public/audio`, so the static site and its downloadable offline HTML artifact can reference `audio/nihao.ogg`.

Audio is referenced from the vocabulary page with HTML5:

```html
<audio controls="controls" preload="none" src="audio/nihao.ogg"></audio>
```

Keep metadata fields:
- `mandarin-audio: audio/<filename>.ogg`
- `mandarin-audio-status: human-credited | tts-reviewed | synthetic-unverified`
- `mandarin-audio-license: <SPDX-style license identifier>`

Only *reviewed* material belongs in pedagogical listening and tone tests. Files produced by eSpeak on the available local runtime are not approved as pronunciation references because the Mandarin pronunciation dictionary was incomplete. This pilot proves storage, conversion and playback; it does not prove the ability to produce 7,000 high-quality TTS clips.

## Attribution

- Recording: “Zh nǐ hǎo.ogg” (你好, nǐ hǎo).
- Author: Sjors Provoost (2011-02-15).
- Source: https://commons.wikimedia.org/wiki/File:Zh_n%C7%90_h%C7%8Eo.ogg
- License: CC BY-SA 3.0 — https://creativecommons.org/licenses/by-sa/3.0/
- Change: none; the original Ogg Vorbis audio is preserved.
- Derived sound file: `assets/audio/nihao.ogg`, still CC BY-SA 3.0.

Do not remove attribution. If later sources are imported, verify rights and record file-level provenance.
