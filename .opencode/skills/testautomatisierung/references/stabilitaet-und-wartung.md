# Stabilität, Flaky Tests und Wartung

Ein instabiler Test kostet mehr, als er nützt: Er verbraucht Aufmerksamkeit, erzeugt
Misstrauen und führt dazu, dass rote Läufe ignoriert werden. **Flaky-Rate ist eine
Führungskennzahl der Automatisierung.**

## Inhalt
1. Ursachen von Instabilität
2. Diagnose
3. Behebung je Ursache
4. Quarantäneprozess
5. Laufzeit senken
6. Wartung als Daueraufgabe
7. Prüfliste

## 1. Ursachen von Instabilität

| Ursache | Typisches Symptom |
| --- | --- |
| Synchronisation | Element nicht gefunden, veraltete Referenz (stale element), Assertion vor dem Laden |
| Testabhängigkeiten | Test besteht allein, scheitert in der Suite oder in anderer Reihenfolge |
| Geteilte Testdaten | Scheitert, wenn parallel oder nach anderem Lauf |
| Umgebung | Scheitert zu bestimmten Zeiten, auf bestimmten Runnern, bei Deployments |
| Nebenläufigkeit im Produkt | Scheitert selten, nicht reproduzierbar, echter Produktfehler |
| Zeitabhängigkeit | Scheitert um Mitternacht, Monatsende, Zeitumstellung |
| Externe Abhängigkeiten | Scheitert bei Ausfall oder Langsamkeit eines Drittsystems |
| Ressourcen | Scheitert bei Speicher- oder CPU-Druck, Browser-Abstürze |
| Fragile Selektoren | Scheitert nach jeder UI-Änderung |
| Animationen, Lazy Loading | Klick trifft ins Leere |
| Zufall im Test | Zufällige Testdaten ohne Seed |

## 2. Diagnose

1. Fehlschlag mehrfach ausführen (lokal und auf dem Runner), Fehlerrate bestimmen.
2. Artefakte auswerten: Screenshot, Video, Trace (Playwright Trace Viewer), Konsolen- und
   Netzwerklog, Server-Log zur gleichen Zeit.
3. Isoliert und in der Suite ausführen; Reihenfolge variieren (`pytest-randomly`,
   `--order random`).
4. Parallel ausführen, um Datenkonflikte sichtbar zu machen.
5. Zeitpunkte der Fehlschläge mit Deployments und Lasten korrelieren.
6. Ergebnis klassifizieren: Testfehler, Umgebungsfehler, Produktfehler. Ein „flaky“
   Produktfehler (Race Condition) ist ein echter Fehler und wird gemeldet.

## 3. Behebung je Ursache

- **Synchronisation:** Auf Zustand warten (Element sichtbar und aktiviert, Netzwerk ruhig,
  Antwort angekommen), nicht auf Zeit. Frameworks mit Auto-Wait nutzen. Nach Aktionen auf
  das Ergebnis der Aktion warten, nicht auf das nächste Element.
- **Abhängigkeiten:** Jeder Test erzeugt eigenen Zustand, idealerweise über API. Keine
  Reihenfolgeannahmen. Setup über Fixtures.
- **Daten:** Eindeutige Kennungen je Lauf, eigene Mandanten oder Namensräume, Aufräumen im
  Teardown.
- **Umgebung:** Dedizierte, reproduzierbare Umgebungen (Container, IaC), Health-Check vor
  dem Lauf, Deployments nicht während Testläufen.
- **Zeit:** Zeit im Test kontrollieren (Clock-Mocking, feste Zeitzone in der Umgebung).
- **Extern:** Virtualisieren oder in eine separate, als instabil markierte Stufe verschieben.
- **Selektoren:** Test-IDs (`data-testid`) oder Rollen und Beschriftungen (Accessibility-
  Selektoren) statt XPath über Struktur und CSS-Klassen. Mit Entwicklern vereinbaren.
- **Animationen:** Deaktivieren in Testumgebung (`prefers-reduced-motion`, Konfiguration).
- **Retries:** Nur als Übergangsmaßnahme mit Kennzeichnung, nie als Dauerlösung. Ein Test,
  der im zweiten Anlauf besteht, ist weiterhin flaky und wird gezählt.

## 4. Quarantäneprozess

1. Test, der ohne Produktänderung wiederholt fehlschlägt, wird markiert (`@flaky`,
   `@quarantine`) und aus dem blockierenden Lauf genommen, läuft aber weiter in einem
   nicht blockierenden Job.
2. Ticket mit Besitzer und Frist (z. B. 5 Arbeitstage).
3. Reparieren oder löschen. Ein Test in Dauerquarantäne ist gelöscht, nur niemand hat es zugegeben.
4. Flaky-Rate je Suite im Dashboard; wöchentlich im Team besprechen.

## 5. Laufzeit senken

- Parallelisieren (Sharding über Runner, Browser-Kontexte statt Browser-Instanzen).
- Ebene senken: GUI-Tests, die Logik prüfen, nach unten verschieben.
- Setup über API statt GUI; Anmeldung einmal, Session wiederverwenden (Storage State).
- Testdaten vorbereitet statt je Test erzeugt, wo es ohne Abhängigkeit geht.
- Testauswahl: Smoke je Commit, volle Regression nächtlich oder je Merge; Impact-Analyse
  (nur betroffene Tests) bei großen Suiten.
- Langsamste Tests messen und gezielt optimieren.

## 6. Wartung als Daueraufgabe

- Kapazität einplanen: ein fester Anteil je Sprint für Suite-Pflege.
- Refactoring der Suite wie Produktcode: Duplikate, tote Tests, veraltete Abstraktionen.
- Tests ohne Fehlschlag seit langer Zeit prüfen: Testen sie noch etwas Relevantes? Würden sie
  fehlschlagen können (Mutationstest, bewusstes Kaputtmachen)?
- Abhängigkeiten (Browser, Treiber, Bibliotheken) regelmäßig aktualisieren; Lockfiles.
- Dokumentation: README, Konventionen, Architekturentscheidungen aktuell halten.
- Löschen ist erlaubt. Jeder Test braucht einen Grund, zu existieren.

## 7. Prüfliste

- [ ] Flaky-Rate wird gemessen und ist sichtbar.
- [ ] Quarantäneprozess mit Frist und Besitzer existiert.
- [ ] Keine festen Schlafzeiten; Auto-Wait oder explizite Bedingungen.
- [ ] Tests laufen in zufälliger Reihenfolge und parallel ohne Fehlschlag.
- [ ] Selektorstrategie (Test-IDs, Rollen) ist mit Entwicklern vereinbart.
- [ ] Retries sind gekennzeichnet und zählen als flaky.
- [ ] Pflegekapazität ist im Sprint eingeplant.
