# Teststufen

## Inhalt
1. Übersicht
2. Komponententest
3. Komponentenintegrationstest
4. Systemtest
5. Systemintegrationstest
6. Abnahmetest
7. Teststufen im agilen Kontext
8. Anti-Patterns
9. Prüfliste

## 1. Übersicht

| Stufe | Testobjekt | Testbasis | Typische Fehler | Verantwortlich | Umgebung |
| --- | --- | --- | --- | --- | --- |
| Komponententest | Einzelne Einheit (Klasse, Modul, Funktion) | Komponentenspezifikation, Design, Code | Logik, Berechnung, Grenzfälle | Entwicklung | Entwicklerrechner, CI |
| Komponentenintegrationstest | Zusammenspiel von Komponenten | Architektur, Schnittstellen, Sequenzen | Schnittstellenfehler, Datenformate, Reihenfolge | Entwicklung, ggf. Test | CI, Integrationsumgebung |
| Systemtest | Gesamtsystem | Anforderungen, Use Cases, Stories, nicht-funktionale Anforderungen | Fehlende/falsche Funktionen, Qualitätsmängel | Testteam (unabhängig) | Systemtestumgebung, produktionsnah |
| Systemintegrationstest | System mit Partnersystemen, Diensten, Infrastruktur | Schnittstellenvereinbarungen, Prozesse, Infrastrukturspezifikation | Integrationsfehler, Protokolle, Ende-zu-Ende-Prozesse | Test, Integrationsmanagement | SIT-Umgebung mit Partnern |
| Abnahmetest | System im Nutzungskontext | Geschäftsprozesse, Nutzeranforderungen, Vertrag, Vorschriften, Betriebshandbuch | Nicht erfüllte Bedürfnisse, Betriebsuntauglichkeit | Fachbereich, Kunde, Betrieb | Abnahmeumgebung, produktionsgleich |

Integrationsstrategien: Top-down, Bottom-up, inkrementell nach Funktionen, Big Bang (vermeiden).
Je inkrementeller, desto leichter die Fehlerlokalisierung.

## 2. Komponententest

- Isoliert mit Test-Doubles; schnell, deterministisch, automatisiert.
- Verfahren: Black-Box auf die Komponentenschnittstelle, White-Box für Überdeckung.
- Oft TDD (Skill `agile-devops-testing`).
- Endekriterien: alle Tests grün, Überdeckungsziel für neue Zeilen, statische Analyse ohne neue Befunde.

## 3. Komponentenintegrationstest

- Schnittstellen und Interaktionen zwischen Komponenten, nicht deren Logik.
- Echte Abhängigkeiten in Containern (Testcontainers) oder Virtualisierung.
- Contract Tests zwischen Services verschiedener Teams.
- Datenbankzugriffe, Messaging, Konfiguration, Transaktionen.

## 4. Systemtest

- Funktionale und nicht-funktionale Prüfung des Gesamtsystems gegen Anforderungen.
- Umgebung möglichst produktionsnah (Konfiguration, Daten, Dimensionierung soweit nötig).
- Ende-zu-Ende-Abläufe innerhalb des Systems, Fehlerbehandlung, Rollen und Rechte.
- Nicht-funktionale Tests: Performance, Sicherheit, Barrierefreiheit, Zuverlässigkeit.
- Meist durch unabhängiges Testteam; Fachexperten unterstützen.

## 5. Systemintegrationstest

- System im Verbund: Partnersysteme, Behördenschnittstellen, Verzeichnisdienste, Druck-,
  Post- und Zahlungsdienste, Cloud-Dienste.
- Geschäftsprozesse über Systemgrenzen hinweg.
- Abstimmung mit Partnern: Zeiten, Daten, Ansprechpartner, Versionen (Skill `spezialtests`,
  Referenz Interoperabilität).
- Oft der Engpass: frühzeitig planen, Virtualisierung als Ausweich.

## 6. Abnahmetest

| Form | Ziel | Durchführung |
| --- | --- | --- |
| Benutzerabnahme (UAT) | Erfüllt das System die Bedürfnisse der Nutzer im Arbeitsalltag? | Fachbereich, Key User, mit realistischen Szenarien |
| Betriebliche Abnahme (OAT) | Ist das System betreibbar? Backup/Restore, Installation, Monitoring, Notfall, Wartung, Sicherheit | Betrieb, Administration |
| Vertragliche Abnahme | Sind vertragliche Abnahmekriterien erfüllt? | Auftraggeber, nach Vertrag (EVB-IT) |
| Regulatorische Abnahme | Werden Gesetze, Normen, Vorschriften erfüllt (BITV, DSGVO, BSI, Branchennormen)? | Prüfstellen, Fachbereich, Datenschutz, IT-Sicherheit |
| Alpha-Test | Frühe Nutzung durch potenzielle Nutzer beim Hersteller | Hersteller-Standort |
| Beta-Test | Nutzung durch echte Nutzer in ihrer Umgebung vor Freigabe | Kunden-Standort |

Hinweise:

- Abnahmetest ist kein zweiter Systemtest; Fehlerfindung ist nicht das Hauptziel, sondern
  Vertrauen und Freigabeentscheidung.
- Key User früh einbinden, schulen, Zeit freistellen; Testszenarien gemeinsam erarbeiten.
- Abnahmekriterien vertraglich und messbar; Fehlerklassen und Fristen vereinbart.
- Abnahmeprotokoll mit Entscheidung, offenen Mängeln und Auflagen.

## 7. Teststufen im agilen Kontext

- Stufen bleiben, werden aber kontinuierlich und oft gleichzeitig durchlaufen.
- Je Story: Komponenten- und Integrationstests im Sprint, Systemtests der Story im Sprint,
  Systemregression in der Pipeline.
- Release-Ebene: Systemintegrationstest, Abnahme, Betriebstests; ggf. Hardening-Sprint vermeiden
  durch kontinuierliche Integration.
- Definition of Done beschreibt, welche Stufen je Story abgeschlossen sein müssen.

## 8. Anti-Patterns

- Systemtest übernimmt Komponententests, weil Entwickler keine schreiben.
- Abnahme als erster Kontakt des Fachbereichs mit dem System.
- Systemintegrationstest erst kurz vor dem Termin; Partner nicht verfügbar.
- Gleiche Testfälle auf allen Stufen ohne unterschiedliche Ziele.
- OAT vergessen; Betrieb übernimmt ein System, das er nicht sichern kann.

## 9. Prüfliste

- [ ] Je Stufe sind Ziel, Testbasis, Testobjekt, Fehlerarten, Umgebung, Verantwortliche festgelegt.
- [ ] Integrationsstrategie ist inkrementell und dokumentiert.
- [ ] Systemintegrationstest mit Partnern ist terminiert, Daten und Ansprechpartner geklärt.
- [ ] Alle relevanten Abnahmeformen (UAT, OAT, vertraglich, regulatorisch) sind geplant.
- [ ] Key User sind benannt, geschult und haben Zeit.
- [ ] Endekriterien je Stufe sind messbar.
