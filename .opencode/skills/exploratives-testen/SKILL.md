---
name: exploratives-testen
description: >
  Plant, führt durch und dokumentiert erfahrungsbasiertes Testen: exploratives Testen mit
  Test-Charters und Sessions (SBTM), intuitive Testfallermittlung (Error Guessing),
  Fehlerangriffe (Fault Attacks), checklistenbasiertes und tour-basiertes Testen. Verwenden,
  wenn eine Spezifikation fehlt, dünn oder veraltet ist, wenn ein neues Feature schnell bewertet
  werden soll, wenn systematische Tests "grün" sind und trotzdem Zweifel bestehen, oder bei
  Stichworten wie "exploratives Testen", "Charter", "Session", "Touren", "Error Guessing",
  "Fehlerangriff", "Testideen", "Heuristiken", "Bug Hunt". Nicht für den formalen
  Überdeckungsnachweis gegen eine Spezifikation.
license: CC BY-SA 4.0. Siehe LICENSE.txt
metadata:
  author: "IT-Beratung Martin Klein"
  copyright: "© 2026 IT-Beratung Martin Klein"
  version: "1.0"
  basis: "ISTQB CTFL 4.0 Kap. 4.4, CTAL-TA Kap. 3.3, Bach/Bolton (RST), Whittaker (Exploratory Software Testing), Hendrickson (Explore It!)"
  sprache: "de"
---

# Exploratives und erfahrungsbasiertes Testen

Du testest **gleichzeitig lernend, entwerfend und ausführend**. Die nächste Testidee entsteht
aus dem Ergebnis der letzten. Dein Werkzeug ist nicht die Tabelle, sondern die Frage
„Was, wenn …?“ und die Disziplin, Beobachtungen festzuhalten.

Die einzelnen Techniken stehen in `references/`. Lade nur, was die Session braucht.

## Haltung

Exploratives Testen belohnt eine andere Denkweise als der systematische Testentwurf.
Nimm sie bewusst ein und halte sie bewusst im Zaum:

- **Assoziative Neugier.** Lass dich von Auffälligkeiten ablenken. Ein seltsamer Ladebalken,
  ein Feld, das kurz flackert, ein Tooltip mit Tippfehler: alles sind Spuren. Folge ihnen,
  auch wenn sie nicht zum Charter passen, und notiere den Abstecher.
- **Über den Tellerrand.** Denke in Rollen, die niemand vorgesehen hat: der ungeduldige Nutzer,
  der Nutzer mit 200 offenen Tabs, der Praktikant mit Admin-Rechten, der Bot, das Zeitzonen-
  Opfer, der Kollege, der gleichzeitig dasselbe bearbeitet.
- **Mustererkennung statt Prüfliste.** Frage dich bei jedem Befund: Wo im System könnte derselbe
  Fehlertyp noch stecken? Ein Fehler ist selten allein.
- **Kritische Distanz zum Produkt.** Du bist nicht da, um zu bestätigen, dass es funktioniert.
  Du bist da, um herauszufinden, wie es scheitert, und zu berichten, was das bedeutet.
- **Disziplin als Gegengewicht.** Das Verträumte braucht einen Rahmen: Charter, Zeitbox,
  Notizen, Debriefing. Ohne diese Disziplin ist exploratives Testen nur Herumklicken.
  Mit ihr ist es die effizienteste Technik, um Unbekanntes zu finden.
- **Ehrlichkeit über Überdeckung.** Du kannst nicht beziffern, was du *nicht* gesehen hast.
  Berichte, was du untersucht hast, wie tief, und wo du nicht warst.

## Vorgehen

### 1. Auftrag klären

- Was ist das Testobjekt, welcher Stand, welche Umgebung?
- Welche Risiken oder Sorgen treiben den Auftrag? Welche Informationen braucht wer?
- Gibt es Spezifikation, Story, Changelog, Fehlerhistorie, Nutzerbeschwerden? Alles lesen,
  aber nicht als Grenze verstehen.
- Zeitbudget festlegen.

### 2. Charters planen

- Aus Risiken, Produktbereichen und Qualitätsmerkmalen Charters formulieren, je Session einer.
  Format und Priorisierung: [charter-und-session.md](references/charter-und-session.md).
- Charters nach Risiko ordnen; wichtigste zuerst, Rest in eine Charter-Backlog-Liste.

### 3. Technik je Charter wählen

| Situation | Technik | Referenz |
| --- | --- | --- |
| Strukturierter Rahmen für jede Session | SBTM: Charter, Zeitbox, Notizen, Debrief | [charter-und-session.md](references/charter-und-session.md) |
| Ideen sammeln, Orakel ohne Spezifikation, Grenz- und Angriffswerte nach Fehlerart, Variationsmuster, Fehlerkategorien | Testheuristiken (SFDIPOT, HICCUPPS, Angriffswerte nach Fehlerart, Kaner) | [heuristiken.md](references/heuristiken.md) |
| Breite Abdeckung eines unbekannten Produkts in kurzer Zeit | Touren (Whittaker) | [touren.md](references/touren.md) |
| Typische Fehlerarten einer Technologie gezielt provozieren | Fehlerangriffe, Error Guessing | [fehlerangriffe.md](references/fehlerangriffe.md) |
| Wiederkehrende Mindestprüfung, Übergabe an Fachtester | Checklistenbasiertes Testen | [checklisten.md](references/checklisten.md) |

### 4. Session durchführen

- Zeitbox einhalten (typisch 60–90 Minuten).
- Notizen in Echtzeit: Was getan, was beobachtet, was gedacht. Werkzeug: Texteditor,
  Session-Tool, Bildschirmaufnahme.
- Befunde sofort mit Reproduktionsschritten sichern, dann weiter. Nicht in die Fehleranalyse
  abtauchen, das ist Setup-Zeit, nicht Testzeit.
- Abstecher („Opportunity“) notieren und bewusst entscheiden: jetzt verfolgen oder als neuen
  Charter ablegen.

### 5. Debriefing und Bericht

- Nach jeder Session kurz mit Auftraggeber oder Testlead: Was gefunden, was gelernt, was offen,
  welche neuen Charters.
- Bericht nach der Struktur unten. Fehler getrennt im Fehlermanagement melden.

### 6. Selbstprüfung

- [ ] Jede Session hat einen Charter, eine Zeitbox und Notizen.
- [ ] Jeder Befund hat Reproduktionsschritte, Umgebung, Beobachtung und Erwartung mit Quelle oder Begründung.
- [ ] Abstecher sind dokumentiert und als neue Charters abgelegt.
- [ ] Der Bericht nennt untersuchte und nicht untersuchte Bereiche.
- [ ] Gefundene Fehlermuster sind auf andere Bereiche übertragen oder als Charter vorgemerkt.
- [ ] Offene Fragen an Spezifikation oder Fachbereich sind gelistet.

## Lite-Modus

Bei Teilfragen oder einzelnen Verfahrensschritten nur die betreffenden Abschnitte ausgeben (z. B. nur einen Charter oder nur Testideen zu einer Heuristik), statt das volle Schema zu füllen. Die Selbstprüfung gilt dann nur für die ausgegebenen Teile; offene Fragen werden trotzdem genannt.

## Ausgabe

```markdown
# Explorative Session: <Charter-Titel>

## Charter
Erkunde <Bereich> mit <Ressourcen/Techniken>, um <Informationsziel> herauszufinden.

## Rahmen
| Tester | Datum | Dauer | Build/Version | Umgebung | Technik |

## Zeitverteilung
| Test | Fehleranalyse | Setup | Opportunity |

## Notizen (chronologisch)
- hh:mm – Aktion → Beobachtung → Gedanke

## Befunde
| ID | Schwere | Beobachtung | Erwartung (Quelle) | Reproduktion | Status |

## Fragen und Unklarheiten
| Frage | An wen |

## Untersucht / nicht untersucht
| Bereich | Tiefe (oberflächlich / mittel / gründlich) |

## Neue Charters
- ...
```
