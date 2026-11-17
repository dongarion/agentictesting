# Synthetische Testdaten

Künstlich erzeugte Daten ohne Bezug zu realen Personen. **Erste Wahl** für die meisten
Teststufen, weil datenschutzfrei, beliebig skalierbar und auf Testziele zuschneidbar.

## Inhalt
1. Anforderungen an synthetische Daten
2. Erzeugungsansätze
3. Realismus herstellen
4. Gezielte Konstellationen
5. Volumen für Last und Migration
6. KI-generierte Daten
7. Werkzeuge
8. Anti-Patterns
9. Prüfliste

## 1. Anforderungen an synthetische Daten

- **Formatgültig:** Prüfziffern, Längen, Zeichensätze, Datumsformate entsprechen der Spezifikation.
- **Fachlich konsistent:** Geburtsdatum vor Vertragsbeginn, Summe gleich Positionen, Status
  passt zur Historie.
- **Referenziell intakt:** Fremdschlüssel zeigen auf existierende Datensätze.
- **Verteilt wie nötig:** Für Funktionstests reicht Abdeckung der Klassen; für Last- und
  Performancetests müssen Mengen und Verteilungen der Produktion ähneln.
- **Reproduzierbar:** Seed und Generatorversion festgehalten.
- **Erkennbar als Testdaten:** Namensschema (`TEST-`), reservierte Nummernkreise,
  Testdomänen (`example.org`), damit sie nie mit echten Daten verwechselt werden.
- **Frei von Personenbezug:** Keine echten Namen aus Mitarbeiterlisten, keine echten Adressen
  mit echten Bewohnern, keine echten Telefonnummern.

## 2. Erzeugungsansätze

| Ansatz | Beschreibung | Eignung |
| --- | --- | --- |
| Regelbasiert | Generator folgt Schema, Constraints, Wertelisten | Standard, volle Kontrolle |
| Kombinatorisch | Klassifikationsbaum, paarweise Kombination der Attribute | Abdeckung von Konstellationen |
| Grammatikbasiert | Aus EBNF/Schema (JSON Schema, XSD) | Nachrichten, Dateien, Payloads |
| Property-based | Strategien in Hypothesis, fast-check | Direkt im Testcode |
| Statistisch | Verteilungen aus Produktion gelernt, Werte neu gezogen | Last, Performance, Analytik; Korrelationen prüfen |
| Modellbasiert (ML, GAN, LLM) | Modell erzeugt realistische Datensätze | Freitexte, komplexe Korrelationen; Risiko von Memorierung |
| Über die Anwendung | Daten per API oder GUI erzeugen | Fachlich garantiert gültig, langsam |

## 3. Realismus herstellen

- Wertelisten aus öffentlichen oder lizenzfreien Quellen: Vornamen- und Nachnamenlisten,
  Straßennamen ohne Hausnummernbezug, PLZ-Verzeichnis, Länder, Berufe.
- Verteilungen aus Produktion ableiten (Häufigkeiten, Altersverteilung, Auftragsgrößen) und als
  Parameter nutzen; dabei nur Aggregate übernehmen, keine Einzelwerte.
- Korrelationen abbilden: Alter und Tarif, Region und Sprache, Produkt und Preis.
- Zeitliche Muster: Saisonalität, Stoßzeiten, Historienlängen.
- Unordnung einbauen: Tippfehler, abweichende Schreibweisen, Leerzeichen, alte Datensätze
  mit fehlenden Feldern; Produktion ist nicht sauber.

## 4. Gezielte Konstellationen

Synthese erlaubt, was Produktion selten liefert:

- Grenzwerte aller Klassen (Black-Box-Skill).
- Seltene Kombinationen (Kunde mit allen Produkten, Antrag mit maximaler Anzahl Anhänge).
- Fehlerhafte Datensätze zur Prüfung der Robustheit (Importe, Migration).
- Zukunfts- und Vergangenheitsdaten (Verträge, die in 10 Jahren ablaufen; Datensätze von vor
  dem letzten Schemawechsel).
- Mehrsprachige und Unicode-Daten (Namen mit Diakritika, RTL-Schrift, Emoji).

Konstellationen benennen und als Builder oder Generatorprofil ablegen.

## 5. Volumen für Last und Migration

- Zielmengen aus Produktion plus Wachstum (z. B. 2 Jahre).
- Kardinalitäten je Beziehung realistisch (Kunden je Verträge, Positionen je Auftrag).
- Indizes und Statistiken nach dem Laden aktualisieren, sonst misst der Lasttest den falschen Ausführungsplan.
- Erzeugung direkt in der Datenbank (Bulk Load) statt über die Anwendung.
- Verteilung über Zeit, damit Abfragen auf Zeiträume realistisch sind.

## 6. KI-generierte Daten

- LLMs liefern plausible Freitexte, Namen, Adressen, Fallbeschreibungen, Dokumente.
- Risiken: Memorierung realer Daten aus dem Training (reale Personen, Adressen), Verzerrung,
  Inkonsistenz zwischen Feldern, Nichtdeterminismus.
- Regeln: Ausgabe gegen Schema und Constraints validieren, Personenbezug prüfen (Namen gegen
  bekannte Personen, Adressen gegen Realität), Seed/Temperatur fixieren, Ergebnis als Datei
  versionieren statt je Lauf neu zu generieren.
- Im Behörden- und Ü2-Umfeld: nur lokale Modelle, keine Schemainformationen an externe Dienste.

## 7. Werkzeuge

| Werkzeug | Hinweis |
| --- | --- |
| Faker (Python, PHP, Ruby, JS: faker-js), Bogus (.NET), Java Faker/Datafaker | Lokalisierte Wertelisten, Basis für eigene Generatoren |
| Hypothesis, fast-check, jqwik | Property-based, direkt im Test |
| Mockaroo, generatedata.com | Schnelle Tabellen per Oberfläche; keine vertraulichen Schemata hochladen |
| Synthetic Data Vault (SDV), Gretel, Tonic, MOSTLY AI | Statistisch/ML-basiert aus Produktionsverteilungen |
| JSON Schema Faker, XSD-Generatoren | Nachrichten aus Schema |
| dbt seeds, Liquibase/Flyway Changesets, SQL-Skripte | Versionierte Bereitstellung |
| Testcontainers mit Init-Skripten | Daten je Lauf |

## 8. Anti-Patterns

- „Max Mustermann“ in jedem Datensatz; Sortierung, Suche und Duplikaterkennung bleiben ungetestet.
- Nur saubere, gültige Daten; Robustheit ungetestet.
- Echte Namen aus dem Team oder Adressen echter Personen als „Testdaten“.
- Generator ohne Seed; Fehler nicht reproduzierbar.
- Lasttest mit 1.000 Datensätzen bei 10 Millionen in Produktion.
- Freitexte per LLM ohne Prüfung auf echten Personenbezug.

## 9. Prüfliste

- [ ] Daten sind formatgültig, fachlich konsistent und referenziell intakt (automatisch geprüft).
- [ ] Testdaten sind als solche erkennbar (Schema, Nummernkreis, Domäne).
- [ ] Kein Personenbezug; Wertelisten sind unbedenklich.
- [ ] Konstellationen für Grenzfälle und Fehlerfälle sind enthalten und benannt.
- [ ] Verteilung und Volumen passen zum Testziel.
- [ ] Seed, Generatorversion und Profil sind versioniert.
