#!/usr/bin/env python3
"""Prüft die Längen der Store-Texte in store/de.md und store/en.md.

Jeder Abschnitt „## <Feld> – höchstens N Zeichen|Byte“ (bzw. „max. N characters|bytes“)
gibt die Grenze vor; jeder ```text-Block darunter wird gezählt. Zeichen = Unicode-Zeichen,
Byte = UTF-8. Die Beschreibung wird zusätzlich mit dem optionalen Absatz zusammen gezählt.

  python3 store/pruefe_laengen.py           # prüfen, Tabelle ausgeben, Status 1 bei Überschreitung
  python3 store/pruefe_laengen.py --write   # zusätzlich die Tabelle in die Dateien schreiben
"""
import re
import sys
from pathlib import Path

HEADING = re.compile(r"^## (.+?) – (?:höchstens|max\.) (\d+) (Zeichen|Byte|characters|bytes)\s*$")
START, END = "<!-- laengen:start -->", "<!-- laengen:end -->"


def blocks(path):
    lines = path.read_text(encoding="utf-8").splitlines()
    field = None
    i = 0
    while i < len(lines):
        line = lines[i]
        m = HEADING.match(line)
        if m:
            field = (m.group(1), int(m.group(2)), m.group(3).startswith("B") or m.group(3) == "bytes")
        elif line.startswith("## "):
            field = None
        elif line.strip() == "```text" and field:
            j = i + 1
            while lines[j].strip() != "```":
                j += 1
            yield field, "\n".join(lines[i + 1:j])
            i = j
        i += 1


def measure(text, in_bytes):
    return len(text.encode("utf-8")) if in_bytes else len(text)


def check(path):
    rows, ok = [], True
    seen = {}
    for (name, limit, in_bytes), text in blocks(path):
        n = seen.get(name, 0) + 1
        seen[name] = n
        label = name if n == 1 else f"{name} ({n})"
        size = measure(text, in_bytes)
        rows.append((label, size, limit, "Byte" if in_bytes else "Zeichen"))
        if in_bytes and (", " in text):
            print(f"{path.name}: {label}: Leerzeichen nach Komma", file=sys.stderr)
            ok = False
        if in_bytes:
            short = [w for w in text.split(",") if len(w) <= 2]
            if short:
                print(f"{path.name}: {label}: zu kurze Wörter {short}", file=sys.stderr)
                ok = False
        if n == 2 and name.startswith(("Beschreibung", "Description")):
            first = next(t for (f, t) in blocks(path) if f[0] == name)
            total = measure(first + "\n\n" + text, in_bytes)
            rows.append((f"{name} mit optionalem Absatz", total, limit, "Zeichen"))
            ok &= total <= limit
        ok &= size <= limit
    return rows, ok


def table(rows):
    out = [START, "", "| Feld | Länge | Grenze | Einheit | ok |", "|---|---:|---:|---|---|"]
    for label, size, limit, unit in rows:
        out.append(f"| {label} | {size} | {limit} | {unit} | {'✔' if size <= limit else '✘'} |")
    out += ["", END]
    return "\n".join(out)


def main():
    base = Path(__file__).resolve().parent
    all_ok = True
    for name in ("de.md", "en.md"):
        path = base / name
        rows, ok = check(path)
        all_ok &= ok
        t = table(rows)
        print(f"\n{name}\n{t}")
        if "--write" in sys.argv:
            s = path.read_text(encoding="utf-8")
            if START in s:
                s = re.sub(re.escape(START) + r".*?" + re.escape(END), lambda _: t, s, flags=re.S)
            else:
                s = s.replace("LAENGEN-TABELLE", t).replace("LENGTH-TABLE", t)
            path.write_text(s, encoding="utf-8")
    sys.exit(0 if all_ok else 1)


if __name__ == "__main__":
    main()
