# Produktrisikoanalyse und Projektrisikomanagement

**Produktrisiko:** Das Produkt erfüllt Bedürfnisse nicht oder verursacht Schaden.
**Projektrisiko:** Etwas gefährdet das Projekt oder den Test (Zeit, Ressourcen, Umgebung, Lieferungen).
Risiko = Eintrittswahrscheinlichkeit × Auswirkung.

## Inhalt
1. Risikobasiertes Testen
2. Produktrisiken identifizieren
3. Produktrisiken bewerten
4. Testintensität ableiten
5. Projektrisiken
6. Risiken überwachen
7. Anti-Patterns
8. Prüfliste

## 1. Risikobasiertes Testen

Risiken steuern **was** getestet wird, **wie gründlich**, **in welcher Reihenfolge** und
**wann genug** ist. Die Risikoanalyse ist ein Gemeinschaftsergebnis von Fachbereich (Auswirkung),
Entwicklung und Architektur (Wahrscheinlichkeit) und Test (Moderation, Ableitung).

## 2. Produktrisiken identifizieren

Methoden:

- Workshop mit Fachbereich, Entwicklung, Betrieb, Test, Sicherheit, Datenschutz.
- Durchgehen von Anforderungen, Geschäftsprozessen, Architektur je Komponente und Schnittstelle.
- Qualitätsmerkmale nach ISO/IEC 25010 als Checkliste: funktionale Eignung, Leistung,
  Kompatibilität, Interaktionsfähigkeit (Usability, Barrierefreiheit), Zuverlässigkeit,
  Sicherheit, Wartbarkeit, Übertragbarkeit, Safety.
- Fehlerhistorie, Produktionsvorfälle, Supporttickets, Erfahrungen aus Vorprojekten.
- FMEA für kritische Komponenten; Threat Modeling für Sicherheit (Skill `spezialtests`).
- Interviews mit Nutzern und Betrieb.

Risiko formulieren: „Wenn <Ursache>, dann <Auswirkung> für <Betroffene>.“
Beispiel: „Wenn die Fristberechnung Feiertage falsch berücksichtigt, werden Bescheide mit
falscher Rechtsbehelfsfrist versandt (Rechtsrisiko, Bürger, Behörde).“

## 3. Produktrisiken bewerten

**Wahrscheinlichkeit** (technisch): Komplexität, Neuheit, Änderungsumfang, Qualität der
Anforderungen, Erfahrung des Teams, Zeitdruck, Fehlerhistorie, Abhängigkeiten.

**Auswirkung** (fachlich): Häufigkeit der Nutzung, Anzahl Betroffener, finanzieller Schaden,
Rechtsfolgen, Datenschutz, Sicherheit, Reputation, Umgehbarkeit (Workaround).

Skala je Faktor 1–3 oder 1–5; Gewichtung transparent. Ergebnis als Risikomatrix:

| | Auswirkung gering | mittel | hoch |
| --- | --- | --- | --- |
| **Wahrscheinlichkeit hoch** | B | A | A |
| **mittel** | C | B | A |
| **gering** | C | C | B |

Qualitative Bewertung ist legitim; Zahlen erzeugen Scheingenauigkeit, wenn die Grundlage
Schätzung ist. Konsens im Workshop, Abweichungen diskutieren (Planning-Poker-ähnlich).

## 4. Testintensität ableiten

| Risikoklasse | Teststufen | Verfahren | Unabhängigkeit | Automatisierung | Reihenfolge |
| --- | --- | --- | --- | --- | --- |
| A | Alle relevanten | Formale Verfahren (Entscheidungstabelle, Grenzwerte 3-Wert, MC/DC wo nötig), Reviews, explorativ | Hoch (unabhängiges Testteam) | Regression vollständig | Zuerst |
| B | Hauptstufen | Standardverfahren (Äquivalenzklassen, Grenzwerte 2-Wert, Zustände), explorativ | Mittel | Kernpfade | Danach |
| C | Mindestens eine | Erfahrungsbasiert, Checklisten | Niedrig (Entwickler/Team) | Smoke | Zuletzt, wenn Zeit |

Abbildung in Testbedingungen: Jede Testbedingung erbt die Risikoklasse; Berichte zeigen
Abdeckung und offene Fehler je Klasse.

## 5. Projektrisiken

Typische Projektrisiken für den Test:

| Risiko | Maßnahme |
| --- | --- |
| Verspätete Lieferung des Testobjekts | Puffer, risikobasierte Kürzung vorbereiten, frühe Teillieferungen |
| Instabile Lieferungen | Eingangskriterien, Smoke-Test, Rücklieferung |
| Testumgebung fehlt oder ist instabil | Frühzeitige Bestellung, Verantwortlicher, IaC, Virtualisierung |
| Testdaten fehlen oder sind datenschutzkritisch | Frühe Klärung mit Datenschutz, Synthese |
| Fachexperten nicht verfügbar | Zeiten vertraglich und im Plan sichern |
| Schlüsselperson fällt aus | Wissensverteilung, Pairing, Dokumentation |
| Anforderungen ändern sich | Änderungsprozess mit Auswirkungsanalyse auf Tests |
| Werkzeuge, Lizenzen, Zugänge (Sicherheitsüberprüfung) | Früh beantragen; Ü2/Ü3-Verfahren dauern Monate |
| Unterschätzter Aufwand | Schätzung mit Bandbreite, Frühwarnkennzahlen |

Je Risiko: Wahrscheinlichkeit, Auswirkung, Maßnahme (vermeiden, mindern, übertragen, akzeptieren),
Verantwortlicher, Auslöser für Eskalation.

## 6. Risiken überwachen

- Risikoliste als lebendes Dokument; Überprüfung je Meilenstein oder Sprint.
- Neue Risiken aus Fehlern, Änderungen, Vorfällen aufnehmen; erledigte schließen.
- Restrisiko je Klasse im Bericht: getestet, offene Fehler, ungetestete Bereiche.
- Am Ende: Restrisiko zur Freigabeentscheidung vorlegen; Risikoakzeptanz dokumentieren.

## 7. Anti-Patterns

- Risikoanalyse durch das Testteam allein; Fachbereich fehlt, Auswirkungen sind geraten.
- Alles ist „hoch“; Priorisierung wird wertlos.
- Risikoanalyse einmal zu Projektbeginn, nie aktualisiert.
- Risikoklasse ohne Folgen für Testintensität.
- Projektrisiken nur im Kopf des Testmanagers.

## 8. Prüfliste

- [ ] Produktrisiken sind mit Fachbereich und Technik identifiziert und formuliert (Ursache → Auswirkung).
- [ ] Bewertung von Wahrscheinlichkeit und Auswirkung ist begründet; Verteilung ist differenziert.
- [ ] Testintensität je Risikoklasse ist festgelegt und auf Testbedingungen übertragen.
- [ ] Projektrisiken haben Maßnahme, Verantwortlichen und Eskalationsauslöser.
- [ ] Risikoliste wird regelmäßig aktualisiert; Restrisiko wird berichtet.
