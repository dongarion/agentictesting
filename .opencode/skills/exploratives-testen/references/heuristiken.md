# Testheuristiken

Heuristiken sind **fehlbare Denkhilfen**. Sie erzeugen Testideen für Bereiche, die die
Spezifikation nicht oder nur lückenhaft abdeckt, und garantieren nichts. Benutze sie als
Fragenkatalog, nicht als Liste zum Abhaken. Sie ergänzen die systematischen Verfahren,
sie ersetzen sie nicht.

Grundlagen: James Bach (Heuristic Test Strategy Model), Michael Bolton (HICCUPPS),
Elisabeth Hendrickson, James Lyndsay und Dale Emery (Test Heuristics Cheat Sheet),
Cem Kaner (Common Software Errors in *Testing Computer Software*), Michael Hunter
(*You Are Not Done Yet*), James Whittaker (*How to Break Software*). Die Inhalte sind
zusammengefasst, neu gegliedert und ergänzt.

## Inhalt
1. Einordnung
2. Was testen: Produktelemente (SFDIPOT)
3. Woran erkennen: Orakel (HICCUPPS)
4. Grenz- und Angriffswerte nach Fehlerart
5. Variationsmuster
6. Schnittstellen: Web und API
7. Qualitätsmerkmale als Fragen
8. Fehlerkategorien als Prüfliste
9. Vorgehen in einer Session
10. Anti-Patterns
11. Prüfliste
12. Beispiel

## 1. Einordnung

- **Systematische Verfahren** im Skill `black-box-testdesign` (Äquivalenzklassen und Grenzwerte,
  Entscheidungstabellen, Zustandsübergänge, Kombinatorik, Anwendungsfälle, Syntaxtest) decken ab,
  was die Spezifikation hergibt.
- **Heuristiken** kommen dort zum Einsatz, wo die Spezifikation endet:
  - im Abschnitt „Hinweise für exploratives Testen“ eines Testentwurfs,
  - in explorativen Sessions (siehe [charter-und-session.md](charter-und-session.md)),
  - als Abgleich der Klassen eines Testentwurfs: Fehlt dort ein Wert aus Abschnitt 4?
- **Ein Heuristik-Treffer ohne spezifiziertes Ergebnis ist eine offene Frage**, kein Testfall mit
  geratenem Ergebnis. Jede Bewertung braucht ein benanntes Orakel (Abschnitt 3).

## 2. Was testen: Produktelemente (SFDIPOT, Bach)

| Element | Fragen |
| --- | --- |
| **S**tructure | Aus welchen Teilen besteht es? Code, Dateien, Konfiguration, Hardware |
| **F**unction | Was tut es? Berechnungen, Fehlerbehandlung, Sicherheitsfunktionen |
| **D**ata | Womit arbeitet es? Eingaben, Ausgaben, Persistenz, große, kleine und ungültige Daten |
| **I**nterfaces | Wie kommuniziert es? Oberfläche, API, Import und Export, Systemschnittstellen |
| **P**latform | Worauf läuft es? Betriebssystem, Browser, Hardware, Abhängigkeiten, Konfiguration |
| **O**perations | Wie wird es genutzt? Nutzertypen, Umgebungen, extreme und ungewöhnliche Nutzung |
| **T**ime | Wann? Zeitabhängigkeit, Nebenläufigkeit, Timeouts, Reihenfolge, Zeitzonen |

Vor einer Session den Bereich einmal gegen alle sieben Elemente durchgehen und je Element
ein bis drei Ideen notieren.

## 3. Woran erkennen: Orakel (HICCUPPS, Bolton)

Wenn keine Spezifikation sagt, was richtig ist: Ein Verhalten ist verdächtig, wenn es
inkonsistent ist mit …

| Orakel | Frage |
| --- | --- |
| **H**istory | … früheren Versionen? |
| **I**mage | … dem Anspruch des Herstellers oder Auftraggebers? |
| **C**omparable products | … vergleichbaren Produkten oder Funktionen? |
| **C**laims | … Dokumentation, Story, Hilfe, Meldungen, Zusagen? |
| **U**ser expectations | … dem, was ein vernünftiger Nutzer erwartet? |
| **P**roduct | … dem Verhalten an anderer Stelle im selben Produkt? |
| **P**urpose | … dem Zweck der Funktion? |
| **S**tatutes and standards | … Gesetzen, Normen, Barrierefreiheit, Datenschutz? |
| **F**amiliarity | … der Abwesenheit bekannter Fehlermuster (siehe Abschnitt 8)? |

Dazu als Fachorakel: eine Fachregel, die der Fachbereich bestätigt. Jeder Befund nennt mindestens
ein Orakel. Das ersetzt im Fehlerbericht die fehlende Spezifikationsstelle.

## 4. Grenz- und Angriffswerte nach Fehlerart

Fehler entstehen selten am Datentyp selbst, sondern an wenigen wiederkehrenden Stellen:
Darstellungsgrenzen, Längen, Kodierung, Formate, Kalender, Ressourcen, Fachregeln und
Eingaben, die ein nachgelagertes System interpretiert. Für jedes Feld und jeden Parameter
fragen: Welche dieser Fehlerarten kann hier auftreten? Dann gezielt Werte wählen.

Mit den Klassen aus `black-box-testdesign/references/aequivalenzklassen-grenzwerte.md`
abgleichen und jeden Wert bei allen Aktionen prüfen, die die Daten berühren: Eingabe, Suche,
Änderung, Anzeige, Export, Import, Druck, Schnittstelle.

| Fehlerart | Prüfidee | Werte wählen nach |
| --- | --- | --- |
| **Darstellungsgrenzen** | Passt der Wert in jeden Typ, durch den er unterwegs ist (Oberfläche, API, Datenbank, Bericht)? | Bitbreiten der beteiligten Typen: jeweils 2^n − 1, 2^n, 2^n + 1 (n = 7, 8, 15, 16, 31, 32, 53, 63); 0, −1, kleinster und größter Wert; Gleitkomma auf Gleichheit (0,1 + 0,2), sehr kleine und sehr große Exponenten |
| **Genauigkeit und Rundung** | Wird an jeder Stelle gleich gerundet, und stimmt die Summe der Teile? | Werte genau auf der Rundungsschwelle (x,xx5); Summen vieler kleiner Beträge; Umrechnung von Einheiten oder Währungen hin und zurück |
| **Länge und Größe** | Wird die Grenze überall gleich gezählt und gleich durchgesetzt? | leer, ein Element, Maximum −1, Maximum, Maximum +1, deutlich zu groß; Zählung in Zeichen gegenüber Bytes (mehrbytige Zeichen am Ende) |
| **Zeichen und Kodierung** | Bleibt jedes Zeichen auf dem ganzen Weg erhalten und vergleichbar? | je Kategorie ein Vertreter: Zeichen außerhalb ASCII, zusammengesetzte Zeichen (gleich aussehend, unterschiedlich kodiert), Schrift mit anderer Laufrichtung, unsichtbare Zeichen, Steuerzeichen, unterschiedliche Zeilenenden, Leerraum am Anfang und Ende, Zeichen, die anderen zum Verwechseln ähnlich sehen |
| **Format und Locale** | Wird dasselbe überall gleich gelesen und geschrieben? | Dezimal- und Tausendertrennzeichen, Datums- und Zeitformate, Sortierregeln der Zielsprache, Groß- und Kleinschreibung mit sprachabhängigen Sonderfällen |
| **Kalender und Zeit** | Stimmen Fristen, Tageszuordnung und Reihenfolge auch an Übergängen? | Tages-, Monats- und Jahreswechsel; Schalttag und ungültige Tage; Zeitumstellung (doppelte und fehlende Stunde); Zeitzonen der Beteiligten; Epochengrenzen der verwendeten Zeitdarstellung; Uhrzeitunterschiede zwischen Systemen; Ablauf von Fristen und Timeouts |
| **Ressourcen** | Was passiert, wenn die Umgebung nicht mitspielt? | vorhanden, fehlend, gesperrt, schreibgeschützt, beschädigt, bereits belegt; Speicher oder Platte voll; Netzpfad nicht erreichbar; plattformspezifisch reservierte Namen und unzulässige Zeichen in Namen |
| **Mengen** | Gibt es einen sinnvollen leeren, einzelnen und vollen Zustand? | 0, 1, 2, viele, Maximum, Maximum +1; Duplikate; Reihenfolge; Seitengrenzen |
| **Fachregeln** | Werden fachlich unmögliche oder widersprüchliche Daten verhindert, echte aber angenommen? | Regel knapp verletzt; Eindeutigkeit verletzt; Pflichtangabe fehlt; abhängige Felder widersprechen sich; reale Sonderfälle der Domäne (Namen nach DIN SPEC 91379, Adressen ohne Hausnummer, Personen ohne Vornamen) |
| **Interpretierte Eingaben** | Kann eine Eingabe in einem nachgelagerten System als Befehl wirken? | Zeichen mit Sonderbedeutung im jeweiligen Zielkontext (Datenbankabfrage, HTML, Pfad, Vorlage, Kommandozeile, Tabellenkalkulation beim Export); Funde an den Security Tester übergeben |

Die Spalte „Werte wählen nach“ beschreibt, *wie* Werte gefunden werden. Die konkreten Werte
leitest du aus der Technik des Prüflings ab: Welche Typen, Kodierungen, Zeitdarstellungen und
Zielsysteme sind beteiligt?

## 5. Variationsmuster

Muster, um aus einem funktionierenden Ablauf viele Varianten zu machen.

### Menge und Position
- **Null, eins, viele:** 0 Datensätze, 1, viele; auch 0 Drucker, 1, mehrere.
- **Goldlöckchen:** zu klein, zu groß, genau richtig.
- **Einige, keine, alle:** bei Auswahl, Rechten, Anhängen, markierten Einträgen.
- **Anfang, Mitte, Ende:** Position im Text, in der Liste, im Ablauf.

### Operationen auf Daten
- **CRUD:** anlegen, lesen, ändern, löschen, in jeder Reihenfolge, auch doppelt.
- **Den Daten folgen:** dieselben Daten durch alle Funktionen schicken (Eingabe → Suche → Export →
  Import → Ändern → Anzeige) und die Integrität nach jedem Schritt prüfen.
- **Abhängigkeiten:** „hat ein“-Beziehungen (Kunde hat Rechnungen) mit den Mengenmustern verbinden:
  Kunden mit 0, 1, n Rechnungen löschen.
- **Zustand der Daten:** gerade angelegt, gerade gelöscht, von jemand anderem geändert, archiviert, gesperrt.
- **Eingabemethode:** tippen, einfügen, importieren, ziehen und ablegen, Oberfläche gegenüber API.
- **Beschränkungen verletzen**, kombiniert mit verschiedenen Eingabemethoden.

### Zeit, Reihenfolge, Unterbrechung
- **Reihenfolge:** Schritte vertauschen, umkehren, Zurück-Taste, Undo und Redo.
- **Unterbrechen:** abmelden, beenden, Prozess abbrechen, Netz trennen, Ruhezustand, Timeout.
- **Liegenlassen:** Vorgang halb fertig stehen lassen, Sitzung ablaufen lassen, zurückkommen.
- **Wiederholen:** sofort noch einmal, zehnmal, tausendmal; Doppelklick.
- **Gleichzeitig:** zwei Tabs, zwei Konten, doppelt angemeldet, gleichzeitig ändern und löschen.
- **Überfluten:** viele Anfragen gleichzeitig.
- **Aushungern:** CPU, Speicher, Platte oder Netz an der Grenze.
- **Uhr:** Datum ändern, Zeitzone wechseln, Zeitumstellung, Jahreswechsel.
- **Dauerlauf:** lange laufen lassen, Speicher und Logs beobachten.

### Umgebung
- **Konfigurationen:** Auflösung, Zoom, Netzgeschwindigkeit, Speicher, Peripherie; dazu die Mengenmuster.
- **Sortierung und Locale:** Buchstaben und Zahlen gemischt, Umlaute, türkisches i (İ, ı), über mehrere Seiten.

### Modell und Erkundung
- **Variablen finden:** offensichtliche, versteckte und abgeleitete veränderbare Werte auflisten.
- **Berührungspunkte:** jede Stelle, an der man etwas sieht oder steuern kann, ist ein Angriffspunkt.
- **Zustände modellieren:** Beobachtungen in ein Zustandsmodell überführen
  (`black-box-testdesign/references/zustandsuebergaenge.md`).
- **Karte zeichnen:** von einem Basiszustand einen Schritt gehen, zurückkehren, nächsten Schritt.

### Menschen
- **Rollen und Personas:** Erstnutzer, Experte, Administrator, Ungeduldige, Hilfsmittelnutzer.
- **Extreme Szenarien:** überzeichnete Lebensgeschichten mit vielen Sonderfällen auf einmal
  („Seifenoper-Szenarien“).

## 6. Schnittstellen: Web und API

### Web
- **Navigation:** Zurück nach dem Absenden (doppelte Vorgänge, abgelaufene Seiten), Neu laden,
  Lesezeichen direkt aufrufen, auch nach dem Abmelden, URL-Parameter ändern oder entfernen,
  mehrere Fenster.
- **Eingaben:** Felder mit sehr langen Texten (> 5000 Zeichen), interpretierte Eingaben aus Abschnitt 4.
- **Einstellungen:** Cookies blockiert, Fenster sehr schmal, Schrift stark vergrößert, Zoom 200 %
  und 400 %, langsame Verbindung.
- Barrierefreiheit ausführlich: Skill `teststufen-testarten`, `references/barrierefreiheit.md`.

### API
- **Grenzen und Leere:** Grenzwerte, leere Werte, `null` gegenüber fehlendem Feld, leere Arrays, negative Zahlen.
- **Ungültiges:** falscher Typ, falsches Format, unbekannte Felder, falscher Content-Type, zu große Payload.
- **Methoden:** HTTP-Verben vertauschen (GET statt POST, DELETE auf eine Sammlung).
- **Zugriff:** ohne Token, mit abgelaufenem Token, mit Rolle ohne Recht, auf fremde Objekte.
- **Fehler und Antworten:** jeder dokumentierte Fehlercode, keine internen Details, Antwortzeit unter Last.
- Ausführlich: Skill `white-box-testdesign`, `references/api-test.md`.

### Mobil
Siehe Skill `spezialtests`, `references/mobile.md` (Unterbrechungen, Netzwechsel, Berechtigungen, Gerätematrix).

## 7. Qualitätsmerkmale als Fragen

Je Merkmal eine Frage an den Bereich stellen: „Was wäre hier ein … Problem?“
Funktionalität, Zuverlässigkeit, Benutzbarkeit, Barrierefreiheit, Sicherheit, Skalierbarkeit,
Performance, Installierbarkeit, Kompatibilität, Unterstützbarkeit (Logs, Diagnose), Testbarkeit,
Wartbarkeit, Portierbarkeit, Lokalisierbarkeit. (Angelehnt an Bachs Liste „CRUSSPIC STMPL“ und
ISO/IEC 25010.)

## 8. Fehlerkategorien als Prüfliste

Häufige Fehlerarten, beim Durchsehen des Prüflings abzufragen (in Anlehnung an Kaner):

| Kategorie | Worauf achten |
| --- | --- |
| Funktion | fehlt, falsch, überflüssig, zu langsam, zu restriktiv |
| Grenzen | versteckte Grenzen durch Hardware, Zeit, Zahlentypen, Puffer |
| Initialisierung | Werte nicht gesetzt, nicht zurückgesetzt, falsch vorbelegt |
| Berechnung | Rundung, Überlauf, falsche Formel oder Operatorrangfolge, `>` statt `>=`, Gleitkomma auf Gleichheit geprüft, UND und ODER vertauscht |
| Kontrollfluss | Endlosschleife, falsches Abbruchkriterium, fehlender Default-Zweig, überlappende Fälle |
| Anzeige und Meldungen | falscher oder abgeschnittener Text, uneinheitliche Schreibweise, Fachjargon, Meldung ohne Handlungsanweisung, Sicherheitsabfrage ohne Rückgängig |
| Konsistenz | Position von Menüs, Abkürzungen, Benennung ähnlicher Funktionen |
| Wiederherstellung | kein Rückgängig, kein Zwischenspeichern, Absturz beim Speichern, keine Wiederherstellung danach |
| Fehlerbehandlung | ungeprüfte Eingaben, ignorierte Rückgabecodes, gleichzeitig geöffnete Dokumente, keine Fortschrittsanzeige |
| Versionierung | falsche Versionsnummer, alter Fehler kehrt durch Integration zurück, Daten in mehreren Ablagen nicht synchron |

## 9. Vorgehen in einer Session

1. **Charter und Zeitbox** festlegen (siehe [charter-und-session.md](charter-und-session.md)),
   z. B. 60 Minuten: „Adressfeld der Kundenmaske auf Datenfehler prüfen“.
2. **Ideen sammeln:** Bereich gegen SFDIPOT (Abschnitt 2) und die passenden Fehlerarten
   (Abschnitt 4) durchgehen, 10 bis 20 Ideen notieren.
3. **Muster wählen,** die zum Charter passen (Abschnitt 5), und die Session danach gliedern.
4. **Erkunden:** Ideen abarbeiten, aber jeder Beobachtung Vorrang geben. Wo ein Fehler ist,
   stecken oft weitere: die Umgebung eines Fundes vertiefen.
5. **Bewerten:** jede Beobachtung gegen ein benanntes Orakel (Abschnitt 3); ohne Orakel offene Frage.
6. **Notieren:** Schritt, Beobachtung, Orakel, Reproduktion, sofort.
7. **Zurückführen:** Zeigt ein Fund ein systematisches Muster (Bereich, Zustand, Regel), wird daraus
   eine Testbedingung im Testentwurf mit einem Verfahren aus `black-box-testdesign`.
8. **Auswerten:** Spezifikationslücken in „Offene Fragen“ übernehmen; festhalten, welche Heuristiken
   Funde erzeugt haben und welche fehlten. Die nächste Session dort vertiefen.

## 10. Anti-Patterns

- Heuristiken als Testentwurf ausgeben: ohne Bezug zu Testbedingungen, mit „Überdeckung“ über alle Heuristiken.
- Ein erwartetes Ergebnis raten, weil die Spezifikation schweigt.
- Die ganze Liste stur abarbeiten, statt auf Beobachtungen zu reagieren.
- Sicherheitsfunde nebenbei notieren, aber nicht an den Security Tester übergeben.
- Nach einem Fund weitermachen, ohne dessen Umgebung zu prüfen.
- Session ohne Charter, ohne Notizen, ohne Auswertung.

## 11. Prüfliste

- [ ] Charter und Zeitbox stehen fest.
- [ ] Ideen sind gegen SFDIPOT und die relevanten Fehlerarten gesammelt.
- [ ] Die gewählten Muster sind benannt.
- [ ] Jede Beobachtung hat ein benanntes Orakel oder steht als offene Frage.
- [ ] Funde haben Reproduktionsschritte.
- [ ] Systematische Muster sind als Testbedingungen in den Testentwurf zurückgeführt.
- [ ] Spezifikationslücken stehen in „Offene Fragen“; Sicherheitsfunde sind übergeben.

## 12. Beispiel

Charter: 60 Minuten, „Adressfeld der Kundenmaske auf Datenfehler prüfen“.

| Muster | Versuch | Beobachtung | Orakel |
| --- | --- | --- | --- |
| Goldlöckchen | Ort mit 1, 50, 255 Zeichen | Bei 255 Zeichen überlappt der Text das nächste Feld | Product: andere Masken umbrechen korrekt |
| Null, eins, viele | 0, 1, 2 Telefonnummern | Zweite Nummer wird ohne Kennzeichnung gespeichert | Offene Frage: Welche Nummer ist die Hauptnummer? |
| Unterbrechen | Sitzung während des Speicherns abbrechen | Adresse halb gespeichert (Straße ohne Ort) | Purpose: Datenintegrität; offene Frage an den Fachbereich |
| Eingabemethode | PLZ per Einfügen mit Leerzeichen | Leerzeichen wird nicht entfernt, Versanddienst weist ab | Fachregel: PLZ ohne Leerzeichen |
| Zeichen und Kodierung | Ort „Gütersloh“ mit ü als u + Umlautzeichen | Suche nach „Gütersloh“ findet den Datensatz nicht | User expectations |
| Aushungern | Speicher nahezu voll | Absturz ohne Meldung | Familiarity: fehlende Fehlerbehandlung; Befund |

Rückführung in den Testentwurf:
- „PLZ mit Leerzeichen“ wird Testbedingung, ungültige Klasse „Format“ nach
  `black-box-testdesign/references/aequivalenzklassen-grenzwerte.md`.
- „Unicode-Normalisierung im Ortsnamen“ wird Testbedingung für Suche und Speicherung.
- „Absturz bei vollem Speicher“ ist ein Befund.
- „Reihenfolge mehrerer Telefonnummern“ ist eine offene Frage.
