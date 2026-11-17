# Weitere nicht-funktionale Tests

Kompatibilität, Zuverlässigkeit und Wiederherstellung, Wartbarkeit, Portabilität/Flexibilität
und Installation, Lokalisierung und Internationalisierung.

## Inhalt
1. Kompatibilitätstest
2. Zuverlässigkeits- und Wiederherstellungstest
3. Wartbarkeitstest
4. Portabilitäts- und Installationstest
5. Lokalisierungs- und Internationalisierungstest
6. Anti-Patterns
7. Prüfliste

## 1. Kompatibilitätstest

**Koexistenz:** Läuft das System neben anderer Software in derselben Umgebung, ohne sich
gegenseitig zu stören (gemeinsame Bibliotheken, Ports, Ressourcen, Virenschutz, Clients am
Behördenarbeitsplatz)?

**Plattformkompatibilität:** Browser, Betriebssysteme, Geräte, Bildschirmauflösungen,
Office-Versionen, Java-/.NET-Laufzeiten, Datenbankversionen.

Vorgehen:

- Kompatibilitätsmatrix aus Vorgaben (Kunde, Zielgruppe, Nutzungsdaten) mit Prioritäten.
- Kombinationen paarweise reduzieren (Skill `black-box-testdesign`, Kombinatorik).
- Kernpfade auf allen priorisierten Kombinationen, Vollumfang auf der Hauptplattform.
- Automatisierung mit Cross-Browser-Grids (Selenium Grid, Playwright-Projekte, BrowserStack,
  Sauce Labs); visuelle Regression je Browser.
- Standardarbeitsplatz des Kunden (Client-Image, Gruppenrichtlinien, Proxy, Zertifikate) als
  eigene Testumgebung.

Interoperabilität: Skill `spezialtests`, Referenz Interoperabilität.

## 2. Zuverlässigkeits- und Wiederherstellungstest

| Aspekt | Prüfung |
| --- | --- |
| Fehlerfreiheit (Maturity) | Fehlerrate im Dauerbetrieb, MTBF, Fehlertrend über Releases |
| Verfügbarkeit | Messung über Zeitraum gegen SLA; geplante Wartung |
| Fehlertoleranz | Verhalten bei Ausfall von Komponenten, Netz, Abhängigkeiten; degradierter Betrieb; Wiederholungen, Timeouts, Circuit Breaker |
| Wiederherstellbarkeit | Neustart, Failover, Backup/Restore, Disaster Recovery; RTO und RPO gemessen |

Vorgehen:

- Anforderungen: Verfügbarkeit in %, RTO (maximale Wiederherstellungszeit), RPO (maximaler
  Datenverlust), Verhalten bei Teilausfällen.
- Failover-Tests: Knoten, Datenbank-Primary, Rechenzentrum; Messung der Umschaltzeit und
  der Auswirkungen auf laufende Transaktionen.
- Backup/Restore: vollständige Wiederherstellung in separater Umgebung, Daten- und
  Anwendungskonsistenz prüfen, Zeit messen. Ein nie getestetes Backup ist keins.
- Disaster-Recovery-Übung: Notfallhandbuch durchspielen, Rollen, Kommunikation.
- Fehlerinjektion und Chaos Engineering (Skill `agile-devops-testing`).
- Dauertest für Langzeitstabilität (siehe [performance.md](performance.md)).

## 3. Wartbarkeitstest

Wartbarkeit wird überwiegend **statisch** geprüft:

- Statische Analyse: Komplexität (zyklomatisch, kognitiv), Duplikate, Kopplung, Kohäsion,
  Code Smells, Regelverstöße, technische Schuld (SonarQube, Codeclimate, NDepend).
- Architekturprüfung: Abhängigkeitsregeln (ArchUnit, jQAssistant, dependency-cruiser), Schichtverletzungen.
- Reviews von Code, Architektur und Dokumentation (Skill `statischer-test`).
- Testbarkeit: Anteil automatisiert testbarer Komponenten, Aufwand für Testerstellung.
- Dynamisch: Änderungsszenarien durchspielen (Wie lange dauert eine typische Änderung?
  Wie viele Komponenten sind betroffen?); Analysierbarkeit über Logs und Diagnose prüfen.
- Kennzahlen mit Schwellwerten als Quality Gate auf neuen Code (nicht nur Gesamtbestand).

## 4. Portabilitäts- und Installationstest

ISO 25010:2023 fasst dies unter **Flexibilität**: Anpassbarkeit, Skalierbarkeit, Installierbarkeit,
Austauschbarkeit.

- **Installierbarkeit:** Erstinstallation, Update, Upgrade über mehrere Versionen, Deinstallation,
  Neuinstallation; unbeaufsichtigte Installation (Softwareverteilung, MSI, Paketmanager,
  Container); mit und ohne Adminrechte; Installation nach Handbuch wörtlich durchspielen.
- **Anpassbarkeit:** Betrieb in verschiedenen Umgebungen (Cloud, On-Premises, Betriebssysteme),
  Konfiguration ohne Codeänderung.
- **Austauschbarkeit:** Ersetzen einer Komponente oder eines Produkts (Datenbank, Bibliothek,
  Vorgängerversion) mit gleicher Funktion; Datenübernahme.
- **Skalierbarkeit:** siehe [performance.md](performance.md).
- Rückfall: Downgrade und Wiederherstellung nach fehlgeschlagenem Update.

## 5. Lokalisierungs- und Internationalisierungstest

- **Internationalisierung (i18n):** Ist das System grundsätzlich mehrsprachig und regionalisierbar?
  Zeichenkodierung (UTF-8 durchgängig), externalisierte Texte, keine zusammengesetzten Sätze
  aus Fragmenten, Platz für längere Texte, RTL-Fähigkeit, Formate über Locale.
- **Lokalisierung (l10n):** Ist eine konkrete Sprach- und Regionalversion korrekt?
  Übersetzungsqualität und Fachterminologie, Vollständigkeit (keine unübersetzten Texte),
  Abschneiden und Umbrüche, Datums-, Zeit-, Zahlen-, Währungsformate, Sortierung (Umlaute,
  ß), Adressformate, Kalender, Feiertage, Zeitzonen, Maßeinheiten, kulturelle Angemessenheit
  von Bildern und Farben, rechtliche Texte.
- Hilfsmittel: Pseudolokalisierung (künstlich verlängerte, akzentuierte Texte) früh im Entwicklungsprozess;
  Screenshot-Tests je Sprache; Muttersprachler für Abnahme.
- Im Behördenumfeld: Leichte Sprache, Gebärdensprache (BITV), Mehrsprachigkeit für
  Bürgerdienste, Namenskonventionen (Sonderzeichen in Namen nach DIN SPEC 91379 / String.Latin+).

## 6. Anti-Patterns

- Kompatibilität nur auf dem Entwicklerbrowser.
- Backup nie wiederhergestellt.
- Failover nur auf dem Papier.
- Wartbarkeit erst messen, wenn das System schon unwartbar ist.
- Installation nur durch Entwickler mit Vollzugriff getestet.
- Lokalisierung durch maschinelle Übersetzung ohne Prüfung durch Muttersprachler.
- Namen mit Sonderzeichen (é, ł, ç) nicht getestet; Bürger können sich nicht registrieren.

## 7. Prüfliste

- [ ] Kompatibilitätsmatrix mit Prioritäten und reduzierten Kombinationen; Kundenarbeitsplatz getestet.
- [ ] Verfügbarkeit, RTO, RPO sind festgelegt und gemessen; Backup/Restore und Failover sind getestet.
- [ ] Wartbarkeitskennzahlen und Architekturregeln laufen als Gate auf neuem Code.
- [ ] Installation, Update, Deinstallation und Rückfall sind nach Handbuch getestet.
- [ ] i18n-Grundlagen sind geprüft; l10n je Sprache inklusive Formate, Sortierung, Namenszeichen.
