# Automatisierungsstrategie und Ebenenwahl

## Inhalt
1. Ziele festlegen
2. Was automatisieren
3. Ebenen und Verteilung
4. Business Case
5. Rollen und Verantwortung
6. Kennzahlen
7. Prüfliste

## 1. Ziele festlegen

Automatisierung dient einem Zweck, den man messen kann:

- Schnelleres Feedback (Regressionslauf von Tagen auf Minuten).
- Höhere Release-Frequenz bei gleichem Risiko.
- Freisetzen von Testerzeit für exploratives und risikobasiertes Testen.
- Reproduzierbarkeit und Nachweis (regulierte Umfelder).
- Testen, was manuell nicht geht (Last, Kombinatorik, Dauerbetrieb).

Ziel ohne Messgröße ist ein Wunsch. „Regressionssuite läuft in < 20 Minuten mit < 2 %
Flaky-Rate und deckt die 30 Top-Risiken ab“ ist ein Ziel.

## 2. Was automatisieren

Kandidaten nach Nutzen:

| Hoher Nutzen | Geringer Nutzen |
| --- | --- |
| Regressionstests für stabile Kernfunktionen | Einmalige Tests, Features im Umbruch |
| Smoke-Tests je Deployment | Usability, Ästhetik, Fachbewertung |
| Datengetriebene Tests mit vielen Varianten | Tests mit hohem Aufwand für Vorbedingungen und seltener Ausführung |
| API- und Vertragstests | Tests an instabilen Oberflächen ohne Testhaken |
| Last-, Performance-, Sicherheitsscans | Exploratives Testen (unterstützen ja, ersetzen nein) |
| Aufwändige Vorbereitung (Testdaten, Umgebungen) | |

Reihenfolge: Risiko × Ausführungshäufigkeit × technische Machbarkeit. Zuerst das, was
häufig läuft und wehtut, wenn es bricht.

## 3. Ebenen und Verteilung

| Ebene | Prüft | Laufzeit | Stabilität | Kosten | Anteil (Pyramide) |
| --- | --- | --- | --- | --- | --- |
| Unit | Logik einer Einheit | ms | hoch | niedrig | breite Basis |
| Komponente/Service | Modul mit echten oder gefakten Nachbarn | s | hoch | niedrig–mittel | breit |
| API/Integration | Schnittstellen, Verträge, Zusammenspiel | s–min | mittel–hoch | mittel | mittel |
| GUI-Komponente | Einzelne UI-Bausteine isoliert | s | hoch | mittel | mittel |
| E2E/GUI-Workflow | Nutzerpfade durch das System | min | niedrig–mittel | hoch | schmale Spitze |
| Manuell/explorativ | Alles, was Urteil braucht | – | – | – | Krone |

Regeln:

- **Niedrigste Ebene, auf der das Verhalten sichtbar ist.** Berechnung → Unit. Vertrag → API.
  Nur der Zusammenbau → E2E.
- **Testing Trophy** (Dodds) für Frontend-lastige Produkte: Schwerpunkt auf Integrationstests
  von Komponenten, wenige Unit-Tests für reine Logik, wenige E2E.
- **Eiscreme-Kegel** (viele GUI-Tests, wenige Unit-Tests) ist ein Warnsignal und meist Folge
  von fehlender Testbarkeit oder getrennten Teams.
- E2E-Suite klein halten: Kernpfade, je Pfad ein Test, unter 15–30 Minuten parallelisiert.

## 4. Business Case

Grobe Rechnung je Test oder Suite:

```
Nutzen = Läufe pro Jahr × (manueller Aufwand je Lauf − automatisierter Aufwand je Lauf)
         + vermiedene Fehlerkosten (geschätzt)
Kosten = Erstellung + Pflege pro Jahr + Infrastruktur
```

Pflege ist der unterschätzte Posten: realistisch 15–30 % der Erstellungskosten pro Jahr,
bei GUI-Tests mehr. Tests, die seltener als monatlich laufen, tragen sich selten.

## 5. Rollen und Verantwortung

- Automatisierungsarchitekt: Architektur, Framework, Standards, Review.
- Test Automation Engineer: Umsetzung, Pflege, Pipeline.
- Entwickler: Unit- und Komponententests, Testbarkeit, Testhaken (IDs, Test-APIs).
- Tester/Testanalyst: Testfälle, Testdaten, Bewertung der Ergebnisse, schlüsselwortgetriebene Tests.
- Betrieb/Plattform: Umgebungen, Runner, Container.

Ohne Entwicklerbeteiligung keine stabile Automatisierung: Testhaken, stabile Selektoren und
Test-APIs entstehen im Produktcode.

## 6. Kennzahlen

| Kennzahl | Aussage |
| --- | --- |
| Laufzeit je Stufe | Feedbackgeschwindigkeit |
| Flaky-Rate (instabile Läufe / alle Läufe) | Vertrauen; Ziel < 1–2 % |
| Fehler, die die Suite vor Produktion gefunden hat | Wirksamkeit |
| Fehler in Produktion, die ein Test hätte finden müssen (Escapes) | Lücken |
| Pflegeaufwand je Sprint | Wirtschaftlichkeit |
| Risikoabdeckung (Top-Risiken mit automatisiertem Test) | Ausrichtung |
| Anteil manueller Regressionsaufwand | Freigesetzte Zeit |

Zu vermeiden: „Anzahl automatisierter Tests“ und „Automatisierungsgrad in %“ als Ziel.
Sie belohnen Masse, nicht Wert.

## 7. Prüfliste

- [ ] Ziel mit Messgröße ist formuliert.
- [ ] Kandidaten sind nach Risiko, Häufigkeit und Machbarkeit priorisiert.
- [ ] Je Kandidat ist die Ebene begründet.
- [ ] Pflegekosten sind im Business Case enthalten.
- [ ] Entwicklerbeteiligung (Testbarkeit, Testhaken) ist vereinbart.
- [ ] Kennzahlen sind festgelegt und werden erhoben.
