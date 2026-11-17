# Klassifikationsbaum und paarweises Testen

Für Testobjekte mit **vielen Parametern**, deren vollständige Kombination nicht testbar ist:
Formulare, Konfigurationen, Browser-/Gerätematrizen, API-Parameter, Tarifrechner.

## Inhalt
1. Klassifikationsbaum aufbauen
2. Kombinationskriterien
3. Paarweises Testen
4. Constraints
5. Werkzeuge
6. Anti-Patterns
7. Prüfliste
8. Beispiel

## 1. Klassifikationsbaum aufbauen

1. **Wurzel:** das Testobjekt oder der Testaspekt.
2. **Klassifikationen:** testrelevante Aspekte (Parameter, Umgebungsmerkmale, Benutzertypen).
3. **Klassen:** disjunkte und vollständige Werte je Klassifikation. Leite sie mit
   [aequivalenzklassen-grenzwerte.md](aequivalenzklassen-grenzwerte.md) ab, nicht frei.
4. Klassen dürfen weiter verfeinert werden (Unterklassifikationen), wenn sich das Verhalten
   innerhalb einer Klasse unterscheidet.
5. Darstellung: Baum als Mermaid-`mindmap` oder eingerückte Liste, darunter die
   **Kombinationstabelle**: Zeilen = Testfälle, Spalten = Klassen, `X` = Klasse gewählt.

## 2. Kombinationskriterien

| Kriterium | Bedeutung | Anzahl Testfälle |
| --- | --- | --- |
| Minimal | Jede Klasse kommt mindestens einmal vor | = Anzahl Klassen der größten Klassifikation |
| Paarweise | Jedes Klassenpaar zweier Klassifikationen kommt mindestens einmal vor | wächst etwa mit dem Produkt der beiden größten Klassifikationen |
| n-fach | Jede Kombination von n Klassifikationen kommt vor | steigt stark mit n |
| Vollständig | Alle Kombinationen | Produkt aller Klassenanzahlen |

Wähle nach Risiko und nenne das Kriterium. Erfahrungswerte aus der Literatur zeigen, dass ein
großer Teil der Fehler durch einzelne Parameter oder Paare ausgelöst wird. Das ist eine
Faustregel, kein Beweis für dein System.

## 3. Paarweises Testen

- Parameter und Werte stammen aus dem Klassifikationsbaum oder den Äquivalenzklassen.
- Ungültige Werte gehören **nicht** in die paarweise Kombination. Teste sie getrennt, je
  einzeln, sonst maskieren sie sich gegenseitig.
- Erzeuge die Kombinationen mit einem Werkzeug, nicht von Hand.
- **Ohne ausführbares Werkzeug:** Paarweise Mengen im Zweifel algorithmisch selbst erzeugen und
  die Paarüberdeckung rechnerisch nachweisen. Vorgehen (Greedy, Prinzip von AETG/IPOG):
  1. Alle zulässigen Wertepaare je Parameterpaar auflisten (Constraints anwenden).
  2. Aus allen zulässigen Vollkombinationen wiederholt diejenige wählen, die die meisten noch
     nicht abgedeckten Paare enthält; abgedeckte Paare streichen.
  3. Wiederholen, bis kein Paar offen ist.
  4. Nachweis als Zählung je Parameterpaar: abgedeckt / zulässig (muss überall gleich sein).
  Kann der Agent Code ausführen, rechnet er das mit einem kurzen Skript; sonst schrittweise in
  einer Tabelle. Das Ergebnis ist nicht zwingend minimal, aber nachweislich vollständig.
- **Prüfe das Ergebnis:** Ist jedes zulässige Wertepaar mindestens einmal enthalten?
  Werkzeuge mit Zufallsanteil liefern bei jedem Lauf andere Mengen. Fixiere den Seed
  oder versioniere die erzeugte Menge.
- Ergänze fachlich wichtige Kombinationen (Hauptszenarien) ausdrücklich als Seed-Zeilen.
- Erhöhe bei hohem Risiko auf 3-fach-Kombinationen für die kritischen Parameter
  (gemischte Stärke, falls das Werkzeug das kann).

## 4. Constraints

- Formuliere ausgeschlossene Kombinationen explizit, z. B.
  `IF [Betriebssystem] = "iOS" THEN [Browser] <> "Edge";`.
- Jeder Constraint braucht eine Quelle (Spezifikation, Plattformbeschränkung).
  Ein Constraint ohne Quelle ist eine Annahme.
- Prüfe, ob Constraints Klassen unerreichbar machen. Eine unerreichbare Klasse ist ein Befund.

## 5. Werkzeuge

| Werkzeug | Hinweis |
| --- | --- |
| PICT (Microsoft) | Kommandozeile, Constraints, gemischte Stärke, Seeds, Gewichtung |
| ACTS (NIST) | Java-GUI und CLI, n-fach bis Stärke 6 |
| allpairspy | Python-Bibliothek, einfach in Testcode einzubinden |
| TESTONA / CTE XL | Klassifikationsbaumeditoren mit Kombinationsgenerierung |

## 6. Anti-Patterns

- Werte frei erfinden statt aus Äquivalenzklassen ableiten.
- Ungültige Werte in die paarweise Generierung aufnehmen.
- Erzeugte Menge nicht auf Paarüberdeckung prüfen.
- Constraints vergessen, sodass unmögliche Testfälle entstehen.
- Paarweise testen und daraus schließen, das System sei „vollständig“ getestet.

## 7. Prüfliste

- [ ] Klassen je Klassifikation sind disjunkt, vollständig und aus der Spezifikation abgeleitet.
- [ ] Kombinationskriterium ist gewählt und begründet.
- [ ] Ungültige Werte sind getrennt und einzeln getestet.
- [ ] Constraints sind mit Quelle formuliert.
- [ ] Die Paarüberdeckung der erzeugten Menge ist rechnerisch nachgewiesen (abgedeckt / zulässig je Parameterpaar).
- [ ] Seed oder Ergebnismenge ist versioniert.

## 8. Beispiel

Parameter eines Antragsformulars:

| Parameter | Werte |
| --- | --- |
| Antragsart | Neu, Verlängerung, Änderung |
| Antragsteller | Privatperson, Unternehmen |
| Kanal | Web, Mobil, Papier |
| Anhang | keiner, PDF, Bild |

Vollständig: 3 × 2 × 3 × 3 = 54 Kombinationen, davon 42 zulässig (der Constraint unten schließt
Papier mit PDF oder Bild aus). Paarweise: mindestens 9 (Produkt der beiden größten
Klassifikationen).

Mit dem Greedy-Verfahren aus Abschnitt 3 erzeugt (11 Testfälle):

| TF | Antragsart | Antragsteller | Kanal | Anhang |
| --- | --- | --- | --- | --- |
| 1 | Neu | Privatperson | Web | keiner |
| 2 | Neu | Unternehmen | Mobil | PDF |
| 3 | Verlängerung | Privatperson | Mobil | Bild |
| 4 | Verlängerung | Unternehmen | Papier | keiner |
| 5 | Änderung | Unternehmen | Web | Bild |
| 6 | Verlängerung | Privatperson | Web | PDF |
| 7 | Änderung | Privatperson | Mobil | keiner |
| 8 | Neu | Privatperson | Papier | keiner |
| 9 | Neu | Privatperson | Web | Bild |
| 10 | Änderung | Privatperson | Web | PDF |
| 11 | Änderung | Privatperson | Papier | keiner |

Nachweis der Paarüberdeckung:

| Parameterpaar | abgedeckt / zulässig |
| --- | --- |
| Antragsart × Antragsteller | 6 / 6 |
| Antragsart × Kanal | 9 / 9 |
| Antragsart × Anhang | 9 / 9 |
| Antragsteller × Kanal | 6 / 6 |
| Antragsteller × Anhang | 6 / 6 |
| Kanal × Anhang | 7 / 7 (Papier nur mit „keiner“) |
| **Gesamt** | **43 / 43** |

PICT-Modell (wenn das Werkzeug verfügbar ist):

```
Antragsart:    Neu, Verlängerung, Änderung
Antragsteller: Privatperson, Unternehmen
Kanal:         Web, Mobil, Papier
Anhang:        keiner, PDF, Bild

IF [Kanal] = "Papier" THEN [Anhang] = "keiner";
```

Offene Frage: Ist der Constraint für den Papierkanal korrekt, oder werden Anhänge dort
nachträglich eingescannt?
