# Tour-basiertes Testen

Touren (Whittaker, 2009) sind **Metaphern für Erkundungsstrategien**. Jede Tour gibt der
Session eine Perspektive, so wie ein Tourist eine Stadt je nach Interesse anders erkundet.
Geeignet, um ein unbekanntes Produkt in kurzer Zeit breit kennenzulernen.

## Inhalt
1. Touren nach Stadtvierteln
2. Tour wählen
3. Tour als Charter
4. Prüfliste

## 1. Touren nach Stadtvierteln

### Geschäftsviertel (Kernfunktionen)

| Tour | Vorgehen |
| --- | --- |
| Guidebook | Der Dokumentation oder Hilfe wörtlich folgen. Jede Abweichung ist ein Befund (Doku oder Produkt). |
| Money | Die Funktionen testen, für die Kunden bezahlen. Verkaufsdemo nachspielen. |
| Landmark | Markante Funktionen in wechselnder Reihenfolge ansteuern, zwischen ihnen navigieren. |
| Intellectual | Dem Produkt die schwersten Aufgaben stellen: größte Datei, komplexestes Dokument, längste Kette. |
| FedEx | Ein Datum durch das ganze System verfolgen: Eingabe, Speicherung, Anzeige, Export, Bericht, Löschung. |
| After-Hours | Hintergrundprozesse, Batchläufe, Wartungsfenster, Aufräumjobs. |
| Garbage Collector | Methodisch Bildschirm für Bildschirm, Menü für Menü, ohne Tiefe, auf Vollständigkeit. |

### Historisches Viertel (Altlasten)

| Tour | Vorgehen |
| --- | --- |
| Bad Neighborhood | Module mit vielen bekannten Fehlern gezielt erkunden. Fehler häufen sich. |
| Museum | Alten Code, selten genutzte Funktionen, Legacy-Schnittstellen. |
| Prior Version | Was ging in der Vorversion? Geht es noch genauso? |

### Unterhaltungsviertel (Nutzerperspektive)

| Tour | Vorgehen |
| --- | --- |
| Supporting Actor | Nebenfunktionen neben der Hauptfunktion: Filter neben der Liste, Hilfe neben dem Formular. |
| Back Alley | Am wenigsten genutzte Funktionen. |
| All-Nighter | Sitzung lange offen lassen, Daten ungespeichert liegen lassen, nach Stunden weitermachen. |

### Touristenviertel (schnelle Breite)

| Tour | Vorgehen |
| --- | --- |
| Collector | Jedes erreichbare Ergebnis einmal erzeugen: jede Meldung, jeder Bericht, jeder Status. |
| Lonely Businessman | So viele Bildschirme wie möglich in kürzester Zeit, ohne Interaktion in der Tiefe. |
| Supermodel | Nur die Oberfläche: Layout, Rechtschreibung, Ausrichtung, Responsiveness, Kontraste. |
| TOGOF (Test One, Get One Free) | Mehrere Instanzen gleichzeitig: zwei Fenster, zwei Tabs, zwei Nutzer. |
| Scottish Pub | Versteckte, undokumentierte Funktionen, Tastenkombinationen, URL-Parameter. |

### Hotelviertel (Ruhezustand)

| Tour | Vorgehen |
| --- | --- |
| Rained-Out | Jeden Vorgang abbrechen: Abbrechen-Button, Escape, Fenster schließen, Netz trennen. |
| Couch Potato | Minimale Eingaben: Defaults übernehmen, Felder leer lassen, nur Pflicht ausfüllen. |

### Verrufenes Viertel (Stress)

| Tour | Vorgehen |
| --- | --- |
| Saboteur | Ressourcen entziehen, Rechte entziehen, Dateien löschen, Dienste stoppen. |
| Antisocial | Immer das Falsche tun: ungültige Eingaben, unlogische Reihenfolge, Gegenteil der Erwartung. |
| Obsessive-Compulsive | Dasselbe wiederholen: speichern, speichern, speichern; sortieren, zurück, sortieren. |

## 2. Tour wählen

| Ziel | Touren |
| --- | --- |
| Produkt schnell kennenlernen | Guidebook, Landmark, Garbage Collector |
| Regressionsrisiko nach Änderung | Prior Version, Bad Neighborhood, FedEx |
| Robustheit | Rained-Out, Saboteur, TOGOF, Obsessive-Compulsive |
| Abnahmevorbereitung | Money, Collector, Supermodel |
| Datenintegrität | FedEx, After-Hours, All-Nighter |

## 3. Tour als Charter

Tour in das Charter-Format einbetten:

> Erkunde **die Antragsverwaltung** mit **der FedEx-Tour (Antragsdaten von der Eingabe bis zum
> Löschprotokoll verfolgen)**, um **Stellen zu finden, an denen Daten verloren, verfälscht
> oder nicht gelöscht werden**.

## 4. Prüfliste

- [ ] Tour passt zum Informationsziel des Charters.
- [ ] Tour ist im Charter benannt, Notizen verweisen auf sie.
- [ ] Nach der Session: Welche Viertel sind noch nicht besucht? Als Charters ablegen.
