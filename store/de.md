---
title: "Store-Texte (Deutsch)"
published: false
---

# Store-Texte Deutsch – Vorlage für App Store Connect

Nicht für Besucher (`published: false`, der Ordner ist zusätzlich in `_config.yml` ausgeschlossen).
Jeder Text steht in einem eigenen Block und wird so in App Store Connect kopiert.
Längen prüft `python3 store/pruefe_laengen.py` (Tabelle am Ende).
Grenzen laut App Store Connect Help, „Platform version information“ und „App information“, geprüft am 21.11.2026.

## Name – höchstens 30 Zeichen

Arbeitstitel, Platzhalter.

```text
Mahjong Meister
```

## Untertitel – höchstens 30 Zeichen

Vorschlag A:

```text
Ruhig spielen. Ohne Werbung.
```

Vorschlag B:

```text
Der ruhige Weg zum Meister
```

## Werbetext – höchstens 170 Zeichen

```text
Ruhiges Mahjong in vier Spielarten – ohne Werbung, ohne Abo, ohne Internet. Steine traditionell oder ausgefallen: Tierkreis in Tusche, Vögel, Tiere oder bunt gemischt.
```

## Beschreibung – höchstens 4000 Zeichen

```text
Ein ruhiges Mahjong-Spiel zum Abschalten. Keine Werbung, kein Abo, kein Tracking – und es braucht kein Internet.

VIER SPIELARTEN
– Klassisch: Finde Paare unter den freien Steinen, bis das Brett leer ist.
– Klassisch mit Ablage: wie Klassisch, mit einer kleinen Ablage zum Parken einzelner Steine.
– Triple Match: Sammle drei gleiche Steine in der Ablage, bevor sie voll ist.
– Shisen-Sho: Verbinde gleiche Steine mit einer Linie, die höchstens zweimal abknickt.
Jede Partie ist lösbar.

DER WEG ZUM MEISTER
Jede Spielart hat ihren eigenen Weg: 60 Level durch wechselnde Landschaften, bis zu drei Sterne je Level. Nach Level 60 öffnet sich das Tor der Meister, dahinter warten 20 Meisterprüfungen, in denen deine Bestzeit zählt.

ZWISCHENDURCH
– Tages-Challenge: jeden Tag ein neues Level in jeder Spielart, mit Kalender.
– Freies Spiel: Spielart und Stufe wählen, dann immer neue Partien – ohne Sterne und ohne Bestzeit. Shisen-Sho auf Wunsch mit Schwerkraft.

STEINE NACH DEINEM GESCHMACK
Traditionelle Mahjong-Steine oder etwas Ausgefallenes: der chinesische Tierkreis in Tusche und als rotes Siegel, farbige Vögel, verspielte Tiere, Weltraum – oder alles bunt gemischt. Für jede Spielart wählst du deinen eigenen Satz.

RUHIG GESTALTET
Im Stil japanischer Tuschemalerei, mit ruhiger Musik und sanften Klängen. Hell und dunkel, Deutsch und Englisch.

HILFEN, WENN DU SIE BRAUCHST
Rückgängig, Hinweis und Mischen – je Level begrenzt, ganz ohne Währung oder Werbung.

FÜR ALLE
Unterstützt VoiceOver, große Schrift und „Bewegung reduzieren“.

DEINE DATEN BLEIBEN BEI DIR
Keine Konten, kein Tracking, keine Analyse. Der Spielstand liegt nur auf deinem iPhone.
```

Optionaler Absatz – erst einfügen, wenn der Kauf in der App umgesetzt ist (Zeichen zählen dann mit):

```text
Kostenlos laden und 14 Tage alles ausprobieren. Danach schaltet ein einmaliger Kauf die App dauerhaft frei. Kein Abo.
```

## Schlüsselwörter – höchstens 100 Byte

Durch Kommas getrennt, ohne Leerzeichen nach dem Komma, ohne den App-Namen, ohne Markennamen Dritter. Jedes Wort länger als zwei Zeichen.

```text
Solitär,Brettspiel,Steine,Paare,Puzzle,Zen,Entspannen,Offline,Denkspiel,Triple Match,Shisen-Sho
```

## Neuerungen (0.8.x) – höchstens 4000 Zeichen

```text
– Freies Spiel: In jeder Spielart Leicht, Mittel oder Schwer wählen und immer neue, lösbare Partien spielen – ohne Sterne und ohne Bestzeit.
– Shisen-Sho: Paare jetzt auch durch Ziehen verbinden. Im Freien Spiel auf Wunsch mit Schwerkraft.
– Neue Steinsätze: „Tierkreis“ in Tusche und Siegel, die verspielten „Tiere“ und der „Mix“ aus allen Bildsätzen.
– „Alle Motive“: jeden Steinsatz in den Einstellungen groß ansehen.
– Startbildschirm in zwei Gruppen: „Der Weg zum Meister“ und „Zwischendurch“.
– Musik gleichmäßiger abgemischt und viele kleine Verbesserungen.
```

## Store-Screenshots (Vorschlag)

Nur Vorschlag; die echten Store-Screenshots entstehen zu 1.0.

1. **Startbildschirm** – „Ruhig spielen, in vier Spielarten.“
2. **Klassisch mit traditionellen Steinen** – „Mahjong, wie man es kennt.“
3. **Level-Weg mit Tor der Meister** – „60 Level bis zum Tor der Meister.“
4. **Triple Match mit Ablage** – „Drei gleiche sammeln.“
5. **Shisen-Sho mit Verbindungslinie** – „Verbinden mit höchstens zwei Knicken.“
6. **Brett mit Steinsatz „Tierkreis“** – „Steine nach deinem Geschmack: Tierkreis in Tusche.“
7. **Brett mit Steinsatz „Tiere“** – „Oder verspielt: Tiere.“
8. **Tages-Challenge mit Kalender** – „Jeden Tag ein neues Level.“

## Adressen

- Support-URL: https://robo-kob.github.io/mahjong/support/
- Datenschutz-URL: https://robo-kob.github.io/mahjong/datenschutz/

## Längen

<!-- laengen:start -->

| Feld | Länge | Grenze | Einheit | ok |
|---|---:|---:|---|---|
| Name | 15 | 30 | Zeichen | ✔ |
| Untertitel | 28 | 30 | Zeichen | ✔ |
| Untertitel (2) | 26 | 30 | Zeichen | ✔ |
| Werbetext | 167 | 170 | Zeichen | ✔ |
| Beschreibung | 1658 | 4000 | Zeichen | ✔ |
| Beschreibung (2) | 117 | 4000 | Zeichen | ✔ |
| Beschreibung mit optionalem Absatz | 1777 | 4000 | Zeichen | ✔ |
| Schlüsselwörter | 96 | 100 | Byte | ✔ |
| Neuerungen (0.8.x) | 564 | 4000 | Zeichen | ✔ |

<!-- laengen:end -->
