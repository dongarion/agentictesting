# Test-Driven Development (TDD)

Entwicklungspraktik: **Test zuerst, dann der kleinste Code, der ihn besteht, dann aufräumen.**
TDD ist primär eine Design- und Entwicklungsdisziplin; der Tester unterstützt, coacht und
nutzt die entstehende Unit-Testbasis als Fundament der Pyramide.

## Inhalt
1. Zyklus
2. Regeln
3. Testbares Design
4. Schulen und Varianten
5. Rolle des Testers
6. Anti-Patterns
7. Prüfliste

## 1. Zyklus

1. **Rot:** Einen kleinen Test schreiben, der ein noch nicht vorhandenes Verhalten beschreibt.
   Test ausführen, er muss fehlschlagen, und zwar aus dem erwarteten Grund.
2. **Grün:** Den einfachsten Code schreiben, der den Test besteht. Keine Vorwegnahme.
3. **Refactor:** Code und Tests verbessern (Duplikate entfernen, Namen, Struktur), alle Tests
   bleiben grün.
4. Wiederholen in Minutenschritten.

## 2. Regeln

- Kein Produktivcode ohne fehlschlagenden Test.
- Nicht mehr Test schreiben, als für einen Fehlschlag nötig; nicht mehr Code, als für Grün nötig.
- Tests sind FIRST: Fast, Independent, Repeatable, Self-validating, Timely.
- Ein Test prüft ein Verhalten; Name beschreibt es (`gibt_null_rabatt_bei_zweiter_bestellung`).
- Struktur Arrange–Act–Assert (oder Given–When–Then).
- Tests gehören zum Code: gleiche Reviews, gleiche Qualitätsansprüche, gleiche Pflege.

## 3. Testbares Design

TDD erzwingt Testbarkeit, und das ist der eigentliche Gewinn:

- Kleine Einheiten mit klarer Verantwortung.
- Abhängigkeiten werden injiziert, nicht intern erzeugt; dadurch ersetzbar durch Test-Doubles.
- Seiteneffekte (Zeit, Zufall, Datei, Netz) hinter Schnittstellen kapseln.
- Reine Funktionen bevorzugen.

Test-Doubles unterscheiden (Meszaros): **Dummy** (Platzhalter), **Stub** (liefert feste
Antworten), **Spy** (zeichnet Aufrufe auf), **Mock** (prüft erwartete Interaktion),
**Fake** (funktionierende Vereinfachung, z. B. In-Memory-Repository). Mocks sparsam einsetzen;
sie koppeln den Test an die Implementierung.

## 4. Schulen und Varianten

- **Klassisch (Detroit/Chicago):** von innen nach außen, echte Kollaborateure, Zustandsprüfung.
- **Mockist (London):** von außen nach innen, Mocks für Kollaborateure, Interaktionsprüfung.
- **Outside-in mit BDD:** erst ein fehlschlagendes Akzeptanzszenario, dann TDD-Zyklen innen,
  bis das Szenario grün ist (Double-Loop).
- **Transformation Priority Premise** (Martin): einfache Transformationen zuerst, um
  Generalisierung schrittweise zu erzwingen.

## 5. Rolle des Testers

- Testideen in Pairing-Sessions einbringen: Grenzfälle, Fehlerfälle, Datenvarianten.
- Mit Entwicklern Testbarkeit im Design besprechen, bevor die Story startet.
- Unit-Tests lesen und Lücken melden (Mutationstest als Hilfsmittel).
- Nicht duplizieren: Was Unit-Tests sicher abdecken, braucht keinen E2E-Test.
- Coaching: Katas, Dojos, Review von Testnamen und Assertions.

## 6. Anti-Patterns

- Tests nach dem Code schreiben und es TDD nennen.
- Test, der sofort grün ist (prüft nichts Neues).
- Riesige Schritte; eine Stunde bis zum nächsten Grün.
- Refactoring auslassen; Testsuite verrottet.
- Private Methoden testen; Tests koppeln an Interna.
- Über-Mocking: Test besteht, obwohl das Zusammenspiel kaputt ist.
- Tests, die Implementierungsdetails spiegeln und bei jedem Refactoring brechen.

## 7. Prüfliste

- [ ] Jeder Test hat vor der Implementierung fehlgeschlagen, aus dem erwarteten Grund.
- [ ] Tests laufen in Sekunden, isoliert und deterministisch.
- [ ] Testnamen beschreiben Verhalten, Struktur ist AAA.
- [ ] Seiteneffekte sind gekapselt, Abhängigkeiten injizierbar.
- [ ] Mocks nur für externe Kollaborateure; Zustandsprüfung bevorzugt.
- [ ] Refactoring-Schritt findet statt; Testcode ist so sauber wie Produktivcode.
