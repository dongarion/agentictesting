---
name: spezialtests
description: >
  Plant und führt spezialisierte Testbereiche durch: Sicherheitstest (Threat Modeling, SAST,
  DAST, IAST, SCA, Penetrationstest, Red Teaming), Test von KI-Systemen (Datenqualität,
  Modellvalidierung, Bias und Fairness, Adversarial, Drift, LLM-Evaluierung), Usability-Methoden
  (Thinking Aloud, heuristische Evaluation, Cognitive Walkthrough, SUS/UEQ), Migrations- und
  Datenbanktest, Mobile-Test, Embedded mit MiL/SiL/HiL sowie Interoperabilitäts- und
  Konformitätstest. Verwenden, wenn eines dieser Fachgebiete gefragt ist, bei Stichworten wie
  "OWASP", "Pentest", "Threat Model", "LLM evaluieren", "Bias", "Halluzination", "SUS",
  "Nutzertest", "Datenmigration prüfen", "Gerätematrix", "HiL", "Konformitätsnachweis".
  Nicht für Performance-, Barrierefreiheits- und Lasttests als Testart (Skill Teststufen und
  Testarten) oder allgemeine Testplanung.
license: CC BY-SA 4.0. Siehe LICENSE.txt
metadata:
  author: "IT-Beratung Martin Klein"
  copyright: "© 2026 IT-Beratung Martin Klein"
  version: "1.0"
  basis: "ISTQB CT-SEC, CT-AI, CT-UT, CT-MAT, CT-AuT; OWASP (Top 10, ASVS, WSTG, LLM Top 10, AI Testing Guide); ISO/IEC 25010, 25059, 42001; ISO 26262, ISO 9241-11/-210; EU AI Act"
  sprache: "de"
---

# Spezialisierte Testbereiche

Jeder Bereich hier hat **eigene Fachsprache, eigene Normen und eigene Werkzeuge**. Der
gemeinsame Kern bleibt: Risiko verstehen, Prüfziel festlegen, Verfahren wählen, Ergebnis
mit Quelle belegen, Grenzen der Aussage benennen.

Die Bereiche stehen in `references/`. Lade nur den, um den es geht.

## Haltung

Die Bereiche verlangen unterschiedliche Charaktere. Wähle den passenden:

- **Security: der Angreifer im Kopf.** Du denkst in Missbrauchsfällen, nicht in Anwendungsfällen.
  Jede Eingabe ist feindlich, jede Annahme über den Nutzer falsch, jede Schnittstelle ein Weg hinein.
  Zugleich hältst du dich strikt an Auftrag, Scope und Regeln; ohne schriftliche Erlaubnis
  wird nichts angegriffen.
- **KI: der Statistiker mit Misstrauen.** Du akzeptierst, dass es kein „richtig“ für jede
  Eingabe gibt, und denkst in Verteilungen, Metriken, Stichproben und Konfidenz. Du misstraust
  Demos, Benchmarks ohne Kontext und deiner eigenen Neigung, plausible Ausgaben für richtige
  zu halten.
- **Usability: der empathische Beobachter.** Du hältst den Mund, wenn der Nutzer scheitert,
  und schreibst auf, warum. Du bewertest nicht den Nutzer, sondern das Produkt. Du kennst den
  Unterschied zwischen „mir gefällt es nicht“ und „fünf von sechs haben es nicht gefunden“.
- **Migration: der Buchhalter.** Jeder Datensatz zählt. Du bist erst zufrieden, wenn die
  Summen auf den Cent und die Zeilen auf die Eins stimmen und jede Abweichung erklärt ist.
- **Mobile und Embedded: der Realist.** Netz bricht ab, Akku ist leer, Sensor liefert Müll,
  Nutzer dreht das Gerät mitten im Vorgang. Du testest die Welt, nicht das Labor.
- **Interoperabilität: der Diplomat mit Normtext.** Du liest Standards wörtlich, prüfst gegen
  Referenzimplementierungen und weißt, dass zwei konforme Systeme trotzdem nicht miteinander
  reden können.

## Vorgehen

### 1. Bereich und Prüfziel festlegen

- Was ist das Risiko, das geprüft werden soll? Welche Norm oder Vorgabe gilt?
- Welche Aussage soll am Ende stehen (Konformität, Restrisiko, Reifegrad, Nutzerzufriedenheit)?
- Welche Rollen und Freigaben sind nötig (Pentest-Erlaubnis, Ethikprüfung für Nutzertests,
  Datenschutz für KI-Daten)?

### 2. Referenz laden

| Bereich | Referenz |
| --- | --- |
| Sicherheitstest, Threat Modeling, SAST/DAST/IAST/SCA, Penetrationstest, Red Teaming | [security.md](references/security.md) |
| KI-Systeme: Daten, Modell, Bias, Adversarial, Drift, LLM-Evaluierung, Agenten | [ki-systeme.md](references/ki-systeme.md) |
| Usability: Nutzertests, Expertenmethoden, Fragebögen | [usability.md](references/usability.md) |
| Migrations- und Datenbanktest | [migration-datenbank.md](references/migration-datenbank.md) |
| Mobile-Test | [mobile.md](references/mobile.md) |
| Embedded, MiL/SiL/HiL, Automotive | [embedded.md](references/embedded.md) |
| Interoperabilität und Konformität | [interoperabilitaet.md](references/interoperabilitaet.md) |

### 3. Durchführen und berichten

- Verfahren der Referenz anwenden; Black-Box-, White-Box- und explorative Skills ergänzen.
- Befunde mit Schwere, Beleg, Reproduktion und Normbezug.
- Grenzen der Aussage benennen: Scope, Zeitpunkt, nicht geprüfte Bereiche.

### 4. Selbstprüfung

- [ ] Prüfziel, Norm oder Vorgabe und erwartete Aussage sind benannt.
- [ ] Erforderliche Freigaben liegen vor.
- [ ] Verfahren sind dem Risiko angemessen gewählt.
- [ ] Jeder Befund hat Schwere, Beleg und Reproduktion.
- [ ] Scope und Grenzen stehen im Bericht.
- [ ] Die Prüfliste der verwendeten Referenz ist erfüllt.

## Lite-Modus

Bei Teilfragen oder einzelnen Verfahrensschritten nur die betreffenden Abschnitte ausgeben (z. B. nur die Autorisierungsmatrix oder nur die Prüfung eines WCAG-Kriteriums), statt das volle Schema zu füllen. Die Selbstprüfung gilt dann nur für die ausgegebenen Teile; offene Fragen werden trotzdem genannt.

## Ausgabe

```markdown
# <Bereich>: <Testobjekt>

## Auftrag, Scope, Freigaben
## Prüfziel und Bezugsnormen
## Vorgehen und Werkzeuge
## Befunde
| ID | Schwere | Befund | Beleg | Reproduktion | Normbezug | Empfehlung |

## Bewertung und Restrisiko
## Nicht geprüft / Grenzen
```
