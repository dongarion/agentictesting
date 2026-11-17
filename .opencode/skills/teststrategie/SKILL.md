---
name: teststrategie
description: >
  Entwickelt, bewertet und begründet Teststrategien: die ISTQB-Strategietypen (analytisch,
  modellbasiert, methodisch, prozess- bzw. standardkonform, angeleitet/beratend,
  regressionsvermeidend, reaktiv) und ergänzende Ansätze (Shift-Left, Shift-Right,
  Testpyramide und Testpokal, agile Testquadranten, Whole-Team-Ansatz, Continuous Testing).
  Verwenden, wenn eine organisationsweite Testrichtlinie, eine Projektteststrategie oder die
  strategischen Kapitel eines Testkonzepts entstehen sollen, wenn eine bestehende Strategie
  bewertet wird oder bei Fragen wie "Wie sollen wir testen?", "Brauchen wir mehr
  Automatisierung?", "Wie früh testen?", "Testen in Produktion?", "Wer testet was?".
  Nicht für die Ausarbeitung einzelner Testfälle oder Testprozessdokumente.
license: CC BY-SA 4.0. Siehe LICENSE.txt
metadata:
  author: "IT-Beratung Martin Klein"
  copyright: "© 2026 IT-Beratung Martin Klein"
  version: "1.0"
  basis: "ISTQB CTFL 4.0, CTAL-TM, CT-TAS, CTFL-AT; ISO/IEC/IEEE 29119-1/-3; Crispin/Gregory (Quadranten); Cohn/Fowler (Pyramide); Dodds (Testing Trophy)"
  sprache: "de"
---

# Teststrategie

Eine Teststrategie beschreibt **wie getestet wird, um die Testziele mit vertretbarem Aufwand
zu erreichen**: welche Ansätze, Stufen, Testarten, Verfahren, Verantwortungen, Automatisierung
und Kriterien. Sie ist die Brücke zwischen Risiken und Testaktivitäten.

Ebenen:

- **Organisation:** Testrichtlinie (Warum testen wir, welche Grundsätze gelten?) und
  organisationsweite Teststrategie (Standards, Vorlagen, Werkzeuge).
- **Projekt/Produkt:** Projektteststrategie im Testkonzept, abgeleitet aus Risiken und Kontext.
- **Teststufe/Iteration:** Konkretisierung je Stufe oder Sprint.

## Haltung

- **Kontext vor Dogma.** Keine Strategie ist universell richtig. Die Testpyramide passt nicht
  zu jedem Produkt, Shift-Right nicht zu jedem Fachverfahren. Du begründest aus dem Kontext.
- **Mischung statt Reinform.** Gute Strategien kombinieren Typen: analytisch-risikobasiert als
  Rückgrat, methodisch für Qualitätsmerkmale, regressionsvermeidend für Stabilität, reaktiv
  für das Unbekannte.
- **Ökonomisches Denken.** Jede Testaktivität kostet; du verteilst den Aufwand dorthin, wo er
  am meisten Risiko senkt und am frühesten Feedback gibt.
- **Weitblick.** Eine Strategie überdauert Sprints und Personen. Du denkst an Wartung,
  Wachstum, Wissenstransfer und Betrieb.
- **Klarheit für alle.** Eine Strategie, die nur der Testmanager versteht, wird nicht gelebt.
  Du schreibst sie so, dass Entwickler, Fachbereich und Management wissen, was von ihnen
  erwartet wird.

## Vorgehen

### 1. Kontext erfassen

- Produktart, Architektur, Lebensdauer, Release-Frequenz.
- Vorgehensmodell, Teamstruktur, Dienstleister, Vertragsart.
- Produktrisiken und Qualitätsmerkmale (Skill `testmanagement`).
- Normen, Regulatorik, Kundenvorgaben, Nachweispflichten.
- Reife: vorhandene Automatisierung, Werkzeuge, Kompetenzen, Umgebungen.

### 2. Bausteine wählen und Referenzen laden

| Frage | Referenz |
| --- | --- |
| Welche Strategietypen kombinieren wir, mit welchem Gewicht? | [strategietypen.md](references/strategietypen.md) |
| Wann im Lebenszyklus testen wir: früh, im Betrieb, kontinuierlich? | [shift-left-right-continuous.md](references/shift-left-right-continuous.md) |
| Wie verteilen wir Tests auf Ebenen, Quadranten und Verantwortliche? | [verteilung-und-verantwortung.md](references/verteilung-und-verantwortung.md) |

### 3. Strategie formulieren

Gliederung einer Projektteststrategie:

1. Kontext und Testziele.
2. Risikobasis: Risikoklassen und daraus folgende Testintensität.
3. Strategiemix: Typen mit Gewicht und Begründung.
4. Teststufen und Testarten je Stufe mit Verantwortlichen (Skill `teststufen-testarten`).
5. Testentwurfsverfahren je Risikoklasse.
6. Verteilung: Pyramide/Trophy, Quadranten, Automatisierungsansatz (Skill `testautomatisierung`).
7. Zeitliche Ausrichtung: Shift-Left-Maßnahmen, Continuous Testing, Shift-Right.
8. Unabhängigkeit der Tests je Stufe.
9. Eingangs- und Endekriterien, Definition of Done.
10. Umgebungen und Testdaten (Skill `testdaten-testumgebung`).
11. Werkzeuge.
12. Fehlermanagement und Berichtswesen.
13. Abweichungen von der Organisationsstrategie mit Begründung.

### 4. Selbstprüfung

- [ ] Jede strategische Entscheidung ist aus Risiko oder Kontext begründet.
- [ ] Strategiemix ist explizit; reaktive Anteile sind eingeplant.
- [ ] Verantwortung je Teststufe und Testart ist klar (auch Entwicklung, Fachbereich, Betrieb).
- [ ] Verteilung und Automatisierungsansatz sind beschrieben und messbar.
- [ ] Shift-Left- und Shift-Right-Maßnahmen sind konkret, nicht nur Schlagworte.
- [ ] Die Strategie ist für alle Beteiligten verständlich und abgestimmt.
- [ ] Die Prüfliste der verwendeten Referenz ist erfüllt.

## Lite-Modus

Bei Teilfragen oder einzelnen Verfahrensschritten nur die betreffenden Abschnitte ausgeben (z. B. nur die Quadranten-Analyse oder nur den Strategiemix), statt das volle Schema zu füllen. Die Selbstprüfung gilt dann nur für die ausgegebenen Teile; offene Fragen werden trotzdem genannt.
