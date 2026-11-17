# Performancetest

Prüft **Zeitverhalten, Ressourcennutzung und Kapazität** unter definierter Last. Ziel ist nicht
eine Zahl, sondern eine belastbare Aussage: „Das System erfüllt die Anforderungen bis zu X
gleichzeitigen Nutzern; bei Y bricht Z ein, weil …“

## Inhalt
1. Testarten
2. Anforderungen messbar machen
3. Lastmodell
4. Testumgebung
5. Skripte entwickeln
6. Durchführung und Messung
7. Auswertung und Engpassanalyse
8. Performance kontinuierlich
9. Werkzeuge
10. Anti-Patterns
11. Prüfliste

## 1. Testarten

| Art | Last | Frage |
| --- | --- | --- |
| Lasttest | Erwartete Last (Normal- und Spitzenlast) | Werden Antwortzeiten und Durchsatz bei realistischer Last erreicht? |
| Stresstest | Über die erwartete Last hinaus bis zum Bruch | Wo ist die Grenze, wie verhält sich das System dort, erholt es sich? |
| Spike-Test | Plötzlicher Lastanstieg | Verkraftet es Lastspitzen (Fristende, Kampagne, Montagmorgen)? |
| Dauertest (Soak/Endurance) | Normallast über Stunden bis Tage | Speicherlecks, Ressourcenerschöpfung, Degradation über Zeit? |
| Volumentest | Große Datenmengen | Verhalten bei großen Beständen, Dateien, Ergebnismengen? |
| Skalierbarkeitstest | Stufenweise Last bei wachsenden Ressourcen | Skaliert das System horizontal/vertikal wie erwartet? |
| Kapazitätstest | Steigende Last bis Grenzwert der Anforderung | Wie viele Nutzer/Transaktionen schafft es innerhalb der Anforderungen? |
| Concurrency-Test | Viele gleichzeitige Zugriffe auf dieselben Daten | Sperren, Deadlocks, Inkonsistenzen? |

## 2. Anforderungen messbar machen

„Schnell“ ist keine Anforderung. Formulierung:

> Bei <Last: n gleichzeitige Nutzer, m Transaktionen/h, Datenbestand d> soll <Transaktion>
> eine Antwortzeit von höchstens <t> Sekunden im <95.> Perzentil haben, bei einer Fehlerrate
> unter <x %> und einer CPU-Auslastung unter <y %>.

- Perzentile (p90, p95, p99) statt Mittelwerte; Mittelwerte verdecken Ausreißer.
- Je Transaktion eigene Ziele (Suche anders als Bescheiderstellung).
- Quellen: Fachbereich (Nutzererwartung), Betrieb (Ressourcen), SLAs, Produktionsmessungen,
  Prognosen (Wachstum, Fristtermine).
- Fehlende Anforderungen sind ein Befund; ohne Ziel kein Bestanden.

## 3. Lastmodell

- **Nutzungsprofil:** Welche Transaktionen in welchem Verhältnis (z. B. 60 % Suche, 25 % Anzeige,
  10 % Bearbeitung, 5 % Bescheid)?
- **Lastverlauf:** Normal, Spitze (Stunde, Tag, Jahr), Hochlauf und Abbau.
- **Nutzerverhalten:** Denkzeiten, Sitzungsdauer, Pacing; Pfade durch die Anwendung.
- **Datenvielfalt:** unterschiedliche Daten je virtuellem Nutzer, um Caches realistisch zu treffen.
- **Quellen:** Produktionslogs, Webanalyse, APM, Fachbereich, Hochrechnung bei Neusystemen.
- Formeln: Little's Law (N = X × R; gleichzeitige Nutzer = Durchsatz × Verweilzeit) zur
  Plausibilisierung.

## 4. Testumgebung

- So produktionsgleich wie möglich in Architektur, Konfiguration, Datenvolumen, Netz.
  Abweichungen dokumentieren und bei der Extrapolation berücksichtigen (Extrapolation ist riskant).
- Isoliert: keine anderen Tests gleichzeitig.
- Lastgeneratoren ausreichend dimensioniert und überwacht (Generator darf nicht Engpass sein).
- Monitoring aller Schichten: Client, Netz, Webserver, Anwendung (APM), Datenbank, Betriebssystem,
  externe Dienste.
- Externe Abhängigkeiten virtualisieren, wenn sie nicht lastfähig sind; Antwortzeiten realistisch simulieren.
- Testdaten im Produktionsvolumen (Skill `testdaten-testumgebung`).

## 5. Skripte entwickeln

- Protokollebene (HTTP, API) für Effizienz; Browser-basiert nur ergänzend für Rendering-Zeiten.
- Korrelation dynamischer Werte (Session-IDs, Tokens, CSRF, ViewState).
- Parametrisierung der Daten je Nutzer und Iteration.
- Prüfungen (Checks) auf fachlich korrekte Antworten, nicht nur HTTP 200.
- Transaktionen benennen und messen (Start/Ende je Geschäftsvorfall).
- Denkzeiten und Pacing einbauen.
- Skripte versionieren und reviewen; Einzeldurchlauf vor Lastlauf.

## 6. Durchführung und Messung

1. Baseline: Einzelnutzer, dann geringe Last.
2. Stufenweise steigern; Messpunkte je Stufe stabil halten.
3. Zielmessung über ausreichende Dauer (mindestens 30–60 Minuten je Stufe bei Lasttests).
4. Wiederholen; Streuung bewerten.
5. Protokoll: Version, Konfiguration, Daten, Lastmodell, Zeitpunkt, Besonderheiten.
6. Nach Änderung (Tuning) unter gleichen Bedingungen erneut messen; jeweils nur eine Änderung.

Messgrößen: Antwortzeiten (Perzentile je Transaktion), Durchsatz, Fehlerrate, Ressourcen
(CPU, Speicher, I/O, Netz, Verbindungen, Threads, Queues), GC, Datenbank (Abfragezeiten,
Sperren, Wartezeiten).

## 7. Auswertung und Engpassanalyse

- Antwortzeit über Last auftragen; Knickpunkt (Sättigung) identifizieren.
- Korrelation mit Ressourcen: Welche Ressource sättigt zuerst?
- Typische Engpässe: Datenbankabfragen ohne Index, N+1-Abfragen, Verbindungspools, Thread-Pools,
  Sperren, Speicher/GC, Logging, externe Dienste, Netzwerk, fehlendes Caching.
- APM-Traces zur Lokalisierung.
- Bericht: Ziele vs. Ergebnis je Transaktion, Kapazitätsgrenze, Engpässe mit Ursache,
  Empfehlungen, Bedingungen und Grenzen der Aussage.

## 8. Performance kontinuierlich

- Performance-Budgets je Komponente und Seite (z. B. Core Web Vitals: LCP, INP, CLS).
- Kurze Lasttests in der Pipeline (Smoke-Load, 5–10 Minuten) mit Schwellwerten gegen die Baseline.
- Microbenchmarks für kritische Funktionen (JMH, BenchmarkDotNet, pytest-benchmark).
- Produktionsmonitoring (APM, RUM) als Feedback für Lastmodell und Prioritäten.
- Großer Lasttest vor Releases mit erwarteten Laständerungen.

## 9. Werkzeuge

| Werkzeug | Hinweis |
| --- | --- |
| Apache JMeter | Open Source, verbreitet, GUI und CLI, viele Protokolle |
| Gatling | Code-basiert (Scala, Java, Kotlin, JS), effizient, gute Berichte |
| k6 (Grafana) | JavaScript, entwicklerfreundlich, CI-tauglich, Browser-Modul |
| Locust | Python, verteilt |
| NeoLoad, LoadRunner (OpenText) | Kommerziell, Enterprise, viele Protokolle (SAP, Citrix) |
| Artillery | Node.js, YAML-Szenarien |
| Lighthouse, WebPageTest | Frontend-Performance |
| APM: Dynatrace, AppDynamics, Datadog, Elastic APM, Grafana Tempo/Prometheus | Serverseitige Analyse |

## 10. Anti-Patterns

- Lasttest ohne Anforderungen; Ergebnis ist eine Zahl ohne Bewertung.
- Mittelwerte statt Perzentile.
- Kleine Testumgebung, Ergebnis linear auf Produktion hochgerechnet.
- Alle virtuellen Nutzer mit denselben Daten; Cache macht alles schnell.
- Keine Denkzeiten; unrealistische Last.
- Nur HTTP-Status prüfen; Fehlerseiten zählen als schnelle Antworten.
- Lasttest einmal kurz vor Produktion; keine Zeit für Behebung.
- Mehrere Tuning-Maßnahmen gleichzeitig; Wirkung nicht zuordenbar.

## 11. Prüfliste

- [ ] Anforderungen sind je Transaktion mit Last, Perzentil, Fehlerrate, Ressourcen formuliert.
- [ ] Lastmodell aus Daten abgeleitet, mit Profil, Verlauf, Denkzeiten, Datenvielfalt.
- [ ] Umgebung ist produktionsnah; Abweichungen dokumentiert; Monitoring aller Schichten aktiv.
- [ ] Skripte korreliert, parametrisiert, mit fachlichen Prüfungen, reviewt.
- [ ] Baseline, stufenweise Steigerung, Wiederholung; Bedingungen protokolliert.
- [ ] Engpässe mit Ursache und Empfehlung; Kapazitätsgrenze benannt.
- [ ] Kontinuierliche Performance-Prüfung in der Pipeline ist eingerichtet.
