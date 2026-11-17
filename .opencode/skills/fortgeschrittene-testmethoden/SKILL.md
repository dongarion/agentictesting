---
name: fortgeschrittene-testmethoden
description: >
  Wählt und wendet Testmethoden an, die über klassische Black- und White-Box-Verfahren
  hinausgehen: modellbasiertes Testen (MBT), Property-based Testing, metamorphes Testen,
  Mutationstest, Fuzzing, Back-to-back-Test, A/B-Test, Crowdtesting und Dogfooding.
  Verwenden, wenn kein Testorakel existiert, wenn die Wirksamkeit vorhandener Tests gemessen
  werden soll, wenn Tests generiert statt handgeschrieben werden sollen, wenn zwei
  Implementierungen verglichen werden, oder bei Stichworten wie "MBT", "Testgenerierung",
  "Hypothesis", "Property", "Mutanten", "Fuzzer", "Orakelproblem", "Vergleichstest",
  "Experiment", "Beta". Nicht für den Standard-Testentwurf aus Anforderungen.
license: CC BY-SA 4.0. Siehe LICENSE.txt
metadata:
  author: "IT-Beratung Martin Klein"
  copyright: "© 2026 IT-Beratung Martin Klein"
  version: "1.0"
  basis: "ISTQB CT-MBT, CTAL-TTA, CTAL-TA; Chen et al. (Metamorphic Testing); DeMillo/Offutt (Mutation); Claessen/Hughes (QuickCheck)"
  sprache: "de"
---

# Fortgeschrittene Testmethoden

Diese Methoden lösen Probleme, an denen klassischer Testentwurf scheitert: **kein Orakel**
(Was ist das richtige Ergebnis?), **zu viele Eingaben** (handgeschriebene Fälle reichen nicht),
**unklare Testgüte** (Sind meine Tests überhaupt scharf?) oder **Verhalten erst im Feld sichtbar**.

Die Methoden stehen in `references/`. Lade nur die passende.

## Haltung

- **Erst das Problem, dann die Methode.** Jede dieser Methoden ist ein Werkzeug für eine
  bestimmte Lücke. Wer Fuzzing einsetzt, weil es modern ist, erzeugt Rauschen.
- **Abstraktionsfreude.** Statt einzelner Beispiele denkst du in Eigenschaften, Relationen,
  Modellen und Invarianten. „Für alle x gilt …“ statt „für x = 5 gilt …“.
- **Statistisches Denken.** Generierte Tests, Mutationswerte und A/B-Ergebnisse sind
  Stichproben. Du kennst den Unterschied zwischen „kein Fehler gefunden“ und „kein Fehler
  vorhanden“ und zwischen Signifikanz und Relevanz.
- **Ingenieurhafte Skepsis gegenüber dem eigenen Modell.** Ein Modell, ein Generator oder eine
  Property kann selbst falsch sein. Jeder Fehlalarm wird untersucht, bevor er dem Produkt
  angelastet wird.
- **Dokumentierte Reproduzierbarkeit.** Zufall braucht Seeds. Jeder gefundene Fall wird als
  deterministischer Regressionstest festgehalten.
- **Lust am Experiment, Disziplin in der Auswertung.** Hypothese vorher, Metrik vorher,
  Abbruchkriterium vorher.

## Vorgehen

### 1. Lücke benennen

| Problem | Passende Methoden |
| --- | --- |
| Kein oder teures Testorakel | Metamorphes Testen, Back-to-back-Test, Property-based Testing |
| Große oder strukturierte Eingaberäume | Property-based Testing, Fuzzing, MBT |
| Zustandsreiche Systeme, Protokolle, Workflows | Modellbasiertes Testen |
| Unklare Wirksamkeit der Testsuite | Mutationstest |
| Robustheit und Sicherheit gegen unerwartete Eingaben | Fuzzing |
| Neuimplementierung, Migration, Refactoring, zwei Anbieter | Back-to-back-Test |
| Wirkung auf echte Nutzer unklar | A/B-Test, Dogfooding, Crowdtesting |
| Gerätevielfalt, reale Umgebungen, Lokalisierung | Crowdtesting |

### 2. Referenz laden

| Methode | Referenz |
| --- | --- |
| Modellbasiertes Testen | [modellbasiert.md](references/modellbasiert.md) |
| Property-based und metamorphes Testen | [property-metamorph.md](references/property-metamorph.md) |
| Mutationstest | [mutationstest.md](references/mutationstest.md) |
| Fuzzing | [fuzzing.md](references/fuzzing.md) |
| Back-to-back-Test | [back-to-back.md](references/back-to-back.md) |
| A/B-Test, Dogfooding, Crowdtesting | [feldmethoden.md](references/feldmethoden.md) |

### 3. Anwenden und absichern

- Seeds, Modellversion, Generatorversion und Konfiguration festhalten.
- Jeden Befund minimieren (Shrinking) und als festen Regressionstest ablegen.
- Fehlalarme (falsches Modell, falsche Property) getrennt zählen; sie sind Befunde an der
  Testbasis, nicht am Produkt.

### 4. Selbstprüfung

- [ ] Die Lücke, die die Methode schließen soll, ist benannt.
- [ ] Orakel oder Relation ist formuliert und begründet.
- [ ] Reproduzierbarkeit ist gesichert (Seed, Version, Konfiguration).
- [ ] Befunde sind minimiert und als Regressionstests abgelegt.
- [ ] Grenzen der Aussage sind im Bericht benannt (Stichprobe, Modellabdeckung, Signifikanz).
- [ ] Die Prüfliste der verwendeten Referenz ist erfüllt.

## Lite-Modus

Bei Teilfragen oder einzelnen Verfahrensschritten nur die betreffenden Abschnitte ausgeben (z. B. nur die Properties oder nur die metamorphen Relationen), statt das volle Schema zu füllen. Die Selbstprüfung gilt dann nur für die ausgegebenen Teile; offene Fragen werden trotzdem genannt.

## Ausgabe

```markdown
# <Methode>: <Testobjekt>

## Ziel und Lücke
<Welches Problem die Methode hier löst>

## Modell / Properties / Relationen / Konfiguration
<je Methode, mit Version und Seed>

## Durchführung
| Lauf | Konfiguration | Umfang (Fälle, Mutanten, Dauer) | Ergebnis |

## Befunde
| ID | Minimales Beispiel | Erwartung (Quelle/Relation) | Beobachtung | Regressionstest |

## Fehlalarme und Modellkorrekturen
| ID | Ursache | Korrektur |

## Aussagekraft und Grenzen
<Was die Ergebnisse belegen und was nicht>
```
