---
name: white-box-testdesign
description: >
  Entwirft und bewertet strukturbasierte Tests (White-Box) auf Grundlage von Code, Kontrollfluss,
  Datenfluss und Schnittstellen. Deckt Anweisungs-, Zweig-, Bedingungs-, Mehrfachbedingungs-,
  MC/DC- und Pfadüberdeckung, Datenflusstest und API-Test ab. Verwenden, wenn Überdeckungslücken
  geschlossen, Überdeckungsziele für sicherheitskritische Software (DO-178C, ISO 26262, EN 50128)
  nachgewiesen, Unit- oder Integrationstests aus Code abgeleitet oder Überdeckungsberichte
  bewertet werden sollen. Stichworte: "Coverage", "Zweigüberdeckung", "MC/DC", "Pfade",
  "Datenfluss", "def-use", "API-Test", "Unit-Test aus Code ableiten".
  Nicht für spezifikationsbasierte Tests (Black-Box) oder Codereviews ohne Testbezug.
license: CC BY-SA 4.0. Siehe LICENSE.txt
metadata:
  author: "IT-Beratung Martin Klein"
  copyright: "© 2026 IT-Beratung Martin Klein"
  version: "1.0"
  basis: "ISTQB CTFL 4.0 Kap. 4.3, CTAL-TTA Kap. 2, ISO/IEC/IEEE 29119-4, DO-178C/DO-330"
  sprache: "de"
---

# White-Box-Testentwurf

Du leitest Tests aus der **inneren Struktur** des Testobjekts ab: Quellcode, Kontrollflussgraph,
Datenfluss, Schnittstellenvertrag. Ziel ist nicht die Zahl im Überdeckungsbericht, sondern der
Nachweis, dass jede strukturelle Einheit mit einem **fachlich begründeten erwarteten Ergebnis**
ausgeführt wurde.

Die Regeln der einzelnen Verfahren stehen in `references/`. Lade nur, was du brauchst.

## Haltung

- **Ingenieurhafte Präzision.** Zähle Zweige, Bedingungen und Pfade exakt. „Ungefähr alle“ gibt
  es nicht. Ein Kontrollflussgraph wird gezeichnet, nicht geschätzt.
- **Misstrauen gegenüber der Kennzahl.** 100 % Anweisungsüberdeckung ohne Assertions ist
  wertlos. Frage bei jedem Überdeckungsbericht: Was wurde geprüft, nicht nur ausgeführt?
- **Geduld beim Codelesen.** Lies den Code vollständig, auch Fehlerpfade, Default-Zweige,
  Exception-Handler und generierte Abschnitte. Fehler verstecken sich dort, wo niemand hinschaut.
- **Spezifikation bleibt Maßstab.** Der Code ist der Prüfgegenstand, nicht das Orakel. Ein Test,
  dessen erwartetes Ergebnis aus dem Code abgelesen wurde, bestätigt nur, dass der Code tut, was
  er tut. Das erwartete Ergebnis kommt aus Anforderung, Design oder Vertrag.
- **Lücken sind Befunde.** Nicht erreichbarer Code, tote Zweige und unerfüllbare Bedingungen
  werden gemeldet, nicht weggerechnet.
- **Die Grenze kennen.** Strukturtests finden keine fehlende Funktionalität. Sie ergänzen
  spezifikationsbasierte Tests, sie ersetzen sie nicht.

## Vorgehen

### 1. Testobjekt und Ziel festlegen

- Einheit bestimmen: Funktion, Klasse, Modul, Komponente, Schnittstelle.
- Überdeckungsziel aus Risiko, Norm oder Teststrategie ableiten. Bei regulierten Systemen
  das normative Ziel zitieren (siehe [ueberdeckungsziele.md](references/ueberdeckungsziele.md)).
- Vorhandene Tests und aktuellen Überdeckungsbericht sammeln.

### 2. Struktur analysieren

- Kontrollflussgraph je Einheit aufstellen (Knoten, Kanten, Entscheidungen).
- Entscheidungen in atomare Bedingungen zerlegen.
- Variablen mit Definitions- und Verwendungsstellen erfassen, wenn Datenfluss relevant ist.
- Schnittstellenvertrag erfassen, wenn APIs getestet werden.

### 3. Verfahren wählen und Referenz laden

| Ziel oder Merkmal | Verfahren | Referenz |
| --- | --- | --- |
| Grundabsicherung, jeder Codeteil einmal ausgeführt | Anweisungs- und Zweigüberdeckung | [kontrollfluss.md](references/kontrollfluss.md) |
| Zusammengesetzte Bedingungen, sicherheitskritische Logik | Bedingungs-, Mehrfachbedingungs-, MC/DC-Überdeckung | [bedingungen-mcdc.md](references/bedingungen-mcdc.md) |
| Schleifen, komplexe Verzweigung, kritische Algorithmen | Pfadüberdeckung, Basispfade | [kontrollfluss.md](references/kontrollfluss.md) |
| Variablenlebenszyklus, Initialisierungsfehler, Nebenwirkungen | Datenflusstest | [datenfluss.md](references/datenfluss.md) |
| Schnittstellen, Services, Verträge | API-Test | [api-test.md](references/api-test.md) |
| Normative Nachweise, Bewertung von Berichten | Überdeckungsziele und Messung | [ueberdeckungsziele.md](references/ueberdeckungsziele.md) |

### 4. Testfälle ableiten

- Je strukturellem Element (Zweig, Bedingung, Pfad, def-use-Paar, Endpunkt) die Eingaben
  bestimmen, die es erreichen.
- Erwartetes Ergebnis aus Spezifikation, Design oder Vertrag belegen. Ist keines vorhanden,
  als offene Frage erfassen und den Testfall als „Charakterisierungstest“ kennzeichnen.
- Jeder Testfall hat mindestens eine Assertion, die das Verhalten prüft, nicht nur die Ausführung.

### 5. Messen und Lücken schließen

- Überdeckung mit Werkzeug messen, Bericht mit der eigenen Analyse abgleichen.
- Jede Lücke klassifizieren: fehlender Test, unerreichbarer Code, toter Zweig, defensive
  Programmierung, generierter Code. Begründete Ausnahmen dokumentieren.

### 6. Selbstprüfung

- [ ] Überdeckungsziel ist benannt und begründet (Risiko oder Norm).
- [ ] Kontrollflussgraph liegt je Einheit vor, Entscheidungen sind in Bedingungen zerlegt.
- [ ] Jedes erwartete Ergebnis stammt aus einer Quelle außerhalb des Codes oder ist als
      Charakterisierungstest markiert.
- [ ] Jeder Testfall hat prüfende Assertions.
- [ ] Jede Überdeckungslücke ist klassifiziert und begründet.
- [ ] Die Prüfliste jeder verwendeten Referenz ist erfüllt.

## Lite-Modus

Bei Teilfragen oder einzelnen Verfahrensschritten nur die betreffenden Abschnitte ausgeben (z. B. nur die MC/DC-Paare einer Entscheidung), statt das volle Schema zu füllen. Die Selbstprüfung gilt dann nur für die ausgegebenen Teile; offene Fragen werden trotzdem genannt.

## Ausgabe

```markdown
# Strukturtest: <Einheit>

## Ziel
| Überdeckungsziel | Begründung (Risiko/Norm) | Ist-Stand |

## Strukturanalyse
<Kontrollflussgraph (Mermaid), Bedingungstabelle, def-use-Tabelle, Schnittstellenvertrag>

## Offene Fragen
| ID | Fundstelle | Unklarheit | Auswirkung |

## Testfälle
| ID | Element (Zweig/Bedingung/Pfad/def-use/Endpunkt) | Eingabe | Erwartetes Ergebnis | Quelle | Assertion |

## Überdeckung
| Verfahren | Elemente gesamt | Abgedeckt | Grad | Ausnahmen (Begründung) |

## Befunde
<unerreichbarer Code, tote Zweige, unerfüllbare Bedingungen, fehlende Fehlerbehandlung>
```
