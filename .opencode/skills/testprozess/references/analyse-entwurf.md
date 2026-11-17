# Testanalyse und Testentwurf

**Testanalyse** beantwortet „Was wird getestet?“ (Testbedingungen).
**Testentwurf** beantwortet „Wie wird getestet?“ (Testfälle, Testdaten, Umgebungsbedarf).

## Inhalt
1. Testbasis bewerten
2. Testbedingungen ableiten
3. Testfälle entwerfen
4. Testfallspezifikation
5. Rückverfolgbarkeit
6. Detailgrad
7. Anti-Patterns
8. Prüfliste

## 1. Testbasis bewerten

- Testbasis sammeln und versionieren: Anforderungen, Stories, Spezifikationen, Architektur,
  Schnittstellen, Risiken, Benutzerhandbuch.
- **Testbarkeit prüfen:** eindeutig, vollständig, widerspruchsfrei, prüfbar, mit Akzeptanzkriterium.
- Mängel als Befunde melden (Review, Skill `statischer-test`); das ist oft der wirksamste
  Fehlerfund des ganzen Projekts.

## 2. Testbedingungen ableiten

- Je Anforderung, Risiko und Qualitätsmerkmal die prüfbaren Aspekte bestimmen.
- Testbedingung: knapp, mit ID und Quelle, ohne konkrete Daten.
  Beispiel: „TB-12: Rabattberechnung für Premiumkunden bei Bestellwert über Schwelle (REQ-34).“
- Priorität aus dem Produktrisiko übernehmen.
- Testbedingungen für nicht-funktionale Merkmale nicht vergessen (Performance, Sicherheit,
  Barrierefreiheit, Usability).

## 3. Testfälle entwerfen

- Verfahren je Testbedingung wählen (Skills `black-box-testdesign`, `white-box-testdesign`,
  `exploratives-testen`).
- Testfälle so wenige wie möglich, so viele wie für die Abdeckung nötig.
- Testdatenanforderungen und Umgebungsbedarf je Testfall festhalten.
- Explorative Charters gelten als Testentwurf für reaktive Anteile.

## 4. Testfallspezifikation

| Feld | Inhalt |
| --- | --- |
| ID, Titel | Eindeutig, sprechend |
| Bezug | Testbedingung, Anforderung, Risiko |
| Priorität | aus Risiko |
| Vorbedingungen | Systemzustand, Daten, Berechtigungen |
| Testdaten | konkret oder Konstellation |
| Schritte | Aktion und erwartetes Ergebnis je Schritt (bei manuellen Tests) |
| Erwartetes Ergebnis | aus der Testbasis belegt |
| Nachbedingungen | Zustand danach, Aufräumen |
| Verfahren | angewandtes Testentwurfsverfahren |

## 5. Rückverfolgbarkeit

- Kette: Anforderung/Risiko ↔ Testbedingung ↔ Testfall ↔ Testergebnis ↔ Fehler.
- Bidirektional: Welche Tests decken eine Anforderung ab? Welche Anforderung prüft ein Test?
- Im Werkzeug pflegen (Xray, Polarion, DOORS, Azure DevOps), nicht in Excel neben dem Werkzeug.
- Auswertungen: nicht abgedeckte Anforderungen, Tests ohne Bezug, Auswirkungen von Änderungen.

## 6. Detailgrad

| Situation | Detailgrad |
| --- | --- |
| Hohe Risiken, Regulatorik, Nachweis, unerfahrene Tester, Übergabe | Detailliert: Schritte, Daten, erwartete Ergebnisse je Schritt |
| Erfahrene Tester, agile Teams, stabile Fachlichkeit | Logisch/abstrakt: Ziel, Bedingungen, erwartetes Verhalten |
| Automatisierung | Testfall ist Code; Spezifikation im Code oder in Gherkin |

## 7. Anti-Patterns

- Testfälle direkt aus der Oberfläche statt aus der Testbasis.
- Erwartetes Ergebnis „funktioniert korrekt“.
- Testfälle ohne Bezug; Rückverfolgbarkeit nachträglich hergestellt.
- Testbasis-Mängel stillschweigend umgehen, statt sie zu melden.
- Gleiche Detailtiefe für alles.

## 8. Prüfliste

- [ ] Testbasis ist versioniert und auf Testbarkeit geprüft; Mängel sind gemeldet.
- [ ] Testbedingungen haben ID, Quelle und Priorität.
- [ ] Verfahrenswahl je Testbedingung ist begründet.
- [ ] Testfälle haben belegte erwartete Ergebnisse und konkrete Daten oder Konstellationen.
- [ ] Rückverfolgbarkeit ist im Werkzeug bidirektional gepflegt.
- [ ] Detailgrad passt zu Risiko und Kontext.
