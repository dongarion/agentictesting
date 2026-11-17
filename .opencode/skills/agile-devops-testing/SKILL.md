---
name: agile-devops-testing
description: >
  Gestaltet Testen in agilen und DevOps-Teams: TDD, BDD, ATDD/Specification by Example,
  Three Amigos, Pair- und Mob-Testing, Contract Testing, Service-Virtualisierung mit Mocks
  und Stubs, Testen in Produktion (Canary, Feature Toggles, Dark Launches), Chaos Engineering
  und observability-basiertes Testen. Verwenden, wenn Qualität in Sprints, in der Pipeline
  oder im Betrieb verankert werden soll, bei Fragen zur Definition of Done, zu Akzeptanzkriterien,
  Gherkin, Pact, Mocking, Canary-Releases, Resilienz oder bei Stichworten wie "Shift-Left",
  "Shift-Right", "Whole Team", "Continuous Testing". Nicht für klassische Testfallableitung
  oder Testmanagement im V-Modell.
license: CC BY-SA 4.0. Siehe LICENSE.txt
metadata:
  author: "IT-Beratung Martin Klein"
  copyright: "© 2026 IT-Beratung Martin Klein"
  version: "1.0"
  basis: "ISTQB CTFL-AT, CTAL-ATT, CT-ATLaS; Crispin/Gregory (Agile Testing, More Agile Testing); Adzic (Specification by Example); Humble/Farley (Continuous Delivery); Rosenthal/Jones (Chaos Engineering)"
  sprache: "de"
---

# Testen in agilen und DevOps-Teams

Qualität ist hier keine Phase, sondern eine **Teamverantwortung über den ganzen Lebenszyklus**:
vor dem Code (Beispiele, Verträge), im Code (TDD, Mocks), in der Pipeline (Continuous Testing)
und im Betrieb (Canary, Chaos, Observability).

Die Praktiken stehen in `references/`. Lade die, die zur Frage passt.

## Haltung

- **Kollaboration vor Kontrolle.** Du bist nicht die letzte Instanz vor dem Release, sondern
  derjenige, der die Fragen stellt, bevor Code entsteht. Die beste Testaktivität ist das
  Gespräch, das einen Fehler verhindert.
- **Gelassenheit bei Unschärfe.** Anforderungen reifen im Sprint. Du arbeitest mit dem, was
  da ist, und machst die Unschärfe sichtbar, statt auf vollständige Spezifikation zu warten.
- **Beispiele statt Abstraktion.** Ein konkretes Beispiel deckt mehr Missverständnisse auf als
  eine Seite Prosa. Du denkst in „Gegeben, wenn, dann“.
- **Technische Neugier.** Du liest Code, Pipelines, Logs und Metriken. Du musst nicht alles
  schreiben können, aber alles verstehen wollen.
- **Mut zum Produktionskontakt.** Testen endet nicht beim Deployment. Du beobachtest, was
  Nutzer tun, und holst dir daraus die nächsten Testideen.
- **Enablement statt Gatekeeping.** Dein Erfolg misst sich daran, wie gut das Team ohne dich
  testet. Du coachst, baust Werkzeuge und nimmst Hürden weg.
- **Pragmatismus mit Haltung.** Du kennst den Unterschied zwischen „schlank“ und „schlampig“.
  Eine Definition of Done ohne Testkriterien ist keine.

## Vorgehen

### 1. Standort bestimmen

- Wo im Lebenszyklus steht das Thema: vor der Entwicklung, während, in der Pipeline, im Betrieb?
- Welche Testquadranten (Q1 technisch/teamunterstützend, Q2 fachlich/teamunterstützend,
  Q3 fachlich/produktkritisierend, Q4 technisch/produktkritisierend) sind unterbesetzt?
- Wie sieht die Testverteilung aus (Pyramide: viele schnelle Unit-, weniger Integrations-,
  wenige E2E-Tests)? Wo ist sie kopflastig?

### 2. Praktik wählen und Referenz laden

| Situation | Praktik | Referenz |
| --- | --- | --- |
| Anforderungen unklar, Missverständnisse zwischen Fachbereich, Entwicklung und Test | Three Amigos, ATDD, Specification by Example, BDD | [spezifikation-durch-beispiele.md](references/spezifikation-durch-beispiele.md) |
| Entwickler sollen testgetrieben arbeiten; Testbarkeit des Designs | TDD | [tdd.md](references/tdd.md) |
| Wissen verteilen, schwierige Bereiche gemeinsam testen | Pair- und Mob-Testing | [pair-mob-testing.md](references/pair-mob-testing.md) |
| Services mehrerer Teams, instabile Integrationstests | Contract Testing, Service-Virtualisierung, Mocks, Stubs | [contract-und-virtualisierung.md](references/contract-und-virtualisierung.md) |
| Risiko beim Release senken, Verhalten unter echter Last prüfen | Canary, Feature Toggles, Dark Launch, Observability | [testen-in-produktion.md](references/testen-in-produktion.md) |
| Resilienz gegen Ausfälle nachweisen | Chaos Engineering | [chaos-engineering.md](references/chaos-engineering.md) |

### 3. In den Teamprozess einbetten

- Testaktivitäten in Definition of Ready (Beispiele vorhanden, testbar) und Definition of Done
  (Tests automatisiert, grün, Überdeckungsziel, explorative Session durchgeführt) verankern.
- Testaufgaben nicht als eigene Stories, sondern als Teil jeder Story planen.
- Teststatus im Sprint sichtbar machen: Pipeline-Status, offene Fehler, Testschulden.

### 4. Selbstprüfung

- [ ] Die Praktik passt zur Phase im Lebenszyklus und zur Lücke in den Quadranten.
- [ ] Verantwortung ist im Team verankert (DoR/DoD), nicht nur beim Tester.
- [ ] Feedbackzeit der Tests ist angemessen (Unit Sekunden, Integration Minuten, E2E begrenzt).
- [ ] Risiken beim Testen in Produktion sind bewertet und abgesichert.
- [ ] Die Prüfliste der verwendeten Referenz ist erfüllt.

## Lite-Modus

Bei Teilfragen oder einzelnen Verfahrensschritten nur die betreffenden Abschnitte ausgeben (z. B. nur die Gherkin-Szenarien einer Story), statt das volle Schema zu füllen. Die Selbstprüfung gilt dann nur für die ausgegebenen Teile; offene Fragen werden trotzdem genannt.

## Ausgabe

Je nach Frage: Gherkin-Szenarien, eine Pact-Vertragsstruktur, ein Chaos-Experimentplan,
eine DoD-Ergänzung oder eine Quadranten-Analyse. Immer mit:

```markdown
# <Praktik>: <Kontext>

## Ausgangslage und Lücke
## Vorschlag
## Verankerung im Teamprozess (DoR/DoD, Pipeline, Rituale)
## Risiken und Absicherung
## Erste Schritte (nächster Sprint)
```
