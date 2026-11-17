# Anwendungsfallbasierter Test

Für Abläufe, in denen ein **Akteur** mit dem System interagiert, um ein fachliches Ziel zu
erreichen. Grundlage sind Anwendungsfälle, User Stories mit Akzeptanzkriterien,
Prozessbeschreibungen oder BPMN-Modelle.

## Inhalt
1. Anwendungsfall analysieren
2. Abläufe identifizieren
3. Testfälle ableiten
4. Überdeckung
5. Bezug zu User Stories
6. Anti-Patterns
7. Prüfliste
8. Beispiel

## 1. Anwendungsfall analysieren

Erfasse je Anwendungsfall:

- Akteur(e) und Ziel,
- Auslöser,
- **Vorbedingungen:** was vor dem Start gelten muss,
- **Nachbedingungen:** Garantie bei Erfolg und Mindestgarantie bei Misserfolg,
- Hauptablauf als nummerierte Schritte,
- Alternativ- und Ausnahmeabläufe mit dem Schritt, an dem sie abzweigen,
- Geschäftsregeln, auf die verwiesen wird.

Fehlt eines davon, ist das eine offene Frage. Besonders häufig fehlen Mindestgarantien und
Ausnahmeabläufe.

## 2. Abläufe identifizieren

- **Hauptablauf:** der erfolgreiche Standardweg.
- **Alternativabläufe:** andere Wege, die ebenfalls zum Ziel führen.
- **Ausnahmeabläufe:** Wege, auf denen das Ziel nicht erreicht wird (Abbruch, Fehler,
  Zeitüberschreitung, fehlende Berechtigung).
- Suche aktiv nach nicht beschriebenen Ausnahmen je Schritt:
  - Was, wenn der Akteur abbricht?
  - Was, wenn ein Fremdsystem nicht antwortet?
  - Was, wenn Daten zwischenzeitlich geändert wurden (Nebenläufigkeit)?
  - Was, wenn die Sitzung abläuft?
  - Was, wenn der Akteur den Schritt wiederholt (Doppelklick, Zurück-Taste)?
  Nicht beschriebene Ausnahmen sind offene Fragen, keine Testfälle mit geratenem Ergebnis.

## 3. Testfälle ableiten

- Je Ablauf mindestens ein Testfall: Hauptablauf, jeder Alternativablauf, jeder Ausnahmeablauf.
- Jeder Testfall stellt die **Vorbedingungen** her und prüft die **Nachbedingungen**,
  bei Ausnahmen die Mindestgarantie.
- Eingabedaten für einzelne Schritte mit
  [aequivalenzklassen-grenzwerte.md](aequivalenzklassen-grenzwerte.md) bestimmen.
- Verweist ein Schritt auf eine Geschäftsregel mit Kombinationen, diese mit
  [entscheidungstabellen.md](entscheidungstabellen.md) behandeln.
- Hat der Ablauf Status, der über mehrere Anwendungsfälle hinweg wirkt, mit
  [zustandsuebergaenge.md](zustandsuebergaenge.md) ergänzen.

## 4. Überdeckung

**Überdeckung** = getestete Abläufe / alle identifizierten Abläufe × 100 %.
Getrennt angeben: spezifizierte Abläufe und zusätzlich identifizierte (offene) Ausnahmen.

## 5. Bezug zu User Stories

- Jedes Akzeptanzkriterium ist mindestens eine Testbedingung.
- Gherkin-Szenarien (Given/When/Then) entsprechen Abläufen: Given = Vorbedingung,
  When = Schritte, Then = Nachbedingung.
- Prüfe Akzeptanzkriterien auf die INVEST-Eigenschaft „testbar“. Nicht prüfbare Kriterien
  („schnell“, „benutzerfreundlich“) sind offene Fragen.

## 6. Anti-Patterns

- Nur den Hauptablauf testen.
- Vorbedingungen nicht herstellen, sondern voraussetzen.
- Nur das Ende des Ablaufs prüfen, nicht die Zwischenschritte und Nachbedingungen.
- Ausnahmeabläufe erfinden und ihnen ein „plausibles“ erwartetes Ergebnis zuweisen.

## 7. Prüfliste

- [ ] Vor- und Nachbedingungen sind je Anwendungsfall erfasst.
- [ ] Haupt-, Alternativ- und Ausnahmeabläufe sind vollständig aufgelistet.
- [ ] Je Schritt ist nach unbeschriebenen Ausnahmen gesucht.
- [ ] Je Ablauf existiert ein Testfall mit Vor- und Nachbedingungsprüfung.
- [ ] Schrittdaten sind mit Äquivalenzklassen bestimmt.

## 8. Beispiel

Anwendungsfall „Antrag einreichen“:

1. Antragsteller öffnet das Formular.
2. Antragsteller füllt die Pflichtfelder aus.
3. Antragsteller lädt Nachweise hoch.
4. Antragsteller sendet den Antrag ab.
5. System vergibt ein Aktenzeichen und versendet eine Eingangsbestätigung.

| Ablauf | Abzweig | Beschreibung | spezifiziert |
| --- | --- | --- | --- |
| H | – | Hauptablauf 1–5 | ja |
| A1 | 3 | Keine Nachweise, Nachreichung später | ja |
| E1 | 2 | Pflichtfeld fehlt → Hinweis, Antrag bleibt im Entwurf | ja |
| E2 | 3 | Datei zu groß | nein → offene Frage |
| E3 | 4 | Sitzung abgelaufen | nein → offene Frage |
| E4 | 5 | Mailversand schlägt fehl | nein → offene Frage |
