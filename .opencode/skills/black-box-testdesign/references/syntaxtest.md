# Syntaxtest

Für Eingaben mit **formal definiertem Aufbau**: Kennungen (IBAN, Aktenzeichen, Steuer-ID),
Dateiformate, Nachrichtenformate (XML, JSON, EDIFACT), Kommandos, Abfragesprachen,
Protokollnachrichten, API-Payloads gegen ein Schema.

## Inhalt
1. Grammatik aufstellen
2. Gültige Testfälle
3. Ungültige Testfälle durch Mutation
4. Bezug zu Fuzzing und Schema-Validierung
5. Anti-Patterns
6. Prüfliste
7. Beispiel

## 1. Grammatik aufstellen

- Formuliere die Syntax formal: BNF/EBNF, regulärer Ausdruck, JSON Schema, XSD oder OpenAPI.
- Steht nur Prosa zur Verfügung, leite die Grammatik ab und kennzeichne sie als rekonstruiert.
- Trenne **Syntax** (Aufbau) von **Semantik** (Bedeutung, z. B. Prüfziffer, Existenz eines
  Aktenzeichens). Semantische Regeln mit
  [aequivalenzklassen-grenzwerte.md](aequivalenzklassen-grenzwerte.md) oder
  [entscheidungstabellen.md](entscheidungstabellen.md) testen.
- Erfasse Mehrdeutigkeiten der Grammatik als offene Fragen: Groß-/Kleinschreibung,
  Leerzeichen, Trennzeichen, Zeichensatz, optionale Elemente.

## 2. Gültige Testfälle

- Jede Regel (jedes Nichtterminal) mindestens einmal.
- Jede Alternative einer Regel mindestens einmal.
- Optionale Elemente: vorhanden und nicht vorhanden.
- Wiederholungen: minimale, typische und maximale Anzahl.

## 3. Ungültige Testfälle durch Mutation

Je Testfall genau **eine** Mutation an einer gültigen Eingabe:

| Mutation | Beispiel |
| --- | --- |
| Element weglassen | Pflichtfeld oder Trennzeichen fehlt |
| Element verdoppeln | Trennzeichen doppelt, Feld zweimal |
| Element vertauschen | Reihenfolge zweier Teile |
| Falsches Zeichen | Buchstabe statt Ziffer, Sonderzeichen, Steuerzeichen |
| Länge unterschreiten | ein Zeichen zu wenig |
| Länge überschreiten | ein Zeichen zu viel, extrem lang |
| Falscher Zeichensatz | Umlaut, Unicode-Lookalike, Nullbyte |
| Leer | leere Zeichenkette, nur Leerzeichen |
| Strukturbruch | ungeschlossene Klammer, ungültiges JSON, falsche Verschachtelung |

Prüfe je Mutation die **spezifizierte Fehlerreaktion**. Fehlt sie, ist das eine offene Frage.
Bei sicherheitsrelevanten Eingaben die Ergebnisse an das Security-Testing weitergeben
(Injection, Puffergrenzen).

## 4. Bezug zu Fuzzing und Schema-Validierung

- Syntaxtest ist systematisch und deterministisch: ausgewählte Mutationen mit bekanntem
  erwarteten Ergebnis.
- Grammatikbasiertes Fuzzing erzeugt große Mengen zufälliger Mutationen und sucht nach
  Abstürzen. Es ergänzt den Syntaxtest, ersetzt ihn aber nicht.
- Liegt ein maschinenlesbares Schema vor, können gültige und ungültige Payloads daraus
  generiert werden (z. B. Schemathesis für OpenAPI). Prüfe auch hier jedes Ergebnis gegen die
  Spezifikation.

## 5. Anti-Patterns

- Nur gültige Eingaben testen.
- Mehrere Mutationen in einem Testfall.
- Syntax und Semantik vermischen (eine syntaktisch korrekte IBAN mit falscher Prüfziffer ist
  ein semantischer Fall).
- Grammatik aus der Implementierung ableiten statt aus der Spezifikation.

## 6. Prüfliste

- [ ] Die Grammatik ist formal notiert und ihre Quelle angegeben.
- [ ] Jede Regel und jede Alternative ist gültig getestet.
- [ ] Optionale Elemente und Wiederholungsgrenzen sind getestet.
- [ ] Jede Mutationsart ist einzeln angewendet.
- [ ] Je Mutation ist die erwartete Fehlerreaktion belegt oder als offene Frage erfasst.
- [ ] Semantische Regeln sind an das passende Verfahren übergeben.

## 7. Beispiel

Spezifikation: „Das Aktenzeichen besteht aus zwei Großbuchstaben, einem Bindestrich, vier Ziffern
für das Jahr, einem Schrägstrich und einer fünfstelligen laufenden Nummer.“

Grammatik: `^[A-Z]{2}-[0-9]{4}/[0-9]{5}$`, gültiges Beispiel `AB-2026/00042`.

| TF | Mutation | Eingabe | Erwartet |
| --- | --- | --- | --- |
| S1 | gültig | AB-2026/00042 | akzeptiert |
| S2 | Bindestrich fehlt | AB2026/00042 | abgewiesen |
| S3 | Kleinbuchstabe | Ab-2026/00042 | ? |
| S4 | Nummer zu kurz | AB-2026/0042 | abgewiesen |
| S5 | Nummer zu lang | AB-2026/000042 | abgewiesen |
| S6 | Umlaut | ÄB-2026/00042 | abgewiesen |
| S7 | Leerzeichen am Ende | „AB-2026/00042 “ | ? |

Offene Fragen:
- Werden Kleinbuchstaben automatisch umgewandelt (S3)?
- Werden führende und folgende Leerzeichen entfernt (S7)?
- Muss das Jahr plausibel sein (semantisch, z. B. nicht 0000 oder 9999)?
