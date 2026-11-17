# Testplanung

Ergebnis: **Testkonzept** (übergreifend, oft Master-Testplan) und bei Bedarf **Testpläne je
Teststufe**. In agilen Kontexten: Teststrategie auf Release-Ebene plus Testaufgaben je
Iteration; die Inhalte bleiben, die Form wird leichter.

## Inhalt
1. Eingaben
2. Gliederung eines Testkonzepts
3. Eingangs- und Endekriterien
4. Agile und hybride Planung
5. Behördenkontext
6. Anti-Patterns
7. Prüfliste

## 1. Eingaben

- Projektauftrag, Vertrag, Lastenheft/Pflichtenheft, Anforderungen, Architektur.
- Produktrisiken und Projektrisiken (Skill `testmanagement`).
- Organisationsweite Teststrategie oder Testrichtlinie, Kundenvorgaben, Normen.
- Release- und Projektplan, Ressourcen, Umgebungen, Werkzeuge.

## 2. Gliederung eines Testkonzepts

Angelehnt an ISO/IEC/IEEE 29119-3; Kundenvorlage hat Vorrang.

1. **Kontext:** Projekt, Testobjekt, Version, Bezugsdokumente, Begriffe.
2. **Testziele:** Was soll der Test nachweisen oder aufdecken? Messbar formuliert.
3. **Testumfang:** Im Scope / außerhalb des Scopes, je Komponente und Qualitätsmerkmal.
4. **Risiken:** Produktrisiken mit Bewertung und daraus abgeleiteter Testintensität;
   Projektrisiken mit Maßnahmen.
5. **Teststrategie:** Teststufen, Testarten, Verfahren je Risikoklasse, Automatisierungsanteil,
   Unabhängigkeitsgrad (Skill `teststrategie`).
6. **Testbasis und Rückverfolgbarkeit:** welche Dokumente, wie verknüpft, mit welchem Werkzeug.
7. **Eingangs- und Endekriterien** je Teststufe (siehe 3).
8. **Unterbrechungs- und Wiederaufnahmekriterien.**
9. **Testmittel und Arbeitsergebnisse:** welche Dokumente und Artefakte entstehen.
10. **Testumgebung und Testdaten:** Umgebungen, Daten, Schnittstellen (Skill `testdaten-testumgebung`).
11. **Werkzeuge:** Testmanagement, Fehlertracker, Automatisierung, CI.
12. **Organisation:** Rollen, Verantwortlichkeiten (RACI), Ansprechpartner, Kommunikation, Eskalation.
13. **Fehlermanagement:** Prozess, Klassifikation, Gremien (Skill `testmanagement`).
14. **Zeitplan und Meilensteine,** abgestimmt mit dem Projektplan.
15. **Aufwand und Ressourcen** mit Schätzgrundlage.
16. **Berichtswesen:** Berichte, Frequenz, Empfänger, Kennzahlen.
17. **Annahmen, Abhängigkeiten, offene Punkte.**
18. **Freigabe und Änderungshistorie.**

## 3. Eingangs- und Endekriterien

**Eingangskriterien** (Definition of Ready für den Test), Beispiele:

- Testobjekt in definierter Version geliefert, Lieferschein/Release Notes vorhanden.
- Vorgelagerte Teststufe abgeschlossen mit Endekriterien erfüllt.
- Testumgebung verfügbar und per Health-Check geprüft; Testdaten bereitgestellt.
- Testfälle für den Umfang spezifiziert und reviewt.
- Smoke-Test bestanden.

**Endekriterien** (Definition of Done für den Test), Beispiele:

- Alle Testfälle mit Priorität hoch durchgeführt; Durchführungsquote gesamt ≥ x %.
- Keine offenen Fehler der Klasse 1 (kritisch), höchstens n der Klasse 2 mit Workaround.
- Anforderungs- und Risikoabdeckung: alle Risiken der Klasse A getestet.
- Überdeckungsziele (Code, Anforderungen) erreicht, wo vereinbart.
- Testabschlussbericht erstellt und freigegeben.

Kriterien messbar, vorab vereinbart, mit Verantwortlichem für die Entscheidung. Abweichungen
werden bewusst entschieden und dokumentiert (Risikoakzeptanz), nicht stillschweigend.

## 4. Agile und hybride Planung

- Release-Ebene: Teststrategie, Quadranten, Automatisierungsansatz, Umgebungen, DoD.
- Iteration: Testaufgaben je Story, Akzeptanzkriterien, explorative Charters, Regressionsumfang.
- Lebendes Dokument im Wiki statt Word-Datei; Änderungen über Retrospektiven.
- Hybrid (agiles Entwicklungsteam, klassische Abnahme): Schnittstelle zwischen DoD der Sprints
  und Eingangskriterien der Abnahme explizit definieren.

## 5. Behördenkontext

- V-Modell XT Bund: Produkte „Prüfplan“, „Prüfspezifikation“, „Prüfprotokoll“, „Prüfbericht“;
  Vorlagen des Auftraggebers verwenden.
- Abnahme nach EVB-IT: Abnahmekriterien vertraglich; Fehlerklassen nach EVB-IT
  (betriebsverhindernd, betriebsbehindernd, leicht) übernehmen.
- Sicherheitskonzept, Datenschutz, BSI-Grundschutz, Barrierefreiheit (BITV) als Testgegenstände
  einplanen.
- Freigabegremien und Fristen früh einplanen.

## 6. Anti-Patterns

- Testkonzept als Kopie des letzten Projekts mit neuem Namen.
- Endekriterien, die nicht messbar sind („ausreichend getestet“).
- Kein Bezug zu Risiken; gleiche Testintensität für alles.
- Testkonzept einmal freigegeben, nie aktualisiert.
- Testumgebung und Testdaten als „wird bereitgestellt“ ohne Verantwortlichen.

## 7. Prüfliste

- [ ] Testziele sind messbar; Umfang und Ausschlüsse sind klar.
- [ ] Testintensität ist aus Produktrisiken abgeleitet.
- [ ] Eingangs-, End-, Unterbrechungs- und Wiederaufnahmekriterien sind messbar und vereinbart.
- [ ] Rollen, Verantwortlichkeiten, Kommunikation und Eskalation sind festgelegt.
- [ ] Umgebung, Testdaten und Werkzeuge haben Verantwortliche und Termine.
- [ ] Schätzung ist begründet; Zeitplan mit Projektplan abgestimmt.
- [ ] Annahmen und offene Punkte sind gelistet; Dokument hat Version und Freigabe.
