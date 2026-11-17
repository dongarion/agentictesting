# Testverteilung, Quadranten und Verantwortung

## Inhalt
1. Testpyramide
2. Testpokal (Testing Trophy) und andere Formen
3. Agile Testquadranten
4. Whole-Team-Ansatz
5. Unabhängigkeit des Testens
6. Verantwortungsmatrix
7. Anti-Patterns
8. Prüfliste

## 1. Testpyramide

Cohn, popularisiert von Fowler: **viele schnelle, isolierte Tests unten, wenige langsame,
integrierte Tests oben.**

```
        /  E2E / GUI  \        wenige, langsam, teuer, fragil
       /  Integration  \       mittel
      /  Unit/Komponente \     viele, schnell, billig, stabil
```

- Leitfrage je Verhalten: Auf welcher niedrigsten Ebene ist es sichtbar? Dort testen.
- Nicht als feste Prozentvorgabe verwenden, sondern als Richtung.
- Manuelle und explorative Tests stehen außerhalb der Pyramide (als „Wolke“ oder „Krone“).

## 2. Testpokal (Testing Trophy) und andere Formen

- **Testing Trophy** (Dodds): statische Analyse als Sockel, wenige Unit-Tests, **Schwerpunkt
  Integrationstests**, wenige E2E. Passt zu Frontend- und Service-lastigen Anwendungen, in
  denen das Zusammenspiel das Hauptrisiko ist.
- **Honeycomb** (Spotify, Microservices): Schwerpunkt auf Integrationstests je Service mit
  echten Abhängigkeiten (Testcontainers), wenige Unit- und E2E-Tests.
- **Eiscreme-Kegel** (Anti-Muster): viele manuelle und GUI-Tests, wenige Unit-Tests.
  Folge von fehlender Testbarkeit, getrennten Teams oder nachträglicher Automatisierung.
- Wahl der Form aus Architektur und Risikoverteilung begründen; Ist-Verteilung messen
  (Anzahl und Laufzeit je Ebene).

## 3. Agile Testquadranten

Brian Marick, ausgearbeitet von Crispin/Gregory. Zwei Achsen: **teamunterstützend vs.
produktkritisierend** und **technisch vs. fachlich**.

| | Teamunterstützend (Anleitung der Entwicklung) | Produktkritisierend (Bewertung des Produkts) |
| --- | --- | --- |
| **Fachlich** | **Q2:** Funktionale Tests, Beispiele, Story-Tests, Prototypen, Simulationen (meist automatisiert und manuell) | **Q3:** Exploratives Testen, Usability, Nutzerakzeptanz, Alpha/Beta, Szenarien (meist manuell) |
| **Technisch** | **Q1:** Unit-Tests, Komponententests, Contract Tests (automatisiert) | **Q4:** Performance, Last, Sicherheit, Zuverlässigkeit, Wartbarkeit, Barrierefreiheit (werkzeuggestützt) |

Nutzung: Je Release oder Feature prüfen, ob alle vier Quadranten angemessen besetzt sind.
Lücken (häufig Q3 und Q4) gezielt einplanen. Die Quadranten sind keine Reihenfolge.

## 4. Whole-Team-Ansatz

Qualität ist **Verantwortung des ganzen Teams**, nicht einer Rolle.

- Entwickler: Unit-, Komponenten-, Integrationstests, Testbarkeit, Fehlerbehebung.
- Tester/Quality Engineers: Teststrategie, Testentwurf, explorative Tests, Automatisierungsarchitektur,
  Coaching, Risiken sichtbar machen.
- PO/Fachbereich: Akzeptanzkriterien, Beispiele, fachliche Abnahme, Priorisierung von Fehlern.
- Betrieb/SRE: Betriebstests, Monitoring, Resilienz.
- Alle: Teilnahme an Three Amigos, Pairing, Bug Bashes, Retrospektiven.

Der Tester wird vom „Qualitätstor“ zum **Quality Coach**: Er befähigt, statt alles selbst zu
prüfen (Quality Assistance, Atlassian). Voraussetzungen: Testkompetenz im Team, Zeit im Sprint,
DoD mit Testkriterien, Management-Unterstützung.

## 5. Unabhängigkeit des Testens

Stufen (CTFL):

1. Autor testet eigenes Arbeitsergebnis.
2. Kollege aus demselben Team.
3. Tester im Team.
4. Unabhängiges Testteam in der Organisation.
5. Externer Dienstleister oder unabhängige Prüfstelle.

Höhere Unabhängigkeit: objektiver, andere Perspektive, findet andere Fehlerarten; aber Gefahr
von Isolation, Kommunikationsaufwand, Verantwortungsabgabe der Entwickler („die Tester finden
das schon“). Wahl je Teststufe nach Risiko und Norm (sicherheitskritische Normen fordern
Unabhängigkeit). Mischformen sind üblich: Teamtests plus unabhängiger Abnahmetest.

## 6. Verantwortungsmatrix

Beispiel (RACI: Responsible, Accountable, Consulted, Informed):

| Aktivität | Entwicklung | Test | Fachbereich/PO | Betrieb | Testmanager |
| --- | --- | --- | --- | --- | --- |
| Unit- und Komponententests | R/A | C | – | – | I |
| Akzeptanzkriterien | C | C | R/A | – | I |
| Systemtest | C | R | C | – | A |
| Automatisierte Regression | R | R | – | – | A |
| Explorative Tests | C | R | C | – | A |
| Performance-/Lasttests | C | R | I | C | A |
| Sicherheitstests | C | R | I | C | A |
| Abnahmetest | I | C | R/A | C | C |
| Betriebstests (OAT) | C | C | I | R/A | C |

An das Projekt anpassen und im Testkonzept festhalten.

## 7. Anti-Patterns

- Pyramide als Prozentquote vorgeschrieben, ohne Blick auf Architektur.
- Q3 und Q4 fehlen völlig; nur funktionale Tests.
- „Whole Team“ als Begründung, Testexpertise abzuschaffen.
- Unabhängiges Testteam ohne Kontakt zur Entwicklung; Fehler werden über Wände geworfen.
- Verantwortung nicht festgelegt; Lücken fallen erst in Produktion auf.

## 8. Prüfliste

- [ ] Verteilungsform (Pyramide, Trophy, Honeycomb) ist aus Architektur begründet; Ist-Verteilung ist gemessen.
- [ ] Alle vier Quadranten sind je Release bewusst besetzt.
- [ ] Rollen im Whole-Team-Ansatz sind beschrieben; Testkompetenz ist im Team vorhanden.
- [ ] Unabhängigkeitsgrad je Teststufe ist nach Risiko und Norm gewählt.
- [ ] Verantwortungsmatrix ist im Testkonzept festgehalten.
