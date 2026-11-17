# Modellbasiertes Testen (MBT)

Tests werden aus einem **expliziten Verhaltensmodell** generiert statt von Hand geschrieben.
Das Modell ist die Testbasis und zugleich Nachweis der Überdeckung.

## Inhalt
1. Wann MBT lohnt
2. Modelltypen
3. Vorgehen
4. Auswahlkriterien für die Generierung
5. Werkzeuge
6. Anti-Patterns
7. Prüfliste

## 1. Wann MBT lohnt

- Zustandsreiches Verhalten: Workflows, Protokolle, Geräte, Benutzerkonten.
- Lange Lebensdauer mit häufigen Änderungen: Modell anpassen ist billiger als hunderte
  Testfälle anpassen.
- Hohe Überdeckungsanforderungen mit Nachweis.
- Nicht lohnend: einmalige Features, reine Oberflächenkosmetik, Systeme ohne klare
  Zustandslogik.

## 2. Modelltypen

| Modell | Eignung | Notation |
| --- | --- | --- |
| Zustandsautomat, Statechart | Reaktive Systeme, Workflows | UML State Machine, SCXML, GraphWalker |
| Aktivitäts-/Prozessmodell | Geschäftsprozesse, Abläufe mit Parallelität | BPMN, UML Activity |
| Entscheidungstabelle / Regelmodell | Geschäftsregeln | DMN, Tabellen |
| Grammatik | Eingabeformate, Protokollnachrichten | EBNF |
| Nutzungsprofil (Markov) | Statistisches Testen nach realer Nutzung | Übergangswahrscheinlichkeiten |
| Datenmodell mit Constraints | Kombinatorik, Testdatengenerierung | Klassifikationsbaum, OCL |

## 3. Vorgehen

1. **Modellzweck festlegen:** Was soll das Modell abbilden, was bewusst nicht?
   Ein Testmodell ist nicht das Entwurfsmodell; es abstrahiert auf das Prüfziel.
2. **Modell erstellen** aus Anforderungen, nicht aus dem Code. Jede Modellaussage mit
   Anforderungsverweis.
3. **Modell validieren:** Review mit Fachbereich, Simulation, Prüfung auf Erreichbarkeit aller
   Zustände und Deadlocks. Widersprüche im Modell sind Befunde an den Anforderungen.
4. **Auswahlkriterien festlegen** (siehe 4).
5. **Abstrakte Tests generieren.**
6. **Konkretisieren:** Abstrakte Aktionen auf ausführbare Schritte abbilden (Adapter,
   Schlüsselwörter, API-Aufrufe), abstrakte Daten auf konkrete Werte.
7. **Ausführen, auswerten, Modell pflegen.** Fehler klassifizieren: Produkt, Modell, Adapter,
   Anforderung.

## 4. Auswahlkriterien für die Generierung

- Strukturell: alle Zustände, alle Übergänge, alle Übergangspaare, alle Pfade bis Länge n.
- Datenbezogen: Äquivalenzklassen und Grenzwerte an Wächterbedingungen.
- Anforderungsbezogen: jede verknüpfte Anforderung mindestens einmal.
- Szenariobasiert: definierte Pfade (Hauptszenarien) erzwingen.
- Zufällig/statistisch: nach Nutzungsprofil gewichtet, mit Seed.
- Kriterium begründen und Generierungsumfang (Anzahl, Dauer) begrenzen.

## 5. Werkzeuge

| Werkzeug | Hinweis |
| --- | --- |
| GraphWalker | Open Source, Graphmodelle, Online- und Offline-Generierung, Java |
| AltWalker | GraphWalker-Frontend für Python, C#, mit Robot-Framework-Anbindung |
| Conformiq, TestCompass, MaTeLo | Kommerziell, UML/BPMN, Nutzungsprofile |
| Modbat, QuickCheck-Zustandsmaschinen (Hypothesis `RuleBasedStateMachine`) | Modellbasiertes Property Testing |
| Eigene Generatoren | Bei einfachen Zustandsautomaten oft ausreichend |

## 6. Anti-Patterns

- Modell aus dem Code reverse-engineeren; dann prüft das Modell nur den Code gegen sich selbst.
- Modell so detailliert wie die Implementierung; Pflegeaufwand übersteigt Nutzen.
- Generierte Tests ohne Prüfung des Orakels; das Modell muss erwartete Ergebnisse liefern.
- Modell nicht versionieren, Generierung nicht reproduzierbar.
- Konkretisierungsschicht (Adapter) ungetestet lassen.

## 7. Prüfliste

- [ ] Modellzweck und Abstraktionsgrad sind dokumentiert.
- [ ] Jede Modellaussage hat einen Anforderungsverweis.
- [ ] Modell ist validiert (Review, Erreichbarkeit, Deadlocks).
- [ ] Auswahlkriterium ist gewählt und begründet.
- [ ] Modellversion, Werkzeugversion und Seed sind festgehalten.
- [ ] Fehlklassifikation (Produkt / Modell / Adapter / Anforderung) wird geführt.
