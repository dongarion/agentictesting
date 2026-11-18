# Testheon - Agentic Testing

Die Heimat der Test-Götter und -Helden.
13 Testagenten für Opencode 2.x mit 13 Skills zum Softwaretest. Agenten, Verantwortung, Haltung und
Skillrechte werden aus der Rollen-Methoden-Matrix erzeugt.

## Verzeichnisstruktur

```
agentic-testing/
├── README.md                     dieses Dokument
├── LICENSE                       Lizenztext CC BY-SA 4.0 (englisch, unverändert)
├── NOTICE.md                     Urheber, Namensnennung, Hinweis auf Ideen Dritter
├── AGENTS.md                     Regeln für alle Agenten (Opencode lädt die Datei automatisch)
├── .opencode/
│   ├── agents/                   13 Agenten, erzeugt durch den Generator
│   └── skills/                   13 Skills mit references/
├── arbeitsbereich/               Ablage für alle Arbeitsergebnisse (siehe AGENTS.md)
├── matrix/
│   └── Rollen-Methoden-Matrix.xlsx   Quelle für den Generator
└── werkzeuge/
    └── generator/generate_agents.py
```

## Einrichtung

1. Ordner als Projekt öffnen oder `.opencode/` und `AGENTS.md` in ein bestehendes Testprojekt kopieren.
   Für alle Projekte: Inhalt von `.opencode/agents/` und `.opencode/skills/` nach
   `~/.config/opencode/agents/` bzw. `~/.config/opencode/skills/` kopieren.
2. Qwen3.8-27B als Modell einrichten (lokal über Ollama, LM Studio, vLLM oder SGLang) und als
   Standardmodell in Opencode wählen. Die Agentendateien setzen bewusst kein `model`, damit alle
   Agenten das Standardmodell nutzen; ein abweichendes Modell je Agent kannst du im Frontmatter mit
   `model: provider/modell` ergänzen.
3. Kontext: Qwen3.8-27B unterstützt nativ 262.144 Token. Lokale Server begrenzen das Fenster oft
   standardmäßig deutlich niedriger (z. B. `num_ctx` bei Ollama). Für Agenten mit vielen Skills
   mindestens 32.000, besser 64.000 Token einstellen.
4. Prüfen: In Opencode die Agentenliste aufrufen; `athene` ist der primäre Agent, die übrigen 12 sind
   Subagenten. Die Skills müssen in der Skill-Liste erscheinen.

## Arbeiten mit den Agenten

- Aufträge an **Athene** geben. Sie zerlegt und verteilt an die Subagenten.
- Einen Subagenten direkt ansprechen: `@ariadne Leite Testbedingungen aus arbeitsbereich/testbasis/antrag.md ab.`
- Modi aufrufen: „Athene, Minos: triagiere die Fehler von heute.“ · „Ariadne, Sphinx: Review der Spezifikation.“ ·
  „Iris, Teiresias: BITV-Prüfung des Antragsformulars.“

- Lite-Modus: Für Teilfragen („Gib mir nur die Grenzwerte für das Feld Alter“) liefern alle Agenten
  nur den betreffenden Abschnitt statt des vollen Ausgabeschemas.

## Skills

| Skill | Referenzen |
| --- | --- |
| `testprozess` | Testplanung, Überwachung/Steuerung, Analyse/Entwurf, Realisierung/Durchführung, Testabschluss |
| `testmanagement` | Risiken, Schätzung/Priorisierung, Fehler-/Konfigurationsmanagement, Metriken/Kommunikation, RCA/Prozessverbesserung |
| `teststrategie` | Strategietypen, Shift-Left/Right/Continuous, Verteilung und Verantwortung |
| `teststufen-testarten` | Teststufen, Testarten, Performance, Barrierefreiheit, weitere nicht-funktionale Tests |
| `statischer-test` | Reviewarten und Prozess, Lesetechniken/Checklisten, statische Analyse |
| `black-box-testdesign` | Äquivalenzklassen/Grenzwerte, Entscheidungstabellen, Zustandsübergänge, Kombinatorik, Anwendungsfälle, Syntaxtest |
| `white-box-testdesign` | Kontrollfluss, Bedingungen/MC/DC, Datenfluss, API-Test, Überdeckungsziele |
| `exploratives-testen` | Charter/SBTM, Testheuristiken (inkl. Angriffswerten), Touren, Fehlerangriffe, Checklisten |
| `fortgeschrittene-testmethoden` | MBT, Property/metamorph, Mutation, Fuzzing, Back-to-back, Feldmethoden |
| `agile-devops-testing` | Specification by Example/BDD, TDD, Pair/Mob, Contract/Virtualisierung, Testen in Produktion, Chaos Engineering |
| `testautomatisierung` | Strategie/Ebenen, Architektur/Muster, Werkzeuge, Stabilität/Wartung, CI/CD, KI und Testagenten |
| `testdaten-testumgebung` | Testdatenmanagement, Anonymisierung, synthetische Daten, Subsetting, Umgebungsmanagement, IaC/ephemer |
| `spezialtests` | Security, KI-Systeme, Usability, Migration/Datenbank, Mobile, Embedded, Interoperabilität |

Jeder Skill trägt im Frontmatter `license` und `metadata` (Autor, Copyright, Version, Basis, Sprache)
und enthält eine eigene `LICENSE.txt`, damit er auch einzeln weitergegeben werden kann.

## Lizenz

Alle Inhalte stehen unter **CC BY-SA 4.0** (Namensnennung – Weitergabe unter gleichen Bedingungen),
siehe `LICENSE` (verbindlicher Lizenztext) und `NOTICE.md` (Urheber und Namensnennung). Nutzung, auch kommerziell, und Bearbeitung sind erlaubt, wenn IT-Beratung Martin
Klein genannt wird, Änderungen kenntlich gemacht werden und Bearbeitungen unter derselben Lizenz
weitergegeben werden. Für Software empfiehlt Creative Commons eigentlich Software-Lizenzen; der
Generator ist hier bewusst mit eingeschlossen.

## Rechte je Agent

Jeder Agent hat dieselben Grundrechte (Opencode-V2-`permissions`):

| Aktion | Regel |
| --- | --- |
| `edit` | nur `arbeitsbereich/**` |
| `shell` | mit Rückfrage |
| `webfetch`, `websearch` | gesperrt (lokaler Betrieb, Kundenumfelder mit Sicherheitsüberprüfung) |
| `skill` | nur die Skills, die die Matrix dem Agenten zuordnet (Kernskills und unterstützende Skills mit mindestens zwei Methoden) |
| `subagent` | nur Athene darf Subagenten aufrufen |

Für einen Einsatz mit Automatisierung braucht Talos Schreibrechte im Testcode. Dazu in
`.opencode/agents/talos.md` eine Regel ergänzen, z. B. `edit` auf `tests/**` mit `allow`. Weil der
Generator die Dateien überschreibt, die Regel danach im Generator (Liste `perms`) nachziehen.

## Agenten neu erzeugen

Nach Änderungen an der Matrix:

1. Die Tabelle als `.xlsx` herunterladen und als `matrix/Rollen-Methoden-Matrix.xlsx` speichern.
2. `pip install openpyxl`
3. `python3 werkzeuge/generator/generate_agents.py`

Der Generator liest die Blätter Agenten, Agent-Methode, Methode-Eigenschaft, Eigenschaften und
Agent-Eigenschaft (Korrekturen). Die Haltung rechnet er selbst nach, wie im Blatt Berechnung.
Voraussetzungen: Die Agentenspalten in Agent-Methode stehen in derselben Reihenfolge wie die Zeilen im
Blatt Agenten; Agent-Methode und Methode-Eigenschaft haben dieselben Methoden in derselben Reihenfolge.
Die Modi (Minos, Themis, Sphinx, Teiresias) stehen als Text im Generator (`MODI`).

### Domänenrollen anpassen

Die Untertitel der Agenten sind Platzhalter (`Domänenrolle A` bis `Domänenrolle M`). Für einen Kunden
im Blatt **Agenten**, Spalte **Untertitel**, durch die Rollenbezeichnungen der Domäne ersetzen (zum
Beispiel Fachbereich, Abteilung oder Funktion beim Kunden) und den Generator neu laufen lassen. Der
Untertitel erscheint in `description` und in der Überschrift jedes Agenten sowie in der Teamtabelle in
`AGENTS.md` (dort von Hand nachziehen).

## Pilot

Empfohlener Einstieg mit fünf Agenten: Athene, Ariadne, Odysseus, Hephaistos, Talos. Je Agent einige
Prüfaufgaben mit bekannter Lösung anlegen, zum Beispiel eine Spezifikation mit eingebauten
Mehrdeutigkeiten für Ariadne oder Code mit eingebauten Fehlern für Hephaistos, und messen: Funde,
Fehlalarme, richtige Agentenwahl durch Athene, richtige Skillwahl.

## Hinweise

- Normwerte, Werkzeuglisten und Rechtsrahmen in den Skills sind Orientierung und vor dem Kundeneinsatz
  gegen die gültige Fassung zu prüfen; sie ersetzen keine Rechts- oder Datenschutzberatung.
- Die Agentennamen stammen aus der griechischen Mythologie (gemeinfrei). Vor einer Nutzung als Marke
  Markenrecherche durchführen.

## Lizenz

© 2026 IT-Beratung Martin Klein · Lizenz CC BY-SA 4.0, siehe `LICENSE` und `NOTICE.md` · Stand 2026-11-18 · Version 1.0
