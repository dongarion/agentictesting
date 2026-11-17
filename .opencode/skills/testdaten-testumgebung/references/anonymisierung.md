# Anonymisierung und Pseudonymisierung

Produktionsdaten im Test sind **personenbezogene Datenverarbeitung** und brauchen eine
Rechtsgrundlage. Testen ist kein Selbstzweck, der sie liefert. Der Weg führt über
Anonymisierung (kein Personenbezug mehr, DSGVO nicht anwendbar) oder Pseudonymisierung
(Personenbezug mit Zusatzwissen herstellbar, DSGVO weiter anwendbar, aber Schutzmaßnahme).

Hinweis: Dieses Dokument ersetzt keine Rechtsberatung. Datenschutzbeauftragten einbeziehen.

## Inhalt
1. Rechtlicher Rahmen
2. Anonymisierung vs. Pseudonymisierung
3. Vorgehen
4. Maskierungstechniken
5. Konsistenz und Referenzen
6. Re-Identifikationsrisiko
7. Werkzeuge
8. Anti-Patterns
9. Prüfliste

## 1. Rechtlicher Rahmen

- DSGVO Art. 5 (Zweckbindung, Datenminimierung), Art. 25 (Datenschutz durch Technikgestaltung),
  Art. 32 (Sicherheit der Verarbeitung; Pseudonymisierung ausdrücklich genannt).
- Erwägungsgrund 26: Anonyme Daten fallen nicht unter die DSGVO; Maßstab sind die Mittel,
  die „vernünftigerweise“ zur Re-Identifikation genutzt werden könnten.
- Besondere Kategorien (Art. 9: Gesundheit, Religion, Herkunft u. a.) und Sozialdaten
  (SGB X) mit erhöhtem Schutz; im Behördenumfeld häufig. Hier nahezu immer synthetisch.
- Verarbeitungsverzeichnis, ggf. Datenschutz-Folgenabschätzung, Auftragsverarbeitung bei
  externen Testdienstleistern und Cloud-Umgebungen.
- Vorgaben des Kunden (Sicherheitskonzept, VS-Einstufung) können strenger sein.

## 2. Anonymisierung vs. Pseudonymisierung

| | Anonymisierung | Pseudonymisierung |
| --- | --- | --- |
| Personenbezug | irreversibel entfernt | mit Schlüssel/Zuordnungstabelle herstellbar |
| DSGVO | nicht mehr anwendbar (wenn wirksam) | anwendbar, Schutzmaßnahme |
| Testeignung | gut für Funktion, Last, Migration | nötig, wenn Rückverfolgung zum Original gebraucht wird (Fehleranalyse mit Produktion) |
| Aufwand | hoch, Nachweis der Wirksamkeit | mittel, Schlüsselverwaltung |
| Typisch | Testumgebungen allgemein | Abnahme mit Fachbereich, Produktionsfehleranalyse |

In der Praxis sind viele „anonymisierte“ Testdaten nur pseudonymisiert, weil Quasi-Identifikatoren
(Geburtsdatum, PLZ, Geschlecht) erhalten bleiben. Dann gelten die Pflichten der DSGVO weiter.

## 3. Vorgehen

1. **Datenklassifikation:** Jede Tabelle und Spalte: direkter Identifikator (Name, ID, E-Mail),
   Quasi-Identifikator (Geburtsdatum, PLZ, Beruf), sensibles Attribut (Diagnose, Einkommen),
   unkritisch. Auch Freitextfelder, Dokumente, Logs, Anhänge, Metadaten.
2. **Testanforderung:** Welche Eigenschaften müssen erhalten bleiben (Format, Verteilung,
   Prüfziffern, Beziehungen, Zeitabstände)?
3. **Regelwerk:** Je Spalte eine Technik (siehe 4) und Konsistenzregel (siehe 5).
4. **Umsetzung:** Maskierung in einer gesicherten Zwischenumgebung, nie auf dem Zielsystem
   mit Zugriff der Tester vorher.
5. **Prüfung:** Automatisierte Tests des Maskierungsergebnisses: keine Originalwerte mehr,
   Formate gültig, Referenzen intakt, Stichproben manuell.
6. **Freigabe** durch Datenschutzbeauftragten; Dokumentation des Verfahrens.
7. **Wiederholbarkeit:** Lauf skriptbasiert, versioniert, bei Schemaänderung angepasst.

## 4. Maskierungstechniken

| Technik | Beschreibung | Eignung |
| --- | --- | --- |
| Löschen/Nullen | Wert entfernen | Wenn Tests den Wert nicht brauchen |
| Substitution | Ersatz aus Wörterbuch (Namen, Orte, Firmen) | Namen, Adressen; realistisch, formattreu |
| Shuffling | Werte innerhalb der Spalte vertauschen | Verteilung erhalten; Vorsicht bei Korrelation mit anderen Spalten |
| Generalisierung | Geburtsdatum → Jahr, PLZ → Region, Betrag → Klasse | Quasi-Identifikatoren entschärfen |
| Rauschen/Perturbation | Zufälligen Offset addieren | Beträge, Messwerte, Daten; Beziehungen prüfen |
| Formatbewahrende Verschlüsselung (FPE) | Chiffrat mit gleichem Format | IDs, Kontonummern, konsistent über Systeme |
| Hashing mit Salt | Deterministisches Pseudonym | Verknüpfbarkeit über Tabellen; Salt geheim halten |
| Tokenisierung | Zuordnungstabelle in Tresor | Pseudonymisierung mit Rückweg |
| Synthese | Wert komplett neu erzeugen | Freitext, Dokumente, Bilder |
| Datumsverschiebung | Alle Daten eines Datensatzes um gleichen Offset | Zeitabstände bleiben konsistent |

Freitexte (Bemerkungsfelder, Notizen, Dokumente) sind die größte Gefahr: Sie enthalten
Namen, Diagnosen, Aktenzeichen. Entweder löschen, synthetisch ersetzen oder mit NER-Werkzeugen
erkennen und maskieren; Ergebnis stichprobenartig prüfen.

## 5. Konsistenz und Referenzen

- Dieselbe Person muss in allen Tabellen und Systemen dasselbe Pseudonym erhalten
  (deterministische Verfahren, gemeinsamer Schlüssel).
- Fremdschlüssel, Prüfziffern (IBAN, Steuer-ID, Versicherungsnummer), Plausibilitäten
  (Geburtsdatum vor Vertragsdatum) müssen nach der Maskierung gültig sein.
- Schnittstellenpartner und Testumgebungen anderer Systeme mit derselben Regel maskieren,
  sonst brechen Integrationstests.
- Aggregierte Werte und Summen nach Perturbation neu berechnen oder akzeptierte Abweichung dokumentieren.

## 6. Re-Identifikationsrisiko

- Prüfen auf Eindeutigkeit von Quasi-Identifikator-Kombinationen (k-Anonymität: jede
  Kombination mindestens k-mal), Vielfalt sensibler Attribute je Gruppe (l-Diversität).
- Seltene Konstellationen (einziger Fall mit bestimmter Kombination) sind besonders riskant;
  generalisieren oder entfernen.
- Hintergrundwissen der Tester berücksichtigen: Sachbearbeiter erkennen ihre Fälle auch an
  Vorgangsmustern.
- Ergebnis dokumentieren; bei Restrisiko Pseudonymisierung mit Zugriffsschutz statt Anonymisierungsbehauptung.

## 7. Werkzeuge

| Werkzeug | Hinweis |
| --- | --- |
| ARX | Open Source, Anonymisierung mit k-Anonymität u. a., Risikoanalyse |
| Amnesia | Open Source, EU-gefördert |
| Microsoft Presidio | Erkennung und Maskierung von PII in Text, Open Source |
| Datenbank-eigene Funktionen | Oracle Data Masking, SQL Server Dynamic Data Masking, PostgreSQL Anonymizer |
| Kommerziell | Delphix, Informatica, IBM Optim, Broadcom TDM, Tonic, K2view |
| Eigene Skripte | Für kleine Schemata ausreichend; Regeln versionieren |

## 8. Anti-Patterns

- Nur Namen ersetzen, Geburtsdatum und Adresse lassen.
- Maskierung auf der Zielumgebung, auf die Tester schon Zugriff haben.
- Freitextfelder vergessen.
- Shuffling von Diagnosen bei erhaltenem Alter und PLZ.
- „Anonymisiert“ behaupten ohne Risikoanalyse.
- Maskierungsskript einmal geschrieben, nie an Schemaänderungen angepasst.

## 9. Prüfliste

- [ ] Alle Spalten, Freitexte, Dokumente und Logs sind klassifiziert.
- [ ] Je Spalte Technik und Konsistenzregel dokumentiert.
- [ ] Maskierung läuft in gesicherter Zwischenumgebung, skriptbasiert, versioniert.
- [ ] Automatisierte Prüfung: keine Originalwerte, Formate und Referenzen gültig.
- [ ] Re-Identifikationsrisiko bewertet; Restrisiko dokumentiert.
- [ ] Freigabe durch Datenschutzbeauftragten liegt vor; Verfahren ist im Verarbeitungsverzeichnis.
- [ ] Löschfristen für maskierte Bestände sind festgelegt.
