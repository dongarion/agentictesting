# Äquivalenzklassen und Grenzwertanalyse

Beide Verfahren gehören zusammen: Äquivalenzklassen zerlegen den Wertebereich, die
Grenzwertanalyse prüft die Ränder geordneter Klassen. Wende sie gemeinsam an.

## Inhalt
1. Äquivalenzklassen bilden
2. Testfälle aus Äquivalenzklassen
3. Grenzwertanalyse
4. Typische Klassen und Grenzen
5. Anti-Patterns
6. Prüfliste
7. Beispiel

## 1. Äquivalenzklassen bilden

Eine Äquivalenzklasse ist eine Menge von Werten, für die das Testobjekt laut Spezifikation
**gleiches Verhalten** zeigt. Ein Repräsentant steht für alle.

- Bilde Klassen für **jeden** Eingabeparameter und für **jede** Ausgabe.
  Auch Ausgaben haben Klassen, zum Beispiel „Rabatt 0 %“, „Rabatt 5 %“, „Fehlermeldung“.
- Unterscheide **gültige** Klassen (spezifiziertes Normalverhalten) und **ungültige** Klassen
  (Werte, die abgewiesen oder als Fehler behandelt werden sollen).
- Die Klassen eines Parameters müssen **disjunkt** und **vollständig** sein: Jeder denkbare
  Wert gehört zu genau einer Klasse.
- Teile eine Klasse weiter auf, sobald die Spezifikation innerhalb der Klasse
  unterschiedliches Verhalten beschreibt oder ein begründeter Verdacht besteht.
- Bilde ungültige Klassen systematisch nach Kategorien:
  - außerhalb des Wertebereichs (darunter, darüber),
  - falscher Datentyp,
  - falsches Format,
  - leer, null, nicht vorhanden,
  - Sonderzeichen, Steuerzeichen, Unicode,
  - semantisch unzulässig (z. B. Enddatum vor Startdatum).

## 2. Testfälle aus Äquivalenzklassen

- **Gültige Klassen** dürfen in einem Testfall kombiniert werden. Ziel: wenige Testfälle,
  die alle gültigen Klassen mindestens einmal abdecken.
- **Ungültige Klassen** je einzeln: höchstens **eine** ungültige Klasse pro Testfall,
  alle übrigen Parameter mit gültigen Werten. Sonst maskiert ein Fehler den anderen:
  Das System weist den ersten ungültigen Wert ab, der zweite wird nie geprüft.
- Wähle Repräsentanten bewusst, typischerweise aus der Klassenmitte. Die Ränder übernimmt
  die Grenzwertanalyse.
- **Überdeckung** = abgedeckte Klassen / alle identifizierten Klassen × 100 %.
  Zählweise je Parameter und gesamt angeben.

## 3. Grenzwertanalyse

Nur für **geordnete** Klassen (Zahlen, Datum, Uhrzeit, Länge, Anzahl, Reihenfolge).

### Grenzen bestimmen

- Jede Klasse hat eine Unter- und eine Obergrenze. Bestimme beide ausdrücklich.
- Ermittle die **Schrittweite** aus der Spezifikation: ganze Zahl, Cent, Millisekunde,
  Zeichen. Fehlt sie, ist das eine offene Frage.
- Prüfe Wörter genau:
  - „bis 18“, „maximal 18“, „höchstens 18“ → 18 eingeschlossen,
  - „unter 18“, „weniger als 18“ → 18 ausgeschlossen,
  - „ab 18“, „mindestens 18“ → 18 eingeschlossen,
  - „zwischen 18 und 65“ → mehrdeutig, immer als offene Frage erfassen.
- Ergänze **implizite Grenzen**: Typgrenzen (`INT_MAX`, `Long.MIN`), maximale Feldlänge,
  Puffergrößen, Datumsgrenzen (1.1., 31.12., 29.2.), Seitengrößen bei Paging.

### Varianten (CTFL 4.0)

- **2-Wert-Grenzwertanalyse:** je Grenze der Grenzwert selbst und der nächste Wert
  in der Nachbarklasse.
- **3-Wert-Grenzwertanalyse:** je Grenze der Grenzwert und beide Nachbarn.
  Findet zusätzlich Fehler wie `==` statt `<=` oder `>=`. Bei hohem Risiko verwenden.

  **Hinweis:** Bei der 3-Wert-Analyse liegt je Grenze ein Nachbar in derselben Klasse wie
  der Grenzwert und einer in der benachbarten Klasse (zur Grenze 0: 1 in der Klasse 0–17,
  −1 in der ungültigen Klasse < 0). Die erwartete Reaktion auf jeden Nachbarn muss
  spezifiziert sein; ist sie es nicht, ist das eine offene Frage, kein geratener Erwartungswert.

  Beispiel Tarifalter (Klassen 0–17 / 18–64 / 65–120): 2-Wert testet −1, 0, 17, 18, 64, 65,
  120, 121. 3-Wert testet zusätzlich die Nachbarn innerhalb der Klassen 1, 16, 19, 63, 66, 119.
  Eine fehlerhafte Bedingung `alter == 65` statt `alter >= 65` besteht an dieser Grenze die
  2-Wert-Werte 64 und 65; erst 66 deckt sie auf. Ein `>` statt `>=` an der Grenze 18 (Wert 18
  fälschlich als Kind eingestuft) fällt dagegen schon bei 2-Wert auf, weil 18 selbst getestet wird.
- **Überdeckung** = getestete Grenzwerte / alle identifizierten Grenzwerte × 100 %,
  getrennt nach Variante.

## 4. Typische Klassen und Grenzen

| Datentyp | Klassen und Grenzen, an die man denken muss |
| --- | --- |
| Ganze Zahl | 0, negativ, Typgrenzen, führende Nullen, Vorzeichen |
| Dezimalzahl | Rundung, Nachkommastellen, Dezimaltrennzeichen nach Locale, Tausenderpunkt, wissenschaftliche Notation |
| Geldbetrag | Cent-Schrittweite, negative Beträge, Währung, kaufmännisches gegenüber mathematischem Runden |
| Text | leer, nur Leerzeichen, führende/folgende Leerzeichen, Min-/Maxlänge, Umlaute, Unicode-Normalisierung, Emoji, Steuerzeichen |
| Datum | Schaltjahr, Monatsende, Jahreswechsel, Format, ungültiges Datum (31.4.), Vergangenheit/Zukunft |
| Uhrzeit | Mitternacht, 23:59:59, Sommerzeitwechsel, Zeitzonen |
| Liste/Menge | leer, ein Element, Maximum, Maximum + 1, Duplikate, Reihenfolge |
| Datei | 0 Byte, Maximalgröße, falscher Typ bei passender Endung, Dateiname mit Sonderzeichen |
| Boolesch / Auswahl | jeder Wert, nicht gesetzt, unbekannter Wert über API |

## 5. Anti-Patterns

- Nur gültige Klassen testen.
- Mehrere ungültige Werte in einem Testfall.
- Grenzen aus Annahme statt aus Spezifikation („wird schon inklusive sein“).
- Ausgabeklassen vergessen.
- Grenzwertanalyse auf ungeordnete Klassen anwenden (z. B. Farben).
- Repräsentant aus der Klasse wählen, der zufällig auch eine Grenze ist, und dann die
  Grenze als „abgedeckt“ zählen, ohne das zu dokumentieren.

## 6. Prüfliste

- [ ] Für jeden Parameter und jede Ausgabe sind Klassen gebildet.
- [ ] Klassen sind disjunkt und vollständig.
- [ ] Jede ungültige Kategorie ist geprüft (Bereich, Typ, Format, leer/null, Zeichen, Semantik).
- [ ] Kein Testfall enthält mehr als eine ungültige Klasse.
- [ ] Jede Grenze hat Wert und Schrittweite aus der Spezifikation oder eine offene Frage.
- [ ] Implizite Grenzen (Typ, Länge, Datum) sind ergänzt.
- [ ] Variante (2- oder 3-Wert) ist gewählt und begründet.
- [ ] Überdeckung ist je Verfahren angegeben.

## 7. Beispiel

Anforderung: „Der Tarif richtet sich nach dem Alter in ganzen Jahren: Kind 0 bis 17,
Erwachsener 18 bis 64, Senior ab 65. Zulässig sind Werte bis 120.“

| ID | Klasse | gültig | Repräsentant |
| --- | --- | --- | --- |
| ÄK1 | 0–17 → Kind | ja | 9 |
| ÄK2 | 18–64 → Erwachsener | ja | 40 |
| ÄK3 | 65–120 → Senior | ja | 80 |
| ÄK4 | < 0 | nein | −5 |
| ÄK5 | > 120 | nein | 150 |
| ÄK6 | keine ganze Zahl | nein | 17,5 |
| ÄK7 | leer bzw. null | nein | (leer) |
| ÄK8 | keine Zahl | nein | „abc“ |

Grenzwerte, 2-Wert: −1, 0, 17, 18, 64, 65, 120, 121 (8 Werte).
Grenzwerte, 3-Wert: zusätzlich 1, 16, 19, 63, 66, 119.

Offene Fragen:
- Welche Fehlerreaktion gilt für ÄK4 bis ÄK8? Ohne Antwort sind die erwarteten Ergebnisse
  nicht belegbar.
- Wird 17,0 als ganze Zahl akzeptiert?
