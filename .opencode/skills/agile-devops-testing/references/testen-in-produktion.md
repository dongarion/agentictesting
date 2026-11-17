# Testen in Produktion und observability-basiertes Testen

Shift-Right: **Verhalten unter echten Bedingungen beobachten und Risiken beim Release
schrittweise freigeben.** Voraussetzung ist Beobachtbarkeit; ohne sie ist Testen in
Produktion Blindflug.

## Inhalt
1. Freigabestrategien
2. Feature Toggles
3. Observability als Testorakel
4. Synthetisches Monitoring
5. Rolle des Testers
6. Risiken und Leitplanken
7. Anti-Patterns
8. Prüfliste

## 1. Freigabestrategien

| Strategie | Prinzip | Prüffragen |
| --- | --- | --- |
| Blue/Green | Zwei identische Umgebungen, Umschalten per Router | Rollback-Zeit? Datenbankmigration kompatibel mit beiden? |
| Canary | Neue Version für kleinen Anteil (1–5 %), dann schrittweise mehr | Welche Metriken entscheiden? Automatischer Rollback bei Schwellwert? |
| Rolling | Instanz für Instanz ersetzen | Mischbetrieb alter und neuer Version verträglich? |
| Dark Launch | Neue Funktion läuft im Hintergrund, Ergebnis wird verworfen oder verglichen | Last und Fehlerverhalten ohne Nutzerwirkung messbar? |
| Shadow Traffic | Produktionsanfragen gespiegelt an neue Version | Nebenwirkungen (Schreibzugriffe, Mails) unterbunden? |
| Ring Deployment | Interne Nutzer, dann Early Adopter, dann alle | Feedbackkanal je Ring? |

Jede Strategie braucht ein **Abbruchkriterium** vor dem Start: Fehlerrate, Latenz,
Geschäftsmetrik, mit Schwellwert und Beobachtungsfenster.

## 2. Feature Toggles

- Typen: Release-Toggle (unfertig verstecken), Experiment-Toggle (A/B), Ops-Toggle
  (Notaus), Permission-Toggle (je Nutzergruppe).
- Testaufgaben:
  - Beide Zustände des Toggles testen, auch in Kombination mit anderen aktiven Toggles
    (paarweises Testen bei vielen Toggles).
  - Umschalten zur Laufzeit: Was passiert mit laufenden Sitzungen, Caches, offenen Transaktionen?
  - Default bei Ausfall des Toggle-Dienstes.
  - Datenmodell: Schreiben mit Toggle an, Lesen mit Toggle aus.
- Lebenszyklus: Jeder Toggle hat Besitzer und Ablaufdatum; abgelaufene Toggles sind
  technische Schuld und Testaufwand.

## 3. Observability als Testorakel

Die drei Säulen und ihre Testnutzung:

| Signal | Testnutzung |
| --- | --- |
| Metriken (RED: Rate, Errors, Duration; USE: Utilization, Saturation, Errors) | Canary-Entscheidung, Regressionsvergleich vor/nach Release, SLO-Prüfung |
| Logs (strukturiert, korreliert) | Fehleranalyse, Nachweis von Geschäftsereignissen, Suche nach unerwarteten Warnungen nach Release |
| Traces (verteilt, OpenTelemetry) | Latenzverteilung je Service, fehlende Spans als Hinweis auf nicht instrumentierte Pfade |

Vorgehen „observability-basiertes Testen“:

1. Vor dem Release: Welche Signale müssen sich wie verhalten, wenn die Änderung korrekt ist?
   Als Hypothese formulieren („Fehlerrate Endpunkt X bleibt < 0,1 %, neue Metrik Y erscheint“).
2. Testbarkeit der Observability selbst prüfen: Erzeugt jede Fehlerklasse ein unterscheidbares
   Signal? Sind IDs korreliert? Fehlt Instrumentierung?
3. Nach dem Release: Hypothesen gegen Dashboards prüfen, Abweichungen als Befund behandeln.
4. SLOs und Error Budgets als Abnahmekriterium für Releases nutzen.

Testen der Observability in der Testumgebung: Alarme auslösen, Dashboards gegen erzeugte
Fehler prüfen, Log-Inhalte auf personenbezogene Daten prüfen.

## 4. Synthetisches Monitoring

Automatisierte Testszenarien laufen regelmäßig gegen Produktion: Anmeldung, Kernprozess,
Schnittstellenaufruf. Testautomatisierung in anderer Rolle.

- Nur lesende oder gekennzeichnete Testtransaktionen (Testkonto, Testflag), die
  Auswertungen nicht verfälschen.
- Frequenz und Standorte nach Kritikalität.
- Alarme mit Eskalation; synthetische Checks ohne Empfänger sind nutzlos.

## 5. Rolle des Testers

- Abbruchkriterien und Beobachtungsfenster mit Betrieb und Produkt definieren.
- Toggle-Kombinationen und Umschaltverhalten testen.
- Produktionsdaten (Fehlerlogs, Nutzungspfade, Supporttickets) als Quelle für Charters und
  Regressionstests nutzen.
- Nach jedem Vorfall: Welcher Test hätte ihn gefunden? Test ergänzen oder bewusst nicht.

## 6. Risiken und Leitplanken

- Datenschutz: Testkonten, keine Testdaten in echten Auswertungen, Logs ohne personenbezogene Daten.
- Nebenwirkungen: Shadow Traffic darf keine Mails, Buchungen oder Benachrichtigungen auslösen.
- Regulierte Umgebungen: Canary für Fachverfahren mit Rechtswirkung nur, wenn beide Versionen
  rechtlich korrekt sind; Behörden-Umfeld oft Blue/Green mit vollständigem Abnahmetest vorher.
- Rollback muss getestet sein, inklusive Datenbank.

## 7. Anti-Patterns

- „Wir testen in Produktion“ als Ersatz für Tests davor.
- Canary ohne Metriken und Schwellwerte; Entscheidung nach Bauchgefühl.
- Toggles ohne Ablaufdatum; Kombinationsexplosion nach einem Jahr.
- Observability nur für den Betrieb gedacht; Tester nutzen sie nicht.
- Synthetische Checks, die echte Bestellungen auslösen.

## 8. Prüfliste

- [ ] Freigabestrategie, Abbruchkriterien und Beobachtungsfenster sind vor dem Release festgelegt.
- [ ] Beide Toggle-Zustände, Umschalten zur Laufzeit und Toggle-Kombinationen sind getestet.
- [ ] Observability-Hypothesen sind formuliert und nach dem Release geprüft.
- [ ] Rollback inklusive Daten ist getestet.
- [ ] Datenschutz und Nebenwirkungen sind abgesichert.
- [ ] Erkenntnisse aus Produktion fließen in Charters und Regressionstests zurück.
