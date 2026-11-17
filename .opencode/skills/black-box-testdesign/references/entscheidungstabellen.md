# Entscheidungstabellen und Ursache-Wirkungs-Graph

Für Geschäftsregeln, bei denen **Kombinationen von Bedingungen** bestimmen, welche Aktionen
ausgeführt werden. Der Ursache-Wirkungs-Graph ist ein Hilfsmittel, um komplexe Logik
zu modellieren. Er wird immer in eine Entscheidungstabelle überführt.

## Inhalt
1. Aufbau
2. Vorgehen
3. Vereinfachen
4. Ursache-Wirkungs-Graph
5. Testfälle und Überdeckung
6. Anti-Patterns
7. Prüfliste
8. Beispiel

## 1. Aufbau

- **Bedingungen** (Zeilen oben): Eingaben oder Zustände, die die Entscheidung beeinflussen.
- **Aktionen** (Zeilen unten): Ergebnisse oder Reaktionen des Systems.
- **Regeln** (Spalten): je eine Kombination von Bedingungswerten mit den zugehörigen Aktionen.
- Notation: `J`/`N` für binäre Bedingungen, konkrete Werte oder Klassen bei mehrwertigen
  Bedingungen (erweiterte Entscheidungstabelle), `X` für ausgeführte Aktionen,
  `–` für „irrelevant“.

## 2. Vorgehen

1. Bedingungen aus der Spezifikation identifizieren. Jede Bedingung muss eindeutig auswertbar sein.
2. Aktionen identifizieren, auch Fehlermeldungen und „keine Aktion“.
3. **Vollständige** Tabelle erzeugen: bei n binären Bedingungen 2^n Regeln. Bei mehrwertigen
   Bedingungen das Produkt der Wertanzahlen.
4. Für jede Regel die Aktionen aus der Spezifikation eintragen.
5. Prüfen:
   - **Lücken:** Regel ohne spezifizierte Aktion → offene Frage.
   - **Widersprüche:** gleiche Bedingungswerte, unterschiedliche Aktionen in der Spezifikation → Befund.
   - **Unmögliche Kombinationen:** ausdrücklich markieren und begründen, nicht stillschweigend löschen.
6. Erst danach vereinfachen.

Bei mehr als etwa 6 binären Bedingungen (64 Regeln): Tabelle in Teiltabellen nach
fachlichen Aspekten zerlegen oder mit [kombinatorik.md](kombinatorik.md) arbeiten.

## 3. Vereinfachen

- Zwei Regeln lassen sich zusammenfassen, wenn sie sich in genau einer Bedingung unterscheiden
  und identische Aktionen haben. Diese Bedingung wird `–`.
- Vereinfache nur, wenn die Spezifikation die Irrelevanz belegt. Im Zweifel nicht vereinfachen.
- Dokumentiere die Ausgangstabelle und die vereinfachte Tabelle.
- Risiko: Eine vereinfachte Regel mit `–` wird oft nur mit einem Wert getestet. Bei hohem
  Risiko beide Ausprägungen testen.

## 4. Ursache-Wirkungs-Graph

Für Logik, die sich in Prosa schwer überblicken lässt.

1. **Ursachen** (Eingabebedingungen) und **Wirkungen** (Ausgaben) nummerieren.
2. Logische Verknüpfungen: Identität, NICHT, UND, ODER.
3. Einschränkungen zwischen Ursachen:
   - **E** (exklusiv): höchstens eine wahr,
   - **I** (inklusiv): mindestens eine wahr,
   - **O** (genau eine): genau eine wahr,
   - **R** (erfordert): a wahr erfordert b wahr.
4. Einschränkung zwischen Wirkungen: **M** (maskiert): Wirkung a unterdrückt Wirkung b.
5. Graph in eine Entscheidungstabelle überführen. Einschränkungen schließen Regeln aus.

## 5. Testfälle und Überdeckung

- Je Regel mindestens ein Testfall. Bei `–` den gewählten Wert dokumentieren.
- Konkrete Daten wählen, die die Bedingung erfüllen. Für Bedingungen mit Wertebereichen
  die Daten mit [aequivalenzklassen-grenzwerte.md](aequivalenzklassen-grenzwerte.md) bestimmen.
- **Überdeckung** = getestete Regeln / alle machbaren Regeln × 100 %.
  Unmögliche Regeln zählen nicht, werden aber aufgeführt.

## 6. Anti-Patterns

- Direkt die vereinfachte Tabelle aufstellen, ohne die vollständige.
- Unmögliche Kombinationen ohne Begründung streichen.
- „Keine Aktion“ als Aktion vergessen.
- Bedingungen, die nicht unabhängig sind, als unabhängig behandeln (z. B. „Neukunde“ und
  „mehr als 10 Bestellungen“).
- Lücken in der Spezifikation mit der „naheliegenden“ Aktion füllen.

## 7. Prüfliste

- [ ] Vollständige Tabelle mit allen Kombinationen liegt vor.
- [ ] Jede Regel hat aus der Spezifikation belegte Aktionen oder eine offene Frage.
- [ ] Widersprüche und Lücken sind als Befunde erfasst.
- [ ] Unmögliche Kombinationen sind begründet.
- [ ] Vereinfachungen sind durch die Spezifikation gedeckt.
- [ ] Je machbarer Regel existiert ein Testfall.

## 8. Beispiel

Anforderung: „Premiumkunden erhalten 10 % Rabatt. Bei Bestellungen über 100 € erhalten alle
Kunden versandkostenfreie Lieferung. Premiumkunden mit Bestellungen über 100 € erhalten
zusätzlich ein Geschenk.“

| | R1 | R2 | R3 | R4 |
| --- | --- | --- | --- | --- |
| B1 Premiumkunde | J | J | N | N |
| B2 Bestellwert > 100 € | J | N | J | N |
| A1 10 % Rabatt | X | X | | |
| A2 Versandkostenfrei | X | | X | |
| A3 Geschenk | X | | | |
| A4 Keine Vergünstigung | | | | X |

Offene Fragen:
- Bezieht sich „über 100 €“ auf den Wert vor oder nach dem Rabatt? Für R1 und R2 entscheidend.
- Gilt genau 100,00 € als „über 100 €“? (Grenzwerte 100,00 und 100,01 testen.)
