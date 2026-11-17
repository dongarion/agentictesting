# Kontrollflussbasierte Verfahren

Anweisungs-, Zweig- und Pfadüberdeckung. Grundlage ist der **Kontrollflussgraph**.

## Inhalt
1. Kontrollflussgraph aufstellen
2. Anweisungsüberdeckung
3. Zweig- und Entscheidungsüberdeckung
4. Pfadüberdeckung und Basispfade
5. Schleifen
6. Anti-Patterns
7. Prüfliste
8. Beispiel

## 1. Kontrollflussgraph aufstellen

- Knoten = Anweisung oder Block sequentieller Anweisungen, Kanten = möglicher Kontrollfluss.
- Entscheidungen (`if`, `switch`, Schleifenköpfe, `?:`, kurzschließende `&&`/`||`,
  `try/catch`, frühe `return`) erzeugen Verzweigungen. Jede davon einzeichnen.
- Implizite Zweige nicht vergessen: `if` ohne `else` hat trotzdem zwei Kanten, `switch` ohne
  `default` hat einen impliziten Durchfall, jede Exception ist eine Kante.
- Zyklomatische Komplexität `V(G) = Kanten − Knoten + 2` berechnen. Sie ist die Obergrenze
  der benötigten Basispfade und ein Indikator für Testaufwand.
- Darstellung als Mermaid `flowchart TD`.

## 2. Anweisungsüberdeckung

- Jede ausführbare Anweisung mindestens einmal.
- Maß: ausgeführte Anweisungen / ausführbare Anweisungen × 100 %.
- Schwaches Kriterium: `if (x) y = 1;` ist mit `x = true` zu 100 % abgedeckt, der Fall
  `x = false` wurde nie geprüft. Nur als Einstieg oder bei sehr niedrigem Risiko ausreichend.

## 3. Zweig- und Entscheidungsüberdeckung

- Jede Kante des Graphen (Zweig) mindestens einmal, also jede Entscheidung mindestens einmal
  wahr und einmal falsch.
- Maß: durchlaufene Zweige / alle Zweige × 100 %.
- Zweigüberdeckung schließt Anweisungsüberdeckung ein, nicht umgekehrt.
- Bei `switch`: jeder `case` und der `default`, auch der implizite.
- Bei Schleifen: Schleifenkörper betreten und Schleife ohne Betreten überspringen.
- CTFL 4.0 verwendet „Zweigüberdeckung“; manche Werkzeuge melden „Decision Coverage“ oder
  „Branch Coverage“ mit leicht abweichender Zählung. Zählweise des Werkzeugs dokumentieren.

## 4. Pfadüberdeckung und Basispfade

- **Vollständige Pfadüberdeckung:** jeder mögliche Pfad vom Start- zum Endknoten. Bei Schleifen
  praktisch unendlich, daher nur für kleine, kritische Einheiten ohne Schleifen oder mit
  begrenzter Iteration.
- **Basispfadtest (McCabe):** `V(G)` linear unabhängige Pfade, aus denen sich alle anderen
  zusammensetzen lassen. Vorgehen:
  1. Einen Hauptpfad wählen.
  2. Je weiteren Pfad genau eine Entscheidung gegenüber einem bereits gewählten Pfad umkehren.
  3. Bis `V(G)` Pfade erreicht sind.
- Prüfe jeden Pfad auf **Erfüllbarkeit**: Manche Pfade sind durch abhängige Bedingungen
  unmöglich. Unerfüllbare Pfade dokumentieren, nicht weglassen.

## 5. Schleifen

Je Schleife mindestens:

- 0 Durchläufe (Schleife wird übersprungen),
- 1 Durchlauf,
- typische Anzahl,
- Maximum und Maximum − 1 (wenn begrenzt),
- bei verschachtelten Schleifen: innere Schleife zuerst variieren, äußere auf Minimum halten,
  dann umgekehrt.

## 6. Anti-Patterns

- Überdeckung durch Tests ohne Assertions „erzeugen“.
- `if` ohne `else` als eine Kante zählen.
- Exception-Pfade und Fehlerbehandlung ignorieren, weil „schwer zu provozieren“.
- Kurzschlussauswertung übersehen: `a && b` enthält einen Zweig, in dem `b` nie ausgewertet wird.
- Zyklomatische Komplexität als alleiniges Qualitätsmaß verwenden.

## 7. Prüfliste

- [ ] Kontrollflussgraph mit allen impliziten Zweigen und Exception-Kanten liegt vor.
- [ ] `V(G)` ist berechnet.
- [ ] Jede Entscheidung ist mindestens einmal wahr und einmal falsch getestet.
- [ ] Jede Schleife ist mit 0, 1, typisch und Maximum getestet.
- [ ] Unerfüllbare Pfade sind dokumentiert.
- [ ] Jeder Testfall prüft ein Ergebnis, nicht nur die Ausführung.

## 8. Beispiel

```python
def rabatt(betrag, kunde):
    r = 0
    if betrag > 100:
        r = 5
    if kunde.premium:
        r += 10
    return betrag * (100 - r) / 100
```

Graph: 2 Entscheidungen, `V(G) = 3`. Zweigüberdeckung braucht 2 Testfälle
(`betrag > 100 ∧ premium`, `betrag ≤ 100 ∧ ¬premium`). Pfadüberdeckung braucht 4
(alle Kombinationen). Grenzwert 100 gegenüber 101 kommt aus der Black-Box-Analyse und muss
zusätzlich gegen die Spezifikation geprüft werden: Ist „über 100“ hier richtig umgesetzt?
