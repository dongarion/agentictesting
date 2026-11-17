# Migrations- und Datenbanktest

Prüft, dass Daten **vollständig, korrekt, konsistent und nutzbar** von einem System oder
Schema in ein anderes gelangen, und dass die Datenbank selbst korrekt arbeitet (Schema,
Constraints, Prozeduren, Performance).

## Inhalt
1. Arten von Migration
2. Testziele
3. Vorgehen
4. Abstimmungsverfahren (Reconciliation)
5. Datenbanktest
6. Umschaltung und Rückfall
7. Werkzeuge
8. Anti-Patterns
9. Prüfliste

## 1. Arten von Migration

| Art | Beispiel | Besonderheit |
| --- | --- | --- |
| Datenbankwechsel | Oracle → PostgreSQL | SQL-Dialekte, Typen, Sortierung, Zeichensätze, Prozeduren |
| Schemaänderung | Versionsmigration mit Flyway/Liquibase | Vorwärts und rückwärts, Mischbetrieb |
| Systemablösung | Altverfahren → Neuverfahren | Fachliche Transformation, Mapping, Historie |
| Plattformwechsel | On-Premises → Cloud | Netz, Latenz, Verschlüsselung, Mandanten |
| Konsolidierung | Mehrere Quellen → eine | Dubletten, Konflikte, führendes System |
| Archivierung/Löschung | Aussonderung nach Aufbewahrungsfrist | Vollständigkeit der Löschung, Nachweis |

## 2. Testziele

- **Vollständigkeit:** Alle Datensätze, die migriert werden sollen, sind da; keine zusätzlichen.
- **Korrektheit:** Jeder Wert ist richtig transformiert (Mapping, Typen, Einheiten, Codes, Zeitzonen).
- **Konsistenz:** Referenzen, Summen, Historien stimmen; Constraints gelten.
- **Nutzbarkeit:** Die Anwendung funktioniert mit den migrierten Daten (Fachprozesse,
  Berichte, Suche, Schnittstellen).
- **Nicht-Funktionales:** Laufzeit der Migration im Zeitfenster, Performance danach,
  Sicherheit und Datenschutz während der Migration.
- **Rückfall:** Rückmigration oder Weiterbetrieb des Altsystems ist möglich und getestet.

## 3. Vorgehen

1. **Mapping-Spezifikation prüfen** (Review): Quelle → Ziel je Feld, Transformationsregeln,
   Default-Werte, Behandlung von Null, ungültigen und historischen Werten, Ausschlusskriterien.
   Lücken sind Befunde vor dem ersten Lauf.
2. **Testdaten:** maskierter Vollbestand oder repräsentatives Subset plus gezielt konstruierte
   Fälle (jede Transformationsregel, jeder Sonderfall, bekannte Datenfehler des Altsystems).
3. **Probeläufe (Mock Migrations):** mehrere, mit Zeitmessung; nach jedem Lauf vollständige
   Abstimmung (siehe 4); Fehler klassifizieren: Mapping, Skript, Quelldaten, Zielschema.
4. **Fachliche Prüfung:** Fachbereich prüft Stichproben und Kennzahlen; Berichte alt gegen neu;
   Fachprozesse auf migrierten Daten durchspielen (Abnahmetest).
5. **Back-to-back:** Altsystem und Neusystem mit identischen Eingaben vergleichen
   (Skill fortgeschrittene Methoden).
6. **Generalprobe (Dress Rehearsal):** vollständiger Durchlauf unter Produktionsbedingungen
   mit Umschalt- und Rückfallplan, Zeitmessung, Beteiligten.
7. **Nach der Umschaltung:** Abstimmung auf Produktion, erhöhte Überwachung, Hypercare.

## 4. Abstimmungsverfahren (Reconciliation)

Mehrstufig, automatisiert, mit Bericht:

| Stufe | Prüfung |
| --- | --- |
| Zeilenzahlen | Je Tabelle/Entität: Quelle (nach Filter) = Ziel |
| Kontrollsummen | Summen, Min/Max, Anzahl Distinct je numerischer und Schlüsselspalte |
| Hash-Vergleich | Hash je Datensatz über normalisierte Felder; Abweichungen listen |
| Feldvergleich | Je Mapping-Regel: Stichprobe oder Vollvergleich mit Toleranz (Rundung, Zeit) |
| Referenzielle Integrität | Verwaiste Fremdschlüssel im Ziel = 0 |
| Fachliche Kennzahlen | Anzahl offener Fälle, Summe Forderungen, Fälle je Status: alt = neu |
| Negativprüfung | Ausgeschlossene Datensätze sind nicht im Ziel; gelöschte sind gelöscht |
| Historie | Zeitreihen und Versionen vollständig und in richtiger Reihenfolge |

Jede Abweichung erklärt (bewusste Bereinigung, Mapping-Fehler, Quellfehler) und dokumentiert.
Null unerklärte Abweichungen ist das Abnahmekriterium.

## 5. Datenbanktest

- **Schema:** Typen, Längen, Nullbarkeit, Defaults, Constraints, Indizes gegen Datenmodell;
  Migrationsskripte vorwärts und rückwärts; idempotent.
- **Constraints und Trigger:** jede Regel mit gültigen und ungültigen Daten testen
  (Black-Box-Skill); Trigger-Nebenwirkungen.
- **Gespeicherte Prozeduren und Funktionen:** Unit-Tests (tSQLt, pgTAP, utPLSQL), Grenzwerte,
  Fehlerbehandlung, Transaktionen.
- **Transaktionen und Nebenläufigkeit:** Isolation, Sperren, Deadlocks, Lost Update.
- **Zeichensätze, Sortierung, Zeitzonen:** Umlaute, Unicode-Normalisierung, Collation-Abhängigkeit
  von Sortierung und Vergleich, DST.
- **Performance:** Ausführungspläne, Indizes, Statistiken nach Migration aktualisiert,
  Abfragezeiten alt gegen neu.
- **Sicherheit:** Rechte, Verschlüsselung, Audit, keine Klartextgeheimnisse.
- **Backup und Restore:** vollständig getestet, Wiederherstellungszeit gemessen.

## 6. Umschaltung und Rückfall

- Umschaltplan mit Schritten, Verantwortlichen, Zeiten, Go/No-Go-Kriterien, Kommunikationsplan.
- Einfrierzeitraum für Quelldaten; Delta-Migration bei langen Fenstern.
- Rückfallplan getestet: Rückmigration oder Weiterbetrieb alt; Datenänderungen in der
  Zwischenzeit berücksichtigt.
- Mischbetrieb (Parallelbetrieb, Koexistenz): Synchronisation in beide Richtungen getestet.
- Hypercare: Dauer, Besetzung, Eskalation, erhöhte Überwachung der Datenqualität.

## 7. Werkzeuge

| Zweck | Werkzeuge |
| --- | --- |
| Schema-Migration | Flyway, Liquibase, Alembic, EF Migrations |
| Datenvergleich | eigene SQL/Python (pandas, Polars), data-diff, Great Expectations, dbt tests, Redgate Data Compare |
| Datenbank-Unit-Tests | tSQLt, pgTAP, utPLSQL, DbUnit |
| Datenqualität | Great Expectations, Deequ, Soda |
| ETL/ELT-Test | Werkzeugintegrierte Tests (Talend, Informatica), eigene Pipelines mit Prüfpunkten |
| Performance | Datenbank-eigene Analysewerkzeuge, JMeter JDBC, pgbench, HammerDB |

## 8. Anti-Patterns

- Nur Zeilenzahlen vergleichen.
- Abweichungen pauschal als „Altsystemfehler“ erklären.
- Erster vollständiger Lauf ist die Produktionsmigration.
- Mapping nur im Kopf des ETL-Entwicklers.
- Statistiken und Indizes nach Migration vergessen; „die neue Datenbank ist langsam“.
- Rückfallplan existiert nur auf Papier.
- Fachbereich sieht die Daten erst nach der Umschaltung.

## 9. Prüfliste

- [ ] Mapping-Spezifikation ist vollständig, reviewt und versioniert.
- [ ] Testdaten decken jede Transformationsregel und bekannte Datenfehler ab.
- [ ] Mindestens zwei Probeläufe mit vollständiger, automatisierter Abstimmung.
- [ ] Null unerklärte Abweichungen; jede erklärte ist dokumentiert.
- [ ] Fachbereich hat Stichproben und Kennzahlen abgenommen; Fachprozesse auf migrierten Daten getestet.
- [ ] Laufzeit passt ins Zeitfenster; Performance nach Migration gemessen.
- [ ] Generalprobe mit Umschalt- und Rückfallplan durchgeführt.
- [ ] Hypercare und Produktionsabstimmung sind geplant.
