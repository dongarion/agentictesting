# Testdatenmanagement

## Inhalt
1. Datenkategorien
2. Quellen und ihre Eignung
3. Lebenszyklus
4. Bereitstellung
5. Testdaten und Testfälle verknüpfen
6. Organisation
7. Anti-Patterns
8. Prüfliste

## 1. Datenkategorien

| Kategorie | Beispiele | Besonderheit |
| --- | --- | --- |
| Referenz-/Stammdaten | Kataloge, Tarife, Postleitzahlen, Rollen | Stabil, versionieren, mit Produktion abgleichen |
| Bewegungs-/Transaktionsdaten | Anträge, Bestellungen, Buchungen | Werden von Tests erzeugt und verändert; zurücksetzbar halten |
| Konfigurationsdaten | Feature-Toggles, Mandanteneinstellungen, Schnittstellenparameter | Teil der Umgebungsdefinition |
| Benutzer und Berechtigungen | Testkonten je Rolle | Keine echten Personen; Passwörter im Secret Store |
| Umgebungsdaten | Zertifikate, Schlüssel, Endpunkte | Getrennt verwalten, Ablaufdaten überwachen |
| Eingabedaten für Testfälle | Werte aus Äquivalenzklassen und Grenzwerten | Gehören zum Testentwurf |
| Große Bestände | Last- und Performancetests, Migration | Volumen und Verteilung realistisch |

## 2. Quellen und ihre Eignung

| Quelle | Vorteile | Nachteile | Typischer Einsatz |
| --- | --- | --- | --- |
| Handgepflegt | Zielgenau | Aufwändig, veraltet schnell | Kleine Stamm- und Referenzdaten, Grenzfälle |
| Synthetisch generiert | Datenschutzfrei, beliebig, reproduzierbar | Realitätsnähe begrenzt, Korrelationen fehlen | Standard für Funktions-, API-, Lasttests |
| Produktion, anonymisiert/pseudonymisiert | Realistisch, vollständig, seltene Konstellationen | Datenschutzaufwand, Re-Identifikationsrisiko, Volumen | Migration, Abnahme, Fehleranalyse, Performance |
| Produktion, Subset | Handhabbar | Konsistenz schwierig | Kombination mit Maskierung |
| Aufgezeichnet (Schnittstellen) | Echte Formate | Bereinigen nötig | Virtualisierung, Vertragsprüfung |

Entscheidungsregel: synthetisch, wenn möglich; Produktion nur mit Maskierung, Freigabe und
nachgewiesenem Bedarf, den synthetische Daten nicht decken.

## 3. Lebenszyklus

1. **Anforderung:** Welcher Test braucht welche Daten, in welcher Menge, mit welchen Eigenschaften?
2. **Entwurf:** Datenmodell der Testdaten, Konstellationen (Standard, Grenzfall, Fehlerfall),
   Namensschema, Kennzeichnung als Testdaten.
3. **Erzeugung:** Skript, Generator, Maskierungslauf. Reproduzierbar mit Seed oder Version.
4. **Bereitstellung:** In Umgebung einspielen, Prüfung auf Konsistenz und Vollständigkeit.
5. **Nutzung:** Tests lesen, erzeugen, ändern. Isolation zwischen Tests und Teams.
6. **Rücksetzung:** Definierter Ausgangszustand per Skript (Snapshot, Neuaufbau, Transaktions-Rollback).
7. **Archivierung oder Löschung:** Nach Testende; personenbezogene Daten nach Löschfrist.

## 4. Bereitstellung

- **Datenbank-Snapshots:** schnell, vollständig; bei Schemaänderungen pflegen.
- **Skriptbasiert (SQL, Migrationen, Fixtures):** versionierbar, nachvollziehbar; bei großen
  Mengen langsam.
- **Über die Anwendungs-API:** fachlich konsistent, validiert; langsam, aber korrekt.
  Bevorzugt für Bewegungsdaten in Automatisierung.
- **Container mit vorgeladenen Daten:** reproduzierbar je Lauf; Image-Pflege.
- **Testdatenservice:** zentrale API, die auf Anfrage passende Datensätze liefert oder
  erzeugt („gib mir einen Kunden mit zwei offenen Anträgen“); lohnt bei vielen Teams.
- **Selbstbedienung:** Tester können Daten selbst anfordern und zurücksetzen, ohne Ticket.

## 5. Testdaten und Testfälle verknüpfen

- Jeder Testfall benennt seine Datenanforderung (Konstellation, nicht konkreten Datensatz).
- Konstellationen zentral beschrieben und benannt (`KUNDE_PREMIUM_MIT_MAHNUNG`).
- Testfall → Konstellation → Erzeugungsskript nachvollziehbar.
- Datenänderungen (Tarifwechsel, neue Pflichtfelder) lösen Prüfung betroffener Testfälle aus.

## 6. Organisation

- **Testdatenmanager** oder Verantwortlicher je System: Besitz, Freigabe, Pflege, Ansprechpartner.
- Abstimmung mit Datenschutzbeauftragtem, Betrieb, Fachbereich (Fachlichkeit der Daten).
- Regeln dokumentiert: Was darf in welche Umgebung, wer darf anfordern, wie lange bleibt es.
- Testdaten im Konfigurationsmanagement wie Testfälle und Code.

## 7. Anti-Patterns

- Produktionskopie „schnell mal“ auf die Testumgebung ohne Maskierung.
- Ein goldener Datensatz, den alle teilen und verändern.
- Testdaten nur im Kopf eines Testers.
- Testkonten mit echten Namen von Mitarbeitenden.
- Keine Rücksetzung; Umgebung verschlammt, Tests werden angepasst statt die Daten.
- Testdaten im Code hartkodiert mit Produktions-IDs.

## 8. Prüfliste

- [ ] Datenkategorien und Schutzbedarf sind erfasst.
- [ ] Quelle je Kategorie ist gewählt und begründet.
- [ ] Erzeugung ist skriptbasiert und reproduzierbar.
- [ ] Rücksetzung auf Ausgangszustand ist automatisiert.
- [ ] Konstellationen sind benannt und mit Testfällen verknüpft.
- [ ] Besitzer, Freigabe und Löschfristen sind festgelegt.
