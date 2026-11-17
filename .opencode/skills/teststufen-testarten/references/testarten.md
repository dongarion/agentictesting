# Testarten

## Inhalt
1. Gliederung
2. Funktionaler und nicht-funktionaler Test
3. Qualitätsmerkmale nach ISO/IEC 25010:2023
4. Black-Box und White-Box
5. Änderungsbezogene Tests
6. Regression organisieren
7. Smoke und Sanity
8. Wartungstest
9. Anti-Patterns
10. Prüfliste

## 1. Gliederung

CTFL 4.0 unterscheidet vier Testarten:

| Testart | Prüfziel |
| --- | --- |
| Funktionaler Test | **Was** das System tut (funktionale Vollständigkeit, Korrektheit, Angemessenheit) |
| Nicht-funktionaler Test | **Wie gut** es das tut (übrige Qualitätsmerkmale) |
| Black-Box-Test | Ableitung aus der Spezifikation, ohne Kenntnis der Struktur |
| White-Box-Test | Ableitung aus der inneren Struktur |

Dazu änderungsbezogen: Fehlernachtest und Regressionstest.

## 2. Funktionaler und nicht-funktionaler Test

- Funktionale Tests auf allen Stufen; Verfahren: Skill `black-box-testdesign`.
- Nicht-funktionale Tests brauchen oft Spezialwissen, Werkzeuge und produktionsnahe Umgebungen;
  sie gehören früh in die Planung, nicht ans Ende.
- Viele nicht-funktionale Tests lassen sich auf niedrigen Stufen beginnen (Komponenten-
  Performance, statische Analyse auf Wartbarkeit, Barrierefreiheit von UI-Komponenten).

## 3. Qualitätsmerkmale nach ISO/IEC 25010:2023

| Merkmal | Untermerkmale (Auswahl) | Test |
| --- | --- | --- |
| Funktionale Eignung | Vollständigkeit, Korrektheit, Angemessenheit | Funktionaler Test |
| Leistungseffizienz | Zeitverhalten, Ressourcennutzung, Kapazität | [performance.md](performance.md) |
| Kompatibilität | Koexistenz, Interoperabilität | [weitere-nichtfunktionale.md](weitere-nichtfunktionale.md), Skill `spezialtests` |
| Interaktionsfähigkeit | Erkennbarkeit der Eignung, Erlernbarkeit, Bedienbarkeit, Schutz vor Benutzerfehlern, Einbindung, Inklusivität, Selbstbeschreibungsfähigkeit | Skill `spezialtests` (Usability), [barrierefreiheit.md](barrierefreiheit.md) |
| Zuverlässigkeit | Fehlerfreiheit, Verfügbarkeit, Fehlertoleranz, Wiederherstellbarkeit | [weitere-nichtfunktionale.md](weitere-nichtfunktionale.md) |
| Sicherheit (Security) | Vertraulichkeit, Integrität, Nichtabstreitbarkeit, Verantwortlichkeit, Authentizität, Widerstandsfähigkeit | Skill `spezialtests` (Security) |
| Wartbarkeit | Modularität, Wiederverwendbarkeit, Analysierbarkeit, Modifizierbarkeit, Testbarkeit | [weitere-nichtfunktionale.md](weitere-nichtfunktionale.md), Skill `statischer-test` |
| Flexibilität (vormals Übertragbarkeit) | Anpassbarkeit, Skalierbarkeit, Installierbarkeit, Austauschbarkeit | [weitere-nichtfunktionale.md](weitere-nichtfunktionale.md) |
| Safety (neu 2023) | Betriebseinschränkung, Risikoerkennung, Ausfallsicherheit, Gefahrenwarnung, sichere Integration | Skill `spezialtests` (Embedded), Normen |

Die Version 2023 hat Usability zu „Interaktionsfähigkeit“ und Portabilität zu „Flexibilität“
umbenannt und Safety ergänzt. Kundenvorgaben beziehen sich oft noch auf ISO 25010:2011;
Begriffe abgleichen.

## 4. Black-Box und White-Box

- Black-Box: Skill `black-box-testdesign`; auf allen Stufen, Schwerpunkt System und Abnahme.
- White-Box: Skill `white-box-testdesign`; Schwerpunkt Komponente und Integration, auf
  Systemebene als Überdeckung von Menüs, Prozessen, Geschäftsregeln.
- Erfahrungsbasiert als dritte Familie: Skill `exploratives-testen`.

## 5. Änderungsbezogene Tests

- **Fehlernachtest (Re-Test, Confirmation Testing):** Bestätigen, dass ein gemeldeter Fehler
  behoben ist; gleiche Schritte, gleiche Daten, plus Varianten.
- **Regressionstest:** Sicherstellen, dass Änderungen (Fehlerbehebung, Feature, Konfiguration,
  Umgebung, Abhängigkeit) keine unerwünschten Seiteneffekte haben.

## 6. Regression organisieren

- **Auswirkungsanalyse** je Änderung: Welche Komponenten, Schnittstellen, Prozesse sind
  betroffen? Grundlage: Architektur, Rückverfolgbarkeit, Code-Abhängigkeiten, Test Impact Analysis.
- **Regressionssuiten** gestuft: Smoke (Minuten), Kernregression (je Merge/Nacht), volle
  Regression (vor Release).
- **Auswahl** nach Risiko, Änderungsbezug, Fehlerhistorie, Nutzungshäufigkeit.
- **Automatisierung** zuerst für Regression, weil häufig wiederholt (Skill `testautomatisierung`).
- **Pflege**: veraltete Tests entfernen, neue aus Fehlern ergänzen (jeder behobene Fehler
  bekommt einen Regressionstest), Laufzeit überwachen.
- **Wachstum begrenzen**: Regressionssuiten wachsen sonst unkontrolliert; regelmäßig auf
  Redundanz und Wert prüfen.

## 7. Smoke und Sanity

- **Smoke-Test:** breiter, flacher Test nach jeder Lieferung oder jedem Deployment: läuft das
  System grundsätzlich (Start, Anmeldung, Kernfunktion je Bereich, Schnittstellen erreichbar)?
  Eingangskriterium für weitere Tests. Automatisiert, wenige Minuten.
- **Sanity-Test:** schmaler, tiefer Test nach einer bestimmten Änderung: Ist die Änderung
  plausibel umgesetzt, bevor die volle Regression läuft? Oft manuell.

## 8. Wartungstest

Tests an einem System im Betrieb nach Änderungen: Fehlerbehebungen, Erweiterungen,
Migrationen, Plattformwechsel, Außerbetriebnahme (Archivierung, Löschung, Datenübernahme).
Umfang nach Auswirkungsanalyse und Risiko; Regression im Vordergrund. Herausforderung oft:
veraltete Dokumentation und fehlende Testmittel aus dem Ursprungsprojekt.

## 9. Anti-Patterns

- Nicht-funktionale Tests als „Phase am Ende“, wenn keine Zeit mehr bleibt.
- Regression ohne Auswirkungsanalyse: alles oder nichts.
- Behobene Fehler ohne Regressionstest; derselbe Fehler kommt wieder.
- Smoke-Test, der 90 Minuten dauert.
- Qualitätsmerkmale aus der Norm ungeprüft übernommen, ohne Relevanz zu bewerten.

## 10. Prüfliste

- [ ] Relevante Qualitätsmerkmale sind bewertet; Ausschlüsse begründet.
- [ ] Nicht-funktionale Tests sind früh geplant und Stufen zugeordnet.
- [ ] Regressionsstufen (Smoke, Kern, voll) mit Auslösern und Laufzeiten sind festgelegt.
- [ ] Auswirkungsanalyse steuert den Regressionsumfang.
- [ ] Jeder behobene Fehler erhält einen Regressionstest.
- [ ] Wartungstests sind für Änderungen im Betrieb geplant.
