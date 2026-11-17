# Statische Analyse

Werkzeuggestützte Prüfung von Code, Konfiguration, Modellen und Dokumenten ohne Ausführung.

## Inhalt
1. Arten der statischen Analyse
2. Kontroll- und Datenflussanalyse
3. Metriken
4. Einführung und Regelwerk
5. Befunde bewerten
6. Quality Gates
7. Werkzeuge
8. Anti-Patterns
9. Prüfliste

## 1. Arten der statischen Analyse

| Art | Findet | Beispiele |
| --- | --- | --- |
| Formatierung und Stil | Inkonsistente Formatierung, Namenskonventionen | Prettier, Black, gofmt, Checkstyle |
| Linting / Regelprüfung | Fehleranfällige Konstrukte, ungenutzte Variablen, Code Smells | ESLint, Ruff, Pylint, PMD, RuboCop, ShellCheck |
| Typprüfung | Typfehler vor Laufzeit | TypeScript, mypy, Pyright |
| Fehlermusteranalyse | Null-Dereferenzierung, Ressourcenlecks, Nebenläufigkeitsfehler | SpotBugs, Error Prone, Infer, Clang Static Analyzer |
| Sicherheitsanalyse (SAST) | Injection, unsichere APIs, Kryptofehler, Geheimnisse | Semgrep, CodeQL, Bandit, Fortify (Skill `spezialtests`) |
| Abhängigkeitsanalyse (SCA) | Verwundbare und veraltete Bibliotheken, Lizenzen | Dependency-Check, Trivy, Renovate |
| Architekturanalyse | Schichtverletzungen, Zyklen, unerlaubte Abhängigkeiten | ArchUnit, jQAssistant, dependency-cruiser, Sonargraph |
| Komplexitäts- und Qualitätsmetriken | Komplexität, Duplikate, technische Schuld | SonarQube, Lizard, radon |
| Codierstandards (sicherheitskritisch) | Verstöße gegen MISRA, CERT, AUTOSAR C++ | Helix QAC, Polyspace, Parasoft, PC-lint |
| Formale Laufzeitfehleranalyse | Nachweis der Abwesenheit bestimmter Laufzeitfehler | Polyspace Code Prover, Astrée, Frama-C |
| IaC und Konfiguration | Fehlkonfiguration, unsichere Einstellungen | Checkov, tfsec, hadolint, kube-linter |
| Dokumente und Modelle | Rechtschreibung, Terminologie, Modellregeln, Schema | Vale, LanguageTool, Modellprüfer, Schema-Validatoren |

## 2. Kontroll- und Datenflussanalyse

- **Kontrollflussanalyse:** unerreichbarer Code, Endlosschleifen, fehlende Rückgabewerte,
  Sprünge in Schleifen; Grundlage für Komplexitätsmetriken.
- **Datenflussanalyse:** Anomalien ur (Verwendung ohne Definition), dd (doppelte Definition),
  du (Definition ohne Verwendung); Taint-Analyse (Weg nicht vertrauenswürdiger Daten zu
  kritischen Senken) für Sicherheit. Details: Skill `white-box-testdesign`, Referenz Datenfluss.

## 3. Metriken

| Metrik | Aussage | Hinweis |
| --- | --- | --- |
| Zyklomatische Komplexität (McCabe) | Anzahl unabhängiger Pfade; Testaufwand | Schwellwerte je Funktion, z. B. ≤ 10–15 |
| Kognitive Komplexität | Verständlichkeit | Besser als McCabe für Lesbarkeit |
| Verschachtelungstiefe | Lesbarkeit, Fehleranfälligkeit | |
| Funktions- und Klassengröße | Verantwortungsumfang | |
| Duplikatanteil | Wartungsaufwand, Inkonsistenzrisiko | |
| Kopplung (Fan-in/Fan-out), Kohäsion | Modularität | |
| Kommentar- und Dokumentationsgrad | Analysierbarkeit | Menge sagt wenig über Qualität |
| Technische Schuld (geschätzte Behebungszeit) | Wartbarkeit gesamt | Werkzeugschätzung, Größenordnung |
| Halstead-Metriken, Maintainability Index | Komplexität aus Operatoren/Operanden | Eher für Trends |

Metriken zeigen Hotspots; Kombination mit Änderungshäufigkeit (Code-Churn) und Fehlerdichte
zeigt, wo sich Refactoring und Testvertiefung lohnen.

## 4. Einführung und Regelwerk

1. Ziel festlegen: Fehler vermeiden, Sicherheit, Normkonformität, Wartbarkeit.
2. Regelwerk auswählen: Standardprofil des Werkzeugs als Start, an Projekt anpassen;
   bei Normen das geforderte Regelwerk (MISRA, CERT).
3. **Baseline:** Bestehende Befunde erfassen und einfrieren; Gate zunächst nur auf **neuen Code**
   („Clean as you code“), Altbestand schrittweise abbauen.
4. Integration in IDE (Feedback beim Schreiben), Pre-Commit, Pipeline (Gate), Merge-Request-Kommentare.
5. Regelwerk versionieren; Änderungen im Team abstimmen.
6. Schulung: Was bedeuten die Regeln, warum gibt es sie?

## 5. Befunde bewerten

- Jeden Befund klassifizieren: echter Fehler, Risiko, Stil, Fehlalarm.
- Fehlalarme begründet unterdrücken (im Code mit Kommentar oder im Werkzeug), nicht pauschal
  Regeln abschalten.
- Regeln mit dauerhaft hoher Fehlalarmquote anpassen oder entfernen.
- Kritische Befunde (Sicherheit, Datenverlust) wie Fehler behandeln: Ticket, Frist.
- Trends verfolgen: neue Befunde je Merge Request, Altbestand über Zeit.

## 6. Quality Gates

Beispiele für ein Gate auf neuem Code:

- Keine neuen Befunde der Schwere „blocker“ und „kritisch“.
- Keine neuen Sicherheitsbefunde hoher Schwere.
- Duplikatanteil im neuen Code unter Schwellwert.
- Überdeckung neuer Zeilen über Schwellwert (aus dynamischen Tests).
- Komplexität neuer Funktionen unter Schwellwert.
- Bewertung Wartbarkeit/Zuverlässigkeit/Sicherheit mindestens A (SonarQube-Ratings).

Gate mit Ausnahmeprozess (begründet, freigegeben, befristet).

## 7. Werkzeuge

Plattformen: SonarQube/SonarCloud, Qodana, Codacy, CodeScene (Verhaltensanalyse mit Churn).
Sprachspezifische Linter und Analysatoren siehe Abschnitt 1. IDE-Integration: SonarLint,
Sprachserver, ESLint/Ruff-Plugins. Pipeline: GitLab Code Quality, GitHub Code Scanning (SARIF).

## 8. Anti-Patterns

- Werkzeug eingeführt, Bericht mit 30.000 Befunden, niemand schaut hin.
- Gate auf Gesamtbestand; jeder Merge Request scheitert, Gate wird abgeschaltet.
- Regeln pauschal deaktiviert statt begründet unterdrückt.
- Metriken als Zielvorgabe für Entwickler (Gaming der Kennzahlen).
- Statische Analyse als Ersatz für Code-Reviews.

## 9. Prüfliste

- [ ] Ziel und Regelwerk sind festgelegt und versioniert; Normregelwerk, wo gefordert.
- [ ] Baseline erfasst; Gate gilt für neuen Code.
- [ ] Analyse läuft in IDE, Pre-Commit und Pipeline.
- [ ] Befunde werden bewertet; Fehlalarme begründet unterdrückt.
- [ ] Hotspots (Komplexität × Änderungshäufigkeit × Fehlerdichte) werden für Refactoring und Tests genutzt.
- [ ] Gate hat Ausnahmeprozess; Trends werden verfolgt.
