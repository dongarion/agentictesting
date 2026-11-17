# Mutationstest

Misst die **Fehlererkennungsstärke** einer Testsuite: Das Werkzeug erzeugt viele Varianten
des Codes mit je einem künstlichen Fehler (Mutanten) und prüft, ob die Tests ihn erkennen
(„töten“). Überdeckung sagt, was ausgeführt wurde; der Mutationswert sagt, was geprüft wurde.

## Inhalt
1. Begriffe
2. Mutationsoperatoren
3. Vorgehen
4. Ergebnis interpretieren
5. Aufwand begrenzen
6. Werkzeuge
7. Anti-Patterns
8. Prüfliste

## 1. Begriffe

- **Mutant:** Kopie des Codes mit einer Änderung.
- **Getötet (killed):** mindestens ein Test schlägt fehl.
- **Überlebt (survived):** alle Tests bestehen trotz Änderung. Lücke in den Assertions oder den Eingaben.
- **Äquivalent:** Mutant verhält sich semantisch gleich; nicht tötbar. Muss manuell erkannt und ausgeschlossen werden.
- **Timeout / Fehler:** Mutant erzeugt Endlosschleife oder Absturz; zählt meist als getötet.
- **Mutationswert (Mutation Score):** getötete / (alle − äquivalente) × 100 %.

## 2. Mutationsoperatoren

| Kategorie | Beispiel |
| --- | --- |
| Arithmetik | `+` ↔ `−`, `*` ↔ `/` |
| Relationen | `<` ↔ `<=`, `==` ↔ `!=` |
| Bedingungen | Bedingung negieren, `&&` ↔ `\|\|`, Bedingung durch `true`/`false` ersetzen |
| Konstanten | `0` → `1`, `n` → `n+1`, leere Zeichenkette |
| Rückgabewerte | `return x` → `return null` / `0` / `!x` |
| Anweisungen | Methodenaufruf entfernen (Void Call), Zuweisung entfernen |
| Inkremente | `i++` ↔ `i--` |
| Sprachspezifisch | Exception-Handling entfernen, Lambda-Ersatz, Optional-Umkehr |

Starte mit dem Standard-Set des Werkzeugs; erweitere gezielt für kritische Logik.

## 3. Vorgehen

1. Voraussetzung: grüne, schnelle, deterministische Testsuite. Flaky Tests zuerst beseitigen.
2. Geltungsbereich festlegen: kritische Module, geänderte Dateien, nicht das ganze System.
3. Lauf starten; Inkrementalmodus nutzen, wo verfügbar.
4. Überlebende Mutanten durchgehen, je Mutant entscheiden:
   - **Testlücke:** Assertion oder Eingabe ergänzen.
   - **Äquivalenter Mutant:** dokumentieren und ausschließen.
   - **Toter oder redundanter Code:** Refactoring-Befund.
5. Mutationswert je Modul festhalten, Trend beobachten.

## 4. Ergebnis interpretieren

- Ein überlebender Mutant im Kern der Geschäftslogik wiegt schwerer als zehn in Logging-Code.
  Nach Modul und Risiko bewerten, nicht nur den Gesamtwert.
- Typische Ursachen überlebender Mutanten: fehlende Assertion, Assertion zu schwach
  (`assertNotNull` statt Wertprüfung), nur Happy Path, Grenzwerte nicht getestet
  (`<` gegenüber `<=` überlebt genau dann).
- Zielwerte sind projektabhängig. Realistisch für Kernlogik: 70–90 %. 100 % ist wegen
  äquivalenter Mutanten und Aufwand selten sinnvoll.

## 5. Aufwand begrenzen

- Nur geänderte Klassen im Pull Request mutieren (PIT `--targetClasses`, Stryker `--since`).
- Operatoren auf das Standard-Set beschränken.
- Tests nach Überdeckung vorselektieren (Werkzeuge machen das automatisch).
- Nächtlich für das ganze Modul, im PR nur inkrementell.

## 6. Werkzeuge

| Sprache | Werkzeug |
| --- | --- |
| Java/Kotlin | PIT (pitest) |
| JavaScript/TypeScript, C#, Scala | Stryker Mutator |
| Python | mutmut, cosmic-ray |
| C/C++ | mull, Dextool Mutate |
| Go | go-mutesting, gremlins |
| Rust | cargo-mutants |

## 7. Anti-Patterns

- Mutationstest auf eine Suite mit instabilen Tests anwenden; Ergebnisse sind Rauschen.
- Mutationswert als Teamziel ohne Modulgewichtung; führt zu Assertions auf Nebensächliches.
- Äquivalente Mutanten mit Pseudo-Tests „töten“.
- Ganzes System nächtlich mutieren und den Bericht nie lesen.

## 8. Prüfliste

- [ ] Testsuite ist grün und deterministisch.
- [ ] Geltungsbereich und Operatoren sind festgelegt.
- [ ] Jeder überlebende Mutant im Geltungsbereich ist klassifiziert (Lücke / äquivalent / Refactoring).
- [ ] Mutationswert je Modul ist dokumentiert.
- [ ] Inkrementeller Lauf ist in die CI integriert oder bewusst nicht.
