# Strategietypen nach ISTQB

CTFL 4.0 nennt sieben Typen. In der Praxis wird kombiniert; die Frage ist das Gewicht.

## Inhalt
1. Übersicht
2. Die Typen im Einzelnen
3. Strategiemix bilden
4. Beispiele
5. Anti-Patterns
6. Prüfliste

## 1. Übersicht

| Typ | Grundlage | Stärke | Schwäche |
| --- | --- | --- | --- |
| Analytisch | Analyse eines Faktors: Risiken, Anforderungen | Zielgerichtet, begründbar | Nur so gut wie die Analyse |
| Modellbasiert | Modelle des Verhaltens, der Nutzung, der Last | Systematisch, generierbar | Modellaufwand, Modellfehler |
| Methodisch | Feste Listen: Checklisten, Qualitätsmerkmale, Fehlerkataloge | Breite, Konsistenz | Starr, wenig zielgerichtet |
| Prozess-/standardkonform | Externe Normen, Branchenstandards | Nachweisbar, auditfest | Kann Aufwand ohne Nutzen erzeugen |
| Angeleitet/beratend | Rat von Stakeholdern, Fachexperten, Nutzern | Fachlich relevant | Abhängig von Verfügbarkeit und Urteil |
| Regressionsvermeidend | Wiederverwendung, Automatisierung, Standard-Suiten | Stabilität, schnelles Feedback | Findet wenig Neues |
| Reaktiv | Reaktion auf das Testobjekt während des Tests (explorativ) | Findet Unbekanntes, flexibel | Schwer planbar, Abdeckung schwer nachweisbar |

## 2. Die Typen im Einzelnen

**Analytisch.** Häufigste Form: risikobasiertes Testen (Skill `testmanagement`). Varianten:
anforderungsbasiert (jede Anforderung getestet), änderungsbasiert (Auswirkungsanalyse).
Als Rückgrat fast jeder Strategie geeignet.

**Modellbasiert.** Zustandsmodelle (MBT, Skill `fortgeschrittene-testmethoden`), Nutzungsprofile
für statistisches Testen und Lasttests (Lastmodell aus Produktionsdaten), Bedrohungsmodelle für
Sicherheit. Sinnvoll bei zustandsreichen Systemen, langer Lebensdauer, Performance-kritischen Systemen.

**Methodisch.** ISO/IEC 25010 als Liste der Qualitätsmerkmale; Checklisten (Skill
`exploratives-testen`); Fehlertaxonomien; OWASP ASVS; WCAG-Erfolgskriterien. Stellt sicher,
dass nichts Grundsätzliches vergessen wird.

**Prozess-/standardkonform.** ISO 26262, DO-178C, IEC 62304, EN 50128, V-Modell XT,
ISO/IEC/IEEE 29119, Kundenrahmen. Pflicht, wo gefordert; Maßstab ist dann der Nachweis.
Nicht übererfüllen, wo der Standard Spielraum lässt.

**Angeleitet/beratend.** Fachexperten bestimmen Schwerpunkte, Nutzer definieren Abnahmeszenarien,
Sicherheitsexperten den Pentest-Scope. Wichtig bei komplexer Fachlichkeit und bei Abnahmetests.

**Regressionsvermeidend.** Automatisierte Regressionssuiten, Smoke-Tests je Deployment,
Wiederverwendung von Testmitteln. Unverzichtbar bei häufigen Releases und langer Lebensdauer.

**Reaktiv.** Exploratives Testen, Fehlerangriffe, Bug Bashes. Gleicht die Lücken analytischer
Strategien aus (fehlende Anforderungen, unerwartete Wechselwirkungen). Sollte geplant und mit
Zeitbudget versehen werden, nicht nur „wenn Zeit bleibt“.

## 3. Strategiemix bilden

1. Rückgrat wählen (meist analytisch-risikobasiert).
2. Pflichtanteile ergänzen (standardkonform, wo gefordert).
3. Für jedes wichtige Qualitätsmerkmal methodische Abdeckung (Checklisten, Normen).
4. Regressionsvermeidend für alles, was häufig geändert und ausgeliefert wird.
5. Reaktiven Anteil mit Budget festlegen (Richtwert: 10–30 % der Durchführungszeit, je nach
   Neuheit und Qualität der Testbasis).
6. Angeleitete Anteile dort, wo Fachwissen den Ausschlag gibt (Abnahme, Fachlogik).
7. Gewichte und Begründung dokumentieren; bei Änderung des Kontexts überprüfen.

## 4. Beispiele

**Fachverfahren einer Bundesbehörde, V-Modell XT, Releases halbjährlich:**
analytisch-risikobasiert (Rückgrat) · standardkonform (V-Modell XT, BITV, BSI-Grundschutz, EVB-IT-Abnahme) ·
angeleitet (Fachbereich definiert Abnahmeszenarien) · regressionsvermeidend (automatisierte
Regressionssuite für Kernprozesse) · reaktiv (explorative Sessions je Release, 15 %).

**SaaS-Produkt, Continuous Delivery, mehrere Deployments täglich:**
regressionsvermeidend (Pyramide, Pipeline-Gates) · analytisch-änderungsbasiert (Test Impact
Analysis) · reaktiv (explorativ je Feature, Bug Bash vor großen Releases) · Shift-Right
(Canary, Monitoring) · methodisch (Sicherheitsscans, Barrierefreiheitsscans).

**Steuergerät, ASIL C:**
standardkonform (ISO 26262, ASPICE) · analytisch-anforderungsbasiert mit voller Rückverfolgbarkeit ·
modellbasiert (MiL/SiL, Back-to-back) · regressionsvermeidend (HiL-Nachtläufe) ·
reaktiv in engem Rahmen (Fehlerinjektion, explorativ am Prüfstand).

## 5. Anti-Patterns

- Nur ein Typ („wir testen anforderungsbasiert“) ohne reaktive Anteile.
- Reaktiv als einzige Strategie („wir testen einfach drauflos“).
- Standardkonformität als Selbstzweck; Dokumente ohne Testwirkung.
- Regressionsvermeidung ohne Pflege; Suite wird alt und blind.
- Strategiemix nicht dokumentiert; jeder versteht etwas anderes.

## 6. Prüfliste

- [ ] Rückgrat-Strategie ist benannt und begründet.
- [ ] Pflichtanteile aus Normen und Verträgen sind enthalten.
- [ ] Qualitätsmerkmale sind methodisch abgedeckt.
- [ ] Regressionsvermeidung passt zur Release-Frequenz.
- [ ] Reaktiver Anteil hat ein Budget.
- [ ] Gewichte und Begründungen sind dokumentiert und abgestimmt.
