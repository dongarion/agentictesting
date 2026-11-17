# Testüberwachung und Teststeuerung

**Überwachung** vergleicht den Ist-Stand mit dem Plan. **Steuerung** leitet Maßnahmen ab,
wenn sie abweichen. Beides läuft über die gesamte Testdauer.

## Inhalt
1. Kennzahlen
2. Fortschrittsbericht
3. Steuerungsmaßnahmen
4. Dashboards
5. Anti-Patterns
6. Prüfliste

## 1. Kennzahlen

| Bereich | Kennzahl |
| --- | --- |
| Fortschritt | Geplante, durchgeführte, bestandene, fehlgeschlagene, blockierte Testfälle; Trend über Zeit |
| Abdeckung | Anforderungen mit Test / gesamt; Risiken mit Test je Klasse; Codeüberdeckung, wo vereinbart |
| Fehler | Neu, offen, behoben, verifiziert je Klasse; Fehlerfindungs- und Behebungsrate; Alter offener Fehler; Wiedereröffnungsquote |
| Aufwand | Ist gegen Plan; Restaufwand; Produktivität (Testfälle/Tag) |
| Umgebung | Verfügbarkeit, umgebungsbedingte Ausfallzeit |
| Automatisierung | Laufzeit, Flaky-Rate, Ergebnis je Lauf |
| Qualität des Produkts | Fehlerdichte je Komponente, Restrisiko je Risikoklasse |

Regeln: Jede Kennzahl mit Stichtag und Bezugsgröße. Kennzahlen erklären, nicht nur zeigen.
Wenige, aussagekräftige Kennzahlen statt vieler.

## 2. Fortschrittsbericht

Gliederung (wöchentlich oder je Sprint, Empfänger: Projektleitung, PO, Auftraggeber):

1. **Ampel und Kernaussage** in zwei Sätzen: Liegen wir im Plan, was ist das größte Risiko?
2. **Fortschritt** gegen Plan (Tabelle oder Burn-up).
3. **Fehlerlage** je Klasse mit Trend; kritische Fehler einzeln mit Status.
4. **Abdeckung** von Anforderungen und Risiken.
5. **Blocker und Risiken** mit Maßnahmen und Verantwortlichen.
6. **Entscheidungsbedarf:** Was muss der Empfänger entscheiden?
7. **Ausblick** auf die nächste Periode.

Kurz: eine Seite. Details im Anhang oder im Dashboard.

## 3. Steuerungsmaßnahmen

| Abweichung | Mögliche Maßnahmen |
| --- | --- |
| Verzug in der Durchführung | Priorisieren nach Risiko; Ressourcen umschichten; Automatisierung nutzen; Umfang mit Auftraggeber anpassen |
| Viele Fehler in einer Komponente | Gezielte Vertiefung (explorativ, Review); Rücklieferung an Entwicklung; Eingangskriterien schärfen |
| Testobjekt instabil, viele Blocker | Testunterbrechung nach Kriterium; Smoke-Test vor jeder Lieferung |
| Umgebung nicht verfügbar | Eskalation; Ersatzumgebung; Virtualisierung |
| Fehlerbehebung zu langsam | Fehlergremium häufiger; Priorisierung mit PO; Behebungskapazität einfordern |
| Endekriterien nicht erreichbar | Restrisiko bewerten und zur Entscheidung vorlegen; Kriterium nicht stillschweigend ändern |

Jede Maßnahme mit Verantwortlichem, Termin und erwarteter Wirkung; Wirkung beim nächsten
Bericht prüfen.

## 4. Dashboards

- Live aus dem Testmanagement- und Fehlerwerkzeug (Jira/Xray, Azure DevOps, TestRail, Polarion).
- Getrennte Sichten: Team (operativ, täglich), Management (Ampel, Trend, Risiken).
- Automatisierungsergebnisse aus der Pipeline einbinden.
- Dashboard ersetzt keinen kommentierten Bericht; Zahlen brauchen Interpretation.

## 5. Anti-Patterns

- Grüne Ampel trotz offener kritischer Fehler, weil „wird noch behoben“.
- Testfallzahlen ohne Risikobezug; 95 % bestanden, aber das Kernrisiko ungetestet.
- Kennzahlen als Leistungsbewertung von Testern (fördert triviale Testfälle und Fehlermeldungen).
- Bericht ohne Entscheidungsbedarf; Probleme bleiben liegen.
- Endekriterien kurz vor dem Termin „angepasst“.

## 6. Prüfliste

- [ ] Kennzahlen sind festgelegt, haben Stichtag und Bezugsgröße.
- [ ] Bericht hat Kernaussage, Risiken und Entscheidungsbedarf.
- [ ] Abweichungen haben Maßnahmen mit Verantwortlichem und Termin.
- [ ] Restrisiko wird transparent zur Entscheidung vorgelegt.
- [ ] Dashboard und Bericht sind konsistent.
