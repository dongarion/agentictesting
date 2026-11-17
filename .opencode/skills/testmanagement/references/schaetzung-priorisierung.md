# Testaufwandsschätzung und Testpriorisierung

## Inhalt
1. Grundsätze der Schätzung
2. Schätzverfahren
3. Einflussfaktoren
4. Schätzung darstellen
5. Testpriorisierung
6. Anti-Patterns
7. Prüfliste

## 1. Grundsätze der Schätzung

- Schätzung ist eine Prognose mit Unsicherheit, keine Zusage. Bandbreite und Konfidenz angeben.
- Mehrere Verfahren kombinieren und Abweichungen erklären.
- Die Menschen schätzen lassen, die die Arbeit tun.
- Annahmen ausdrücklich: Umfang, Qualität der Lieferungen, Verfügbarkeit von Umgebung und
  Fachexperten, Anzahl Testzyklen, Automatisierungsgrad.
- Schätzung bei neuen Informationen aktualisieren (Kegel der Unsicherheit).

## 2. Schätzverfahren

| Verfahren | Art | Prinzip | Eignung |
| --- | --- | --- | --- |
| Expertenschätzung | expertenbasiert | Erfahrene Personen schätzen je Arbeitspaket | Schnell, bei Erfahrung mit ähnlichen Systemen |
| Wideband Delphi | expertenbasiert | Mehrere Experten schätzen anonym, diskutieren Abweichungen, schätzen erneut | Wichtige Schätzungen, Konsens |
| Planning Poker | expertenbasiert, relativ | Team schätzt Story Points mit Karten; Testaufwand ist Teil der Story | Agile Teams |
| Drei-Punkt-Schätzung (PERT) | expertenbasiert, statistisch | E = (O + 4M + P) / 6, Standardabweichung (P − O) / 6 | Unsicherheit beziffern |
| Kennzahlenbasiert / Extrapolation | metrikbasiert | Aus historischen Daten: Aufwand je Testfall, je Anforderung, je Function Point | Wenn verlässliche Historie existiert |
| Verhältnisbasiert | metrikbasiert | Testaufwand als Anteil am Entwicklungsaufwand (organisationsspezifisch) | Grobe Plausibilisierung, nicht als alleinige Methode |
| Work Breakdown Structure | analytisch | Testaktivitäten zerlegen bis schätzbar, aufsummieren | Testkonzept, Angebote |
| Test Point Analysis (TPA) | analytisch, metrikbasiert | Function Points gewichtet nach Qualitätsmerkmalen und Umgebungsfaktoren | Formale Angebote, Festpreis |

Für Angebote: WBS plus Drei-Punkt je Paket plus Plausibilisierung über Verhältnis oder Historie.

## 3. Einflussfaktoren

- **Produkt:** Größe, Komplexität, Qualitätsanforderungen, Regulatorik, Testbasis-Qualität.
- **Prozess:** Vorgehensmodell, Automatisierungsgrad, Werkzeuge, Anzahl Testzyklen,
  Fehlerbehebungszeiten.
- **Menschen:** Erfahrung, Teamstabilität, Domänenwissen, Verfügbarkeit von Fachexperten.
- **Umfeld:** Umgebungen, Testdaten, Schnittstellenpartner, Sicherheitsauflagen, Zeitdruck.
- **Ergebnisse:** Erwartete Fehlerzahl und Nachtestaufwand; oft unterschätzt.

Nicht vergessen: Planung, Berichte, Meetings, Fehlermanagement, Umgebungsprobleme,
Wartung der Automatisierung, Einarbeitung, Urlaub.

## 4. Schätzung darstellen

```
Arbeitspaket          O     M     P     E      σ
Testplanung           5     8    12    8,2    1,2
Testentwurf          30    45    70   46,7    6,7
Realisierung/Daten   15    25    45   26,7    5,0
Durchführung 2 Zyklen 40   60   100   63,3   10,0
Fehlernachtest       10    20    40   21,7    5,0
Abschluss             3     5     8    5,2    0,8
Summe (PT)                              171,8  ~14,0 (Wurzel der Varianzsumme)
→ 172 PT, Bandbreite 158–186 PT bei ±1σ
```

Dazu: Annahmenliste, Risiken der Schätzung, Bedingungen für Neuschätzung.

## 5. Testpriorisierung

Reihenfolge der Testfälle oder Testbedingungen:

| Strategie | Prinzip |
| --- | --- |
| Risikobasiert | Höchstes Risiko zuerst (Standard) |
| Überdeckungsbasiert | Testfälle mit größtem Zuwachs an Überdeckung zuerst (additional coverage) |
| Anforderungsbasiert | Nach Priorität der Anforderung (MoSCoW, Geschäftswert) |
| Abhängigkeitsbasiert | Was Voraussetzung für andere ist, zuerst |
| Änderungsbasiert | Geänderte und betroffene Bereiche zuerst (Regression) |
| Fehlerhistorisch | Bereiche mit vielen bisherigen Fehlern zuerst |

Praxis: risikobasiert mit Berücksichtigung von Abhängigkeiten. Ziel: Wenn der Test jederzeit
abgebrochen werden muss, ist das Wichtigste bereits getestet.

Für Regressionssuiten in der Pipeline: Testfallauswahl nach Änderung und Priorisierung nach
Fehlerwahrscheinlichkeit (Test Impact Analysis).

## 6. Anti-Patterns

- Schätzung „rückwärts“ aus dem Termin.
- Einzelwert ohne Bandbreite; wird zur Zusage.
- Nachtest- und Regressionsaufwand vergessen.
- Priorisierung nach Bequemlichkeit (einfache Tests zuerst, um Zahlen zu produzieren).
- Keine Nachkalkulation; Historie wird nie besser.

## 7. Prüfliste

- [ ] Mindestens zwei Schätzverfahren; Abweichungen erklärt.
- [ ] Schätzung hat Bandbreite und Annahmenliste.
- [ ] Alle Aktivitäten inkl. Nachtest, Regression, Management, Umgebungsprobleme sind enthalten.
- [ ] Schätzer sind die Ausführenden oder eingebunden.
- [ ] Priorisierungsstrategie ist benannt; Reihenfolge ist risikobasiert begründet.
- [ ] Nachkalkulation ist geplant.
