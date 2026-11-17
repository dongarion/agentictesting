# Datenflusstest

Verfolgt den **Lebenszyklus von Variablen**: wo ein Wert gesetzt (Definition), wo er gelesen
(Verwendung) und wo er ungültig wird. Findet Fehler, die Kontrollflusstests übersehen:
nicht initialisierte Werte, überschriebene Werte ohne Verwendung, Nebenwirkungen über Aufrufe.

## Inhalt
1. Begriffe
2. Statische Anomalien
3. Überdeckungskriterien
4. Vorgehen
5. Anti-Patterns
6. Prüfliste
7. Beispiel

## 1. Begriffe

- **def** (Definition): Variable erhält einen Wert (Zuweisung, Parameterübergabe, Einlesen).
- **use** (Verwendung):
  - **c-use** (computational): Wert fließt in eine Berechnung oder Ausgabe,
  - **p-use** (predicate): Wert steuert eine Entscheidung.
- **kill / undefine**: Variable verlässt den Gültigkeitsbereich oder wird freigegeben.
- **def-use-Paar (du-Paar):** Definition und eine Verwendung, zwischen denen ein
  definitionsfreier Pfad liegt (die Variable wird dazwischen nicht neu gesetzt).

## 2. Statische Anomalien

Vor dem Test den Code auf Anomalien prüfen. Sie sind Befunde ohne Testausführung:

| Muster | Bedeutung |
| --- | --- |
| ur (undefined → referenced) | Verwendung ohne vorherige Definition |
| dd (defined → defined) | Doppelte Definition ohne Verwendung dazwischen, oft vergessene Logik |
| du (defined → undefined) | Definition ohne Verwendung, toter Code oder vergessene Nutzung |

Statische Analysewerkzeuge finden die meisten davon. Ergebnisse übernehmen und bewerten.

## 3. Überdeckungskriterien

Aufsteigend in Strenge:

| Kriterium | Forderung |
| --- | --- |
| all-defs | Jede Definition erreicht mindestens eine Verwendung |
| all-c-uses | Jede Definition erreicht jede ihrer Berechnungsverwendungen |
| all-p-uses | Jede Definition erreicht jede ihrer Entscheidungsverwendungen |
| **all-uses** | Jede Definition erreicht jede ihrer Verwendungen (Standardziel) |
| all-du-paths | Jeder definitionsfreie Pfad je du-Paar (bei Schleifen begrenzen) |

Maß: abgedeckte du-Paare / alle du-Paare × 100 %.

## 4. Vorgehen

1. Variablen auswählen: Zustandsvariablen, Parameter, Rückgabewerte, globale und geteilte
   Variablen, Ressourcen-Handles. Lokale Hilfsvariablen nur bei Bedarf.
2. Je Variable alle def- und use-Stellen mit Zeilennummer tabellieren.
3. du-Paare bilden, definitionsfreie Pfade prüfen.
4. Je du-Paar einen Testfall, der genau diesen Pfad erzwingt, mit Assertion auf den
   verwendeten Wert.
5. Besonderes Augenmerk:
   - Definitionen in Ausnahme- oder Fehlerpfaden,
   - Variablen, die über mehrere Methoden oder Threads geteilt werden,
   - Ressourcen (Dateien, Verbindungen): öffnen = def, schließen = kill. Jeder Pfad muss zum
     kill führen.

## 5. Anti-Patterns

- Nur lokale Variablen betrachten und Zustands- oder Objektattribute ignorieren.
- du-Paare zählen, aber den Wert an der Verwendungsstelle nicht prüfen.
- Statische Anomalien als „Werkzeugrauschen“ abtun.

## 6. Prüfliste

- [ ] Relevante Variablen sind ausgewählt und begründet.
- [ ] def/use-Tabelle je Variable mit Zeilennummern liegt vor.
- [ ] Statische Anomalien (ur, dd, du) sind geprüft und als Befunde erfasst.
- [ ] Kriterium ist gewählt, du-Paare sind vollständig aufgelistet.
- [ ] Jeder Testfall prüft den Wert an der Verwendungsstelle.
- [ ] Ressourcenpfade enden in Freigabe.

## 7. Beispiel

```python
def mittelwert(werte):
    summe = 0                 # def summe
    anzahl = 0                # def anzahl
    for w in werte:           # p-use werte
        summe += w            # c-use/def summe
        anzahl += 1           # c-use/def anzahl
    if anzahl > 0:            # p-use anzahl
        ergebnis = summe / anzahl   # c-use summe, anzahl; def ergebnis
    return ergebnis           # c-use ergebnis
```

Befund: `ergebnis` hat einen **ur-Pfad** (leere Liste → `anzahl == 0` → `return ergebnis`
ohne Definition). Testfall: `werte = []`, erwartetes Ergebnis laut Spezifikation klären
(0, `None`, Fehler?). Offene Frage, bis die Spezifikation es sagt.
