# Reviewarten, Rollen und Reviewprozess

## Inhalt
1. Reviewarten
2. Rollen
3. Reviewprozess
4. Erfolgsfaktoren
5. Reviews in agilen Teams
6. Kennzahlen
7. Anti-Patterns
8. Prüfliste

## 1. Reviewarten

| Art | Formalität | Leitung | Hauptziel | Typischer Einsatz |
| --- | --- | --- | --- | --- |
| Informelles Review | gering, kein definierter Prozess | Autor oder Kollege | Schnelle Rückmeldung, Fehler finden | Pair Review, Buddy Check, Merge Request mit einem Reviewer |
| Walkthrough | gering bis mittel | Autor | Verständnis, Wissenstransfer, Konsens, Fehler finden | Autor führt Team durch Entwurf, Lösungsansatz, Szenario |
| Technisches Review | mittel bis hoch | Moderator (nicht Autor) | Konsens zu technischem Ansatz, Alternativen bewerten, Fehler finden | Architektur, Design, Schnittstellen, Teststrategie |
| Inspektion | hoch, definierter Prozess, Metriken | ausgebildeter Moderator | Maximale Fehlerfindung, Prozessverbesserung | Sicherheitskritische Anforderungen, Verträge, normrelevante Dokumente |
| Audit | hoch, extern oder unabhängig | Auditor | Konformität mit Standards, Verträgen, Prozessen nachweisen | Prozessaudits, Normkonformität, Assessments |

Wahl: Je höher Risiko, Normanforderung und Kosten eines übersehenen Fehlers, desto formaler.
Für Lernen und Konsens eher Walkthrough; für Fehlerfindung bei kritischen Dokumenten Inspektion.
Mehrere Arten nacheinander sind üblich (informell früh, technisches Review vor Freigabe).

## 2. Rollen

| Rolle | Aufgaben |
| --- | --- |
| Manager | Entscheidet über Reviews, stellt Zeit und Ressourcen bereit, legt Ziele fest |
| Autor | Erstellt das Arbeitsergebnis, behebt Befunde |
| Moderator (Facilitator) | Plant und leitet die Sitzung, sorgt für Fokus, Zeit, Ton, sicheres Klima |
| Protokollant (Scribe) | Sammelt Befunde, hält Entscheidungen fest |
| Gutachter (Reviewer) | Prüft das Arbeitsergebnis aus festgelegter Perspektive, meldet Befunde |
| Review-Leiter | Gesamtverantwortung, Organisation, Teilnehmerauswahl (bei kleinen Reviews oft Moderator) |

In Inspektionen zusätzlich oft **Vorleser** (paraphrasiert das Dokument abschnittsweise),
damit das Team das Dokument in eigener Lesart erlebt und nicht der Autor seine Absicht erklärt.

Gutachter nach Perspektiven auswählen: Tester (Prüfbarkeit), Entwickler (Umsetzbarkeit),
Fachbereich (fachliche Korrektheit), Nutzer, Betrieb, Sicherheit, Datenschutz, Barrierefreiheit.
3–6 Gutachter; mehr erhöht Aufwand stärker als Nutzen.

## 3. Reviewprozess

CTFL 4.0 / ISO/IEC 20246:

1. **Planung:** Umfang, Ziel, Reviewart, Rollen, Eingangs- und Endekriterien, Zeitplan,
   Checklisten, Teilnehmer. Eingangskriterium: Arbeitsergebnis ist vollständig genug und
   formal geprüft (Rechtschreibung, Vorlage) – sonst Zeitverschwendung.
2. **Initiierung (Kick-off):** Teilnehmer erhalten Arbeitsergebnis, Bezugsdokumente, Rollen,
   Perspektiven, Checklisten; kurze Einführung bei Bedarf.
3. **Individuelles Review (Vorbereitung):** Jeder Gutachter prüft allein, notiert Befunde mit
   Fundstelle. Empfohlene Prüfrate z. B. 5–10 Seiten pro Stunde Text, 100–200 Zeilen pro
   Stunde Code (organisationsspezifisch kalibrieren). Hier entsteht der Großteil der Befunde.
4. **Kommunikation und Analyse (Sitzung):** Befunde zusammentragen, Duplikate zusammenführen,
   klären, klassifizieren, Schwere festlegen. Keine Lösungsdiskussion; Sitzung höchstens 2 Stunden.
   Bei informellen Reviews kann die Sitzung entfallen (Kommentare im Werkzeug).
5. **Behebung und Bericht:** Autor bearbeitet Befunde; Moderator prüft Nacharbeit; Entscheidung
   (freigegeben, mit Änderungen, erneutes Review); Kennzahlen; Endekriterien prüfen.

Befundklassen: Fehler (falsch, fehlend, widersprüchlich), Unklarheit (mehrdeutig), Frage,
Verbesserungsvorschlag, Formfehler. Schwere: kritisch, hoch, mittel, gering.

## 4. Erfolgsfaktoren

- Klare Ziele und messbare Endekriterien.
- Passende Reviewart; kleine, handhabbare Portionen statt 200 Seiten auf einmal.
- Ausreichend Vorbereitungszeit im Projektplan.
- Geschulte Moderatoren und Gutachter; Checklisten und Lesetechniken.
- Management unterstützt, nutzt Ergebnisse aber nicht zur Bewertung von Autoren.
- Sicheres Klima: Befunde sind willkommen, Autoren werden geschützt.
- Nacharbeit wird verfolgt; Erkenntnisse fließen in Vorlagen und Checklisten.

## 5. Reviews in agilen Teams

- Story-Refinement mit Three Amigos als informelles Review der Anforderungen (Skill `agile-devops-testing`).
- Merge Requests: jeder Code durch mindestens eine andere Person; klare Review-Checkliste;
  kleine Merge Requests (unter 400 Zeilen ändern); zeitnah (innerhalb eines Arbeitstags).
- Pair Programming als kontinuierliches Review.
- Architektur-Entscheidungen (ADR) mit technischem Review.
- Definition of Ready enthält „Story ist reviewt und testbar“; Definition of Done enthält
  „Code ist reviewt, statische Analyse ohne neue Befunde“.

## 6. Kennzahlen

- Befunde je Seite/LOC, je Stunde Vorbereitung, je Schwere.
- Prüfrate (Seiten/Stunde) und ihr Zusammenhang mit Befunddichte (zu schnell = weniger Befunde).
- Aufwand je Review; eingesparte Kosten (Schätzung über Fehlerkosten je Phase).
- Anteil der Fehler, die in Reviews gegenüber später gefunden werden.

Kennzahlen dienen der Verbesserung des Prozesses, nicht der Bewertung von Autoren.

## 7. Anti-Patterns

- Review ohne Vorbereitung; Gutachter lesen das Dokument erst in der Sitzung.
- Autor moderiert die Inspektion und verteidigt jede Zeile.
- Lösungsdiskussionen in der Sitzung; nach 2 Stunden Seite 3 von 40.
- Zu große Prüfumfänge, zu kurze Zeit.
- Befunde ohne Nachverfolgung.
- Merge-Request-Reviews als Stempel („LGTM“ nach 30 Sekunden bei 2.000 Zeilen).
- Reviewergebnisse in Leistungsbeurteilungen.

## 8. Prüfliste

- [ ] Reviewart passt zu Ziel und Risiko; Eingangskriterien sind erfüllt.
- [ ] Rollen sind besetzt; Moderator ist nicht der Autor (außer informell/Walkthrough).
- [ ] Gutachter haben festgelegte Perspektiven und Checklisten.
- [ ] Individuelles Review vor der Sitzung mit angemessener Prüfrate.
- [ ] Sitzung ohne Lösungsdiskussion, höchstens 2 Stunden.
- [ ] Befunde klassifiziert; Nacharbeit verfolgt; Entscheidung dokumentiert; Kennzahlen erhoben.
