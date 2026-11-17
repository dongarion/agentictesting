# Fehlermanagement, Triage und Konfigurationsmanagement

## Inhalt
1. Fehlerlebenszyklus
2. Klassifikation
3. Triage und Fehlergremium
4. Fehlerbericht (Qualität)
5. Fehlerauswertung
6. Konfigurationsmanagement der Testmittel
7. Anti-Patterns
8. Prüfliste

## 1. Fehlerlebenszyklus

Beispiel (an Werkzeug und Kunde anpassen):

```
Neu → Analysiert (Triage) → Zugewiesen → In Bearbeitung → Behoben → Im Nachtest
   → Geschlossen
   ↘ Abgelehnt (kein Fehler / Duplikat / nicht reproduzierbar / gewünschtes Verhalten)
   ↘ Zurückgestellt (bewusste Entscheidung, mit Zielversion)
Im Nachtest → Wiedereröffnet → Zugewiesen
```

Jeder Übergang hat Verantwortlichen und Pflichtfelder. Ablehnung und Zurückstellung brauchen
Begründung und Entscheider.

## 2. Klassifikation

| Attribut | Inhalt | Wer |
| --- | --- | --- |
| Schwere (Severity) | Auswirkung auf Nutzung: kritisch, hoch, mittel, gering | Tester (Vorschlag), Gremium bestätigt |
| Priorität | Dringlichkeit der Behebung | PO/Fachbereich, Gremium |
| Fehlerart | Funktion, Daten, Oberfläche, Performance, Sicherheit, Dokumentation, Anforderung | Analyse |
| Fehlerursache | Anforderung, Entwurf, Code, Konfiguration, Daten, Umgebung | Entwickler nach Analyse |
| Phase der Entstehung / Entdeckung | Anforderung … Betrieb | Analyse; Grundlage für Fehlerentdeckungsrate |
| Komponente | Betroffene Komponente | Tester |
| Reproduzierbarkeit | immer, sporadisch, einmalig | Tester |

Im Behördenumfeld oft EVB-IT-Fehlerklassen: betriebsverhindernd, betriebsbehindernd, leichter
Mangel; mit vertraglichen Reaktions- und Behebungsfristen.

## 3. Triage und Fehlergremium

- **Triage:** Neue Fehler täglich (oder je Sprint-Tag) sichten: vollständig? reproduzierbar?
  Duplikat? Schwere plausibel? Zuweisung.
- **Fehlergremium (Defect Review Board):** Vertreter Test, Entwicklung, Fachbereich/PO,
  ggf. Betrieb und Projektleitung; Frequenz nach Fehleraufkommen (in heißen Phasen täglich).
  Entscheidet Priorität, Zielversion, Zurückstellung, Akzeptanz.
- Eskalation: kritische Fehler sofort, nicht erst im nächsten Gremium.
- In agilen Teams: Fehler aus dem Sprint direkt im Sprint beheben; Fehler aus Produktion oder
  Altbestand als Backlog-Einträge priorisieren.

## 4. Fehlerbericht (Qualität)

Mindestinhalt siehe Skill `testprozess`, Referenz Realisierung und Durchführung.
Qualitätskriterien: eindeutiger Titel, minimale Reproduktionsschritte, Version und Umgebung,
erwartetes Ergebnis mit Quelle, Beleg, ein Fehler je Bericht, sachlicher Ton.
Stichprobenartige Reviews von Fehlerberichten verbessern die Qualität schnell.

## 5. Fehlerauswertung

- Offene Fehler je Schwere über Zeit (Trend); Fehlerfindungsrate vs. Behebungsrate
  (konvergieren die Kurven?).
- Alter offener Fehler; Behebungszeit je Schwere gegen Ziel.
- Wiedereröffnungsquote (Qualität der Behebung), Ablehnungsquote (Qualität der Meldungen).
- Fehlerdichte je Komponente (Hotspots für Tests und Refactoring).
- Fehlerentdeckungsrate je Phase (Defect Detection Percentage): Anteil der Fehler, die vor
  der nächsten Phase gefunden wurden; Produktionsfehler (Escapes) gesondert analysieren.
- Grundlage für RCA (siehe [rca-und-prozessverbesserung.md](rca-und-prozessverbesserung.md)).

## 6. Konfigurationsmanagement der Testmittel

Ziel: Jedes Testergebnis ist reproduzierbar einem eindeutigen Stand zugeordnet.

- **Konfigurationseinheiten:** Testobjekt (Build, Version), Testfälle, Testskripte, Testdaten,
  Umgebungsdefinitionen, Werkzeugversionen, Testkonzept und Berichte.
- **Identifikation:** Eindeutige Versionen; Testobjekt mit Build-Nummer, Commit-Hash, Release Notes.
- **Versionierung:** Testcode und Daten im Repository mit Tags je Release; Testfälle im
  Testmanagement-Werkzeug mit Versionen; Dokumente mit Änderungshistorie.
- **Baselines:** Je Meilenstein ein eingefrorener Stand aller Testmittel.
- **Änderungssteuerung:** Änderungen an Testbasis lösen Auswirkungsanalyse auf Testmittel aus.
- **Statusbericht:** Welche Version wurde mit welchen Testmitteln auf welcher Umgebung getestet.

## 7. Anti-Patterns

- Schwere und Priorität vermischt oder vom Tester allein festgelegt.
- Fehler per Mail oder Chat statt im Werkzeug.
- Gremium ohne Fachbereich; Prioritäten sind technisch statt geschäftlich.
- „Nicht reproduzierbar“ als Schublade ohne weitere Analyse.
- Testergebnis ohne Build-Nummer; niemand weiß, was getestet wurde.
- Fehlerzahlen als Leistungsmaß von Testern oder Entwicklern.

## 8. Prüfliste

- [ ] Fehlerlebenszyklus mit Rollen und Pflichtfeldern ist definiert.
- [ ] Schwere und Priorität sind getrennt; Klassen und Fristen vereinbart.
- [ ] Triage und Fehlergremium mit Teilnehmern und Frequenz sind etabliert.
- [ ] Fehlerauswertungen werden regelmäßig erstellt und genutzt.
- [ ] Konfigurationseinheiten, Versionierung und Baselines sind festgelegt.
- [ ] Jedes Testergebnis ist einer eindeutigen Version zugeordnet.
