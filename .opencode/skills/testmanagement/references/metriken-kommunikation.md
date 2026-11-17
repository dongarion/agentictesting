# Testmetriken, Stakeholder-Kommunikation und Teamführung

## Inhalt
1. Metriken auswählen (GQM)
2. Metrikkatalog
3. Stakeholder-Analyse
4. Kommunikation je Zielgruppe
5. Business Case des Testens
6. Teamführung
7. Anti-Patterns
8. Prüfliste

## 1. Metriken auswählen (Goal-Question-Metric)

1. **Ziel:** Was wollen wir erreichen oder wissen? („Freigabefähigkeit von Release 3 beurteilen“)
2. **Fragen:** Was müssen wir dafür beantworten? („Sind die A-Risiken getestet? Welche kritischen Fehler sind offen?“)
3. **Metriken:** Welche Daten beantworten die Fragen? („Abdeckung A-Risiken in %, offene Fehler Klasse 1“)

Jede Metrik hat Definition, Formel, Datenquelle, Erhebungsfrequenz, Verantwortlichen, Zielwert
oder Interpretationshilfe. Wenige Metriken, die genutzt werden, schlagen viele, die nur erhoben werden.

## 2. Metrikkatalog

| Kategorie | Beispiele |
| --- | --- |
| Projektfortschritt | Testfälle ausgeführt/geplant, bestanden; Burn-up; Aufwand Ist/Plan |
| Produktqualität | Offene Fehler je Schwere, Fehlerdichte je Komponente, Restrisiko je Klasse, Zuverlässigkeit (MTBF) |
| Testabdeckung | Anforderungs-, Risiko-, Codeüberdeckung |
| Testwirksamkeit | Defect Detection Percentage, Escapes in Produktion, Mutationswert |
| Testeffizienz | Kosten je gefundenem Fehler, Durchlaufzeit Regression, Automatisierungsnutzen |
| Prozess | Behebungszeit, Wiedereröffnungsquote, Ablehnungsquote, Flaky-Rate, Umgebungsausfallzeit |
| Team | Auslastung, Weiterbildung, Zufriedenheit (vertraulich, nicht als Leistungsbewertung) |

## 3. Stakeholder-Analyse

| Stakeholder | Interesse | Einfluss | Informationsbedarf | Kanal/Frequenz |
| --- | --- | --- | --- | --- |
| Auftraggeber / Lenkungsausschuss | Termin, Kosten, Freigabe | hoch | Ampel, Restrisiko, Entscheidungsbedarf | monatlich, Meilenstein |
| Projektleitung | Plan, Risiken | hoch | Fortschritt, Blocker, Prognose | wöchentlich |
| Fachbereich / PO | Fachliche Korrektheit, Abnahme | hoch | Fehler fachlich, Abnahmestand | Sprint, Gremium |
| Entwicklung | Fehler, Stabilität | mittel | Fehlerdetails, Pipeline-Status | täglich |
| Betrieb | Betriebsfähigkeit | mittel | Performance, Betriebstests, bekannte Probleme | Meilenstein |
| Datenschutz / IT-Sicherheit | Konformität | mittel | Testdaten, Sicherheitstests | anlassbezogen |
| Testteam | Klarheit, Entwicklung | – | Ziele, Prioritäten, Feedback | täglich |

## 4. Kommunikation je Zielgruppe

- **Management:** Kernaussage zuerst, Ampel mit Begründung, Restrisiko in Geschäftssprache
  („Fristberechnung ungetestet für Schaltjahre: Risiko falscher Bescheide“), Optionen mit
  Folgen, klare Bitte um Entscheidung. Eine Seite.
- **Fachbereich:** Fehler in Fachsprache, Auswirkungen auf Prozesse, was sie prüfen sollen.
- **Entwicklung:** Präzise, technisch, mit Belegen, ohne Wertung.
- Schlechte Nachrichten: früh, persönlich vor schriftlich, mit Fakten und Vorschlag.
- Konflikte (Termin gegen Qualität): Entscheidung nicht selbst treffen, sondern Entscheider mit
  Risiken und Optionen in die Lage versetzen; Entscheidung dokumentieren.

## 5. Business Case des Testens

- Kosten des Testens: Personal, Werkzeuge, Umgebungen, Zeit.
- Nutzen: vermiedene Fehlerkosten (Fehler in Produktion kosten ein Vielfaches gegenüber früher
  Entdeckung; Größenordnung organisationsspezifisch belegen), vermiedene Rechts-, Datenschutz-
  und Reputationsschäden, schnellere Releases durch Automatisierung, Nachweise für Audits.
- Argumente mit eigenen Daten (Produktionsvorfälle, Fehlerkosten, Release-Dauer) statt mit
  allgemeinen Studien.

## 6. Teamführung

- **Rollen und Kompetenzen:** Kompetenzmatrix (Rolle × Fähigkeit), Lücken, Entwicklungspläne,
  Zertifizierungen (ISTQB-Pfade).
- **Arbeitsorganisation:** klare Ziele, Prioritäten, Eigenverantwortung; Pairing für Wissenstransfer.
- **Motivation:** sinnvolle Arbeit (exploratives Testen, Automatisierung), Anerkennung von
  Befunden, Schutz vor Schuldzuweisung.
- **Verteilte Teams und Dienstleister:** klare Schnittstellen, gemeinsame Werkzeuge, Vereinbarungen
  zu Qualität der Ergebnisse, regelmäßige Abstimmung, kulturelle Unterschiede beachten.
- **Unabhängigkeit:** Grad der Unabhängigkeit nach Risiko wählen (Entwickler, Teamkollege,
  separates Testteam, externer Dienstleister); Vorteile (Objektivität) und Nachteile (Isolation,
  Wissensverlust) abwägen.

## 7. Anti-Patterns

- Metriken ohne Ziel; Datensammlung um ihrer selbst willen.
- Eine Metrik als Ziel (Goodhart): „90 % Testfälle bestanden“ fördert triviale Testfälle.
- Gleicher Bericht für alle Zielgruppen.
- Schlechte Nachrichten verzögert, bis sie unvermeidbar sind.
- Tester an Fehlerzahl messen.

## 8. Prüfliste

- [ ] Metriken sind nach GQM abgeleitet und definiert.
- [ ] Stakeholder sind mit Interessen, Informationsbedarf und Kanal erfasst.
- [ ] Berichte sind je Zielgruppe zugeschnitten; Management-Bericht passt auf eine Seite.
- [ ] Entscheidungen bei Zielkonflikten sind mit Optionen vorbereitet und dokumentiert.
- [ ] Business Case nutzt eigene Daten.
- [ ] Kompetenzentwicklung des Teams ist geplant.
