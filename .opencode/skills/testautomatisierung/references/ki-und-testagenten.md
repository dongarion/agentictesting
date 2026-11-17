# KI-gestützte Automatisierung und Testagenten

KI verändert, **wer** Tests schreibt, **wie** sie entstehen und **wie** sie sich an
Änderungen anpassen. Sie ändert nicht, was einen guten Test ausmacht: klares Orakel,
Reproduzierbarkeit, Wartbarkeit, Nachvollziehbarkeit.

## Inhalt
1. Einsatzstufen
2. Self-Healing und robuste Selektoren
3. Testgenerierung mit LLMs
4. Testagenten (Agentic Testing)
5. Risiken und Leitplanken
6. Bewertung von KI-Werkzeugen
7. Prüfliste

## 1. Einsatzstufen

| Stufe | Was die KI tut | Mensch |
| --- | --- | --- |
| Assistenz | Code vervollständigen, Testideen vorschlagen, Testdaten erzeugen, Fehlschläge zusammenfassen | entscheidet und schreibt |
| Generierung | Testfälle aus Anforderungen, Gherkin aus Stories, Unit-Tests aus Code, Page Objects aus DOM | prüft und übernimmt |
| Anpassung | Selektoren heilen, Tests nach UI-Änderung anpassen, Flaky-Ursachen vorschlagen | genehmigt Änderungen |
| Agenten | Explorieren, Charters ausführen, Fehler melden, Tests schreiben und einchecken, Pipelines beobachten | setzt Ziele, Leitplanken, prüft Ergebnisse |

Je höher die Stufe, desto wichtiger sind Nachvollziehbarkeit und Freigabeprozess.

## 2. Self-Healing und robuste Selektoren

- Werkzeuge speichern mehrere Merkmale je Element (ID, Text, Rolle, Position, visuelle
  Signatur) und wählen bei Fehlschlag ein Ersatzmerkmal (Testim, mabl, Functionize,
  Healenium für Selenium, Playwright-Erweiterungen).
- Nutzen: weniger Pflege bei kosmetischen Änderungen.
- Risiko: Die Heilung kann das falsche Element wählen und einen echten Fehler verdecken.
  Jede Heilung muss protokolliert und bestätigt werden; dauerhafte Heilungen gehören in den
  Code zurück.
- Besser als Heilung: stabile Testhaken (Test-IDs, ARIA-Rollen, Beschriftungen) mit den
  Entwicklern vereinbaren. Self-Healing ist Symptombehandlung.

## 3. Testgenerierung mit LLMs

Geeignet:

- Erste Fassung von Unit-Tests für bestehenden Code (Charakterisierungstests), danach
  Review auf Assertions und Grenzfälle.
- Testideen und Grenzfälle aus Anforderungen; Äquivalenzklassen und Entscheidungstabellen
  als strukturierte Aufgabe (dieser Skill-Katalog als Kontext).
- Gherkin-Entwürfe aus Stories für die Three Amigos, nicht als Ersatz dafür.
- Testdaten mit Struktur und Vielfalt, ohne Personenbezug.
- Zusammenfassung und Erstklassifizierung von Fehlschlägen aus Logs und Traces.

Regeln:

- Generierte Tests gelten als ungeprüft, bis ein Mensch Orakel und Assertions bestätigt hat.
  LLMs erzeugen gern Tests, die den Code bestätigen, statt ihn zu prüfen.
- Überdeckung durch generierte Tests mit Mutationstest validieren.
- Kontext mitgeben: Spezifikation, Konventionen, Beispiele guter Tests aus dem Repository.
- Generierte Tests, die niemand versteht, werden nicht übernommen.

## 4. Testagenten (Agentic Testing)

Ein Agent erhält ein Ziel, Werkzeuge (Browser, API-Client, Repository, Fehlertracker) und
Leitplanken, plant selbst und führt mehrstufig aus.

Einsatzmuster:

| Muster | Beschreibung |
| --- | --- |
| Explorationsagent | Führt einen Charter aus, navigiert, beobachtet, meldet Auffälligkeiten mit Belegen |
| Generierungsagent | Liest Story und Code, erzeugt Tests, führt sie aus, iteriert bis grün, öffnet Merge Request |
| Wartungsagent | Analysiert Fehlschläge, unterscheidet Produkt- und Testfehler, schlägt Korrektur vor |
| Triage-Agent | Dedupliziert und klassifiziert Fehlermeldungen, ergänzt Reproduktionsschritte |
| Orchestrator | Verteilt Teilaufgaben an spezialisierte Agenten, führt Ergebnisse zusammen |

Architektur eines Testagenten:

- **Ziel und Charter** in natürlicher Sprache, mit Abbruchkriterien (Zeit, Schritte, Kosten).
- **Werkzeuge** mit minimalen Rechten: Testumgebung, nie Produktion; Lesezugriff auf Code,
  Schreibzugriff nur per Merge Request.
- **Skills** als Wissensbasis: Verfahren, Heuristiken, Konventionen (dieser Katalog).
- **Gedächtnis**: Was wurde schon geprüft, welche Befunde existieren.
- **Beobachtbarkeit**: Jeder Schritt, jede Werkzeugnutzung, jede Entscheidung protokolliert.
- **Mensch im Kreis**: Befunde, Testcode und Änderungen werden geprüft, bevor sie wirken.

Bewertung eines Agenten wie ein Tester: Findet er bekannte, eingebaute Fehler
(Seeded Bugs)? Wie hoch ist die Fehlalarmquote? Sind Berichte reproduzierbar? Kosten je Befund?

## 5. Risiken und Leitplanken

- **Verdeckte Fehler:** Heilung oder Neuinterpretation macht rote Tests grün. Gegenmaßnahme:
  Änderungen nur per Review, Mutationstest, Seeded Bugs.
- **Nichtdeterminismus:** Gleicher Lauf, anderes Ergebnis. Gegenmaßnahme: Temperatur und
  Modellversion fixieren, Ergebnisse als deterministische Tests festschreiben.
- **Datenschutz und Vertraulichkeit:** Code, Testdaten und Fehlerberichte an externe Modelle.
  Gegenmaßnahme: Lokale Modelle oder vertraglich abgesicherte Dienste, Datenminimierung;
  im Behördenumfeld (Ü2, VS-NfD) meist nur lokal.
- **Kosten:** Token- und Laufzeitkosten je Lauf messen; Abbruchkriterien.
- **Kompetenzverlust:** Team versteht die eigene Suite nicht mehr. Gegenmaßnahme: Review-
  Pflicht, Pairing mit dem Agenten, Dokumentation.
- **Haftung und Nachweis:** In regulierten Umfeldern muss nachvollziehbar sein, wer welche
  Prüfung freigegeben hat. Agentenprotokolle archivieren.

## 6. Bewertung von KI-Werkzeugen

Fragen vor der Einführung:

1. Welches konkrete Problem löst es (Pflegeaufwand, Erstellzeit, Abdeckung)? Messgröße?
2. Wohin gehen Code und Daten? Modell lokal, EU, USA? Vertrag, Löschung, Training?
3. Wie nachvollziehbar sind Entscheidungen (Heilungen, generierte Schritte)?
4. Lock-in: Sind Tests exportierbar, oder leben sie nur in der Plattform?
5. Pilot mit Seeded Bugs und Vergleich zur bestehenden Suite.

## 7. Prüfliste

- [ ] Einsatzstufe ist bewusst gewählt; Freigabeprozess passt dazu.
- [ ] Self-Healing protokolliert und erfordert Bestätigung; Testhaken werden parallel verbessert.
- [ ] Generierte Tests sind auf Orakel und Assertions geprüft, Mutationstest bestätigt die Schärfe.
- [ ] Agenten haben minimale Rechte, Abbruchkriterien, Protokollierung und Mensch im Kreis.
- [ ] Datenschutz- und Vertraulichkeitsanforderungen sind geprüft (lokal vs. extern).
- [ ] Nutzen wird gemessen (Pflegeaufwand, Befunde, Fehlalarme, Kosten).
