# Embedded-Test und MiL/SiL/HiL

Software, die **Hardware steuert, in Echtzeit reagiert und oft sicherheitskritisch** ist.
Test findet auf mehreren Integrationsebenen statt, von der Simulation bis zum realen Steuergerät.
Normen (ISO 26262, IEC 61508, DO-178C, IEC 62304, EN 50128) bestimmen Umfang und Nachweise.

## Inhalt
1. X-in-the-Loop-Ebenen
2. Besonderheiten eingebetteter Systeme
3. Teststufen und Nachweise nach Norm
4. Testumgebung und Prüfstände
5. Testverfahren
6. Automotive-Spezifika
7. Werkzeuge
8. Anti-Patterns
9. Prüfliste

## 1. X-in-the-Loop-Ebenen

| Ebene | Was läuft | Was wird simuliert | Zweck |
| --- | --- | --- | --- |
| **MiL** (Model-in-the-Loop) | Funktionsmodell (Simulink, ASCET) | Umgebung, Fahrzeug, Sensorik | Funktionale Absicherung früh, Anforderungsüberdeckung am Modell |
| **SiL** (Software-in-the-Loop) | Generierter oder handgeschriebener Code auf PC | Hardware, Umgebung | Code gegen Modell (Back-to-back), Unit- und Integrationstests, hohe Automatisierung |
| **PiL** (Processor-in-the-Loop) | Code auf Zielprozessor oder Evaluationsboard | Umgebung | Timing, Speicher, Compiler-Effekte |
| **HiL** (Hardware-in-the-Loop) | Reales Steuergerät | Umgebung über Echtzeitsimulator mit I/O | Systemtest mit echter Hardware, Fehlersimulation, Dauerlauf |
| **VIL / Fahrzeug / Feld** | Gesamtsystem real | nichts oder Teile | Abnahme, Erprobung, Homologation |

Prinzip: so früh und so virtuell wie möglich, so real wie nötig. Jede Ebene hat eigene
Testfälle, die sich zu einem großen Teil wiederverwenden lassen (gleiche Stimuli, andere Adapter).

## 2. Besonderheiten eingebetteter Systeme

- **Echtzeit:** Zeitanforderungen (Deadlines, Zykluszeiten, Jitter) sind funktionale Anforderungen;
  WCET-Analyse, Timing-Tests, Überlastverhalten.
- **Ressourcen:** Speicher, Stack, CPU-Last; Fragmentierung; Verhalten bei Erschöpfung.
- **Hardware-Schnittstellen:** Sensoren mit Rauschen, Ausfall, Drift; Aktuatoren mit Trägheit;
  Busse (CAN, LIN, FlexRay, Ethernet, SPI, I2C) mit Fehlerinjektion.
- **Zustände und Betriebsmodi:** Start, Normal, Degradation, Notlauf, Schlaf, Update, Diagnose.
- **Fehlertoleranz:** Watchdog, Redundanz, Plausibilisierung, sicherer Zustand.
- **Begrenzte Beobachtbarkeit:** Debug-Schnittstellen (JTAG, Trace), Logging kostet Ressourcen;
  Testhaken im Code bewusst gestalten und in Serienbuild entfernen oder sichern.
- **Lebensdauer und Varianten:** viele Hardware- und Softwarevarianten, lange Wartung,
  Updates über die Luft (OTA) mit eigenen Risiken.

## 3. Teststufen und Nachweise nach Norm

- **Anforderungsbasiert:** Jeder Testfall verweist auf eine Anforderung; bidirektionale
  Rückverfolgbarkeit ist Pflicht.
- **Strukturüberdeckung** je Sicherheitsstufe (Skill White-Box, Referenz Überdeckungsziele):
  Anweisung, Zweig, MC/DC; Messung oft am Zielcode.
- **Unabhängigkeit:** Je höher die Stufe, desto unabhängiger muss der Test von der Entwicklung sein.
- **Werkzeugqualifikation:** Testwerkzeuge, deren Fehler einen Fehler verdecken könnten,
  brauchen Qualifikation (ISO 26262-8, DO-330).
- **Nachweise:** Testpläne, Testspezifikationen, Ergebnisse, Überdeckungsberichte, Abweichungen,
  Reviews, versioniert und archiviert.
- **Sicherheitsanalysen** (FMEA, FTA, HARA) liefern Testfälle für Fehlerreaktionen.

## 4. Testumgebung und Prüfstände

- **HiL-Aufbau:** Echtzeitrechner, I/O-Karten, Bus-Simulation, Fehlersimulationsbox
  (Kurzschluss, Unterbrechung, Übergangswiderstand), Restbussimulation, Lastnachbildung.
- **Modelle:** Umgebungs- und Fahrzeugmodelle validiert; Modellgüte dokumentiert.
- **Reproduzierbarkeit:** Zustand des Prüfstands, Modellversion, Software-Stand, Parametrierung
  je Lauf festgehalten.
- **Virtuelle Steuergeräte** (vECU) und Cloud-SiL für Skalierung; HiL-Zeit ist knapp und teuer,
  daher Vorselektion auf SiL.
- **Prüfstandsbuchung** und Kalibrierung wie bei jeder Umgebung (Skill Testdaten und Testumgebung).

## 5. Testverfahren

- Anforderungsbasierte Black-Box-Verfahren (Äquivalenzklassen, Grenzwerte, Zustandsübergänge) auf
  Signale, Modi und Zeit angewandt.
- **Back-to-back MiL ↔ SiL ↔ PiL:** gleiche Stimuli, Ausgaben mit Toleranzen vergleichen;
  Nachweis, dass Codegenerierung und Compiler das Modell erhalten.
- **Fehlerinjektion:** Sensorausfall, Busfehler, Spannungseinbruch, Speicherfehler;
  Prüfung der Fehlerreaktion und des sicheren Zustands.
- **Timing-Tests:** Zykluszeiten, Reaktionszeiten, Verhalten bei Überlast; Messung mit Trace.
- **Dauerlauf und Stress:** Langzeitbetrieb, Temperatur, Spannung, Speicherleck.
- **Diagnose:** Fehlerspeicher (DTC), Diagnoseprotokolle (UDS), Flashen, Reprogrammierung.
- **Regression auf HiL:** automatisiert, nächtlich, mit Signalaufzeichnung und Bewertung.
- **Statische Analyse:** MISRA C/C++, Laufzeitfehleranalyse (Polyspace, Astrée) als Pflichtbestandteil.

## 6. Automotive-Spezifika

- **ISO 26262:** ASIL A–D bestimmt Methoden (Tabellen in Teil 6 für Software), Unabhängigkeit,
  Überdeckung, Werkzeugqualifikation.
- **ASPICE:** Prozessreife für SWE.4–SWE.6 (Unit-Verifikation, Integrationstest, Qualifikationstest)
  und SYS.4–SYS.5; Kunden fordern Level 2 oder 3.
- **ISO/SAE 21434:** Cybersicherheit, TARA, Sicherheitstests inkl. Pentest am Fahrzeug.
- **SOTIF (ISO 21448):** Absicherung von Funktionen mit Sensorik und Algorithmen gegen
  unbekannte Szenarien; szenariobasiertes Testen, Simulation großer Szenarienräume.
- **AUTOSAR:** Schichtenarchitektur; Tests gegen Schnittstellen der RTE, Basissoftware-Konfiguration.
- **Homologation:** UNECE-Regelungen (R155 Cybersecurity, R156 Software Update) verlangen
  nachweisbare Prozesse und Tests.

## 7. Werkzeuge

| Zweck | Werkzeuge |
| --- | --- |
| Modellierung, MiL | MATLAB/Simulink mit Simulink Test, ASCET, SCADE |
| SiL, vECU | dSPACE VEOS, Synopsys Silver, Vector CANoe mit SIL Adapter, eigene PC-Builds |
| HiL | dSPACE SCALEXIO, NI VeriStand/PXI, Vector VT System, ETAS LABCAR |
| Testautomatisierung | ECU-TEST (tracetronic), dSPACE AutomationDesk, Vector vTESTstudio, Robot Framework mit Adaptern |
| Unit-Test (C/C++) | VectorCAST, Cantata, Tessy, GoogleTest, Unity/Ceedling |
| Überdeckung | VectorCAST, Cantata, LDRA, gcov (nicht für Zielcode-Nachweis) |
| Statische Analyse | Polyspace, Astrée, Helix QAC, Coverity, Cppcheck |
| Bus und Diagnose | CANoe, CANalyzer, CANape, Wireshark |
| Anforderungen, Traceability | DOORS, Polarion, Codebeamer, Jama |

## 8. Anti-Patterns

- Alles auf dem HiL testen; Prüfstand ist Engpass, SiL ungenutzt.
- Testfälle ohne Anforderungsbezug; Nachweis vor dem Assessor nicht möglich.
- Überdeckung am PC gemessen und für Zielcode behauptet.
- Fehlerinjektion ausgelassen, weil „kommt im Betrieb nicht vor“.
- Modelle ohne Validierung; Simulation bestätigt sich selbst.
- Werkzeuge ohne Qualifikation in sicherheitsrelevanten Nachweisen.

## 9. Prüfliste

- [ ] Sicherheitsstufe und daraus folgende Methoden, Überdeckung und Unabhängigkeit sind festgelegt.
- [ ] Jeder Testfall ist bidirektional mit Anforderungen verknüpft.
- [ ] Testverteilung auf MiL/SiL/PiL/HiL ist begründet; Wiederverwendung der Stimuli geplant.
- [ ] Back-to-back zwischen Ebenen mit dokumentierten Toleranzen.
- [ ] Fehlerinjektion, Timing, Ressourcen, Betriebsmodi und Diagnose sind abgedeckt.
- [ ] Prüfstand, Modelle und Softwarestand je Lauf sind reproduzierbar dokumentiert.
- [ ] Werkzeuge mit Nachweisrelevanz sind qualifiziert.
- [ ] Nachweise sind versioniert und assessmentfähig abgelegt.
