# CI/CD-Integration

Continuous Testing: **Jede Änderung löst die passenden Tests aus, das Ergebnis ist in
Minuten sichtbar und entscheidet automatisch über den nächsten Schritt.**

## Inhalt
1. Pipeline-Stufen
2. Quality Gates
3. Testumgebungen in der Pipeline
4. Parallelisierung und Caching
5. Artefakte und Reporting
6. Geheimnisse und Sicherheit
7. Anti-Patterns
8. Prüfliste

## 1. Pipeline-Stufen

| Stufe | Auslöser | Tests | Zielzeit |
| --- | --- | --- | --- |
| Pre-Commit / lokal | Entwickler | Linting, Formatierung, schnelle Unit-Tests | Sekunden |
| Commit / Merge Request | Push | Build, Unit, Komponenten, statische Analyse, Secret-Scan, Lizenz- und Abhängigkeitsprüfung (SCA) | < 10 min |
| Integration | Merge in Hauptzweig | API-, Vertrags-, Integrationstests mit Containern, Smoke-E2E | < 20–30 min |
| Abnahme / Staging | Deployment auf Testumgebung | Regressions-E2E, Barrierefreiheitsscan, DAST, Performance-Smoke | < 60 min, ggf. nächtlich voll |
| Nächtlich / wöchentlich | Zeitplan | Volle Regression, Lasttest, Mutationstest, Fuzzing, Cross-Browser-Matrix | Stunden |
| Produktion | Deployment | Synthetisches Monitoring, Canary-Analyse | laufend |

Prinzip: **Fail fast.** Billige Tests zuerst, teure nur, wenn die billigen grün sind.

## 2. Quality Gates

Automatisch prüfbare Kriterien je Stufe. Beispiele:

- Alle Tests der Stufe grün (Quarantäne-Tests ausgenommen, aber sichtbar).
- Überdeckung der geänderten Zeilen ≥ Schwellwert (nicht Gesamtüberdeckung, die sinkt
  bei jedem großen Feature).
- Keine neuen kritischen Befunde aus SAST, SCA, Secret-Scan.
- Keine Verschlechterung definierter Performance-Kennzahlen über Toleranz.
- Vertragsprüfung (`can-i-deploy`) bestanden.
- Barrierefreiheits-Scan ohne neue Fehler der Stufe A/AA.

Gates mit Ausnahmeprozess (begründet, dokumentiert, befristet), sonst werden sie umgangen.

## 3. Testumgebungen in der Pipeline

- **Ephemer:** Umgebung je Merge Request (Kubernetes-Namespace, Docker Compose,
  Review Apps), nach dem Lauf entsorgt. Keine Konflikte, keine Drift.
- **Testcontainers** für Datenbanken, Broker, Browser innerhalb des Testlaufs.
- Statische Umgebungen (Staging, Abnahme) nur, wo Fremdsysteme oder Lizenzen es erzwingen;
  dann mit Buchung und Health-Check.
- Datenbereitstellung per Skript und Migration; Zustand vor jedem Lauf definiert.
- Infrastructure as Code für alles, was reproduzierbar sein muss.

## 4. Parallelisierung und Caching

- Tests sharden (Playwright `--shard`, pytest-xdist, Gradle parallel, Robot Framework pabot).
- Matrix-Jobs für Browser, Betriebssysteme, Versionen; nur dort, wo Unterschiede erwartet werden.
- Abhängigkeiten und Build-Artefakte cachen; Browser-Images vorbereiten.
- Testauswahl nach Änderung (Impact-Analyse, Tags, geänderte Pfade) bei großen Suiten.
- Runner-Kapazität planen; Warteschlangen sind versteckte Laufzeit.

## 5. Artefakte und Reporting

- JUnit-XML für die Pipeline-Integration; zusätzlich HTML-Report (Allure, Playwright Report,
  Robot Log) als Artefakt.
- Bei Fehlschlag: Screenshot, Video, Trace, Konsolen- und Netzwerklog, Server-Log-Ausschnitt.
  Ohne Artefakte ist ein Fehlschlag in der Pipeline nicht analysierbar.
- Historie und Trends: Flaky-Rate, Laufzeit, Fehlschläge je Test (ReportPortal, Allure TestOps,
  eigene Auswertung).
- Benachrichtigung zielgerichtet: Verursacher des Commits, nicht der ganze Kanal.
- Testergebnisse an das Testmanagement melden, wenn Nachweise gefordert sind (Xray, Zephyr).

## 6. Geheimnisse und Sicherheit

- Zugangsdaten aus dem Secret Store der Plattform (GitLab CI Variables maskiert, Vault),
  nie im Repository, nie im Log.
- Testkonten mit minimalen Rechten; produktionsnahe Rechte nur in isolierten Umgebungen.
- Pipeline-Container aus vertrauenswürdigen Registries, gepinnte Versionen.
- Testdaten ohne Personenbezug (siehe Skill Testdaten und Testumgebung).

## 7. Anti-Patterns

- Alle Tests in einer Stufe; 90 Minuten bis zum ersten Ergebnis.
- Pipeline rot als Normalzustand; niemand schaut hin.
- Gates ohne Ausnahmeprozess; Entwickler kommentieren Tests aus.
- Tests gegen eine geteilte Staging-Umgebung, auf der gleichzeitig manuell getestet wird.
- Fehlschlag ohne Artefakte; „bei mir lokal geht es“.
- Zugangsdaten in der `.gitlab-ci.yml`.

## 8. Prüfliste

- [ ] Stufen mit Zielzeiten sind definiert; billige Tests laufen zuerst.
- [ ] Quality Gates sind automatisiert und haben einen Ausnahmeprozess.
- [ ] Umgebungen sind ephemer oder gebucht und per Health-Check geprüft.
- [ ] Parallelisierung und Caching sind eingerichtet; Laufzeit wird gemessen.
- [ ] Jeder Fehlschlag liefert Artefakte zur Analyse.
- [ ] Geheimnisse kommen aus dem Secret Store; Logs sind maskiert.
- [ ] Trends (Flaky-Rate, Laufzeit) sind sichtbar und werden besprochen.
