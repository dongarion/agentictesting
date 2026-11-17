# Three Amigos, ATDD, Specification by Example, BDD

Vier Namen für eine Idee: **Anforderungen werden als konkrete Beispiele formuliert, bevor
Code entsteht, und diese Beispiele werden zu ausführbaren Tests.**

## Inhalt
1. Begriffe abgrenzen
2. Three Amigos durchführen
3. Beispiele finden und auswählen
4. Gherkin schreiben
5. Automatisierung
6. Lebende Dokumentation
7. Anti-Patterns
8. Prüfliste

## 1. Begriffe abgrenzen

| Begriff | Schwerpunkt |
| --- | --- |
| Three Amigos | Das Gespräch: Fachbereich, Entwicklung, Test klären eine Story gemeinsam |
| ATDD | Akzeptanzkriterien werden vor der Implementierung als Tests festgelegt |
| Specification by Example (Adzic) | Methode: Schlüsselbeispiele ableiten, verfeinern, automatisieren, als lebende Dokumentation pflegen |
| BDD | Sprache und Werkzeuge (Gherkin, Cucumber, SpecFlow, Behave), Fokus auf Verhalten aus Nutzersicht |

## 2. Three Amigos durchführen

- Zeitpunkt: im Refinement, bevor die Story in den Sprint kommt. 15–30 Minuten je Story.
- Teilnehmer: Product Owner oder Fachexperte, ein Entwickler, ein Tester. Weitere nach Bedarf
  (UX, Betrieb, Security).
- Ablauf:
  1. PO erzählt die Story und den Nutzen.
  2. Tester fragt nach Beispielen: „Gib mir ein konkretes Beispiel. Und eins, wo es nicht
     klappt. Und eins am Rand.“
  3. Entwickler fragt nach Technik und Abhängigkeiten.
  4. Beispiele auf Karten oder in einer Tabelle festhalten.
  5. Offene Fragen notieren; Story ist erst „ready“, wenn sie geklärt sind.
- Rolle des Testers: die Fragen stellen, die später Fehler würden. Grenzfälle, Fehlerfälle,
  Rollen, Zustände, Nebenläufigkeit, Nicht-Funktionales.

## 3. Beispiele finden und auswählen

- Heuristiken: Äquivalenzklassen und Grenzwerte (Black-Box-Skill), Zustände, Rollen,
  Zero-One-Many, Fehlerfälle, Zeitabhängigkeit.
- **Schlüsselbeispiele** auswählen: so wenige wie möglich, dass jede Regel einmal illustriert
  ist. Erschöpfende Tabellen gehören in den Testentwurf, nicht in die Spezifikation.
- Beispiele mit konkreten Werten, nicht mit Platzhaltern. „Kunde mit 3 Bestellungen über
  insgesamt 250 €“, nicht „Bestandskunde“.
- Aus Beispielen Regeln ableiten und beides festhalten: Die Regel erklärt, das Beispiel prüft.

## 4. Gherkin schreiben

```gherkin
# language: de
Funktionalität: Rabatt für Stammkunden
  Als Vertrieb möchte ich Stammkunden belohnen, damit sie wiederkommen.

  Regel: Ab der dritten Bestellung innerhalb von 12 Monaten gibt es 5 % Rabatt

    Szenario: Dritte Bestellung erhält Rabatt
      Angenommen Kundin "Meier" hat in den letzten 12 Monaten 2 Bestellungen
      Wenn sie eine Bestellung über 100,00 € aufgibt
      Dann beträgt der Rabatt 5,00 €

    Szenario: Zweite Bestellung erhält keinen Rabatt
      Angenommen Kundin "Meier" hat in den letzten 12 Monaten 1 Bestellung
      Wenn sie eine Bestellung über 100,00 € aufgibt
      Dann beträgt der Rabatt 0,00 €

    Szenariogrundriss: Bestellungen am Rand des Zeitfensters
      Angenommen Kundin "Meier" hat eine Bestellung vor <Tagen> Tagen
      Und 1 weitere Bestellung
      Wenn sie eine Bestellung über 100,00 € aufgibt
      Dann beträgt der Rabatt <Rabatt>
      Beispiele:
        | Tagen | Rabatt |
        | 364   | 5,00 € |
        | 365   | 5,00 € |
        | 366   | 0,00 € |
```

Regeln für gutes Gherkin:

- **Deklarativ**, nicht imperativ: Was passiert, nicht welche Buttons geklickt werden.
  „Wenn sie eine Bestellung aufgibt“ statt „Wenn sie auf ‚Kaufen‘ klickt und dann …“.
- Ein Verhalten je Szenario, ein `Wenn`.
- `Angenommen` beschreibt Zustand, nicht Aktionen.
- `Dann` prüft Beobachtbares aus Nutzersicht, keine Datenbankfelder.
- Fachsprache des Teams (ubiquitäre Sprache), konsistent über alle Szenarien.
- Szenariogrundriss nur, wenn die Tabelle das Verständnis verbessert; nicht als
  Datentreiber für hunderte Zeilen.

## 5. Automatisierung

- Schrittdefinitionen (Step Definitions) binden Gherkin an Code. Sie bleiben dünn und rufen
  eine Fachschicht (Fixtures, Page Objects, API-Clients) auf.
- Szenarien so weit unten wie möglich ausführen: gegen Domänenlogik oder API, nicht gegen
  die Oberfläche, wenn das Verhalten dort nicht liegt.
- Werkzeuge: Cucumber (Java, JS, Ruby), SpecFlow/Reqnroll (.NET), Behave und pytest-bdd (Python),
  Robot Framework mit Gherkin-Stil.
- Szenarien laufen in der Pipeline; rote Szenarien blockieren die Story.

## 6. Lebende Dokumentation

- Die Szenarien sind die aktuelle Spezifikation. Veraltete Szenarien werden gelöscht oder
  angepasst, nicht auskommentiert.
- Berichte (Cucumber Reports, Pickles, Serenity) für Fachbereich lesbar veröffentlichen.
- Regeln und Hintergrund in der Feature-Datei halten, nicht in einem getrennten Wiki, das
  auseinanderläuft.

## 7. Anti-Patterns

- Gherkin als Skriptsprache für UI-Tests („Klicke auf …, gib ein …“).
- Tester schreibt Szenarien allein nach dem Refinement; das Gespräch fehlt.
- Hunderte Szenariogrundriss-Zeilen; Testentwurf in der Spezifikation.
- Szenarien, die technische Details prüfen (Statuscodes, Tabellenfelder).
- Feature-Dateien, die niemand außer dem Testteam liest.

## 8. Prüfliste

- [ ] Three Amigos haben vor Sprintbeginn stattgefunden; offene Fragen sind geklärt.
- [ ] Schlüsselbeispiele decken jede Regel, Grenzfälle und Fehlerfälle ab.
- [ ] Szenarien sind deklarativ, ein Verhalten je Szenario, in Fachsprache.
- [ ] Automatisierung läuft auf der niedrigsten sinnvollen Ebene und in der Pipeline.
- [ ] Szenarien dienen als aktuelle, veröffentlichte Dokumentation.
