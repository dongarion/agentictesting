# Lesetechniken und Checklisten

## Inhalt
1. Lesetechniken
2. Checkliste Anforderungen und Spezifikationen
3. Checkliste User Stories und Akzeptanzkriterien
4. Checkliste Architektur und Entwurf
5. Checkliste Code
6. Checkliste Testfälle und Testkonzepte
7. Typische Mehrdeutigkeiten in Anforderungen
8. Prüfliste

## 1. Lesetechniken

| Technik | Prinzip | Eignung |
| --- | --- | --- |
| Ad hoc | Ohne Anleitung lesen | Nur informell; abhängig von Erfahrung |
| Checklistenbasiert | Fragenkatalog abarbeiten | Standard; Checklisten kurz und aktuell halten |
| Szenariobasiert | Dokument anhand von Nutzungsszenarien durchspielen („Was passiert, wenn ein Bürger …“) | Anforderungen, Prozesse, Use Cases |
| Perspektivenbasiert | Jeder Gutachter liest aus einer Rolle und erzeugt dabei ein Artefakt (Tester: Testfälle; Entwickler: Entwurfsskizze; Nutzer: Bedienablauf) | Höchste Wirksamkeit bei Anforderungen; unterschiedliche Fehlerklassen |
| Rollenbasiert | Lesen als bestimmter Nutzertyp (Anfänger, Experte, Admin, Angreifer, Nutzer mit Screenreader) | Usability, Sicherheit, Barrierefreiheit |

Perspektivenbasiertes Lesen ist für Tester besonders wirksam: Wer beim Lesen Testfälle
ableitet, stolpert sofort über fehlende Grenzwerte, unklare Fehlerreaktionen und undefinierte Zustände.

## 2. Checkliste Anforderungen und Spezifikationen

Angelehnt an Qualitätskriterien für Anforderungen (ISO/IEC/IEEE 29148):

- [ ] **Eindeutig:** Nur eine Interpretation möglich? (siehe 7)
- [ ] **Vollständig:** Normalfall, Sonderfälle, Fehlerfälle, Grenzen, alle Rollen beschrieben?
- [ ] **Widerspruchsfrei:** Keine Konflikte mit anderen Anforderungen, Glossar, Gesetzen?
- [ ] **Prüfbar:** Messbares Akzeptanzkriterium vorhanden? Kann ich einen Testfall schreiben?
- [ ] **Notwendig:** Begründung und Quelle bekannt?
- [ ] **Machbar:** Technisch und wirtschaftlich umsetzbar?
- [ ] **Atomar:** Eine Anforderung je Aussage?
- [ ] **Rückverfolgbar:** ID, Quelle, Priorität, Verknüpfungen?
- [ ] **Lösungsneutral:** Beschreibt was, nicht wie (außer bei Vorgaben)?
- [ ] Nicht-funktionale Anforderungen messbar (Zahl, Einheit, Messverfahren)?
- [ ] Begriffe im Glossar definiert und konsistent verwendet?
- [ ] Datenschutz, Sicherheit, Barrierefreiheit, Betrieb berücksichtigt?

## 3. Checkliste User Stories und Akzeptanzkriterien

- [ ] Rolle, Ziel und Nutzen klar („Als … möchte ich …, damit …“)?
- [ ] INVEST: unabhängig, verhandelbar, wertvoll, schätzbar, klein, testbar?
- [ ] Akzeptanzkriterien konkret, mit Beispielen, inklusive Fehlerfälle und Grenzen?
- [ ] Nicht-funktionale Erwartungen genannt (Antwortzeit, Barrierefreiheit, Berechtigungen)?
- [ ] Abhängigkeiten und Annahmen sichtbar?
- [ ] Offene Fragen geklärt, bevor die Story in den Sprint geht?

## 4. Checkliste Architektur und Entwurf

- [ ] Anforderungen (funktional und Qualitätsziele) nachvollziehbar abgedeckt?
- [ ] Schnittstellen vollständig spezifiziert (Format, Fehler, Timeouts, Versionen)?
- [ ] Fehlerbehandlung, Wiederholungen, Fallbacks, Transaktionen beschrieben?
- [ ] Sicherheitsarchitektur: Vertrauensgrenzen, Authentifizierung, Autorisierung, Verschlüsselung?
- [ ] Skalierung, Lastannahmen, Engpässe benannt?
- [ ] Betrieb: Deployment, Monitoring, Logging, Backup, Updates?
- [ ] Testbarkeit: Isolierbarkeit, Testhaken, Testumgebungen, Testdaten?
- [ ] Architekturentscheidungen mit Alternativen und Begründung (ADR)?

## 5. Checkliste Code

- [ ] Erfüllt der Code die Anforderung? Fehlende Fälle?
- [ ] Fehler- und Grenzfälle behandelt (null, leer, Überlauf, Timeout, Nebenläufigkeit)?
- [ ] Eingaben validiert, Ausgaben kodiert, keine Geheimnisse im Code, keine unsicheren Funktionen?
- [ ] Ressourcen werden freigegeben (Dateien, Verbindungen, Sperren)?
- [ ] Verständlich: Namen, Struktur, Komplexität, Kommentare wo nötig?
- [ ] Keine Duplikate, keine toten Codeteile?
- [ ] Tests vorhanden und aussagekräftig (Assertions, Grenzfälle)?
- [ ] Logging angemessen, ohne personenbezogene Daten?
- [ ] Konform zu Konventionen und Architekturregeln?

Werkzeuge erledigen Formatierung und viele Regeln; Menschen konzentrieren sich auf Logik,
Entwurf, Sicherheit, Verständlichkeit.

## 6. Checkliste Testfälle und Testkonzepte

- [ ] Bezug zu Anforderung und Risiko vorhanden?
- [ ] Erwartetes Ergebnis konkret und aus der Testbasis belegt?
- [ ] Vorbedingungen und Testdaten vollständig?
- [ ] Verfahren angemessen; Grenzen und Fehlerfälle abgedeckt?
- [ ] Schritte verständlich und reproduzierbar für andere?
- [ ] Testkonzept: messbare Endekriterien, Rollen, Umgebung, Risiken, Zeitplan?

## 7. Typische Mehrdeutigkeiten in Anforderungen

| Muster | Beispiel | Frage |
| --- | --- | --- |
| Vage Adjektive | schnell, benutzerfreundlich, sicher, flexibel, robust | Woran messen wir das? |
| Unklare Mengen | einige, mehrere, viele, meist, ca. | Wie viele genau? |
| Offene Grenzen | bis, zwischen, ab, innerhalb von | Inklusive oder exklusiv? |
| Zeitangaben | sofort, zeitnah, regelmäßig, täglich | Wie lange? Wann genau? Welche Zeitzone? |
| Pronomen | es, dieser, er | Worauf bezieht sich das? |
| Passiv ohne Akteur | Der Antrag wird geprüft. | Wer prüft? System oder Mensch? |
| Und/Oder | Nutzer und Administratoren oder Gäste … | Logische Klammerung? |
| Platzhalter | TBD, usw., etc., ggf. | Was fehlt? |
| Negationen | nicht unzulässig | Positiv formulieren |
| Universalaussagen | immer, nie, alle, jeder | Wirklich ohne Ausnahme? |
| Unterspezifizierter Fehlerfall | Bei ungültiger Eingabe erfolgt eine Meldung. | Welche Meldung, welcher Zustand danach? |

## 8. Prüfliste

- [ ] Lesetechnik ist je Gutachter festgelegt; perspektivenbasiert bei Anforderungen.
- [ ] Passende Checkliste ist ausgewählt, kurz und aktuell.
- [ ] Mehrdeutigkeitsmuster wurden systematisch gesucht.
- [ ] Befunde aus Checklisten fließen in Vorlagen und Checklisten zurück.
