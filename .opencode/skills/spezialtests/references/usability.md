# Usability-Test

Gebrauchstauglichkeit nach ISO 9241-11: **Effektivität, Effizienz, Zufriedenheit** in einem
Nutzungskontext. Geprüft wird das Produkt, nicht der Nutzer. Barrierefreiheit ist ein eigenes
Qualitätsmerkmal mit eigener Norm (BITV 2.0 / WCAG / EN 301 549) und wird im Skill Teststufen
und Testarten behandelt; beide Bereiche überschneiden sich in der Praxis.

## Inhalt
1. Methodenüberblick
2. Nutzertest planen
3. Nutzertest durchführen
4. Expertenmethoden
5. Fragebögen und Kennzahlen
6. Auswertung und Bericht
7. Ethik und Datenschutz
8. Anti-Patterns
9. Prüfliste

## 1. Methodenüberblick

| Methode | Art | Wann | Aufwand |
| --- | --- | --- | --- |
| Moderierter Nutzertest mit Thinking Aloud | empirisch, qualitativ | Prototyp bis Release; tiefes Verständnis von Problemen | mittel |
| Unmoderierter Remote-Test | empirisch, quantitativ/qualitativ | Viele Teilnehmer, einfache Aufgaben | niedrig–mittel |
| Heuristische Evaluation | Experten, analytisch | Früh, schnell, vor Nutzertests | niedrig |
| Cognitive Walkthrough | Experten, analytisch | Erlernbarkeit bei Erstnutzung | niedrig |
| Fragebögen (SUS, UEQ, UMUX) | quantitativ | Benchmark, Vergleich von Versionen | niedrig |
| Nutzungsdaten, Heatmaps, Funnel | quantitativ, Betrieb | Nach Release; wo brechen Nutzer ab? | mittel |
| Kontextuelle Beobachtung (Field Study) | qualitativ | Anforderungen verstehen, reale Arbeitsplätze (Sachbearbeitung) | hoch |

Kombination: Heuristische Evaluation zuerst (offensichtliche Probleme beseitigen), dann
Nutzertest, begleitend SUS.

## 2. Nutzertest planen

1. **Ziel und Fragen:** Was wollen wir wissen? („Finden Sachbearbeiter die Funktion X ohne Hilfe?“)
2. **Zielgruppe und Rekrutierung:** Personas, Kriterien (Rolle, Erfahrung, Hilfsmittel),
   5–8 Teilnehmer je Gruppe für qualitative Tests (Nielsen: 5 finden ~80 % der Probleme),
   mehr für quantitative Aussagen.
3. **Aufgaben:** realistisch, aus dem Nutzungskontext, mit klarem Erfolgskriterium, ohne
   Lösungshinweise in der Formulierung. Szenario statt Anleitung: „Ein Bürger hat angerufen
   und möchte wissen, ob sein Antrag eingegangen ist. Finden Sie das heraus.“ 5–8 Aufgaben je Sitzung.
4. **Metriken:** Erfolgsquote, Zeit, Fehler, Hilfebedarf, Zufriedenheit (SEQ je Aufgabe, SUS gesamt).
5. **Setting:** Labor, Arbeitsplatz oder remote; Aufzeichnung (Bildschirm, Ton, ggf. Video)
   mit Einwilligung.
6. **Pilot** mit einer Person; Aufgaben und Ablauf korrigieren.
7. **Rollen:** Moderator, Protokollant, Beobachter (Entwickler, PO) im Nebenraum oder Stream.

## 3. Nutzertest durchführen

- Begrüßung, Zweck erklären, Einwilligung, Betonung: „Wir testen das System, nicht Sie.
  Es gibt keine falschen Antworten.“
- **Thinking Aloud:** Teilnehmer spricht Gedanken laut aus. Moderator erinnert neutral
  („Was denken Sie gerade?“), hilft nicht, erklärt nicht, verteidigt nicht.
- Neutrale Fragen: „Was haben Sie erwartet?“ statt „War das verwirrend?“.
- Bei Scheitern: warten, dann Hinweis abgestuft, Hilfebedarf protokollieren, Aufgabe ggf. abbrechen.
- Protokoll je Aufgabe: Erfolg (ja/teilweise/nein), Zeit, Pfad, Fehler, Zitate, Emotionen, Hilfe.
- Nach jeder Aufgabe: Single Ease Question (SEQ, 1–7). Am Ende: SUS oder UEQ, offenes Gespräch.
- Debrief des Teams direkt danach: Top-3-Beobachtungen festhalten.

## 4. Expertenmethoden

**Heuristische Evaluation** (Nielsen): 3–5 Experten prüfen unabhängig gegen Heuristiken,
dann Konsolidierung.

Nielsens 10 Heuristiken: Sichtbarkeit des Systemstatus · Übereinstimmung System und Realität ·
Nutzerkontrolle und Freiheit · Konsistenz und Standards · Fehlervermeidung · Wiedererkennen
statt Erinnern · Flexibilität und Effizienz · Ästhetik und minimalistisches Design ·
Hilfe bei Fehlern · Hilfe und Dokumentation.
Alternativ: ISO 9241-110 Interaktionsprinzipien (Aufgabenangemessenheit, Selbstbeschreibungs-
fähigkeit, Erwartungskonformität, Erlernbarkeit, Steuerbarkeit, Robustheit gegen Benutzungsfehler,
Benutzerbindung). Im Behördenumfeld oft als Prüfgrundlage genannt.

**Cognitive Walkthrough:** Je Aufgabenschritt vier Fragen: Versucht der Nutzer das Richtige?
Sieht er, dass die richtige Aktion verfügbar ist? Verbindet er sie mit seinem Ziel?
Erkennt er am Feedback den Fortschritt?

Experten finden andere Probleme als Nutzer; beide Methoden ergänzen sich.

## 5. Fragebögen und Kennzahlen

| Instrument | Inhalt | Nutzung |
| --- | --- | --- |
| SUS (System Usability Scale) | 10 Items, Score 0–100; 68 ist Durchschnitt | Benchmark, Versionen vergleichen; nicht diagnostisch |
| UEQ / UEQ-S | Attraktivität, Durchschaubarkeit, Effizienz, Steuerbarkeit, Stimulation, Originalität | Differenzierter, Benchmark-Datensatz vorhanden |
| UMUX / UMUX-Lite | 4 bzw. 2 Items | Kurzform, korreliert mit SUS |
| SEQ | 1 Item je Aufgabe | Schwierigkeit je Aufgabe |
| NPS | Weiterempfehlung | Produktmetrik, keine Usability-Diagnose |
| Erfolgsquote, Zeit, Fehlerzahl | Leistungsmetriken | Effektivität und Effizienz |

Stichprobengröße für statistisch belastbare Vergleiche beachten; bei 5 Teilnehmern sind
Scores Hinweise, keine Beweise.

## 6. Auswertung und Bericht

- Beobachtungen über Teilnehmer konsolidieren: Problem, Häufigkeit, Schwere
  (kritisch: Aufgabe nicht lösbar; ernst: große Verzögerung oder Fehler; gering: Irritation).
- Je Problem: Beschreibung, Beleg (Zitat, Clip, Screenshot), betroffene Aufgabe, Ursache
  (Hypothese), Empfehlung.
- Positives festhalten; es verhindert, dass Gelungenes beim Redesign verloren geht.
- Highlight-Video (3–5 Minuten) überzeugt Stakeholder mehr als jede Tabelle.
- Kennzahlen mit Vergleich zur Vorversion oder Benchmark.
- Befunde ins Fehler- oder Backlog-Management mit Priorität.

## 7. Ethik und Datenschutz

- Informierte Einwilligung für Teilnahme und Aufzeichnung; Widerruf jederzeit; Aufwandsentschädigung.
- Daten minimieren, pseudonymisieren (T1, T2), Löschfrist für Aufzeichnungen.
- Keine echten Falldaten in Testaufgaben; synthetische Szenarien.
- Bei Mitarbeitenden als Teilnehmer: Freiwilligkeit, keine Leistungsbewertung, ggf. Personalrat
  einbeziehen.
- Barrierefreie Teilnahme ermöglichen; Nutzer mit Hilfsmitteln gezielt einladen.

## 8. Anti-Patterns

- Moderator erklärt die Oberfläche, bevor der Nutzer sie sieht.
- Aufgaben, die die Lösung verraten („Klicken Sie auf Anträge und dann …“).
- Teilnehmer aus dem Projektteam.
- SUS-Score als einziges Ergebnis.
- Probleme nach Meinung des lautesten Stakeholders priorisieren statt nach Beobachtung.
- Nutzertest erst nach dem Release, wenn Änderungen teuer sind.

## 9. Prüfliste

- [ ] Ziel, Fragen und Metriken sind vorab festgelegt.
- [ ] Teilnehmer entsprechen der Zielgruppe; Pilot ist durchgeführt.
- [ ] Aufgaben sind realistisch, ohne Lösungshinweise, mit Erfolgskriterium.
- [ ] Einwilligungen liegen vor; Daten sind pseudonymisiert; Löschfrist festgelegt.
- [ ] Moderation ist neutral; Protokoll je Aufgabe mit Belegen.
- [ ] Befunde sind konsolidiert, nach Schwere priorisiert, mit Empfehlung und Beleg.
- [ ] Ergebnisse sind ins Backlog übernommen; Nachtest ist geplant.
