# Shift-Left, Shift-Right und Continuous Testing

Zeitliche Ausrichtung der Strategie: **so früh wie möglich Fehler verhindern und finden,
so kontinuierlich wie möglich Feedback geben, und im Betrieb weiter lernen.**

## Inhalt
1. Shift-Left
2. Continuous Testing
3. Shift-Right
4. Zusammenspiel und Grenzen
5. Einführung
6. Anti-Patterns
7. Prüfliste

## 1. Shift-Left

Testaktivitäten früher im Lebenszyklus, weil Fehler umso billiger sind, je früher sie gefunden
oder verhindert werden.

Konkrete Maßnahmen:

| Maßnahme | Wirkung | Bezug |
| --- | --- | --- |
| Reviews von Anforderungen und Stories, Testbarkeit prüfen | Fehler in der Spezifikation vor dem Code | Skill `statischer-test` |
| Three Amigos, Specification by Example, ATDD | Gemeinsames Verständnis, Akzeptanztests vor Code | Skill `agile-devops-testing` |
| Testanalyse parallel zur Anforderungsentwicklung | Lücken früh sichtbar | Skill `testprozess` |
| TDD, Unit-Tests, Pairing | Fehler im Moment der Entstehung | Skill `agile-devops-testing` |
| Statische Analyse, SAST, Linting in IDE und Pipeline | Codefehler und Sicherheitslücken vor dem Merge | Skill `statischer-test`, `spezialtests` |
| Threat Modeling im Entwurf | Sicherheitsanforderungen und Tests vor dem Code | Skill `spezialtests` |
| Testbarkeit als Architekturanforderung | Testhaken, Schnittstellen, Beobachtbarkeit | Skill `testautomatisierung` |
| Frühe Performance-Tests auf Komponentenebene | Engpässe vor der Integration | Skill `teststufen-testarten` |
| Contract Testing | Integrationsfehler ohne integrierte Umgebung | Skill `agile-devops-testing` |

## 2. Continuous Testing

Automatisierte Tests als fester Bestandteil jeder Änderung, mit Feedback in Minuten und
automatischen Entscheidungen (Quality Gates).

- Pipeline-Stufen mit Zielzeiten (Skill `testautomatisierung`, Referenz CI/CD-Integration).
- Testpyramide als Leitbild für schnelle, stabile Rückmeldung.
- Ephemere Umgebungen je Änderung.
- Risikobasierte Testauswahl je Änderung (Test Impact Analysis).
- Quality Gates: Tests, Überdeckung neuer Zeilen, Sicherheit, Verträge, Performance-Budget.
- Kennzahlen: Durchlaufzeit, Flaky-Rate, Escapes; Change Failure Rate und Lead Time (DORA).

## 3. Shift-Right

Testen und Lernen im Betrieb, weil Labore die Realität nie vollständig abbilden.

| Maßnahme | Zweck |
| --- | --- |
| Canary-Releases, Blue/Green, Feature Toggles | Risiko beim Ausrollen begrenzen |
| Synthetisches Monitoring | Kernpfade in Produktion laufend prüfen |
| Observability (Metriken, Logs, Traces) als Testorakel | Wirkung von Änderungen sehen |
| A/B-Tests | Wirkung auf Nutzer messen |
| Chaos Engineering | Resilienz nachweisen |
| Nutzungsanalyse, Supporttickets, Fehlerlogs | Neue Testideen, Priorisierung |
| Beta-Programme, Dogfooding | Frühes Feedback echter Nutzer |

Details: Skill `agile-devops-testing` (Testen in Produktion, Chaos Engineering),
Skill `fortgeschrittene-testmethoden` (A/B, Dogfooding, Crowd).

## 4. Zusammenspiel und Grenzen

- Shift-Left und Shift-Right ersetzen das Testen in der Mitte nicht; sie verkleinern es und
  machen es zielgerichteter.
- Shift-Right braucht Beobachtbarkeit, schnelle Rücknahme und rechtliche Zulässigkeit.
  Fachverfahren mit Rechtswirkung (Bescheide, Zahlungen) erlauben Shift-Right meist nur
  für nicht-funktionale Aspekte und Betriebsbeobachtung; die fachliche Korrektheit muss vor
  dem Release nachgewiesen sein.
- Shift-Left braucht Zeit der Fachexperten und Entwickler früh im Projekt; das muss im
  Projektplan stehen, nicht nur im Testkonzept.
- Behördenumfeld: lange Freigabeketten verhindern Continuous Delivery in Produktion oft;
  Continuous Testing bis zur Abnahmeumgebung ist trotzdem möglich und lohnend.

## 5. Einführung

1. Ausgangslage messen: Wo werden Fehler gefunden (Phase), wie viele Escapes, wie lange
   dauert Regression?
2. Größten Hebel wählen (oft: Reviews der Anforderungen, Automatisierung der Regression,
   statische Analyse).
3. Pilot in einem Team, Wirkung messen.
4. Ausrollen mit Schulung und Anpassung der DoD.
5. Kennzahlen weiter verfolgen.

## 6. Anti-Patterns

- „Shift-Left“ heißt: Tester sollen früher anfangen, aber niemand sonst ändert etwas.
- „Shift-Right“ als Ausrede für weniger Tests vor dem Release.
- Continuous Integration ohne aussagekräftige Tests; die Pipeline ist grün und sagt nichts.
- Monitoring ohne Empfänger und Reaktion.

## 7. Prüfliste

- [ ] Shift-Left-Maßnahmen sind konkret, mit Verantwortlichen und Zeitbudget im Projektplan.
- [ ] Pipeline-Stufen, Gates und Zielzeiten sind definiert.
- [ ] Shift-Right-Maßnahmen sind auf Zulässigkeit, Beobachtbarkeit und Rücknahme geprüft.
- [ ] Rückfluss von Betriebserkenntnissen in Tests ist organisiert.
- [ ] Wirkung wird mit Kennzahlen gemessen (Fehlerphase, Escapes, Durchlaufzeit).
