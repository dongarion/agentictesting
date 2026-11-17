# Bedingungs-, Mehrfachbedingungs- und MC/DC-Überdeckung

Für Entscheidungen aus **mehreren atomaren Bedingungen**. Pflicht in sicherheitskritischen
Bereichen (DO-178C Level A verlangt MC/DC, ISO 26262 ASIL D empfiehlt es dringend).

## Inhalt
1. Begriffe
2. Hierarchie der Kriterien
3. MC/DC-Vorgehen
4. Kurzschlussauswertung und Kopplung
5. Anti-Patterns
6. Prüfliste
7. Beispiel

## 1. Begriffe

- **Atomare Bedingung:** boolescher Ausdruck ohne weitere boolesche Operatoren (`x > 5`, `flag`).
- **Entscheidung:** Gesamtausdruck aus atomaren Bedingungen und Operatoren
  (`x > 5 && (flag || y == 0)`).
- Jede Entscheidung in ihre atomaren Bedingungen zerlegen und tabellarisch nummerieren (A, B, C).

## 2. Hierarchie der Kriterien

| Kriterium | Forderung | Testfälle bei n Bedingungen | Schwäche |
| --- | --- | --- | --- |
| Entscheidungsüberdeckung | Entscheidung einmal wahr, einmal falsch | 2 | Einzelne Bedingungen können unbeachtet bleiben |
| Bedingungsüberdeckung | Jede atomare Bedingung einmal wahr, einmal falsch | 2 | Die Entscheidung selbst kann immer gleich ausfallen |
| Bedingungs-/Entscheidungsüberdeckung | beides zugleich | 2 | Einfluss der einzelnen Bedingung nicht nachgewiesen |
| **MC/DC** | Jede Bedingung beeinflusst nachweislich unabhängig das Ergebnis | n+1 bis 2n | Aufwand bei Kopplung |
| Mehrfachbedingungsüberdeckung | Alle Kombinationen | 2^n | Explodiert schnell |

## 3. MC/DC-Vorgehen

Modified Condition/Decision Coverage. Für jede atomare Bedingung muss ein **Testfallpaar**
existieren, in dem

- nur diese eine Bedingung ihren Wert ändert,
- alle anderen Bedingungen gleich bleiben,
- und das Ergebnis der Entscheidung sich ändert.

Vorgehen:

1. Wahrheitstabelle der Entscheidung aufstellen (alle 2^n Zeilen, bei n ≤ 5 vollständig,
   sonst gezielt).
2. Für jede Bedingung die Zeilenpaare suchen, die sich nur in dieser Bedingung und im Ergebnis
   unterscheiden.
3. Minimale Menge von Zeilen wählen, die für jede Bedingung ein solches Paar enthält.
   Minimum ist n+1 Testfälle.
4. Varianten kennen: **Unique Cause MC/DC** (strikt: nur eine Bedingung ändert sich),
   **Masking MC/DC** (andere Bedingungen dürfen sich ändern, wenn sie maskiert sind).
   Die Norm oder der Kunde legt die Variante fest. Dokumentieren.

## 4. Kurzschlussauswertung und Kopplung

- Bei `&&` und `||` mit Kurzschluss werden nachfolgende Bedingungen nicht ausgewertet.
  Werkzeuge zählen hier unterschiedlich. Zählweise des Werkzeugs und der Norm abgleichen.
- **Gekoppelte Bedingungen** (dieselbe Variable in mehreren atomaren Bedingungen, z. B.
  `x > 0 && x < 10`) lassen sich nicht unabhängig variieren. Dokumentieren und Masking MC/DC
  oder eine Begründung für die Nichterreichbarkeit verwenden.
- Bedingungen mit Nebenwirkungen (Funktionsaufrufe in der Entscheidung) sind ein Befund
  für das Review, unabhängig vom Test.

## 5. Anti-Patterns

- Mehrfachbedingungsüberdeckung fordern, wo MC/DC genügt, und dann aus Aufwandsgründen gar
  nichts erreichen.
- MC/DC-Paare aus dem Werkzeugbericht übernehmen, ohne die Wahrheitstabelle selbst zu prüfen.
- Bedingungsüberdeckung mit Entscheidungsüberdeckung verwechseln.
- Komplexe Entscheidung testen, statt das Refactoring in benannte Teilbedingungen vorzuschlagen.

## 6. Prüfliste

- [ ] Jede Entscheidung ist in atomare Bedingungen zerlegt und tabelliert.
- [ ] Kriterium ist gewählt und aus Norm oder Risiko begründet.
- [ ] Für MC/DC: je Bedingung ist das Testfallpaar benannt, Variante (Unique Cause/Masking) ist angegeben.
- [ ] Kurzschlussauswertung und Kopplung sind berücksichtigt und dokumentiert.
- [ ] Zählweise des Werkzeugs ist mit dem geforderten Kriterium abgeglichen.

## 7. Beispiel

Entscheidung: `(A && B) || C`

| Nr | A | B | C | Ergebnis |
| --- | --- | --- | --- | --- |
| 1 | T | T | T | T |
| 2 | T | T | F | T |
| 3 | T | F | T | T |
| 4 | T | F | F | F |
| 5 | F | T | T | T |
| 6 | F | T | F | F |
| 7 | F | F | T | T |
| 8 | F | F | F | F |

MC/DC-Paare: A → (2, 6), B → (2, 4), C → (4, 3) oder (6, 5) oder (8, 7).
Minimale Menge: {2, 3, 4, 6} = 4 Testfälle (n+1) statt 8.
