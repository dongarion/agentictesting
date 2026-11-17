# Fehlerursachenanalyse, Retrospektiven und Testprozessverbesserung

## Inhalt
1. Fehlerursachenanalyse (RCA)
2. Methoden der RCA
3. Retrospektiven
4. Testprozessverbesserung: Ansätze
5. Modelle im Überblick
6. Verbesserungszyklus (IDEAL)
7. Anti-Patterns
8. Prüfliste

## 1. Fehlerursachenanalyse (RCA)

Ziel: **Systematische Ursachen finden und beseitigen**, damit gleichartige Fehler nicht wieder
entstehen. Gegenstand: schwere Fehler, Produktionsvorfälle, Häufungen.

Ablauf:

1. Auswahl: Welche Fehler oder Fehlergruppen lohnen eine Analyse?
2. Fakten sammeln: Zeitleiste, Beteiligte, Artefakte, Änderungen.
3. Ursachen ermitteln (Methoden in 2): unmittelbare Ursache, beitragende Faktoren, Grundursache.
4. Maßnahmen ableiten: Was verhindert die Entstehung? Was hätte die Entdeckung früher ermöglicht?
5. Umsetzen, Wirkung prüfen.

Zwei Fragen je Fehler: **Warum ist er entstanden?** und **Warum haben wir ihn nicht früher gefunden?**

Blameless: Analyse von Prozessen und Bedingungen, nicht von Personen. Wer Schuld sucht,
bekommt Schweigen.

## 2. Methoden der RCA

| Methode | Vorgehen | Eignung |
| --- | --- | --- |
| 5 Why | Fünfmal „Warum?“ fragen, bis eine beeinflussbare Ursache erreicht ist | Einzelne Fehler, schnell |
| Ishikawa (Fischgräte) | Ursachen nach Kategorien (Mensch, Methode, Material/Daten, Maschine/Umgebung, Messung, Management) sammeln | Komplexe Fehler, Workshop |
| Fehlerbaumanalyse (FTA) | Top-down, logische Verknüpfungen von Ursachen | Sicherheitskritische Vorfälle |
| Pareto-Analyse | Fehler nach Ursachenkategorie zählen, die wenigen häufigen zuerst | Fehlerhäufungen |
| Orthogonal Defect Classification (ODC) | Fehler nach Auslöser, Art, Wirkung klassifizieren, Muster erkennen | Große Fehlermengen |
| Timeline / Post-Incident Review | Chronologie, Entscheidungspunkte, beitragende Faktoren | Produktionsvorfälle |

## 3. Retrospektiven

- Regelmäßig (Sprintende, Meilenstein, Projektende), mit allen Beteiligten.
- Struktur (Derby/Larsen): Rahmen setzen → Daten sammeln → Erkenntnisse gewinnen →
  Maßnahmen beschließen → abschließen.
- Formate: Start/Stop/Continue, Mad/Sad/Glad, Sailboat, Timeline, 4L (Liked, Learned, Lacked,
  Longed for). Format wechseln, damit es lebendig bleibt.
- Daten mitbringen: Fehlerauswertung, Escapes, Flaky-Rate, Durchlaufzeiten.
- Wenige Maßnahmen (1–3) mit Verantwortlichem; zu Beginn der nächsten Retro prüfen.
- Testthemen gehören in die Team-Retro, nicht nur in eine separate Test-Retro.

## 4. Testprozessverbesserung: Ansätze

| Ansatz | Prinzip | Wann |
| --- | --- | --- |
| Modellbasiert (präskriptiv) | Reifegradmodell gibt Ziele und Reihenfolge vor (TMMi) | Organisation will Benchmark, Zertifizierung, strukturierten Pfad |
| Modellbasiert (nicht präskriptiv) | Kontinuierliches Modell, Schwerpunkte frei wählbar (TPI NEXT) | Gezielte Verbesserung einzelner Bereiche |
| Analytisch (inhaltsbezogen) | Eigene Probleme analysieren, Maßnahmen ableiten (CTP, STEP, RCA, GQM) | Konkrete Schmerzpunkte, kleine Organisationen |
| Agil | Retrospektiven, Kaizen, kleine Experimente | Agile Teams |

Häufig kombiniert: Assessment mit Modell als Spiegel, Maßnahmen analytisch auf die eigenen
Probleme zugeschnitten.

## 5. Modelle im Überblick

- **TMMi (Test Maturity Model integration):** 5 Stufen, gestuft (Initial, Managed, Defined,
  Measured, Optimization); Prozessbereiche je Stufe (z. B. Stufe 2: Testrichtlinie und
  -strategie, Testplanung, Testüberwachung und -steuerung, Testentwurf und -durchführung,
  Testumgebung); formale Assessments durch akkreditierte Assessoren möglich.
- **TPI NEXT (Sogeti):** 16 Kernbereiche, Reifestufen je Bereich (kontrolliert, effizient,
  optimierend), Prüfpunkte, Testreifematrix; Clusterung für Verbesserungsreihenfolge.
- **CTP (Critical Testing Processes, Black):** 12 kritische Testprozesse, analytisch, flexibel.
- **STEP (Systematic Test and Evaluation Process, Craig):** anforderungsbasierte Strategie,
  Fokus auf frühen Testentwurf.
- **ISO/IEC 33063** Prozessbewertungsmodell für Testen (Grundlage ISO/IEC/IEEE 29119-2).

## 6. Verbesserungszyklus (IDEAL)

1. **Initiating:** Ziele, Sponsor, Rahmen, Nutzenargument.
2. **Diagnosing:** Assessment (Modell, Interviews, Dokumente, Kennzahlen), Ist-Zustand, Empfehlungen.
3. **Establishing:** Priorisieren, Maßnahmenplan, Pilot, Messgrößen für Wirkung.
4. **Acting:** Pilot durchführen, bewerten, ausrollen, schulen.
5. **Learning:** Wirkung messen, Erfahrungen sichern, nächsten Zyklus planen.

Erfolgsfaktoren: Management-Unterstützung, Beteiligung der Betroffenen, kleine sichtbare
Erfolge, Kommunikation, Messung der Wirkung, Veränderungsmanagement (Widerstände ernst nehmen).

## 7. Anti-Patterns

- RCA als Schuldsuche.
- Maßnahmen ohne Verantwortlichen, die nie umgesetzt werden.
- Retro-Maßnahmen jedes Mal dieselben, weil nichts passiert.
- Reifegrad als Ziel statt Werkzeug; Dokumente für das Assessment statt besseres Testen.
- Alles auf einmal verbessern.
- Verbesserung ohne Messung der Wirkung.

## 8. Prüfliste

- [ ] Schwere Fehler und Escapes werden regelmäßig per RCA analysiert, blameless.
- [ ] Je Fehler beide Fragen (Entstehung, späte Entdeckung) beantwortet.
- [ ] Retrospektiven finden statt, mit Daten und wenigen, verfolgten Maßnahmen.
- [ ] Verbesserungsansatz (Modell, analytisch, agil) ist bewusst gewählt.
- [ ] Assessment-Ergebnis ist priorisiert, Pilot geplant, Wirkung messbar.
- [ ] Sponsor und Beteiligung sind gesichert.
