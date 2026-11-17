# Fehlerangriffe und intuitive Testfallermittlung

**Error Guessing** nutzt Erfahrung: Wo sind in ähnlichen Systemen Fehler aufgetreten?
**Fault Attacks** (Whittaker, *How to Break Software*) systematisieren das: Für jede bekannte
Fehlerklasse gibt es einen gezielten Angriff.

## Inhalt
1. Fehlerliste aufbauen
2. Angriffe auf Eingaben
3. Angriffe auf Ausgaben
4. Angriffe auf Daten und Zustand
5. Angriffe auf Umgebung und Abhängigkeiten
6. Angriffe auf Web und Mobile
7. Anti-Patterns
8. Prüfliste

## 1. Fehlerliste aufbauen

Error Guessing wird besser mit einer gepflegten Liste. Quellen:

- Fehlerhistorie des Projekts, nach Ursache gruppiert.
- Fehlerhistorie der Technologie (Framework-Issues, bekannte Bibliotheksfehler).
- Allgemeine Fehlerklassifikationen: Beizer-Taxonomie, Common Weakness Enumeration (CWE),
  OWASP Top 10.
- Eigene Erfahrung, als Katalog festgehalten: „Bei Datumsfeldern geht immer … schief.“

Je Eintrag: Fehlerklasse, typisches Symptom, Angriff, der ihn provoziert.

## 2. Angriffe auf Eingaben

| Angriff | Ziel |
| --- | --- |
| Jede Eingabefehlermeldung erzwingen | Vollständigkeit und Qualität der Validierung |
| Default-Werte überall stehen lassen | Fehlende Pflichtprüfung, falsche Defaults |
| Ungültige Zeichen, falsche Typen, falsches Format | Robustheit der Parser |
| Puffer überlaufen lassen: Maximallänge + 1, extrem lang | Längenprüfung, Abschneiden ohne Hinweis |
| Werte, die zusammen illegal sind, einzeln legal eingeben | Feldübergreifende Validierung |
| Dieselbe Eingabe mehrfach: Duplikate anlegen | Eindeutigkeitsregeln |
| Eingaben, die interne Berechnungen in Grenzbereiche treiben (0, negativ, Division) | Arithmetikfehler |
| Eingaben in Client-seitig gesperrte Felder über API oder DevTools | Serverseitige Validierung |

## 3. Angriffe auf Ausgaben

| Angriff | Ziel |
| --- | --- |
| Ausgaben erzwingen, die nicht in das Anzeigefeld passen | Abschneiden, Überlauf, Layout |
| Ausgaben mit Sonderzeichen, HTML, Skript erzeugen | Escaping, XSS |
| Ausgabe ändern und erneut erzeugen | Caching, veraltete Anzeige |
| Berichte mit 0, 1 und sehr vielen Datensätzen | Leere Zustände, Paging, Performance |
| Export und Re-Import | Datenverlust, Formatfehler, Rundung |

## 4. Angriffe auf Daten und Zustand

| Angriff | Ziel |
| --- | --- |
| Daten in jedem Zustand ändern, löschen, wieder herstellen | Zustandsmaschine |
| Referenzierte Daten löschen (Kunde mit offenen Aufträgen) | Referenzielle Integrität |
| Daten parallel in zwei Sitzungen ändern | Lost Update, Sperren |
| Transaktion mitten im Vorgang abbrechen | Atomarität, Teilzustände |
| Historische Daten nach Schema- oder Regeländerung öffnen | Migration, Abwärtskompatibilität |
| Zeit manipulieren: Systemuhr, Zeitzone, Jahreswechsel | Zeitlogik |

## 5. Angriffe auf Umgebung und Abhängigkeiten

| Angriff | Ziel |
| --- | --- |
| Netz trennen, verzögern, Pakete verlieren | Timeouts, Wiederholung, Fehlermeldung |
| Abhängigen Dienst stoppen oder langsam machen | Fallback, Circuit Breaker, Meldung |
| Dienst mit ungültigen Antworten antworten lassen (Mock) | Robustheit gegen Fremdfehler |
| Platte voll, Speicher knapp, Rechte entzogen | Fehlerbehandlung auf Betriebssystemebene |
| Konfiguration ändern, fehlen lassen, korrumpieren | Startverhalten, Defaults |
| Mehrfach installieren, updaten, zurückrollen | Installierbarkeit, Migration |

## 6. Angriffe auf Web und Mobile

| Angriff | Ziel |
| --- | --- |
| Zurück-Taste, Reload, Mehrfach-Tabs, URL manipulieren | Zustand, Berechtigung, CSRF |
| Session ablaufen lassen, Token manipulieren | Authentifizierung |
| Direkter Aufruf geschützter URLs und APIs ohne Rolle | Autorisierung |
| Browser-Zoom, kleine Fenster, Tastatur-only, Screenreader | Responsiveness, Barrierefreiheit |
| Mobil: Anruf, Rotation, App in Hintergrund, Netzwechsel WLAN/Mobilfunk, Akku leer | Unterbrechungen |
| Langsame Verbindung (Throttling) | Ladeverhalten, Spinner, doppelte Requests |

## 7. Anti-Patterns

- Angriffe ohne Hypothese: Welche Fehlerklasse soll provoziert werden?
- Nur Eingabeangriffe; Zustand, Umgebung und Zeit vergessen.
- Befunde als „unrealistisch“ verwerfen, ohne den Auftraggeber zu fragen. Ob ein Szenario
  realistisch ist, entscheidet das Risiko, nicht der Tester allein.
- Fehlerliste nicht pflegen; dasselbe Wissen jedes Mal neu erfinden.

## 8. Prüfliste

- [ ] Fehlerliste des Projekts ist gesichtet.
- [ ] Je Angriff ist die Hypothese (Fehlerklasse) notiert.
- [ ] Eingaben, Ausgaben, Daten/Zustand, Umgebung und Plattform sind abgedeckt.
- [ ] Neue Fehlerklassen aus den Befunden sind in die Liste aufgenommen.
