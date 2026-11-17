---
name: testprozess
description: >
  Führt durch den ISTQB-Testprozess und erstellt seine Arbeitsergebnisse: Testplanung,
  Testüberwachung und -steuerung, Testanalyse, Testentwurf, Testrealisierung,
  Testdurchführung und Testabschluss. Verwenden, wenn ein Testkonzept oder Testplan erstellt,
  der Testfortschritt bewertet, Testbedingungen und Testfälle aus einer Testbasis abgeleitet,
  Testläufe vorbereitet und protokolliert, Fehlerberichte geschrieben oder ein
  Testabschlussbericht verfasst werden soll. Stichworte: "Testkonzept", "Testplan",
  "Testbericht", "Testabschluss", "Testfortschritt", "Testspezifikation", "Testprotokoll",
  "Fehlerbericht", "Eingangskriterien", "Endekriterien". Nicht für die Wahl einzelner
  Testentwurfsverfahren (Skill Black-Box/White-Box) oder übergreifende Managementthemen
  wie Schätzung und Risikomanagement im Detail (Skill Testmanagement).
license: CC BY-SA 4.0. Siehe LICENSE.txt
metadata:
  author: "IT-Beratung Martin Klein"
  copyright: "© 2026 IT-Beratung Martin Klein"
  version: "1.0"
  basis: "ISTQB CTFL 4.0 Kap. 1.4, 5; CTAL-TM; CTAL-TA Kap. 1; ISO/IEC/IEEE 29119-2 und -3"
  sprache: "de"
---

# Testprozess

Der Testprozess ist kein Wasserfall, sondern eine **Menge von Aktivitäten**, die je nach
Vorgehensmodell sequenziell, iterativ oder parallel laufen. Jede Aktivität hat Eingaben,
Aufgaben und Arbeitsergebnisse. Dieser Skill sorgt dafür, dass keine Aktivität vergessen
wird und jedes Arbeitsergebnis nachvollziehbar entsteht.

Die Aktivitäten stehen in `references/`. Lade nur die, an der du gerade arbeitest.

## Haltung

- **Ordnung und Nachvollziehbarkeit.** Jedes Arbeitsergebnis hat eine Quelle, eine Version
  und einen Platz in der Kette Testbasis → Testbedingung → Testfall → Ergebnis → Fehler.
  Was nicht rückverfolgbar ist, gilt als nicht getestet.
- **Angemessenheit statt Formalismus.** Ein Testkonzept für eine Behörde mit V-Modell XT
  sieht anders aus als eines für ein Scrum-Team. Du passt Tiefe und Form an Risiko,
  Vorgehensmodell und Vertrag an, ohne Inhalte wegzulassen, die gebraucht werden.
- **Faktentreue.** Berichte enthalten Zahlen mit Bezug, keine Stimmungen. „87 von 112
  Testfällen bestanden, 3 kritische Fehler offen“ statt „läuft gut“.
- **Ehrlichkeit gegenüber Stakeholdern.** Du berichtest Risiken, Verzug und Lücken früh und
  unverblümt. Ein schlechter Zwischenstand ist eine Information, kein Versagen.
- **Abschluss als Lernchance.** Der Testabschluss ist nicht Papierkram, sondern die Stelle,
  an der das nächste Projekt besser wird.

## Vorgehen

### 1. Kontext bestimmen

- Vorgehensmodell (V-Modell XT, Wasserfall, Scrum, SAFe, hybrid), Vertragsart, Normen,
  Kundenvorlagen.
- Teststufen und Verantwortliche, vorhandene Dokumente und Werkzeuge (Testmanagement,
  Fehlertracker).
- Welche Aktivität steht an, welches Arbeitsergebnis wird gebraucht?

### 2. Aktivität wählen und Referenz laden

| Aktivität | Arbeitsergebnisse | Referenz |
| --- | --- | --- |
| Testplanung | Testkonzept, Testplan je Stufe, Eingangs- und Endekriterien | [testplanung.md](references/testplanung.md) |
| Testüberwachung und -steuerung | Fortschrittsberichte, Steuerungsmaßnahmen, Kennzahlen | [ueberwachung-steuerung.md](references/ueberwachung-steuerung.md) |
| Testanalyse und Testentwurf | Testbedingungen, Testfälle, Testdatenanforderungen, Rückverfolgbarkeit | [analyse-entwurf.md](references/analyse-entwurf.md) |
| Testrealisierung und Testdurchführung | Testabläufe, Testsuiten, Testlaufplan, Testprotokolle, Fehlerberichte | [realisierung-durchfuehrung.md](references/realisierung-durchfuehrung.md) |
| Testabschluss | Testabschlussbericht, archivierte Testmittel, Lessons Learned | [testabschluss.md](references/testabschluss.md) |

### 3. Arbeitsergebnis erstellen

- Vorlage des Kunden verwenden, wenn vorhanden; sonst Struktur der Referenz (angelehnt an
  ISO/IEC/IEEE 29119-3).
- Jede Aussage mit Quelle (Anforderung, Risiko, Messwert).
- Offene Punkte und Annahmen ausdrücklich ausweisen.

### 4. Selbstprüfung

- [ ] Das Arbeitsergebnis passt zu Vorgehensmodell und Vertrag.
- [ ] Rückverfolgbarkeit zur Testbasis und zu Risiken ist hergestellt.
- [ ] Zahlen haben Bezugsgröße und Stichtag.
- [ ] Annahmen, Risiken und offene Punkte sind ausgewiesen.
- [ ] Die Prüfliste der verwendeten Referenz ist erfüllt.

## Lite-Modus

Bei Teilfragen oder einzelnen Verfahrensschritten nur die betreffenden Abschnitte ausgeben (z. B. nur die Endekriterien oder nur einen Fehlerbericht), statt das volle Schema zu füllen. Die Selbstprüfung gilt dann nur für die ausgegebenen Teile; offene Fragen werden trotzdem genannt.

## Querverweise

- Risikoanalyse, Schätzung, Priorisierung, Fehlermanagement im Detail: Skill `testmanagement`.
- Wahl und Ausrichtung der Teststrategie: Skill `teststrategie`.
- Testentwurfsverfahren: Skills `black-box-testdesign`, `white-box-testdesign`, `exploratives-testen`.
- Teststufen und Testarten einordnen: Skill `teststufen-testarten`.
