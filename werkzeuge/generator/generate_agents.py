#!/usr/bin/env python3
# © 2026 IT-Beratung Martin Klein · Lizenz CC BY-SA 4.0, siehe LICENSE und NOTICE.md
"""Erzeugt die Opencode-Agentendateien (.opencode/agents/*.md) aus der Rollen-Methoden-Matrix.

Aufruf (aus dem Projektwurzelverzeichnis):
    python3 werkzeuge/generator/generate_agents.py matrix/Rollen-Methoden-Matrix.xlsx

Eingabe ist der xlsx-Export der Tabelle mit den Blättern Agenten, Agent-Methode,
Methode-Eigenschaft, Eigenschaften und Agent-Eigenschaft. Die Haltung wird hier aus den
Rohdaten berechnet (gleiche Rechnung wie im Blatt Berechnung), damit der Export keine
zwischengespeicherten Formelwerte braucht. Korrekturen aus Agent-Eigenschaft gelten vorrangig.

Benötigt: openpyxl (pip install openpyxl)
"""
import sys, re
from collections import defaultdict, Counter
from pathlib import Path
from openpyxl import load_workbook

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / ".opencode" / "agents"

# Modi: feste Texte, da sie keine Matrixdaten sind
MODI = {
 "athene": [("Minos", "Triage",
   "Wenn neue Fehlerberichte zu sichten sind: Prüfe jeden auf Vollständigkeit und Reproduzierbarkeit, erkenne Duplikate, "
   "schlage Schwere und Priorität getrennt vor und erstelle die Vorlage für das Fehlergremium. Grundlage: Skill "
   "`testmanagement`, Referenz `fehler-und-konfigurationsmanagement.md`; für Ursachenanalysen `rca-und-prozessverbesserung.md`. "
   "Ausgabe: Triage-Tabelle in `arbeitsbereich/fehler/`."),
   ("Themis", "Assessment",
   "Wenn der Testprozess bewertet oder verbessert werden soll: Führe ein Assessment nach TMMi oder TPI NEXT durch "
   "(Dokumente, Interviews, Kennzahlen), leite priorisierte Verbesserungsmaßnahmen ab und plane einen Pilot. Grundlage: "
   "Skill `testmanagement`, Referenz `rca-und-prozessverbesserung.md`. Ausgabe: Assessment-Bericht in `arbeitsbereich/berichte/`.")],
 "ariadne": [("Sphinx", "Review",
   "Wenn ein Arbeitsergebnis geprüft werden soll: Wähle die Reviewart, lege Rollen und Perspektiven fest, prüfe mit "
   "Checklisten und perspektivenbasiertem Lesen, sammle Befunde ohne Lösungsdiskussion und protokolliere die Entscheidung. "
   "Grundlage: Skill `statischer-test`. Ausgabe: Reviewprotokoll in `arbeitsbereich/reviews/`.")],
 "iris": [("Teiresias", "BITV",
   "Wenn Barrierefreiheit zu prüfen ist: Prüfe nach EN 301 549 / WCAG 2.2 AA und BITV 2.0, mit Tastatur, Screenreader, "
   "Zoom und Reflow, auch Dokumente und PDFs. Grundlage: Skill `teststufen-testarten`, Referenz `barrierefreiheit.md`. "
   "Ausgabe: Prüfbericht in `arbeitsbereich/berichte/` und Entwurf der Erklärung zur Barrierefreiheit.")],
}

ORCHESTRATOR = "athene"
COPYRIGHT = ("<!-- © 2026 IT-Beratung Martin Klein · Lizenz CC BY-SA 4.0, siehe LICENSE und NOTICE.md · "
             "erzeugt aus der Rollen-Methoden-Matrix mit werkzeuge/generator/generate_agents.py -->")
MIN_SUPPORT = 2  # unterstützender Skill wird freigegeben, wenn der Agent bei mind. so vielen Methoden darin mitwirkt


def slug(s):
    return re.sub(r"[^a-z0-9-]", "", s.lower().replace(" ", "-"))


def find_row(ws, text, col=1, prefix=False):
    for r in range(1, ws.max_row + 1):
        v = ws.cell(r, col).value
        if isinstance(v, str) and (v.startswith(text) if prefix else v.strip() == text):
            return r
    raise SystemExit(f"Zeile '{text}' im Blatt {ws.title} nicht gefunden")


def load(path):
    wb = load_workbook(path, data_only=False)
    # Agenten
    ws = wb["Agenten"]
    hdr = find_row(ws, "Name")
    agents = []
    r = hdr + 1
    while ws.cell(r, 1).value:
        name, sub, desc, role, modi, datei = (ws.cell(r, c).value for c in range(1, 7))
        agents.append(dict(name=name, untertitel=sub, beschreibung=desc, rolle=role,
                           modi=modi or "", id=Path(datei or slug(name)).stem))
        r += 1
    # Agent-Methode (Spalten C.. in Reihenfolge der Agenten, letzte Spalte Skill-Referenz)
    ws = wb["Agent-Methode"]
    hdr = find_row(ws, "Kategorie")
    refcol = 3 + len(agents)
    if ws.cell(hdr, refcol).value != "Skill-Referenz":
        raise SystemExit("Agent-Methode: erwartet je Agent eine Spalte (Reihenfolge wie im Blatt Agenten), "
                         "danach 'Skill-Referenz'.")
    methods = []
    r = hdr + 1
    while ws.cell(r, 2).value:
        marks = {}
        for i, a in enumerate(agents):
            v = ws.cell(r, 3 + i).value
            if v in ("●", "○"):
                marks[a["id"]] = v
        methods.append(dict(kat=ws.cell(r, 1).value, name=ws.cell(r, 2).value,
                            ref=ws.cell(r, refcol).value, marks=marks))
        r += 1
    # Methode-Eigenschaft
    ws = wb["Methode-Eigenschaft"]
    hdr = find_row(ws, "Kategorie")
    chars = []
    c = 3
    while ws.cell(hdr, c).value:
        chars.append(ws.cell(hdr, c).value); c += 1
    for i, m in enumerate(methods):
        rr = hdr + 1 + i
        if ws.cell(rr, 2).value != m["name"]:
            raise SystemExit(f"Methode-Eigenschaft Zeile {rr}: '{ws.cell(rr, 2).value}' ≠ '{m['name']}'. "
                             "Beide Blätter müssen dieselbe Reihenfolge haben.")
        m["bedarf"] = {ch: (ws.cell(rr, 3 + j).value or 0) for j, ch in enumerate(chars)}
    # Eigenschaften (Prompttexte)
    ws = wb["Eigenschaften"]
    hdr = find_row(ws, "Charakter")
    texte = {}
    r = hdr + 1
    while ws.cell(r, 1).value:
        texte[ws.cell(r, 1).value] = ws.cell(r, 3).value; r += 1
    # Korrekturen
    ws = wb["Agent-Eigenschaft"]
    k0 = find_row(ws, "Korrektur", prefix=True) + 2
    korr = {}
    for i, a in enumerate(agents):
        for j, ch in enumerate(chars):
            v = ws.cell(k0 + i, 3 + j).value
            if v not in (None, ""):
                korr[(a["id"], ch)] = int(v)
    return agents, methods, chars, texte, korr


def haltung(agents, methods, chars, korr):
    w = {"●": 2, "○": 1}
    raw = {a["id"]: {ch: sum(w.get(m["marks"].get(a["id"]), 0) * m["bedarf"][ch] for m in methods)
                     for ch in chars} for a in agents}
    col = {ch: sum(raw[a][ch] for a in raw) for ch in chars}
    out = {}
    for aid, rv in raw.items():
        sc = {ch: (rv[ch] ** 2 / col[ch] if col[ch] else 0) for ch in chars}
        mx = max(sc.values()) or 1
        lv = {}
        for ch in chars:
            if rv[ch] > 0:
                lv[ch] = 3 if sc[ch] >= .66 * mx else 2 if sc[ch] >= .33 * mx else 1
            if (aid, ch) in korr:
                lv[ch] = korr[(aid, ch)]
        out[aid] = {ch: v for ch, v in lv.items() if v}
    return out


def skill_of(ref):
    return ref.split("/")[0] if ref else None


def build(agents, methods, chars, texte, korr):
    hal = haltung(agents, methods, chars, korr)
    byid = {a["id"]: a for a in agents}
    lead = defaultdict(list)  # Methode -> führende Agenten
    for m in methods:
        lead[m["name"]] = [aid for aid, v in m["marks"].items() if v == "●"]
    OUT.mkdir(parents=True, exist_ok=True)
    for a in agents:
        aid = a["id"]
        own = [m for m in methods if m["marks"].get(aid) == "●"]
        mit = [m for m in methods if m["marks"].get(aid) == "○"]
        core = Counter(skill_of(m["ref"]) for m in own)
        core_refs = defaultdict(Counter)
        for m in own:
            core_refs[skill_of(m["ref"])][m["ref"].split("/")[-1]] += 1
        support_all = Counter(skill_of(m["ref"]) for m in mit if skill_of(m["ref"]) not in core)
        support = Counter({s: n for s, n in support_all.items() if n >= MIN_SUPPORT})
        allowed = sorted(set(core) | set(support))

        # Beschreibung für die Agentenauswahl
        top = ", ".join(m["name"] for m in own[:6]) + (" und weitere" if len(own) > 6 else "")
        desc = (f"Testrolle {a['rolle']} ({a['untertitel']}). {a['beschreibung']} "
                f"Zuständig für {top}.")
        desc = desc.replace('"', "'")

        perms = [
            ("edit", "*", "deny"), ("edit", "arbeitsbereich/**", "allow"),
            ("shell", "*", "ask"), ("webfetch", "*", "deny"), ("websearch", "*", "deny"),
            ("skill", "*", "deny"),
        ] + [("skill", s, "allow") for s in allowed]
        if aid == ORCHESTRATOR:
            perms += [("subagent", "*", "deny")] + [("subagent", o["id"], "allow") for o in agents if o["id"] != aid]
        else:
            perms += [("subagent", "*", "deny")]

        L = ["---", f'description: "{desc}"', f"mode: {'primary' if aid == ORCHESTRATOR else 'subagent'}", "permissions:"]
        for act, res, eff in perms:
            L += [f'  - action: {act}', f'    resource: "{res}"', f'    effect: {eff}']
        L += ["---", "", COPYRIGHT, "", f"# {a['name']} · {a['untertitel']}", "", a["beschreibung"], "",
              f"Du bist **{a['name']}**, der Agent für die Testrolle **{a['rolle']}** im Team Agentic Testing. "
              "Du arbeitest auf Deutsch, präzise und nachvollziehbar.", ""]

        # Haltung
        L += ["## Haltung", ""]
        for lvl, wort in ((3, "prägend"), (2, "deutlich")):
            for ch in chars:
                if hal[aid].get(ch) == lvl:
                    L += [f"- **{ch}** ({wort}): {texte[ch]}"]
        schwach = [ch for ch in chars if hal[aid].get(ch) == 1]
        if schwach:
            L += [f"- Als Gegengewicht, aber nicht bestimmend: {', '.join(schwach)}."]
        L += [""]

        # Verantwortung
        L += ["## Verantwortung", "", "Hauptverantwortlich für:", ""]
        bykat = defaultdict(list)
        for m in own: bykat[m["kat"]].append(m["name"])
        for k, ms in bykat.items():
            L += [f"- **{k}:** {', '.join(ms)}"]
        if mit:
            L += ["", "Wirkt mit bei (führend ist ein anderer Agent):", ""]
            bykat = defaultdict(list)
            for m in mit:
                lead_names = ", ".join(byid[x]["name"] for x in lead[m["name"]]) or "–"
                bykat[m["kat"]].append(f"{m['name']} (führt: {lead_names})")
            for k, ms in bykat.items():
                L += [f"- **{k}:** {'; '.join(ms)}"]
        L += [""]

        # Skills
        L += ["## Skills", "", "Lade Skills mit dem Skill-Werkzeug, bevor du mit einer Aufgabe beginnst. "
              "Lies in `references/` nur die Datei, die die aktuelle Aufgabe braucht.", "", "Kernskills:", ""]
        for s, n in core.most_common():
            refs = ", ".join(f"`{r}`" for r, _ in core_refs[s].most_common())
            L += [f"- `{s}`: {refs}"]
        if support:
            L += ["", "Unterstützend, nur bei Bedarf:", ""]
            for s, _ in support.most_common():
                L += [f"- `{s}`"]
        L += [""]

        # Modi
        if aid in MODI:
            L += ["## Modi", "", "Wenn der Auftrag einen Modus nennt oder eindeutig zu ihm passt, arbeite nach dem Abschnitt:", ""]
            for name, kurz, text in MODI[aid]:
                L += [f"### {name} ({kurz})", "", text, ""]

        # Orchestrierung
        if aid == ORCHESTRATOR:
            L += ["## Orchestrierung", "",
                  "Du bist der primäre Agent. Zerlege Aufträge in Teilaufgaben und übergib sie an den zuständigen "
                  "Subagenten. Gib jedem Subagenten Ziel, Eingaben (Pfade im `arbeitsbereich/`), erwartetes Ergebnis "
                  "und Abgabeort mit. Prüfe jedes Ergebnis, bevor du es weitergibst oder berichtest.", "",
                  "| Agent | Testrolle | Zuständig für |", "| --- | --- | --- |"]
            for o in agents:
                if o["id"] == aid: continue
                o_own = [m["name"] for m in methods if m["marks"].get(o["id"]) == "●"][:5]
                L += [f"| `{o['id']}` ({o['name']}) | {o['rolle']} | {', '.join(o_own)} |"]
            L += [""]

        # Arbeitsweise
        L += ["## Arbeitsweise", "",
              "- Ergebnisse sind Dateien im `arbeitsbereich/`, im Ausgabeformat des verwendeten Skills. "
              "Nenne am Ende Pfad und Kernaussage.",
              "- Lite-Modus: Bei Teilfragen oder einzelnen Verfahrensschritten nur die betreffenden Abschnitte "
              "ausgeben (z. B. nur die Klassen und Grenzwerte), statt das volle Schema zu füllen. "
              "Offene Fragen trotzdem nennen.",
              "- Jede Aussage hat eine Quelle (Anforderung, Risiko, Messung, Beobachtung). Keine stillen Annahmen: "
              "Unklarheiten kommen in den Abschnitt „Offene Fragen“.",
              "- Aufgaben außerhalb deiner Verantwortung gibst du mit einem Satz zurück und nennst den zuständigen Agenten.",
              "- Du änderst nichts außerhalb von `arbeitsbereich/` und führst Befehle nur nach Freigabe aus.",
              "- Keine echten personenbezogenen Daten in Testdaten, Berichten oder Logs.", ""]

        (OUT / f"{aid}.md").write_text("\n".join(L), encoding="utf-8")
        print(f"{aid:11} Kern: {len(core):2}  unterstützend: {len(support):2}  Methoden ●{len(own):3} ○{len(mit):3}")


if __name__ == "__main__":
    src = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "matrix" / "Rollen-Methoden-Matrix.xlsx"
    build(*load(src))
