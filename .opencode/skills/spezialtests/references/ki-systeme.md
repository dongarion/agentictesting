# Test von KI-Systemen

KI-Systeme sind **probabilistisch, datengetrieben und oft nicht erklärbar**. Das Orakel ist
selten eindeutig, das Verhalten ändert sich mit Daten und Modellversionen, und Qualität umfasst
neue Merkmale: Fairness, Robustheit, Transparenz, Autonomiegrad.

## Inhalt
1. Besonderheiten und Qualitätsmerkmale
2. Testobjekte entlang der ML-Pipeline
3. Datenqualitätstest
4. Modellvalidierung und Metriken
5. Bias und Fairness
6. Robustheit und Adversarial-Test
7. LLM-Evaluierung
8. Agentische Systeme testen
9. Drift und Monitoring
10. Regulatorik
11. Werkzeuge
12. Prüfliste

## 1. Besonderheiten und Qualitätsmerkmale

- Kein deterministisches Orakel: Aussagen über Verteilungen, Schwellwerte, Stichproben.
- Testdaten sind Teil des Systems: Trainings-, Validierungs- und Testdaten strikt trennen
  (keine Leckage).
- Qualitätsmerkmale nach ISO/IEC 25059 und CT-AI: Flexibilität, Anpassbarkeit, Autonomie,
  Evolution, Bias, Ethik, Nebenwirkungen, Belohnungsmanipulation, Transparenz, Erklärbarkeit,
  Sicherheit, Robustheit.
- Teststufen bleiben: Komponente (Modell), Integration (Pipeline, Vor-/Nachverarbeitung),
  System (Anwendung mit Modell), Abnahme (fachlich, ethisch, rechtlich).

## 2. Testobjekte entlang der ML-Pipeline

| Stufe | Testobjekt | Beispiele |
| --- | --- | --- |
| Daten | Rohdaten, Features, Labels | Vollständigkeit, Verteilung, Label-Qualität, Leckage |
| Training | Trainingscode, Hyperparameter, Reproduzierbarkeit | Deterministische Läufe mit Seed, Unit-Tests für Feature-Code |
| Modell | Vorhersagen, Metriken, Fairness, Robustheit | Validierung auf Holdout, Slices, Störungen |
| Integration | Vor-/Nachverarbeitung, Schnittstellen, Latenz | Gleiche Features in Training und Inferenz (Training-Serving-Skew) |
| System | Anwendung inkl. Fallbacks, UI, Mensch-in-der-Schleife | Verhalten bei Unsicherheit, Ablehnung, Erklärung |
| Betrieb | Drift, Performance, Feedbackschleifen | Monitoring, Re-Training-Auslöser |

## 3. Datenqualitätstest

- Schema- und Typprüfung, Wertebereiche, Pflichtfelder, Duplikate, Ausreißer.
- Verteilungen je Feature und je Klasse; Vergleich Training vs. Produktion.
- Label-Qualität: Stichprobe manuell prüfen, Inter-Annotator-Agreement, Label-Rauschen.
- Repräsentativität: Sind alle relevanten Gruppen und Situationen enthalten? Unterrepräsentation
  ist eine Bias-Quelle.
- Leckage: Features, die das Label verraten; zeitliche Leckage (Zukunftsinformation).
- Herkunft und Rechte: Lizenz, Einwilligung, Personenbezug; Datenblatt (Datasheets for Datasets).
- Werkzeuge: Great Expectations, Deequ, pandera, whylogs, TFDV.

## 4. Modellvalidierung und Metriken

- Metriken zum Problem: Klassifikation (Precision, Recall, F1, ROC-AUC, Konfusionsmatrix),
  Regression (MAE, RMSE), Ranking (NDCG), Generierung (siehe 7). Metrik mit Fachbereich wählen;
  Accuracy allein täuscht bei unbalancierten Klassen.
- **Slices:** Metriken je Teilgruppe (Region, Gerät, Sprache, Altersgruppe), nicht nur gesamt.
- Schwellwerte als Abnahmekriterien vorab; Vergleich zu Baseline (Vorgängermodell, einfache Regel).
- Kalibrierung: Stimmen Konfidenzwerte mit Trefferquoten überein?
- Metamorphe Tests (Skill fortgeschrittene Methoden): Invarianzen und erwartete Änderungen.
- Golden Sets: kuratierte, versionierte Testfälle mit bekannten Erwartungen, auch für Grenzfälle.
- Reproduzierbarkeit: Modellversion, Datenversion, Code, Seed; Experiment-Tracking (MLflow, W&B).

## 5. Bias und Fairness

- Geschützte Merkmale und Proxys identifizieren (PLZ als Proxy für Herkunft).
- Fairness-Metriken je Kontext: demografische Parität, Chancengleichheit (Equal Opportunity),
  ausgeglichene Fehlerraten (Equalized Odds), Kalibrierung je Gruppe. Sie widersprechen sich
  teils; Wahl mit Fachbereich und Recht begründen.
- Tests: Metriken je Gruppe, kontrafaktische Tests (nur geschütztes Merkmal ändern),
  metamorphe Fairness-Relationen.
- Quellen von Bias: Daten, Labels, Features, Zielfunktion, Feedbackschleifen im Betrieb.
- Werkzeuge: Fairlearn, AIF360, What-If Tool, Aequitas.
- Dokumentation: Model Card mit Einsatzgrenzen und bekannten Verzerrungen.

## 6. Robustheit und Adversarial-Test

- Störungen in Eingaben: Rauschen, Tippfehler, Paraphrasen, Bildtransformationen; Vorhersage
  sollte stabil bleiben (metamorphe Relation).
- Adversarial Examples: gezielt konstruierte Eingaben, die Fehlklassifikation auslösen
  (FGSM, PGD für Bilder; TextAttack für Text).
- Out-of-Distribution: Eingaben außerhalb des Trainingsbereichs; erwartetes Verhalten ist
  Unsicherheit oder Ablehnung, nicht eine selbstbewusste falsche Antwort.
- Datenvergiftung und Modell-Diebstahl als Bedrohungen im Threat Model (MITRE ATLAS).
- Werkzeuge: Adversarial Robustness Toolbox (ART), CleverHans, TextAttack, Foolbox.

## 7. LLM-Evaluierung

Für Anwendungen auf Basis großer Sprachmodelle (Chatbots, RAG, Assistenten):

**Was geprüft wird**

| Dimension | Prüffrage |
| --- | --- |
| Korrektheit/Faktentreue | Stimmt die Antwort? Bei RAG: ist sie durch die Quellen gedeckt (Groundedness)? |
| Relevanz und Vollständigkeit | Beantwortet sie die Frage, nichts Fremdes, nichts Fehlendes? |
| Halluzination | Erfundene Fakten, Quellen, Zahlen |
| Format und Vertrag | Hält sie Schema, Länge, Sprache, Ton ein? Parsebar? |
| Sicherheit | Prompt Injection, Jailbreaks, Datenabfluss, schädliche Inhalte (OWASP LLM Top 10) |
| Fairness und Ton | Stereotype, Diskriminierung, Unangemessenes |
| Robustheit | Paraphrasen, Tippfehler, andere Sprache, lange Kontexte |
| Konsistenz | Gleiche Frage, gleiche Kernaussage über Läufe und Formulierungen |
| Kosten und Latenz | Token, Zeit je Anfrage |

**Wie geprüft wird**

- **Evaluationsdatensatz** aus realen (anonymisierten) und konstruierten Fällen mit erwarteten
  Eigenschaften; versioniert; Grenzfälle und Angriffsfälle enthalten; regelmäßig erweitern
  aus Produktionsfeedback.
- **Deterministische Prüfungen:** Schema, Pflichtinhalte, verbotene Inhalte (Regex, Parser),
  Zitatprüfung bei RAG (zitierte Quelle existiert und enthält die Aussage).
- **Referenzbasierte Metriken:** exakte Übereinstimmung, Embedding-Ähnlichkeit; klassische
  Metriken (BLEU, ROUGE) nur mit Vorsicht.
- **LLM-as-Judge:** zweites Modell bewertet nach Rubrik; Rubrik präzise, Judge gegen menschliche
  Bewertungen kalibrieren (Stichprobe), Positionsverzerrung und Selbstbevorzugung kennen,
  Judge-Version fixieren.
- **Menschliche Bewertung:** Stichprobe durch Fachbereich mit Rubrik; Inter-Rater-Agreement messen.
- **Red Teaming:** gezielte Angriffe (Injection über Dokumente, Rollenspiel-Jailbreaks,
  Extraktion von Systemprompt und Daten); automatisiert (Garak, PyRIT, promptfoo red team)
  und manuell.
- **Regression:** Evaluationslauf bei jeder Prompt-, Modell-, Retrieval- oder Datenänderung;
  Schwellwerte als Gate.
- **RAG-spezifisch:** Retrieval getrennt bewerten (Recall@k, Precision der Treffer), dann
  Generierung (Groundedness, Antwortrelevanz); Metriken wie in RAGAS.

Werkzeuge: promptfoo, DeepEval, RAGAS, Inspect (UK AISI), lm-evaluation-harness, LangSmith,
Langfuse, Arize Phoenix, Giskard, Garak, PyRIT.

## 8. Agentische Systeme testen

Agenten planen, nutzen Werkzeuge und handeln mehrstufig. Zusätzlich zu 7:

- **Trajektorien** bewerten, nicht nur Endergebnis: richtige Werkzeuge, sinnvolle Reihenfolge,
  keine unnötigen oder gefährlichen Aktionen, Abbruch bei Unsicherheit.
- **Werkzeugaufrufe** als Verträge testen: Parameter korrekt, Fehlerbehandlung bei Werkzeugfehlern.
- **Sandbox** mit gemockten Werkzeugen für deterministische Tests; Seeded-Szenarien mit
  bekanntem optimalen Pfad.
- **Sicherheitsgrenzen:** Rechte minimal, destruktive Aktionen mit Bestätigung, Injection über
  Werkzeugausgaben (Webseiten, Dokumente, E-Mails) gezielt testen.
- **Kosten- und Schleifenkontrolle:** maximale Schritte, Token-Budget, Endlosschleifen-Erkennung.
- **Beobachtbarkeit:** vollständige Traces je Lauf; ohne Trace ist ein Agentenfehler nicht analysierbar.

## 9. Drift und Monitoring

- **Datendrift:** Verteilung der Eingaben ändert sich (PSI, KS-Test je Feature).
- **Konzeptdrift:** Zusammenhang Eingabe–Ziel ändert sich; Metrikverfall, sobald Ground Truth vorliegt.
- **Vorhersagedrift:** Verteilung der Ausgaben ändert sich.
- Monitoring mit Schwellwerten und Alarmen; Auslöser für Analyse und Re-Training; Shadow-
  Vergleich neues gegen altes Modell vor Umschaltung.
- Feedbackschleifen: Beeinflusst das Modell die Daten, die es später trainieren (Empfehlungen)?
- Werkzeuge: Evidently, whylogs, NannyML, Arize, Fiddler.

## 10. Regulatorik

- **EU AI Act:** Risikoklassen; Hochrisiko-Systeme (u. a. viele Behördenanwendungen: Sozialleistungen,
  Migration, Strafverfolgung, Bildung, Beschäftigung) mit Pflichten zu Datenqualität, Dokumentation,
  Protokollierung, menschlicher Aufsicht, Genauigkeit, Robustheit, Cybersicherheit, Konformitätsbewertung.
  Testergebnisse sind Teil der technischen Dokumentation.
- **ISO/IEC 42001** (KI-Managementsystem), **ISO/IEC 23894** (Risikomanagement), **ISO/IEC 25059**
  (Qualitätsmodell), **ISO/IEC TR 29119-11** (Testen KI-basierter Systeme).
- DSGVO Art. 22 (automatisierte Entscheidungen), Datenschutz der Trainings- und Evaluationsdaten.
- Dokumentation: Model Card, Data Sheet, Evaluationsbericht, Risikoanalyse.

## 11. Werkzeuge

Siehe Abschnitte; zusammengefasst: Great Expectations, pandera, whylogs (Daten) · MLflow,
W&B (Tracking) · Fairlearn, AIF360 (Fairness) · ART, TextAttack (Robustheit) · promptfoo,
DeepEval, RAGAS, Inspect, Giskard (LLM-Eval) · Garak, PyRIT (Red Teaming) · Evidently,
NannyML (Drift) · Langfuse, Phoenix (Tracing).

## 12. Prüfliste

- [ ] Trainings-, Validierungs- und Testdaten sind getrennt; Leckage geprüft.
- [ ] Datenqualität ist automatisiert geprüft; Repräsentativität bewertet.
- [ ] Metriken, Slices, Schwellwerte und Baseline sind vorab festgelegt.
- [ ] Fairness-Metriken je geschützter Gruppe sind gemessen und begründet gewählt.
- [ ] Robustheit gegen Störungen, OOD und Adversarial-Eingaben ist getestet.
- [ ] LLM: Evaluationsdatensatz versioniert, deterministische Checks, kalibrierter Judge, Red Teaming, Regressions-Gate.
- [ ] Agenten: Trajektorien, Werkzeugverträge, Sicherheitsgrenzen, Budgets, Traces.
- [ ] Drift-Monitoring mit Schwellwerten und Re-Training-Prozess steht.
- [ ] Regulatorische Einordnung (AI Act) und Dokumentation (Model Card, Evaluationsbericht) liegen vor.
- [ ] Modell-, Daten-, Prompt- und Code-Versionen jedes Ergebnisses sind festgehalten.
