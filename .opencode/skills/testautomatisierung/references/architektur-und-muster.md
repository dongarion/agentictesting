# Architektur, Ansätze und Entwurfsmuster

## Inhalt
1. Generische Testautomatisierungsarchitektur (gTAA)
2. Skriptansätze
3. Entwurfsmuster
4. Testdaten im Testcode
5. Struktur eines Repositories
6. Framework-Wahl
7. Anti-Patterns
8. Prüfliste

## 1. Generische Testautomatisierungsarchitektur (gTAA, CT-TAE)

Vier Schichten, strikt getrennt:

| Schicht | Inhalt | Wer pflegt |
| --- | --- | --- |
| Testgenerierung | Testfälle entwerfen, manuell oder aus Modellen | Testanalyst, MBT-Werkzeug |
| Testdefinition | Testfälle, Testdaten, Prozeduren in Fachsprache (Schlüsselwörter, Gherkin) | Testanalyst, Fachtester |
| Testausführung | Framework, Runner, Reporting, Logging | Automation Engineer |
| Testadaption | Technikadapter: Browser-, API-, DB-, Gerätetreiber; Page Objects | Automation Engineer |

Testfälle kennen keine Selektoren, keine URLs, keine SQL-Statements. Adapter kennen keine
Fachlogik. Ändert sich die Oberfläche, ändert sich nur die Adaptionsschicht.

Schnittstellen zu: Testmanagement (Traceability), Fehlermanagement, CI/CD, Konfigurations-
management, Testumgebungen.

## 2. Skriptansätze

| Ansatz | Prinzip | Eignung |
| --- | --- | --- |
| Capture/Replay | Aufzeichnen, abspielen | Nur zum Lernen oder als Startpunkt; nicht wartbar |
| Linear | Ein Skript je Test, alles inline | Wegwerftests, Prototypen |
| Strukturiert | Funktionen, Bibliotheken, Kontrollstrukturen | Basis jedes ernsthaften Frameworks |
| Datengetrieben | Ein Skript, viele Datensätze aus Tabelle/CSV/DB | Viele Varianten derselben Logik |
| Schlüsselwortgetrieben | Fachliche Schlüsselwörter („Antrag anlegen“), implementiert in Bibliotheken | Fachtester schreiben Tests; Robot Framework ist das Standardbeispiel |
| Verhaltensgetrieben | Gherkin-Szenarien an Schrittdefinitionen | Gemeinsame Spezifikation mit Fachbereich |
| Modellbasiert | Generierung aus Modellen | Zustandsreiche Systeme |

In der Praxis kombiniert: schlüsselwortgetrieben mit datengetriebenen Varianten auf einer
strukturierten Bibliothek.

## 3. Entwurfsmuster

- **Page Object:** Je Seite oder Komponente eine Klasse mit Elementen und fachlichen Aktionen
  (`anmelden(benutzer)`), keine Assertions darin. Rückgabe des nächsten Page Objects. Bei
  großen Seiten in Komponentenobjekte zerlegen.
- **Screenplay (Journey):** Akteure, Aufgaben, Interaktionen, Fragen. Besser skalierbar als
  Page Objects bei vielen Nutzerrollen und Workflows; höhere Einstiegshürde (Serenity, Boa Constrictor).
- **Fixtures und Setup/Teardown:** Vorbedingungen über API oder Datenbank herstellen, nie
  über die GUI. Aufräumen garantiert, auch bei Fehlschlag.
- **Testdaten-Builder / Object Mother:** `Antrag.gueltig().mitBetrag(100).ohneAnhang()`
  statt handgebauter Objekte in jedem Test.
- **Fluent Assertions und eigene Matcher:** `assertThat(antrag).istGenehmigtMitBetrag(100)`.
- **Wait-Strategien:** Explizite Bedingungen (Element sichtbar, Request beendet) statt
  fester Schlafzeiten. Playwright und Cypress warten automatisch; Selenium braucht Explicit Waits.
- **Facade für fachliche Abläufe:** `AntragsService.anlegenUndEinreichen()` kapselt mehrere
  Page-Object-Schritte, damit Tests kurz bleiben.
- **Konfiguration von außen:** Umgebung, URLs, Zugangsdaten per Umgebungsvariable oder
  Konfigurationsdatei, nie im Code. Geheimnisse aus dem Secret Store.

## 4. Testdaten im Testcode

- Jeder Test erzeugt seine Daten selbst (über API, Fixture, Builder) und räumt sie auf oder
  nutzt eindeutige Kennungen (Zeitstempel, UUID), damit Läufe parallel laufen können.
- Keine geteilten „goldenen“ Datensätze, die ein Test verändert und der nächste erwartet.
- Referenzdaten (Stammdaten, Kataloge) versioniert und per Skript einspielbar.
- Details im Skill Testdaten und Testumgebung.

## 5. Struktur eines Repositories

```
tests/                 # Testfälle in Fachsprache (Robot, Gherkin, pytest)
  smoke/
  regression/
resources/             # Schlüsselwörter, Schrittdefinitionen, Facades
pages/ oder screens/   # Page Objects, Komponentenobjekte
api/                   # API-Clients
data/                  # Testdaten, Builder
config/                # Umgebungen
utils/                 # Hilfsfunktionen, Logging
README.md              # Start, Konventionen, Umgebungen
```

Konventionen dokumentieren: Namensschema, Tagging (smoke, regression, slow, flaky),
Verzeichnisregeln, Review-Checkliste.

## 6. Framework-Wahl

Kriterien, in dieser Reihenfolge:

1. Passt zur Technologie des Produkts (Web, Mobile, Desktop, API, Embedded)?
2. Passt zu den Menschen, die die Tests schreiben und pflegen (Sprache, Lernkurve)?
3. Passt zur Architektur (Schichtentrennung möglich, Erweiterbarkeit)?
4. Integration in CI/CD, Reporting, Testmanagement.
5. Community, Pflege, Lizenz, Langlebigkeit.
6. Erst dann: Features.

Robot Framework ist stark, wenn Fachtester und Automatisierer gemeinsam arbeiten und
Schlüsselwörter die gemeinsame Sprache sind. Playwright oder Cypress mit TypeScript passen,
wenn Entwickler die Tests schreiben. pytest mit Playwright oder REST-Clients ist ein guter
Python-Standard. Entscheidung dokumentieren (ADR).

## 7. Anti-Patterns

- Selektoren und URLs in Testfällen.
- Assertions in Page Objects.
- `sleep(5)` als Synchronisation.
- Tests, die voneinander abhängen (Test 3 braucht Daten aus Test 2).
- Ein riesiger E2E-Test, der alles prüft und bei Schritt 2 stirbt.
- Testcode ohne Review, ohne Linting, ohne Versionierung der Abhängigkeiten.
- Framework-Wechsel als Lösung für Architekturprobleme.

## 8. Prüfliste

- [ ] Vier gTAA-Schichten sind erkennbar getrennt.
- [ ] Skriptansatz passt zu den Autoren der Tests.
- [ ] Page Objects oder Screenplay ohne Assertions; Facades für Abläufe.
- [ ] Explizite Wartebedingungen, keine festen Schlafzeiten.
- [ ] Jeder Test erzeugt und entfernt eigene Daten; Parallelausführung möglich.
- [ ] Konfiguration und Geheimnisse von außen.
- [ ] Repository-Struktur und Konventionen sind dokumentiert; Framework-Entscheidung als ADR.
