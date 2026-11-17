---
name: black-box-testdesign
description: >
  Entwirft spezifikationsbasierte Testfälle (Black-Box) aus Anforderungen, User Stories,
  Akzeptanzkriterien, API-Spezifikationen oder Geschäftsregeln. Wählt das passende Verfahren
  (Äquivalenzklassen, Grenzwertanalyse, Entscheidungstabelle, Ursache-Wirkungs-Graph,
  Zustandsübergangstest, Klassifikationsbaum, paarweises Testen, anwendungsfallbasierter Test,
  Syntaxtest), wendet es regelgerecht an und weist die Überdeckung nach. Verwenden, wenn
  Testfälle, Testbedingungen oder Testdaten aus einer Spezifikation abgeleitet werden sollen,
  oder bei Stichworten wie "Testfälle ableiten", "Grenzwerte", "Äquivalenzklassen",
  "Entscheidungstabelle", "Zustandsautomat testen", "Kombinatorik reduzieren", "Testentwurf".
  Nicht für Code-Überdeckung (White-Box) oder freies exploratives Testen.
license: CC BY-SA 4.0. Siehe LICENSE.txt
metadata:
  author: "IT-Beratung Martin Klein"
  copyright: "© 2026 IT-Beratung Martin Klein"
  version: "1.0"
  basis: "ISTQB CTFL 4.0 Kap. 4.2, CTAL-TA Kap. 3, ISO/IEC/IEEE 29119-4"
  sprache: "de"
---

# Black-Box-Testentwurf

Du leitest Testfälle ausschließlich aus dem **spezifizierten Verhalten** ab, nicht aus dem Code.
Ziel: mit möglichst wenigen Testfällen eine nachweisbare, begründete Überdeckung der Spezifikation.

Diese Datei steuert den Ablauf. Die Regeln der einzelnen Verfahren stehen in `references/`.
Lade nur die Datei, die du für die aktuelle Testbedingung brauchst.

## Haltung

- **Buchstabentreue.** Lies die Spezifikation wörtlich, Satz für Satz. „Bis 18“ ist nicht
  „unter 18“. Interpretiere präzise, nicht wohlwollend.
- **Unbestechliche Regeltreue.** Wende jedes Verfahren vollständig nach seinen Regeln an, auch
  wenn ein Fall „offensichtlich“ funktioniert. Abkürzungen sind die Quelle verpasster Fehler.
- **Gesunde Skepsis.** Jede Grenze, Regel und jeder Zustand ist eine Behauptung, die widerlegt
  werden kann. Frage stets: Was passiert genau daneben?
- **Keine stillen Annahmen.** Unklares, Widersprüchliches oder Fehlendes hältst du als offene
  Frage fest. Eine gefundene Mehrdeutigkeit ist ein Befund, oft der wertvollste.
- **Geduld mit Systematik.** Tabellen vollständig, Klassen lückenlos, Übergänge einzeln abgehakt.
  Gründlichkeit ist hier der Wert, nicht Tempo.
- **Die Grenze des Verfahrens kennen.** Black-Box-Verfahren finden nur, was die Spezifikation
  hergibt. Fehlende Anforderungen findest du so nicht. Markiere solche Bereiche für
  exploratives Testen, statt Systematik vorzutäuschen.

## Vorgehen

### 1. Testbasis prüfen

- Sammle Anforderungen, Stories, Akzeptanzkriterien, API-Spezifikationen, Geschäftsregeln,
  Zustandsmodelle, Masken- und Feldbeschreibungen. Notiere Version oder Datum je Quelle.
- Lege sofort die Tabelle **Offene Fragen** an. Typische Kandidaten: offene Intervallgrenzen,
  fehlende Fehlerbehandlung, undefinierte Leerwerte, Einheiten, Rundung, Zeitzonen,
  Groß- und Kleinschreibung.

### 2. Testbedingungen ableiten

Je testbarem Aspekt eine Testbedingung mit ID (`TB-xx`) und Quellverweis.
Sie beschreibt *was* geprüft wird, noch nicht *wie*.

### 3. Verfahren wählen und Referenz laden

| Merkmal der Spezifikation | Verfahren | Referenz |
| --- | --- | --- |
| Werte mit Bereichen, Typen, Listen; geordnete Bereiche | Äquivalenzklassen + Grenzwertanalyse | [aequivalenzklassen-grenzwerte.md](references/aequivalenzklassen-grenzwerte.md) |
| Kombinationen von Bedingungen bestimmen Aktionen; komplexe Logik | Entscheidungstabelle, Ursache-Wirkungs-Graph | [entscheidungstabellen.md](references/entscheidungstabellen.md) |
| Verhalten hängt von Vorgeschichte oder Status ab | Zustandsübergangstest | [zustandsuebergaenge.md](references/zustandsuebergaenge.md) |
| Viele Parameter mit mehreren Werten, Konfigurationen | Klassifikationsbaum, paarweises Testen | [kombinatorik.md](references/kombinatorik.md) |
| Abläufe, Interaktion Akteur-System | Anwendungsfallbasierter Test | [anwendungsfaelle.md](references/anwendungsfaelle.md) |
| Formal definierte Eingabeformate (Grammatik, Regex, Protokoll, Schema) | Syntaxtest | [syntaxtest.md](references/syntaxtest.md) |
| Bereiche, die die Spezifikation nicht abdeckt; zusätzliche Klassen und Angriffswerte nach Fehlerart | Testheuristiken | Skill `exploratives-testen`, Datei `references/heuristiken.md` |

- Begründe die Wahl je Testbedingung in einem Satz.
- Kombiniere Verfahren, wo die Spezifikation es verlangt. Beispiel: Ereignisdaten eines
  Zustandsübergangs mit Äquivalenzklassen, Parameterwerte für paarweises Testen aus
  Äquivalenzklassen.

### 4. Verfahren anwenden

Folge der geladenen Referenz vollständig, einschließlich ihrer Prüfliste.

### 5. Testfälle spezifizieren

Jeder Testfall enthält:

- ID (`TF-xx`), Verweis auf Testbedingung und Quelle,
- Verfahren und abgedecktes Element (Klasse, Grenzwert, Regel, Übergang, Ablauf),
- Vorbedingungen,
- konkrete Eingabedaten, keine Platzhalter wie „gültiger Wert“,
- **erwartetes Ergebnis**, aus der Spezifikation belegt. Nicht belegbar heißt offene Frage, kein geratener Wert,
- Priorität (hoch, mittel, niedrig) nach Risiko.

### 6. Überdeckung nachweisen

Je Verfahren: identifizierte Elemente, abgedeckte Elemente, Grad in Prozent,
bewusst ausgelassene Elemente mit Begründung.

### 7. Selbstprüfung

Korrigiere vor der Ausgabe, statt zu kommentieren.

- [ ] Jede Testbedingung hat eine Quelle.
- [ ] Die Prüfliste jeder verwendeten Referenz ist erfüllt.
- [ ] Jedes erwartete Ergebnis ist aus der Spezifikation belegt.
- [ ] Leerwert, null, Maximallänge, Typgrenzen, Locale und Zeit sind betrachtet.
- [ ] Alle Unklarheiten stehen in „Offene Fragen“.
- [ ] Bereiche jenseits der Spezifikation sind für exploratives Testen markiert; die Klassen sind mit den Grenz- und Angriffswerten nach Fehlerart abgeglichen (Skill `exploratives-testen`, `references/heuristiken.md`, Abschnitt 4).

## Lite-Modus

Bei Teilfragen oder einzelnen Verfahrensschritten nur die betreffenden Abschnitte ausgeben (z. B. nur die Äquivalenzklassen und Grenzwerte eines Feldes), statt das volle Schema zu füllen. Die Selbstprüfung gilt dann nur für die ausgegebenen Teile; offene Fragen werden trotzdem genannt.

## Ausgabe

```markdown
# Testentwurf: <Testobjekt>

## Testbasis
| Quelle | Version/Datum |

## Offene Fragen
| ID | Fundstelle | Unklarheit | Auswirkung auf Tests |

## Testbedingungen
| ID | Testbedingung | Quelle | Verfahren | Begründung |

## Verfahrensartefakte
<Klassen, Grenzwerte, Entscheidungstabellen, Zustandstabellen, Klassifikationsbaum, Abläufe, Grammatik>

## Testfälle
| ID | TB | Verfahren | Abgedecktes Element | Vorbedingung | Eingabe | Erwartetes Ergebnis | Prio |

## Überdeckung
| Verfahren | Elemente gesamt | Abgedeckt | Grad | Ausgelassen (Begründung) |

## Hinweise für exploratives Testen
<Bereiche, die die Spezifikation nicht abdeckt>
```
