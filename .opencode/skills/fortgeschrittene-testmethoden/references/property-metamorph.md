# Property-based Testing und metamorphes Testen

Beide Methoden ersetzen das Beispiel-Orakel („bei Eingabe 5 kommt 25 heraus“) durch eine
**allgemeine Aussage** über das Verhalten.

## Inhalt
1. Property-based Testing (PBT)
2. Property-Muster
3. Metamorphes Testen (MT)
4. Metamorphe Relationen finden
5. Werkzeuge
6. Anti-Patterns
7. Prüfliste
8. Beispiele

## 1. Property-based Testing (PBT)

- Eine **Property** ist eine Aussage, die für alle Eingaben aus einem Bereich gilt.
- Das Framework erzeugt viele zufällige Eingaben, prüft die Property und **verkleinert**
  (shrinkt) einen Fehlerfall auf ein minimales Beispiel.
- Generatoren beschreiben den Eingaberaum: Typen, Bereiche, Strukturen, Constraints.
- Jeder Lauf ist reproduzierbar über den Seed; gefundene Beispiele werden als feste
  Regressionsfälle gespeichert (Hypothesis macht das automatisch in einer Datenbank).

Vorgehen:

1. Funktion oder Komponente wählen, deren Eingaberaum groß oder strukturiert ist.
2. Generator schreiben; Verteilung prüfen (erzeugt er auch Grenzfälle, leere Strukturen, Unicode?).
3. Properties nach den Mustern in Abschnitt 2 formulieren. Mehrere kleine Properties sind
   besser als eine große.
4. Laufen lassen, Fehlerfälle minimieren, klassifizieren: Produktfehler, falsche Property,
   schlechter Generator.
5. Anzahl der Beispiele und Deadline pro Test festlegen (CI-Zeit).

## 2. Property-Muster

| Muster | Beispiel |
| --- | --- |
| Roundtrip / Inverse | `parse(format(x)) == x`, `decrypt(encrypt(x)) == x` |
| Idempotenz | `normalize(normalize(x)) == normalize(x)` |
| Invariante | Nach `sort(xs)`: gleiche Länge, gleiche Elemente, aufsteigend |
| Kommutativität / Reihenfolge | `add(a, b) == add(b, a)`; Reihenfolge der Filter egal |
| Vergleich mit Referenz | Ergebnis gleich einer einfachen, langsamen Referenzimplementierung |
| Harte Grenzen | Ergebnis immer im Bereich, nie `null`, nie Exception außer definierter |
| Monotonie | Mehr Rabattpunkte ergeben nie höheren Preis |
| Konsistenz zweier Wege | `count(filter(xs))` entspricht `len([x for x in xs if …])` |
| Zustandsmaschine | Beliebige Aktionsfolgen auf ein Objekt, Invarianten nach jedem Schritt |

## 3. Metamorphes Testen (MT)

Für Systeme **ohne Orakel**: Suchmaschinen, Optimierer, Simulationen, ML-Modelle,
Bildverarbeitung, Compiler, wissenschaftliche Berechnungen.

Statt zu fragen „Ist Ausgabe y für Eingabe x korrekt?“, fragt MT:
„Wenn ich x nach Regel R zu x' verändere, muss sich y nach Regel R' zu y' verändern.“
Die **metamorphe Relation (MR)** verbindet mehrere Ausführungen.

Vorgehen:

1. Quell-Testfall wählen (beliebige gültige Eingabe, auch generiert).
2. MR anwenden: Folge-Testfall erzeugen.
3. Beide ausführen, Relation zwischen den Ausgaben prüfen.
4. Verletzung der Relation ist ein Befund, auch ohne zu wissen, welche der beiden Ausgaben falsch ist.

## 4. Metamorphe Relationen finden

| Fragetyp | Beispiel-MR |
| --- | --- |
| Permutation | Reihenfolge der Eingabeliste ändern → Summe gleich, sortierte Ausgabe gleich |
| Hinzufügen/Entfernen | Suchbegriff um UND-Term erweitern → Ergebnismenge ist Teilmenge |
| Skalierung | Alle Eingaben verdoppeln → Mittelwert verdoppelt, Varianz vervierfacht |
| Symmetrie | Bild spiegeln → erkannte Objekte gespiegelt, Anzahl gleich |
| Äquivalente Umformung | Programm umbenennen, Kommentare ändern → Compiler erzeugt gleiches Verhalten |
| Komposition | `route(A→C)` ist nie kürzer als `route(A→B) + route(B→C)` |
| Rauschen | Irrelevantes Attribut ändern → Klassifikation gleich (Robustheit von ML) |
| Monotonie | Höheres Einkommen bei sonst gleichen Daten → Kreditscore nicht schlechter (Fairness) |

MRs mit Fachexperten erarbeiten und mit Anforderungsbezug dokumentieren. Mehrere MRs
kombinieren; eine MR allein findet nur eine Fehlerklasse.

## 5. Werkzeuge

| Sprache | PBT-Framework |
| --- | --- |
| Python | Hypothesis (inkl. Zustandsmaschinen, Datenbank für Fehlerfälle) |
| Java/Kotlin | jqwik, QuickTheories, Kotest Property |
| JavaScript/TypeScript | fast-check |
| C# | FsCheck, CsCheck |
| Haskell/Erlang | QuickCheck (Ursprung), PropEr |
| Rust | proptest, quickcheck |
| Go | rapid, gopter |

Metamorphes Testen braucht kein eigenes Framework; es lässt sich mit jedem Testframework
oder mit PBT-Generatoren umsetzen.

## 6. Anti-Patterns

- Property, die die Implementierung nachbaut (dann testet man den Code gegen sich selbst).
- Generator, der nur „schöne“ Daten liefert; Grenzfälle fehlen.
- `assume()`-Filter, die 90 % der Beispiele verwerfen; Generator umbauen.
- Fehlerfälle nicht als feste Regressionstests sichern.
- MR ohne fachliche Begründung; eine falsche MR erzeugt Fehlalarme.

## 7. Prüfliste

- [ ] Properties oder MRs sind mit Anforderungsbezug formuliert.
- [ ] Generatorverteilung ist geprüft (Grenzfälle, leere Strukturen, Sonderzeichen).
- [ ] Seed und Beispielanzahl sind festgelegt.
- [ ] Minimierte Fehlerfälle sind als Regressionstests gespeichert.
- [ ] Fehlalarme sind klassifiziert und Properties korrigiert.

## 8. Beispiele

```python
from hypothesis import given, strategies as st

@given(st.lists(st.integers()))
def test_sort_invarianten(xs):
    ys = sortiere(xs)
    assert len(ys) == len(xs)
    assert sorted(xs) == ys          # Referenz
    assert all(a <= b for a, b in zip(ys, ys[1:]))
```

Metamorph, Suchfunktion: Für jede Anfrage `q` gilt `ergebnisse(q + " AND x") ⊆ ergebnisse(q)`.
Metamorph, Tarifrechner: Bei sonst gleichen Daten darf ein höheres Alter innerhalb derselben
Altersklasse den Tarif nicht ändern.
