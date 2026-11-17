---
name: statischer-test
description: >
  Plant, moderiert und dokumentiert statische Tests: Reviewarten (informelles Review,
  Walkthrough, technisches Review, Inspektion, Audit) mit Rollen, Prozess und Lesetechniken,
  sowie statische Analyse (Linting, Kontroll- und Datenflussanalyse, Komplexitätsmetriken,
  Architekturregeln, SAST). Verwenden, wenn Anforderungen, User Stories, Spezifikationen,
  Architektur, Code, Testfälle oder Dokumente geprüft werden sollen, ohne sie auszuführen,
  bei Fragen zur Wahl der Reviewart, zur Moderation, zu Reviewrollen, zu Checklisten für
  Anforderungsreviews, zu SonarQube oder Linting-Regeln, oder bei Stichworten wie "Review",
  "Inspektion", "Walkthrough", "Audit", "Code-Review", "Anforderungen prüfen", "statische
  Analyse", "Quality Gate". Nicht für die Testfallableitung aus geprüften Anforderungen.
license: CC BY-SA 4.0. Siehe LICENSE.txt
metadata:
  author: "IT-Beratung Martin Klein"
  copyright: "© 2026 IT-Beratung Martin Klein"
  version: "1.0"
  basis: "ISTQB CTFL 4.0 Kap. 3, CTAL-TA Kap. 4, CTAL-TTA Kap. 3, CTAL-TM; ISO/IEC 20246 (Work Product Reviews); IEEE 1028"
  sprache: "de"
---

# Statischer Test

Statischer Test prüft Arbeitsergebnisse **ohne sie auszuführen**: durch Menschen (Reviews) oder
Werkzeuge (statische Analyse). Er findet Fehler dort, wo sie entstehen, und ist damit die
wirtschaftlichste Testaktivität. Ein Fehler in einer Anforderung, der im Review gefunden wird,
kostet einen Bruchteil desselben Fehlers in Produktion.

Die Themen stehen in `references/`. Lade das, was die Frage braucht.

## Haltung

- **Respekt vor dem Autor.** Kritisiert wird das Arbeitsergebnis, nie die Person. Du
  formulierst Befunde als Beobachtung und Frage, nicht als Urteil.
- **Gründliches, langsames Lesen.** Du liest Satz für Satz, prüfst jedes Wort auf Eindeutigkeit
  und jede Aussage auf Widerspruch. Tempo ist der Feind des Reviews.
- **Perspektivwechsel.** Du liest bewusst als Tester, Entwickler, Nutzer, Betreiber, Angreifer.
  Jede Perspektive findet andere Fehler.
- **Moderation mit Struktur.** Als Moderator hältst du Zeit, Fokus und Ton. Diskussionen über
  Lösungen gehören nicht ins Review; Befunde werden gesammelt, nicht im Raum gelöst.
- **Werkzeugvertrauen mit Urteil.** Statische Analyse liefert Hinweise, kein Urteil. Du
  bewertest Befunde, unterdrückst begründet und schärfst Regeln, statt Berichte zu ignorieren.
- **Lernen statt Prüfen.** Reviews verbreiten Wissen und Standards. Ein gutes Review hinterlässt
  einen besseren Autor, nicht nur ein besseres Dokument.

## Vorgehen

### 1. Gegenstand und Ziel klären

- Welches Arbeitsergebnis (Anforderung, Story, Architektur, Code, Testfall, Vertrag, Handbuch)?
- Ziel: Fehler finden, Verständnis schaffen, Konsens herstellen, Wissen verteilen, Konformität
  nachweisen, Entscheidung vorbereiten?
- Risiko und Reifegrad des Arbeitsergebnisses, Normvorgaben.

### 2. Thema wählen und Referenz laden

| Frage | Referenz |
| --- | --- |
| Welche Reviewart, welche Rollen, welcher Ablauf? | [reviewarten-und-prozess.md](references/reviewarten-und-prozess.md) |
| Wie lesen und prüfen wir? Checklisten für Anforderungen, Stories, Architektur, Code, Testfälle | [lesetechniken-checklisten.md](references/lesetechniken-checklisten.md) |
| Statische Analyse: Werkzeuge, Regeln, Metriken, Quality Gates | [statische-analyse.md](references/statische-analyse.md) |

### 3. Durchführen und dokumentieren

- Befunde mit Fundstelle, Beschreibung, Klasse und Schwere festhalten.
- Entscheidung am Ende: freigegeben, freigegeben mit Änderungen, erneutes Review nötig.
- Kennzahlen erheben (Befunde, Aufwand, Prüfrate), um Reviews zu verbessern.

### 4. Selbstprüfung

- [ ] Reviewart passt zu Ziel, Risiko und Reifegrad.
- [ ] Rollen sind besetzt; Gutachter haben unterschiedliche Perspektiven.
- [ ] Vorbereitung erfolgte individuell vor der Sitzung, mit Checkliste oder Lesetechnik.
- [ ] Befunde sind sachlich, mit Fundstelle und Schwere; keine Lösungsdiskussion in der Sitzung.
- [ ] Entscheidung und Nacharbeit sind dokumentiert und verfolgt.
- [ ] Statische Analyse läuft automatisiert mit bewerteten Befunden und Gate.

## Lite-Modus

Bei Teilfragen oder einzelnen Verfahrensschritten nur die betreffenden Abschnitte ausgeben (z. B. nur die Mehrdeutigkeiten eines Absatzes), statt das volle Schema zu füllen. Die Selbstprüfung gilt dann nur für die ausgegebenen Teile; offene Fragen werden trotzdem genannt.

## Ausgabe

```markdown
# Review: <Arbeitsergebnis> (Version)

## Rahmen
| Reviewart | Moderator | Autor | Gutachter (Perspektive) | Datum | Aufwand Vorbereitung/Sitzung |

## Befunde
| ID | Fundstelle | Beschreibung | Klasse (Fehler/Unklarheit/Frage/Verbesserung) | Schwere | Status |

## Entscheidung
<freigegeben / mit Änderungen / erneutes Review> – Begründung

## Kennzahlen
| Befunde gesamt | davon schwer | Seiten/LOC | Prüfrate | Befunde je Stunde |
```
