# Überdeckungsziele, Normen und Bewertung von Berichten

## Inhalt
1. Ziele nach Risiko und Norm
2. Überdeckungsbericht bewerten
3. Lücken klassifizieren
4. Mutationstest als Qualitätsprüfung der Tests
5. Prüfliste

## 1. Ziele nach Risiko und Norm

Überdeckungsziele sind **Mindestanforderungen**, kein Qualitätsbeweis. Zitiere die Quelle.

| Kontext | Typisches Ziel | Quelle |
| --- | --- | --- |
| Geschäftsanwendung, mittleres Risiko | Zweigüberdeckung 70–80 % für Kernlogik | Teststrategie des Projekts |
| Sicherheitsrelevante Komponenten, hohes Risiko | Zweigüberdeckung 100 %, MC/DC für komplexe Entscheidungen | Teststrategie, Kunde |
| Luftfahrt DAL A | MC/DC, Entscheidungs- und Anweisungsüberdeckung 100 % | DO-178C Tabelle A-7 |
| Luftfahrt DAL B | Entscheidungs- und Anweisungsüberdeckung | DO-178C |
| Luftfahrt DAL C | Anweisungsüberdeckung | DO-178C |
| Automotive ASIL D | Anweisung, Zweig, MC/DC jeweils „++“ (dringend empfohlen) | ISO 26262-6 Tabelle 9 |
| Automotive ASIL B | Anweisung „++“, Zweig „+“ | ISO 26262-6 |
| Bahn SIL 3/4 | Anweisung, Zweig, zusammengesetzte Bedingung, Datenfluss, Pfad „HR“ | EN 50128 Tabelle A.21 |
| Medizin Klasse C | Strukturüberdeckung als Teil der Unit-Verifikation | IEC 62304 (kein Prozentziel) |

Exakte Tabellen und Formulierungen aus der jeweils gültigen Normversion entnehmen; die Werte
hier dienen der Orientierung.

## 2. Überdeckungsbericht bewerten

Ein Bericht beantwortet die Frage „Was wurde ausgeführt?“. Prüfe zusätzlich:

1. **Zählweise:** Zeilen, Anweisungen, Zweige, Bedingungen? Werkzeuge mischen Begriffe
   (JaCoCo „Branches“, gcov „Branches“, Istanbul „Branches“ zählen unterschiedlich).
2. **Ausschlüsse:** Welcher Code ist ausgenommen (generiert, Test-Utilities, Annotationen wie
   `@Generated`, `// LCOV_EXCL`)? Jeder Ausschluss braucht eine Begründung.
3. **Assertions:** Stichprobe der Tests mit höchstem Überdeckungsbeitrag. Prüfen sie Ergebnisse?
4. **Verteilung:** Gesamtprozent verschleiert. Überdeckung je Modul betrachten; kritische Module
   zuerst.
5. **Trend:** Sinkende Überdeckung bei wachsendem Code ist ein Frühwarnsignal.
6. **Instrumentierung:** Verändert sie Zeitverhalten oder Optimierung (relevant bei Embedded)?
   Für normative Nachweise oft Messung am Zielcode erforderlich.

## 3. Lücken klassifizieren

| Klasse | Behandlung |
| --- | --- |
| Fehlender Test | Testfall ergänzen |
| Unerreichbarer Code | Befund, Entfernung vorschlagen |
| Defensive Programmierung (theoretisch unmöglich) | Begründete Ausnahme, mit Review bestätigen |
| Fehlerpfad schwer provozierbar | Mit Mock, Fault Injection oder Unit-Test auf tieferer Ebene erreichen |
| Generierter Code | Ausschluss, wenn Generator qualifiziert ist |
| Plattform- oder Compiler-spezifisch | Je Zielplattform messen |

Jede Ausnahme mit Fundstelle, Begründung und Freigeber dokumentieren.

## 4. Mutationstest als Qualitätsprüfung der Tests

Überdeckung misst Ausführung, Mutationstest misst **Fehlererkennung**: Das Werkzeug baut
künstliche Fehler ein (Operator vertauscht, Konstante geändert, Bedingung negiert) und prüft, ob
mindestens ein Test fehlschlägt. Überlebende Mutanten zeigen Tests ohne wirksame Assertions.
Werkzeuge: PIT (Java), Stryker (JS/TS, .NET, Scala), mutmut und cosmic-ray (Python), mull (C/C++).
Details im Skill für fortgeschrittene Testmethoden.

## 5. Prüfliste

- [ ] Überdeckungsziel ist mit Normstelle oder Strategieabschnitt belegt.
- [ ] Zählweise des Werkzeugs ist dokumentiert und mit dem Ziel kompatibel.
- [ ] Ausschlüsse sind einzeln begründet.
- [ ] Stichprobe der Tests auf Assertions ist durchgeführt.
- [ ] Überdeckung je kritischem Modul liegt vor, nicht nur gesamt.
- [ ] Jede Lücke ist klassifiziert und bei Ausnahme freigegeben.
