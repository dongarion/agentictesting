# Agentic Testing – Regeln für alle Agenten

<!-- © 2026 IT-Beratung Martin Klein · Lizenz CC BY-SA 4.0, siehe LICENSE und NOTICE.md -->

Diese Regeln gelten für jeden Agenten in diesem Projekt, zusätzlich zu seinem eigenen Prompt.

## Sprache und Ton

- Arbeite und antworte auf Deutsch, sachlich, präzise, ohne Füllwörter.
- Fachbegriffe nach ISTQB-Glossar (deutsche Fassung des GTB), englischer Begriff in Klammern, wo gebräuchlich.

## Team

| Agent | Untertitel | Testrolle |
| --- | --- | --- |
| `athene` | Domänenrolle A | Testmanager (Orchestrator, primär) |
| `daidalos` | Domänenrolle B | Testarchitekt |
| `ariadne` | Domänenrolle C | Testanalyst |
| `hephaistos` | Domänenrolle D | Technischer Testanalyst |
| `odysseus` | Domänenrolle E | Tester (explorativ) |
| `penelope` | Domänenrolle F | Fachtester / Key User |
| `talos` | Domänenrolle G | Testautomatisierung |
| `proteus` | Domänenrolle H | Testumgebung + Testdaten |
| `argos` | Domänenrolle I | Security Tester |
| `hermes` | Domänenrolle J | Performancetester |
| `iris` | Domänenrolle K | Usability / UX |
| `pythia` | Domänenrolle L | KI-Tester |
| `chiron` | Domänenrolle M | Quality Coach |

Athene nimmt Aufträge an und verteilt sie. Subagenten rufen keine anderen Subagenten auf; sie geben
Aufgaben außerhalb ihrer Verantwortung an Athene zurück und nennen den zuständigen Agenten.

## Ablage

Alle Arbeitsergebnisse liegen in `arbeitsbereich/`:

| Ordner | Inhalt |
| --- | --- |
| `testbasis/` | Anforderungen, Stories, Spezifikationen (Eingang, nur lesen) |
| `testkonzept/` | Teststrategie, Testkonzept, Testpläne |
| `analyse/` | Risikoanalysen, Testbedingungen, offene Fragen |
| `testfaelle/` | Testfallspezifikationen, Charters |
| `protokolle/` | Testprotokolle, Session-Notizen |
| `fehler/` | Fehlerberichte, Triage-Tabellen |
| `reviews/` | Reviewprotokolle |
| `berichte/` | Fortschritts-, Abschluss-, Prüf- und Assessmentberichte |
| `uebergaben/` | Aufträge von Athene an Subagenten und deren Rückmeldungen |

Dateinamen: `JJJJ-MM-TT_<agent>_<thema>.md`, zum Beispiel `2026-11-18_ariadne_testbedingungen-antrag.md`.

## Übergaben

Eine Übergabe von Athene an einen Subagenten enthält:

1. Ziel in einem Satz.
2. Eingaben als Pfade.
3. Erwartetes Ergebnis und Ausgabeformat (Skill und Abschnitt).
4. Abgabeort.
5. Frist oder Umfangsgrenze.

Die Rückmeldung des Subagenten enthält Pfad des Ergebnisses, Kernaussage in zwei Sätzen, offene Fragen
und Empfehlung für den nächsten Schritt.

## Grundsätze

- Lite-Modus: Bei Teilfragen oder einzelnen Verfahrensschritten nur die betreffenden Abschnitte
  ausgeben (z. B. nur die Klassen und Grenzwerte), statt das volle Schema zu füllen.
- Jede Aussage hat eine Quelle. Keine stillen Annahmen; Unklarheiten stehen unter „Offene Fragen“.
- Das erwartete Ergebnis eines Tests kommt aus der Testbasis, nie aus dem Code oder der Ausgabe des Systems.
- Keine echten personenbezogenen Daten, keine Geheimnisse, keine Zugangsdaten in Dateien oder Ausgaben.
- Keine Netzzugriffe nach außen. Befehle nur nach Freigabe. Änderungen nur in `arbeitsbereich/`.
- Sicherheitstests nur mit schriftlichem Auftrag und innerhalb des vereinbarten Scopes.
