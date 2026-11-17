# Testabschluss

Findet an Meilensteinen statt: Ende einer Teststufe, eines Release, eines Projekts, einer
Iteration (dort leichtgewichtig in Review und Retrospektive).

## Inhalt
1. Aufgaben
2. Testabschlussbericht
3. Archivierung und Übergabe
4. Lessons Learned
5. Anti-Patterns
6. Prüfliste

## 1. Aufgaben

- Endekriterien prüfen und Ergebnis dokumentieren.
- Offene Fehler klären: behoben, verschoben (mit Entscheidung), akzeptiert (mit Risikoakzeptanz).
- Testabschlussbericht erstellen und freigeben lassen.
- Testmittel archivieren oder übergeben (Wartung, Betrieb, Folgeprojekt).
- Testumgebungen und Testdaten zurückbauen oder übergeben; personenbezogene Daten löschen.
- Lessons Learned erheben und umsetzen.

## 2. Testabschlussbericht

1. **Zusammenfassung und Empfehlung:** Freigabe ja/nein/unter Auflagen, mit Begründung.
2. **Testobjekt und Umfang:** Versionen, Umgebungen, Zeitraum, Abweichungen vom Plan.
3. **Endekriterien:** je Kriterium Soll, Ist, erfüllt/nicht erfüllt.
4. **Ergebnisse:** Durchführung, Abdeckung von Anforderungen und Risiken, Überdeckung.
5. **Fehler:** gefundene, behobene, offene je Klasse; offene einzeln mit Workaround und Entscheidung.
6. **Restrisiken:** nicht oder eingeschränkt getestete Bereiche, offene Fehler, Annahmen.
7. **Abweichungen vom Testkonzept** mit Begründung.
8. **Bewertung des Testprozesses:** Aufwand Plan/Ist, Probleme, Verbesserungen.
9. **Anhänge:** Testprotokolle, Fehlerlisten, Abdeckungsberichte.

Die Empfehlung gibt der Test; die Freigabeentscheidung trifft der Auftraggeber.

## 3. Archivierung und Übergabe

- Testmittel (Testfälle, Skripte, Daten, Umgebungsdefinitionen) versioniert ablegen mit Bezug
  zum Release.
- Übergabe an Wartung oder Betrieb: Regressionssuite, Smoke-Tests, bekannte Probleme,
  Werkzeuge, Ansprechpartner.
- Aufbewahrungsfristen beachten (Verträge, Normen, Behördenvorgaben).

## 4. Lessons Learned

- Format: Retrospektive mit allen Beteiligten, nicht nur dem Testteam.
- Leitfragen: Was hat gut funktioniert? Was nicht? Welche Fehler sind spät oder in Produktion
  gefunden worden, und warum? Welche Schätzungen lagen daneben? Was ändern wir konkret?
- Maßnahmen mit Verantwortlichem und Termin; im nächsten Projekt prüfen.
- Eingang in Testprozessverbesserung (Skill `testmanagement`).

## 5. Anti-Patterns

- Kein Abschlussbericht, weil das Release schon läuft.
- Offene Fehler ohne Entscheidung „in die nächste Version“ verschoben.
- Lessons Learned als Liste ohne Maßnahmen, die niemand wieder liest.
- Testdaten mit Personenbezug bleiben auf Umgebungen liegen.

## 6. Prüfliste

- [ ] Endekriterien sind einzeln bewertet.
- [ ] Jeder offene Fehler hat eine dokumentierte Entscheidung.
- [ ] Restrisiken sind benannt; Empfehlung ist begründet.
- [ ] Bericht ist freigegeben.
- [ ] Testmittel sind archiviert oder übergeben; Umgebungen und Daten bereinigt.
- [ ] Lessons Learned haben Maßnahmen mit Verantwortlichen.
