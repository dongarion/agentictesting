# Checklistenbasiertes Testen

Der Tester arbeitet eine **Liste von Prüfpunkten** ab und entwirft die konkreten Tests dazu
während der Durchführung. Geeignet als wiederkehrende Mindestprüfung, als Rahmen für
Fachtester ohne Testausbildung und als Gedächtnisstütze gegen Routinefehler.

## Inhalt
1. Eigenschaften einer guten Checkliste
2. Checkliste erstellen
3. Durchführung
4. Pflege
5. Beispiel-Checklisten
6. Anti-Patterns
7. Prüfliste

## 1. Eigenschaften einer guten Checkliste

- **Prüfpunkte, keine Testfälle.** „Pflichtfelder werden geprüft“ statt „Gib in Feld X nichts
  ein und klicke Speichern“. Die Konkretisierung bleibt beim Tester.
- **Kurz.** 10 bis 30 Punkte je Liste. Längere Listen in Themenlisten aufteilen.
- **Begründet.** Jeder Punkt hat eine Herkunft: Fehler aus der Vergangenheit, Norm, Risiko.
- **Prüfbar.** Jeder Punkt lässt sich mit ja, nein oder nicht anwendbar beantworten.
- **Versioniert.** Datum, Autor, Änderungsgrund.

## 2. Checkliste erstellen

1. Quelle wählen: Fehlerhistorie, Qualitätsmerkmal, Norm (z. B. WCAG), Abnahmekriterien,
   Erfahrungswissen eines ausscheidenden Kollegen.
2. Punkte formulieren, nach Bereich gruppieren.
3. Jeden Punkt mit Herkunft versehen.
4. Mit zwei Personen gegenlesen: Ist jeder Punkt verständlich und prüfbar?
5. Pilotlauf, dann Freigabe.

## 3. Durchführung

- Je Punkt: Tester entwirft spontan 1–3 Prüfungen, führt sie aus, hält Ergebnis
  (ok / Befund / n. a.) und einen Satz zur Prüfung fest.
- Befunde im Fehlermanagement melden, nicht nur in der Liste ankreuzen.
- Was dem Tester außerhalb der Liste auffällt, notieren. Das sind Kandidaten für neue Punkte
  oder für explorative Charters.
- Verschiedene Tester führen dieselbe Liste unterschiedlich aus. Das ist gewollt und erhöht
  die Vielfalt. Bei Wiederholung durch denselben Tester bewusst andere Prüfungen wählen.

## 4. Pflege

- Nach jedem Release: Welche Punkte haben Befunde erzeugt? Welche nie? Nie treffende Punkte
  nach drei Durchläufen hinterfragen.
- Neue Fehlerklassen aus Produktion und Test aufnehmen.
- Liste bleibt kurz: für jeden neuen Punkt einen alten prüfen.

## 5. Beispiel-Checklisten

### Formular (Auszug)

| Nr | Prüfpunkt | Herkunft |
| --- | --- | --- |
| F1 | Pflichtfelder sind markiert und werden serverseitig geprüft | BUG-2024-117 |
| F2 | Fehlermeldungen nennen Feld und Ursache | Usability-Richtlinie |
| F3 | Eingaben bleiben nach Validierungsfehler erhalten | BUG-2024-131 |
| F4 | Tastaturbedienung vollständig, sichtbarer Fokus | WCAG 2.1.1, 2.4.7 |
| F5 | Doppeltes Absenden erzeugt keinen doppelten Datensatz | BUG-2025-008 |
| F6 | Maximallängen entsprechen der Datenbank, kein stilles Abschneiden | Fehlerhistorie |
| F7 | Datums- und Zahlenformate nach Locale | Kundenbeschwerde |

### Release-Smoke (Auszug)

| Nr | Prüfpunkt |
| --- | --- |
| S1 | Anmeldung mit Standardrolle möglich |
| S2 | Startseite lädt ohne Konsolenfehler |
| S3 | Ein Datensatz je Kernentität anlegen, lesen, ändern, löschen |
| S4 | Ein Bericht erzeugen und exportieren |
| S5 | Versionsnummer entspricht dem Release |
| S6 | Schnittstelle zu System X antwortet |

## 6. Anti-Patterns

- Checkliste als Ersatz für Testfallspezifikation bei hohem Risiko.
- Liste über Jahre nur erweitern, nie kürzen.
- Ankreuzen ohne Notiz, was geprüft wurde.
- Prüfpunkte ohne Herkunft, die niemand mehr hinterfragt.

## 7. Prüfliste

- [ ] Jeder Punkt ist prüfbar und hat eine Herkunft.
- [ ] Liste hat höchstens etwa 30 Punkte oder ist thematisch geteilt.
- [ ] Ergebnis je Punkt mit kurzer Notiz dokumentiert.
- [ ] Auffälligkeiten außerhalb der Liste sind erfasst.
- [ ] Pflegetermin nach dem Release ist eingeplant.
