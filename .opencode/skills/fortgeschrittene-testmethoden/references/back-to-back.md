# Back-to-back-Test (Vergleichstest)

Zwei oder mehr **Implementierungen derselben Spezifikation** erhalten identische Eingaben;
Abweichungen in den Ausgaben sind Befunde. Das Orakel ist die jeweils andere Implementierung.

## Inhalt
1. Einsatzfälle
2. Vorgehen
3. Vergleichsregeln
4. Abweichungen bewerten
5. Werkzeuge und Umsetzung
6. Anti-Patterns
7. Prüfliste

## 1. Einsatzfälle

- **Migration und Ablösung:** Altsystem gegen Neusystem (Host → Java, Monolith → Services,
  Anbieterwechsel).
- **Refactoring und Reimplementierung:** alte Version gegen neue Version derselben Komponente.
- **Diversität in sicherheitskritischen Systemen:** unabhängig entwickelte Implementierungen
  (N-Version-Programming, Modell gegen Code bei Automotive/MiL-SiL).
- **Compiler, Datenbanken, Bibliotheken:** Differential Testing verschiedener Produkte.
- **KI-Modelle:** neues Modell gegen Vorgängerversion oder gegen regelbasierte Referenz.

## 2. Vorgehen

1. **Vergleichsumfang festlegen:** Welche Funktionen, welche Ausgaben, welche Nebenwirkungen
   (Datenbankzustand, Nachrichten, Logs)?
2. **Eingabemenge aufbauen:**
   - Produktionsdaten (anonymisiert) für Realitätsnähe,
   - systematisch entworfene Fälle (Black-Box-Skill) für Grenzen,
   - generierte Fälle (PBT, Fuzzing) für Breite.
3. **Ausführungsrahmen bauen:** gleiche Eingaben, gleiche Ausgangsdaten, gleiche Zeitbasis,
   isolierte Umgebungen. Shadow Traffic (Spiegelung echter Anfragen) bei Services.
4. **Vergleichen** nach festen Regeln (siehe 3).
5. **Abweichungen klassifizieren** (siehe 4), beheben oder als akzeptiert dokumentieren.
6. **Übereinstimmungsquote** je Funktion berichten und Abbruchkriterium für die Umstellung festlegen.

## 3. Vergleichsregeln

- **Normalisieren** vor dem Vergleich: Zeitstempel, IDs, Reihenfolge ungeordneter Mengen,
  Whitespace, Rundung auf vereinbarte Stellen, Zeitzonen.
- **Toleranzen** nur, wo die Spezifikation sie zulässt (Gleitkomma, Zeit). Jede Toleranz
  dokumentieren.
- **Felder ausschließen** nur mit Begründung (technische Metadaten).
- Strukturierte Vergleiche (JSON-Diff, Tabellen-Diff je Schlüssel) statt Textvergleich.
- Auch **Fehlerverhalten** vergleichen: gleiche Eingabe muss in beiden Systemen zum
  gleichen Fehlertyp führen.

## 4. Abweichungen bewerten

| Klasse | Behandlung |
| --- | --- |
| Fehler im neuen System | Beheben |
| Fehler im alten System | Dokumentieren; bewusst entscheiden, ob das neue System den Fehler nachbilden muss (Kompatibilität) oder korrigieren darf |
| Spezifikationslücke | Beide Systeme interpretieren anders; Fachbereich entscheidet, Spezifikation ergänzen |
| Zulässige Abweichung | Toleranz oder Normalisierungsregel ergänzen, begründen |
| Testrahmenfehler | Normalisierung oder Datenbereitstellung korrigieren |

Die häufigste Erkenntnis in Migrationsprojekten: Das Altsystem war nie so spezifiziert, wie
alle dachten. Diese Lücken früh an den Fachbereich geben.

## 5. Werkzeuge und Umsetzung

- Datenvergleich: eigene Skripte (pandas, jq, SQL-Except), Datenbank-Diff-Werkzeuge,
  Great Expectations für Datenqualitätsregeln.
- Service-Vergleich: Shadow-Deployment, Diffy (Twitter, archiviert, Konzept weiterhin gültig),
  eigene Proxy-Lösungen, Feature-Toggle mit Doppelausführung.
- Modell gegen Code: Simulationsframeworks (Simulink Test), HiL/SiL-Prüfstände.
- ML: Offline-Replay von Produktionsanfragen gegen beide Modelle, Metrikvergleich.

## 6. Anti-Patterns

- Textueller Vollvergleich ohne Normalisierung; tausende Scheinabweichungen.
- Abweichungen pauschal als „Altsystemfehler“ abtun, ohne Fachentscheidung.
- Nur Erfolgsfälle vergleichen, Fehlerverhalten ignorieren.
- Übereinstimmung als Korrektheitsbeweis verkaufen: Beide können gleich falsch sein, besonders
  wenn das neue System aus dem alten abgeleitet wurde.

## 7. Prüfliste

- [ ] Vergleichsumfang inklusive Nebenwirkungen ist festgelegt.
- [ ] Eingabemenge kombiniert reale, systematische und generierte Fälle.
- [ ] Normalisierung und Toleranzen sind dokumentiert und begründet.
- [ ] Jede Abweichung ist klassifiziert, Spezifikationslücken sind an den Fachbereich gemeldet.
- [ ] Übereinstimmungsquote je Funktion und Abbruchkriterium sind berichtet.
- [ ] Grenze der Aussage („gleich“ heißt nicht „richtig“) steht im Bericht.
