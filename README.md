# mahjong

Webseite zur iPhone-App: Handbuch, Support und Datenschutz, auf Deutsch und Englisch.
Erreichbar über GitHub Pages unter <https://robo-kob.github.io/mahjong/>.

- Reines Markdown mit Jekyll, wie GitHub Pages es baut; eigenes schlichtes Layout in `_layouts/`,
  keine externen Ressourcen, kein Build-Werkzeug.
- Der Name der App steht nur in `_config.yml` (`app_name`).
- `store/` enthält die Vorlagen für die Texte in App Store Connect (nicht veröffentlicht);
  `python3 store/pruefe_laengen.py` prüft ihre Längen.
- `impressum.md` ist vorbereitet, aber nicht veröffentlicht.
