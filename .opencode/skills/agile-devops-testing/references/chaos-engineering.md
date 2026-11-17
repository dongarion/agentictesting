# Chaos Engineering

**Kontrollierte Experimente**, die Ausfälle gezielt herbeiführen, um Vertrauen in die
Widerstandsfähigkeit eines Systems unter realen Störungen zu gewinnen. Kein Zufallschaos,
sondern Hypothese, Experiment, Messung.

## Inhalt
1. Prinzipien
2. Experiment entwerfen
3. Störungstypen
4. Reifegrad und Umgebung
5. Werkzeuge
6. GameDays
7. Anti-Patterns
8. Prüfliste

## 1. Prinzipien (principlesofchaos.org)

1. Hypothese über den stabilen Zustand (Steady State) formulieren, messbar über Geschäfts-
   und Systemmetriken.
2. Reale Ereignisse variieren: Hardwareausfall, Netzstörung, Latenz, Abhängigkeitsausfall,
   Lastspitzen.
3. Experimente in Produktion anstreben, aber dort beginnen, wo das Risiko tragbar ist.
4. Experimente automatisieren und kontinuierlich laufen lassen.
5. Auswirkungsradius (Blast Radius) minimieren; jederzeit abbrechbar.

## 2. Experiment entwerfen

| Schritt | Inhalt |
| --- | --- |
| Steady State | Metriken, die „normal“ definieren: Erfolgsrate, Latenz p99, Durchsatz, Geschäftsmetrik (Bestellungen/min) |
| Hypothese | „Wenn Instanz X ausfällt, bleibt die Erfolgsrate > 99,5 % und die Latenz p99 < 800 ms, weil der Load Balancer in < 10 s umschaltet.“ |
| Störung | Was genau, wo, wie lange, mit welchem Auswirkungsradius |
| Abbruchkriterium | Schwellwert, bei dem das Experiment sofort gestoppt wird; Verantwortlicher für den Stopp |
| Rollback | Wie wird die Störung beendet, wie lange dauert die Erholung |
| Beobachtung | Dashboards, Alarme, Logs, die während des Experiments verfolgt werden |
| Ergebnis | Hypothese bestätigt oder widerlegt; Befunde; Folgemaßnahmen |

Das Experiment ist auch ein Test der **Alarmierung und Reaktion**: Hat jemand gemerkt, dass
etwas passiert? Wie lange bis zur Diagnose?

## 3. Störungstypen

| Ebene | Störung |
| --- | --- |
| Infrastruktur | Instanz, Knoten, Zone oder Region beenden; Platte voll; CPU- und Speicherdruck |
| Netz | Latenz, Paketverlust, Partition, DNS-Ausfall, Zertifikatsablauf |
| Abhängigkeiten | Datenbank, Cache, Message Broker, Drittanbieter nicht erreichbar oder langsam |
| Anwendung | Exceptions injizieren, Thread-Pools erschöpfen, Konfiguration verfälschen |
| Zeit | Uhr verstellen, NTP-Drift |
| Mensch und Prozess | Bereitschaft nicht erreichbar, Runbook veraltet (GameDay) |

## 4. Reifegrad und Umgebung

1. Testumgebung mit produktionsnaher Topologie; Hypothesen und Werkzeuge erproben.
2. Vorproduktion mit Shadow Traffic oder Lasttest.
3. Produktion mit minimalem Auswirkungsradius (eine Instanz, ein Prozent der Nutzer),
   während der Geschäftszeit mit besetztem Team, nie am Freitagabend.
4. Automatisiert und wiederkehrend.

Für Fachverfahren mit Rechtswirkung und im Behördenumfeld: Stufe 1 und 2 sind oft die
Grenze; dort liegt trotzdem der größte Erkenntnisgewinn, weil Failover selten geübt wird.

## 5. Werkzeuge

| Werkzeug | Hinweis |
| --- | --- |
| Chaos Mesh, LitmusChaos | Kubernetes-nativ, Open Source |
| Gremlin | Kommerziell, breite Störungspalette, Sicherheitsmechanismen |
| AWS Fault Injection Service, Azure Chaos Studio | Cloud-nativ |
| Toxiproxy | Netzstörungen zwischen Services, auch lokal im Test |
| Chaos Toolkit | Experimentbeschreibung als JSON/YAML, erweiterbar |
| Eigene Skripte | `tc netem`, `stress-ng`, `kill`; ausreichend für den Einstieg |

## 6. GameDays

Geplante Übung (halber bis ganzer Tag): Team führt Experimente durch, Betrieb reagiert wie
im Ernstfall. Ablauf: Briefing, Szenarien nacheinander, Beobachtung, Debriefing mit Zeitleiste.
Ergebnis sind Befunde an System, Monitoring, Runbooks und Kommunikation.

## 7. Anti-Patterns

- Störung ohne Hypothese und ohne Steady-State-Messung; man lernt nur, dass etwas kaputtgeht.
- Kein Abbruchkriterium, kein Verantwortlicher für den Stopp.
- Erstes Experiment in Produktion mit großem Auswirkungsradius.
- Ergebnisse ohne Folgemaßnahmen; dasselbe Experiment scheitert ein Jahr später wieder.
- Chaos Engineering als Ersatz für Lasttest oder Failover-Test; es ergänzt sie.

## 8. Prüfliste

- [ ] Steady State ist mit Metriken und Schwellwerten definiert.
- [ ] Hypothese ist schriftlich, falsifizierbar und begründet.
- [ ] Auswirkungsradius, Abbruchkriterium, Rollback und Verantwortliche sind festgelegt.
- [ ] Beobachtung und Alarmierung sind Teil des Experiments.
- [ ] Umgebung entspricht dem Reifegrad; Freigabe durch Betrieb und Produktverantwortliche liegt vor.
- [ ] Befunde haben Maßnahmen mit Besitzer; Experiment wird wiederholt.
