# Testrealisierung und Testdurchführung

**Realisierung:** Alles bereitstellen, was für die Durchführung nötig ist.
**Durchführung:** Tests ausführen, Ergebnisse protokollieren, Abweichungen melden.

## Inhalt
1. Testrealisierung
2. Testlaufplan
3. Testdurchführung
4. Fehlerbericht
5. Fehlernachtest und Regression
6. Anti-Patterns
7. Prüfliste

## 1. Testrealisierung

- Testabläufe (Testprozeduren) aus Testfällen bilden: sinnvolle Reihenfolge, gemeinsame Vorbedingungen.
- Testsuiten zusammenstellen: Smoke, Regression, Feature, Abnahme.
- Testdaten erzeugen und laden; Testumgebung prüfen (Health-Check).
- Automatisierte Tests implementieren und in die Pipeline einbinden.
- Testmittel reviewen: Testfälle, Skripte, Daten.
- Eingangskriterien prüfen; erst dann starten.

## 2. Testlaufplan

- Welche Testsuiten in welcher Reihenfolge, auf welcher Umgebung, durch wen, bis wann.
- Reihenfolge nach Risiko, Abhängigkeiten und Bereitstellung.
- Smoke-Test zuerst; bei Fehlschlag Testunterbrechung nach Kriterium.
- Puffer für Fehlernachtests und Regression einplanen.

## 3. Testdurchführung

- Tests nach Plan ausführen; erfahrungsbasierte Anteile als Sessions (Skill `exploratives-testen`).
- **Protokoll** je Ausführung: Testfall, Version des Testobjekts, Umgebung, Daten, Tester,
  Datum, Ergebnis (bestanden, fehlgeschlagen, blockiert, nicht ausgeführt), Belege.
- Abweichungen analysieren: Fehler im Testobjekt, im Testfall, in den Daten, in der Umgebung?
  Erst dann melden.
- Unerwartete Beobachtungen auch außerhalb des Testfalls melden.
- Status zeitnah im Werkzeug pflegen; Grundlage für die Überwachung.

## 4. Fehlerbericht

| Feld | Inhalt |
| --- | --- |
| ID, Titel | Kurz, eindeutig, Symptom und Ort („Rabatt wird bei Premiumkunden ab 100,01 € nicht gewährt“) |
| Testobjekt und Version | Build, Umgebung, Konfiguration |
| Bezug | Testfall, Anforderung, Risiko |
| Schritte zur Reproduktion | Minimal, nummeriert, mit Daten |
| Erwartetes Ergebnis | mit Quelle |
| Tatsächliches Ergebnis | Beobachtung, ohne Interpretation |
| Belege | Screenshot, Log, Trace, Request/Response (ohne echte Personendaten) |
| Schwere | Auswirkung auf Nutzung (kritisch, hoch, mittel, gering; oder EVB-IT-Klassen) |
| Priorität | Dringlichkeit der Behebung (vom Fehlergremium/PO) |
| Reproduzierbarkeit | immer, sporadisch (x von n), einmalig |
| Status | Lebenszyklus (Skill `testmanagement`) |

Ton: sachlich, beschreibend, ohne Schuldzuweisung. Ein Fehlerbericht ist eine Dienstleistung
für den Entwickler.

## 5. Fehlernachtest und Regression

- **Fehlernachtest:** Gemeldeter Fehler auf neuer Version mit denselben Schritten prüfen;
  zusätzlich Varianten um den Fehler herum.
- **Regressionstest:** Nicht geänderte Bereiche auf unerwünschte Seiteneffekte prüfen;
  Umfang nach Auswirkungsanalyse und Risiko; Automatisierung bevorzugt.

## 6. Anti-Patterns

- Start ohne erfüllte Eingangskriterien; Testzeit wird zur Inbetriebnahmezeit.
- Ergebnisse am Ende des Tages aus dem Gedächtnis nachtragen.
- Fehlerberichte ohne Version, ohne Schritte, ohne erwartetes Ergebnis.
- Schwere und Priorität vermischen.
- Fehlernachtest ohne Regression.

## 7. Prüfliste

- [ ] Eingangskriterien sind erfüllt und dokumentiert.
- [ ] Testlaufplan mit Reihenfolge, Umgebung, Verantwortlichen existiert.
- [ ] Jede Ausführung ist mit Version, Umgebung, Daten, Ergebnis und Belegen protokolliert.
- [ ] Abweichungen sind analysiert, bevor sie gemeldet werden.
- [ ] Fehlerberichte sind reproduzierbar, sachlich, mit Belegen und Bezug.
- [ ] Fehlernachtests und Regression sind eingeplant und durchgeführt.
