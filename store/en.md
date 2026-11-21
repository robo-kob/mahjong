---
title: "Store texts (English)"
published: false
---

# Store texts English – template for App Store Connect

Not for visitors (`published: false`; the folder is also excluded in `_config.yml`).
Each text is in its own block and is copied into App Store Connect as is.
Lengths are checked by `python3 store/pruefe_laengen.py` (table at the end).
Limits per App Store Connect Help, “Platform version information” and “App information”, checked on 2026-11-21.

## Name – max. 30 characters

Working title, placeholder.

```text
Mahjong Meister
```

## Subtitle – max. 30 characters

Option A (matches „Ruhig spielen. Ohne Werbung.“):

```text
Play calmly. No ads.
```

Option B (matches „Der ruhige Weg zum Meister“):

```text
The Calm Path to Mastery
```

## Promotional text – max. 170 characters

```text
Calm Mahjong in four modes – no ads, no subscription, no internet. Tiles traditional or unusual: the Zodiac in ink, Birds, Animals or a colorful mix.
```

## Description – max. 4000 characters

```text
A calm Mahjong game to unwind with. No ads, no subscription, no tracking – and no internet needed.

FOUR MODES
– Classic: find pairs among the free tiles until the board is empty.
– Classic with Tray: like Classic, with a small tray for parking single tiles.
– Triple Match: collect three matching tiles in the tray before it fills up.
– Shisen-Sho: connect matching tiles with a line that bends at most twice.
Every game is solvable.

THE PATH TO MASTERY
Each mode has its own path: 60 levels through changing landscapes, with up to three stars per level. After level 60 the Gate of Masters opens, and behind it 20 Master Trials await, where your best time counts.

ON THE SIDE
– Daily Challenge: a new level in each mode every day, with a calendar.
– Free Play: choose a mode and a difficulty, then play new games again and again – no stars, no best time. Shisen-Sho with gravity if you like.

TILES TO YOUR TASTE
Traditional Mahjong tiles or something different: the Chinese zodiac in ink and as red seals, colorful birds, playful animals, space – or a colorful mix of everything. Choose your own set for each mode.

CALM BY DESIGN
In the style of Japanese ink painting, with calm music and soft sounds. Light and dark, German and English.

ASSISTS WHEN YOU NEED THEM
Undo, hint and shuffle – limited per level, with no currency and no ads.

FOR EVERYONE
Supports VoiceOver, Larger Text and Reduce Motion.

YOUR DATA STAYS WITH YOU
No accounts, no tracking, no analytics. Your progress is stored only on your iPhone.
```

Optional paragraph – add only once the purchase is built into the app (count it then):

```text
Download for free and try everything for 14 days. After that, a one-time purchase unlocks the app for good. No subscription.
```

## Keywords – max. 100 bytes

Comma-separated, no space after the comma, without the app name, without third-party brand names. Each keyword longer than two characters.

```text
solitaire,tiles,pairs,puzzle,zen,relaxing,offline,brain,board game,triple match,shisen-sho,calm
```

## What's New (0.8.x) – max. 4000 characters

```text
– Free Play: choose Easy, Medium or Hard in any mode and play new, solvable games again and again – no stars, no best time.
– Shisen-Sho: you can now also connect pairs by dragging. In Free Play, with gravity if you like.
– New tile sets: “Zodiac” in ink and seals, the playful “Animals” and the “Mix” of all picture sets.
– “All Tiles”: view every tile set at a large size in Settings.
– Home screen in two groups: “The Path to Mastery” and “On the Side”.
– New music and many small improvements.
```

## Store screenshots (suggestion)

Suggestion only; the real store screenshots will be made for 1.0.

1. **Home screen** – “Calm play, in four modes.”
2. **Classic with traditional tiles** – “Mahjong as you know it.”
3. **Path with the Gate of Masters** – “60 levels to the Gate of Masters.”
4. **Triple Match with tray** – “Collect three of a kind.”
5. **Shisen-Sho with connecting line** – “Connect with at most two bends.”
6. **Board with the “Zodiac” tile set** – “Tiles to your taste: the Zodiac in ink.”
7. **Board with the “Animals” tile set** – “Or playful: Animals.”
8. **Daily Challenge with calendar** – “A new level every day.”

## URLs

- Support URL: https://robo-kob.github.io/mahjong/en/support/
- Privacy policy URL: https://robo-kob.github.io/mahjong/en/privacy/

## Lengths

<!-- laengen:start -->

| Feld | Länge | Grenze | Einheit | ok |
|---|---:|---:|---|---|
| Name | 15 | 30 | Zeichen | ✔ |
| Subtitle | 20 | 30 | Zeichen | ✔ |
| Subtitle (2) | 24 | 30 | Zeichen | ✔ |
| Promotional text | 149 | 170 | Zeichen | ✔ |
| Description | 1519 | 4000 | Zeichen | ✔ |
| Description (2) | 124 | 4000 | Zeichen | ✔ |
| Description mit optionalem Absatz | 1645 | 4000 | Zeichen | ✔ |
| Keywords | 95 | 100 | Byte | ✔ |
| What's New (0.8.x) | 497 | 4000 | Zeichen | ✔ |

<!-- laengen:end -->
