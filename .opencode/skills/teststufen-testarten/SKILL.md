---
name: teststufen-testarten
description: >
  Ordnet Tests den Teststufen (Komponententest, Komponentenintegrationstest, Systemtest,
  Systemintegrationstest, Abnahmetest mit UAT, OAT, vertraglicher und regulatorischer Abnahme,
  Alpha und Beta) und den Testarten zu (funktional, nicht-funktional nach ISO/IEC 25010,
  Black-Box, White-Box, Fehlernachtest, Regression, Smoke, Sanity) und plant die
  nicht-funktionalen Tests im Detail: Performance (Last, Stress, Spike, Soak, Volumen,
  Skalierbarkeit), Barrierefreiheit (BITV 2.0, WCAG, EN 301 549), Kompatibilität,
  Zuverlässigkeit und Wiederherstellung, Wartbarkeit, Portabilität und Installation,
  Lokalisierung. Verwenden, wenn geklärt werden soll, welche Stufe was prüft, wer
  verantwortlich ist, wie ein Lasttest oder Barrierefreiheitstest aufgebaut wird, oder bei
  Stichworten wie "Abnahmetest", "UAT", "Lasttest", "JMeter", "k6", "BITV", "WCAG",
  "Regression", "Smoke-Test". Nicht für Sicherheits-, KI- und Usability-Tests im Detail
  (Skill Spezialtests).
license: CC BY-SA 4.0. Siehe LICENSE.txt
metadata:
  author: "IT-Beratung Martin Klein"
  copyright: "© 2026 IT-Beratung Martin Klein"
  version: "1.0"
  basis: "ISTQB CTFL 4.0 Kap. 2.2, CTAL-TA, CTAL-TTA, CT-PT, CT-AcT; ISO/IEC 25010:2023; ISO/IEC/IEEE 29119; BITV 2.0, WCAG 2.2, EN 301 549"
  sprache: "de"
---

# Teststufen und Testarten

**Teststufen** gliedern das Testen nach dem Integrationsgrad des Testobjekts: von der
einzelnen Komponente bis zum System im Einsatzkontext. **Testarten** gliedern nach dem
Prüfziel: welches Qualitätsmerkmal, aus welcher Sicht, mit welchem Anlass. Jede Testart kann
auf jeder Stufe vorkommen.

Die Themen stehen in `references/`. Lade das, was die Frage braucht.

## Haltung

- **Strukturiertes Denken.** Du ordnest jeden Test eindeutig einer Stufe und einem Prüfziel zu.
  So werden Lücken und Doppelarbeit sichtbar.
- **Qualität ist mehr als Funktion.** Du denkst bei jedem System an alle Qualitätsmerkmale,
  besonders an die, nach denen niemand gefragt hat. Nicht-funktionale Mängel sind oft die
  teuersten.
- **Messbarkeit.** Nicht-funktionale Anforderungen wie „schnell“ oder „barrierefrei“ übersetzt
  du in prüfbare Kriterien mit Zahl, Norm und Messverfahren, bevor getestet wird.
- **Inklusion als Haltung.** Barrierefreiheit ist kein Zusatz, sondern Voraussetzung für
  Teilhabe und im öffentlichen Sektor Pflicht. Du testest mit Hilfsmitteln, nicht nur mit Scannern.
- **Messdisziplin bei Performance.** Du misst unter kontrollierten, dokumentierten Bedingungen,
  wiederholst, vergleichst und traust keiner einzelnen Zahl.

## Vorgehen

### 1. Einordnen

| Frage | Referenz |
| --- | --- |
| Welche Teststufe prüft was, mit welcher Testbasis, durch wen? Abnahmeformen? | [teststufen.md](references/teststufen.md) |
| Welche Testarten gibt es, wie wird Regression organisiert? Welche Qualitätsmerkmale? | [testarten.md](references/testarten.md) |
| Performance-, Last-, Stress-, Dauer-, Skalierbarkeitstest | [performance.md](references/performance.md) |
| Barrierefreiheitstest (BITV, WCAG, EN 301 549) | [barrierefreiheit.md](references/barrierefreiheit.md) |
| Kompatibilität, Zuverlässigkeit, Wiederherstellung, Wartbarkeit, Portabilität, Installation, Lokalisierung | [weitere-nichtfunktionale.md](references/weitere-nichtfunktionale.md) |

### 2. Planen

- Matrix Teststufe × Testart mit Verantwortlichen und Umgebung erstellen.
- Nicht-funktionale Anforderungen messbar machen (Zahl, Norm, Verfahren, Umgebung).
- Fehlende nicht-funktionale Anforderungen als Befund melden und mit Fachbereich und Betrieb klären.

### 3. Selbstprüfung

- [ ] Jede Teststufe hat Ziel, Testbasis, Testobjekt, Umgebung, Verantwortliche und Endekriterien.
- [ ] Alle relevanten Qualitätsmerkmale nach ISO/IEC 25010 sind betrachtet; Ausschlüsse begründet.
- [ ] Nicht-funktionale Anforderungen sind messbar formuliert.
- [ ] Regressionsumfang und Auslöser sind festgelegt.
- [ ] Die Prüfliste der verwendeten Referenz ist erfüllt.

## Lite-Modus

Bei Teilfragen oder einzelnen Verfahrensschritten nur die betreffenden Abschnitte ausgeben (z. B. nur die messbare Formulierung einer Performance-Anforderung), statt das volle Schema zu füllen. Die Selbstprüfung gilt dann nur für die ausgegebenen Teile; offene Fragen werden trotzdem genannt.

## Ausgabe

```markdown
# Teststufen und Testarten: <System>

## Matrix
| Teststufe | Funktional | Performance | Sicherheit | Barrierefreiheit | Kompatibilität | Zuverlässigkeit | ... | Verantwortlich | Umgebung |

## Messbare nicht-funktionale Anforderungen
| ID | Merkmal | Kriterium (Zahl/Norm) | Messverfahren | Teststufe |

## Offene Punkte
```
