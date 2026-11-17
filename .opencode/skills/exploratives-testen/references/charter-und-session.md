# Charter und Session-Based Test Management (SBTM)

SBTM (Bach, 2000) gibt explorativem Testen Struktur, ohne die Freiheit zu nehmen:
**Charter** als Auftrag, **Session** als Zeitbox, **Notizen** als Nachweis, **Debriefing**
als Steuerung.

## Inhalt
1. Charter formulieren
2. Charter-Quellen
3. Session-Ablauf
4. Notizen
5. Zeitverteilung (TBS-Metrik)
6. Debriefing
7. Anti-Patterns
8. Prüfliste

## 1. Charter formulieren

Format nach Hendrickson:

> Erkunde **<Zielbereich>** mit **<Ressourcen, Techniken, Daten>**, um **<Information>** herauszufinden.

- Zielbereich: Feature, Workflow, Schnittstelle, Qualitätsmerkmal.
- Ressourcen: Heuristik, Tour, Datensatz, Werkzeug, Persona, Browser.
- Information: die Frage, die der Auftraggeber beantwortet haben will.

Gute Charters sind **spezifisch genug**, dass die Session ein Ende hat, und **offen genug**,
dass der Tester Spielraum hat. Zu eng: „Prüfe, ob der Speichern-Button funktioniert.“
Zu weit: „Teste die Anwendung.“ Passend: „Erkunde den Antragsassistenten mit der Persona
‚ungeduldiger Nutzer‘ (Doppelklicks, Zurück-Taste, Tab-Wechsel), um Zustandsverluste und
Doppelbuchungen zu finden.“

## 2. Charter-Quellen

- Risikoliste und Produktrisikoanalyse.
- Änderungen im aktuellen Build (Changelog, Merge Requests).
- Fehlerhistorie: Module mit vielen Fehlern, wiedereröffnete Fehler.
- Nutzerbeschwerden, Supporttickets, Reviews.
- Qualitätsmerkmale nach ISO 25010 je Bereich durchgehen.
- Heuristiken-Listen (siehe [heuristiken.md](heuristiken.md)).
- Fragen des Entwicklers: „Da bin ich mir nicht sicher.“
- Lücken aus der Testbasis: alles, was die Spezifikation nicht sagt.

Charters in einem Backlog führen, priorisieren, nach jeder Session ergänzen.

## 3. Session-Ablauf

| Phase | Dauer | Inhalt |
| --- | --- | --- |
| Setup | ≤ 10 % | Umgebung, Daten, Werkzeuge bereit; Charter lesen |
| Test | Hauptteil | Erkunden, beobachten, notieren |
| Fehleranalyse | bei Bedarf | Reproduzieren, isolieren, sichern. Begrenzen! |
| Abschluss | 5 min | Notizen vervollständigen, Zeitverteilung schätzen, neue Charters |

Session-Längen: kurz 45 min, normal 90 min, lang 120 min. Länger wird unkonzentriert.
Pairing (zwei Personen, eine Tastatur) erhöht Ideenvielfalt und Notizqualität.

## 4. Notizen

Echtzeit, chronologisch, stichwortartig. Je Eintrag: **Aktion → Beobachtung → Gedanke**.

```
10:12 Antrag anlegen, Pflichtfelder leer, Speichern → Fehlermeldung nennt nur erstes Feld → Nutzer muss iterieren, UX-Frage
10:15 Doppelklick auf Speichern → zwei Anträge mit gleichem Inhalt, IDs 4711/4712 → BUG-1, reproduzierbar 3/3
10:19 Opportunity: Zurück-Taste im Browser nach Speichern → Formular wieder gefüllt, erneutes Speichern möglich → Charter „Browser-Navigation“
```

Markiere: `BUG` (Befund), `?` (Frage), `IDEE` (neuer Charter), `!` (Risiko, das sofort
gemeldet werden sollte).

## 5. Zeitverteilung (TBS-Metrik)

Nach der Session schätzen, in Prozent oder Blöcken:

- **T**est: Zeit, in der getestet wurde.
- **B**ug: Zeit für Reproduktion und Fehleranalyse.
- **S**etup: Zeit für Umgebung, Daten, Blockaden.
- Zusätzlich **Opportunity**: Zeit außerhalb des Charters.

Hohe Setup-Anteile sind ein Prozessproblem. Hohe Bug-Anteile deuten auf instabile Software;
dann Sessions kürzen und Charters enger fassen.

## 6. Debriefing

Kurzgespräch (10–15 min) mit Testlead oder Auftraggeber nach jeder Session oder jedem
Sessionblock. Leitfragen (PROOF, Bach):

- **P**ast: Was ist passiert?
- **R**esults: Was wurde gefunden, erreicht?
- **O**bstacles: Was hat behindert?
- **O**utlook: Was sollte als Nächstes getan werden?
- **F**eelings: Wie fühlt sich das Produkt an? (Ernst gemeint: Unbehagen ist ein Signal.)

## 7. Anti-Patterns

- Charter nachträglich schreiben.
- Session ohne Notizen, Bericht aus dem Gedächtnis.
- Eine Stunde Fehleranalyse in der Testzeit.
- „Exploratives Testen“ als Ausrede, um Testfälle nicht zu dokumentieren.
- Befunde nur mündlich im Debriefing, nicht im Fehlermanagement.

## 8. Prüfliste

- [ ] Charter im Format Erkunde/mit/um.
- [ ] Zeitbox festgelegt und eingehalten.
- [ ] Notizen chronologisch mit Aktion, Beobachtung, Gedanke.
- [ ] TBS-Verteilung geschätzt.
- [ ] Debriefing durchgeführt, neue Charters im Backlog.
