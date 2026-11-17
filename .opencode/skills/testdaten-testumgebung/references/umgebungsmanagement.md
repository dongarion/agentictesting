# Testumgebungsmanagement

Eine Testumgebung ist die **Gesamtheit aus Hardware, Software, Netz, Daten, Schnittstellen
und Konfiguration**, in der getestet wird. Sie ist ein Produkt mit Besitzer, Lebenszyklus,
Kapazität und Nutzern.

## Inhalt
1. Umgebungslandschaft
2. Umgebungsbeschreibung
3. Planung und Buchung
4. Pflege und Konsistenz
5. Schnittstellen und Fremdsysteme
6. Betrieb und Support
7. Kennzahlen
8. Anti-Patterns
9. Prüfliste

## 1. Umgebungslandschaft

Typische Stufen und Zweck; Anzahl und Namen variieren:

| Umgebung | Zweck | Besitzer | Daten |
| --- | --- | --- | --- |
| Lokal / Entwicklung | Entwickeln, Unit-Tests | Entwickler | synthetisch, minimal |
| CI / ephemer | Automatisierte Tests je Commit oder MR | Plattformteam | synthetisch, per Skript |
| Integration / Systemtest | Systemtest, API-Tests, erste Integration | Testteam | synthetisch, Subset maskiert |
| Systemintegration (SIT) | Zusammenspiel mit Fremdsystemen | Integrationsmanager | abgestimmt mit Partnern |
| Abnahme (UAT) / Vorproduktion | Fachliche Abnahme, Performance, Betriebsproben | Fachbereich, Betrieb | maskierte Produktion oder realistische Synthese |
| Schulung | Anwenderschulung | Fachbereich | stabil, zurücksetzbar |
| Referenz / Hotfix | Produktionsstand für Fehlernachstellung | Betrieb | maskierte Produktion |

Jede zusätzliche statische Umgebung kostet Pflege. Ephemere Umgebungen ersetzen viele
davon (siehe [iac-ephemer.md](iac-ephemer.md)).

## 2. Umgebungsbeschreibung

Je Umgebung dokumentiert (als Code oder im Umgebungskatalog):

- Topologie: Komponenten, Instanzen, Netze, Zonen; Diagramm.
- Versionen: Anwendung, Datenbank, Betriebssystem, Middleware, Browser, Zertifikate.
- Konfiguration: Feature-Toggles, Parameter, Mandanten, Zeitzone, Locale.
- Daten: Herkunft, Stand, Maskierung, Rücksetzverfahren.
- Schnittstellen: je Partner echt, virtualisiert oder deaktiviert; Endpunkte, Zugangsdaten
  (im Secret Store).
- Zugänge: Nutzer, Rollen, Jump Hosts, VPN.
- Besitzer, Ansprechpartner, Supportzeiten.
- Abweichungen zur Produktion mit Begründung (Dimensionierung, fehlende Komponenten).

## 3. Planung und Buchung

- Bedarf aus Testplanung ableiten: Welche Teststufe braucht wann welche Umgebung, wie lange,
  mit welchem Stand?
- Buchungskalender je Umgebung; Konflikte früh sichtbar. Werkzeug kann ein Kalender, ein
  Ticketsystem oder ein Umgebungsmanagement-Tool sein (Enov8, Plutora, ServiceNow TEM,
  Apwide Golive, einfache Jira-Boards).
- Regeln: Wer darf deployen, wann (Deployment-Fenster), wie wird angekündigt, wer darf Daten
  zurücksetzen.
- Pufferzeiten für Aufbau und Rücksetzung einplanen.
- Eskalationsweg bei Konflikten (Testmanager, Release-Manager).

## 4. Pflege und Konsistenz

- **Drift vermeiden:** Änderungen nur über Deployment-Pipeline und Konfigurationsmanagement,
  nicht per Hand. Handänderungen, wenn unvermeidbar, protokollieren und zurückführen.
- **Health-Check** vor jedem Testlauf: Dienste erreichbar, Versionen wie erwartet, Datenstand,
  Zertifikate gültig, Schnittstellen antworten. Automatisiert, Ergebnis sichtbar.
- **Rücksetzung** auf definierten Stand per Skript oder Snapshot; Dauer bekannt.
- **Patch- und Versionsstand** mit Produktion abgleichen; Abweichungen bewusst.
- **Zertifikate, Lizenzen, Passwörter** mit Ablaufüberwachung; die häufigste Ursache
  „plötzlich kaputter“ Umgebungen.
- **Zeit:** Systemzeit, Zeitzone, NTP; Zeitreisen für Tests nur auf dafür vorgesehenen Umgebungen.
- **Kapazität** überwachen: Platte, Speicher, Logs, Datenwachstum durch Tests.

## 5. Schnittstellen und Fremdsysteme

- Je Partner festlegen: echte Testumgebung des Partners (Abstimmung, Buchung, gemeinsame
  Testdaten), Service-Virtualisierung (Skill Agile/DevOps) oder deaktiviert mit Stub.
- Testdaten über Systemgrenzen konsistent (gleiche Pseudonyme, gleiche Kennungen).
- Verfügbarkeitszeiten der Partnerumgebungen kennen; Behörden- und Bankschnittstellen haben
  oft Wartungsfenster und eingeschränkte Testzeiten.
- Verträge und Ansprechpartner je Schnittstelle dokumentieren.

## 6. Betrieb und Support

- Supportkanal und Reaktionszeiten für Umgebungsprobleme; Umgebungsstörungen sind
  Projektrisiko und werden als solche berichtet.
- Störungen klassifizieren: Umgebung, Daten, Deployment, Produkt. Umgebungsbedingte
  Testausfälle getrennt zählen (Setup-Zeit).
- Monitoring auch auf Testumgebungen; Logs zugänglich für Tester.
- Änderungsmanagement light: Was sich an der Umgebung ändert, wird angekündigt.

## 7. Kennzahlen

| Kennzahl | Aussage |
| --- | --- |
| Verfügbarkeit je Umgebung | Verlässlichkeit |
| Wartezeit auf Umgebung oder Rücksetzung | Engpass |
| Umgebungsbedingte Testausfälle je Sprint | Qualität der Umgebungen |
| Zeit für Neuaufbau | Reproduzierbarkeit |
| Abweichungen zur Produktion | Aussagekraft der Tests |

## 8. Anti-Patterns

- Eine Staging-Umgebung für alle: Entwickler deployen, Tester testen, Fachbereich schult, gleichzeitig.
- Handgepflegte Umgebung, die niemand neu aufbauen kann („Schneeflocke“).
- Keine Beschreibung; Wissen bei einer Person.
- Zertifikat läuft ab, Tests fallen einen Tag aus, jedes Jahr.
- Testumgebung mit Produktionsdaten und schwächeren Zugriffsschutz als Produktion.
- Umgebungsprobleme als „Testfehler“ in der Statistik.

## 9. Prüfliste

- [ ] Umgebungslandschaft mit Zweck und Besitzer je Umgebung ist dokumentiert.
- [ ] Jede Umgebung hat eine aktuelle Beschreibung (Topologie, Versionen, Daten, Schnittstellen, Abweichungen).
- [ ] Buchung und Deployment-Regeln existieren und werden eingehalten.
- [ ] Health-Check vor Testläufen ist automatisiert.
- [ ] Rücksetzung per Skript; Dauer bekannt.
- [ ] Ablaufdaten (Zertifikate, Lizenzen, Passwörter) werden überwacht.
- [ ] Schnittstellen je Partner geregelt (echt, virtualisiert, deaktiviert).
- [ ] Zugriffsschutz entspricht dem Schutzbedarf der Daten.
