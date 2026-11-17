# Pair- und Mob-Testing

Gemeinsames Testen an einem Bildschirm. Ziel: **mehr Perspektiven, schnellere
Wissensverteilung, höhere Befundqualität.** Keine Effizienzmaßnahme im Sinne von
Personenstunden, sondern eine Qualitäts- und Lernmaßnahme.

## Inhalt
1. Pair Testing
2. Mob Testing (Ensemble Testing)
3. Formate und Rollen
4. Wann einsetzen
5. Moderation
6. Anti-Patterns
7. Prüfliste

## 1. Pair Testing

Zwei Personen, eine Tastatur, ein Charter.

- **Tester + Entwickler:** Entwickler kennt die Implementierung und ihre Risikostellen, Tester
  bringt Testideen und Nutzersicht. Sehr effektiv direkt nach Fertigstellung einer Story
  („Desk Check“, „Show me“), bevor sie in den formalen Test geht.
- **Tester + Fachexperte:** Fachexperte erkennt fachlich falsche Ergebnisse, die der Tester
  für plausibel hält.
- **Tester + Tester:** Einarbeitung, schwierige Bereiche, gegenseitiges Lernen von Heuristiken.
- **Tester + UX/Support/Betrieb:** andere Qualitätsmerkmale im Fokus.

Rollen: **Driver** bedient, **Navigator** denkt voraus, notiert, schlägt vor.
Alle 15–25 Minuten wechseln.

## 2. Mob Testing (Ensemble Testing)

Ganzes Team oder 4–8 Personen, ein Bildschirm, 60–120 Minuten.

- Starker Lerneffekt: Jeder sieht, wie andere testen, denken, Werkzeuge nutzen.
- Geeignet zum Kickoff eines neuen Features, für Bug Bashes vor dem Release, zur Einführung
  explorativen Testens, für schwierige Integrationsszenarien.
- Format nach Hunter/Zuill (Mob Programming) übertragen:
  - **Driver:** bedient, denkt nicht selbst, setzt um, was der Navigator sagt.
  - **Navigator:** eine Person, gibt Anweisungen in Fachsprache („Lege einen Antrag mit leerem
    Datum an“), nicht in Klicks.
  - **Mob:** beobachtet, schlägt dem Navigator vor, notiert Befunde und Ideen.
  - Rotation alle 5–10 Minuten (Timer), Driver wird Mob, nächster wird Driver, nächster Navigator.
- Regel „Strong Style“: Eine Idee muss durch die Hände einer anderen Person gehen.
  Das zwingt zum Aussprechen und macht Denken sichtbar.

## 3. Formate und Rollen

| Format | Teilnehmer | Dauer | Zweck |
| --- | --- | --- | --- |
| Desk Check / Show me | Entwickler + Tester (+ PO) | 15 min | Story vor Übergabe gemeinsam durchgehen |
| Pair-Session | 2 | 60–90 min | Charter zu zweit |
| Bug Bash | Team + Gäste | 60–120 min | Breite Suche vor Release, mit Preis für den besten Fund |
| Mob-Session | 4–8 | 60–120 min | Lernen, schwierige Bereiche, Kickoff |
| Test Dojo | Team | 60 min | Übungsformat an einer Übungsanwendung |

## 4. Wann einsetzen

- Neue Teammitglieder einarbeiten.
- Wissen über ein Modul liegt bei einer Person.
- Formale Tests sind grün, trotzdem Unbehagen.
- Vor Releases mit hohem Risiko.
- Teams, die „Testen ist Sache des Testers“ denken.

Nicht einsetzen: für Routinedurchläufe, die automatisiert gehören; als Dauerzustand ohne
Einzelarbeit.

## 5. Moderation

- Charter und Zeitbox vorher festlegen (siehe Skill exploratives Testen).
- Befunde sofort an einer sichtbaren Stelle sammeln (Board, Dokument), erst nach der Session
  ins Fehlermanagement übertragen.
- Psychologische Sicherheit: Kein Befund ist peinlich, der Code gehört dem Team.
- Debriefing: Was haben wir gelernt, was nehmen wir mit, welche Charters folgen?
- Remote: Bildschirmfreigabe mit Steuerungsübergabe, gemeinsames Notizdokument, kürzere
  Rotation, Kamera an.

## 6. Anti-Patterns

- Navigator klickt selbst; Driver ist nur Zuschauer.
- Eine Person dominiert, andere schauen zu.
- Keine Notizen; am Ende weiß niemand, was geprüft wurde.
- Mob als Meeting ohne Tastatur.
- Pairing als Überwachung von Junioren.

## 7. Prüfliste

- [ ] Charter, Zeitbox und Rotation sind festgelegt.
- [ ] Rollen Driver/Navigator sind besetzt und wechseln.
- [ ] Befunde und Ideen werden sichtbar mitgeschrieben.
- [ ] Debriefing findet statt, Folge-Charters sind abgelegt.
- [ ] Befunde sind ins Fehlermanagement übertragen.
