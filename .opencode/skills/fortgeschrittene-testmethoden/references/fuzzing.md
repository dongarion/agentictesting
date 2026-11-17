# Fuzzing

Automatisches Einspeisen großer Mengen **zufälliger, mutierter oder grammatikbasierter
Eingaben**, um Abstürze, Hänger, Speicherfehler, unbehandelte Ausnahmen und
Sicherheitslücken zu finden. Orakel ist meist nur „stürzt nicht ab, verletzt keine Invariante“.

## Inhalt
1. Fuzzing-Arten
2. Ziele und Orakel
3. Vorgehen
4. Fuzz-Ziele schreiben
5. Werkzeuge
6. Umgang mit Befunden
7. Anti-Patterns
8. Prüfliste

## 1. Fuzzing-Arten

| Art | Prinzip | Eignung |
| --- | --- | --- |
| Mutationsbasiert | Gültige Beispiel-Eingaben (Seeds) werden verändert | Parser, Dateiformate, Protokolle |
| Generationsbasiert / grammatikbasiert | Eingaben aus Grammatik oder Schema erzeugt | Strukturierte Formate, APIs mit OpenAPI |
| Coverage-guided | Eingaben, die neue Codepfade erreichen, werden bevorzugt weiterentwickelt | Alles mit Instrumentierung (AFL++, libFuzzer) |
| Protokoll-Fuzzing | Zustandsbehaftete Nachrichtenfolgen | Netzwerkprotokolle, IoT |
| API-/Web-Fuzzing | Parameter, Header, Pfade, Payloads | REST, GraphQL, Formulare |

## 2. Ziele und Orakel

Fuzzing findet, was ohne Spezifikation erkennbar ist:

- Absturz, Signal, Panic, unbehandelte Exception.
- Speicherfehler (mit Sanitizern: ASan, UBSan, MSan).
- Hänger, Timeouts, exzessiver Ressourcenverbrauch (DoS).
- Verletzte Assertions oder Invarianten im Code.
- Unterschiedliches Verhalten zweier Implementierungen (Differential Fuzzing).
- HTTP 500 oder Stacktrace in der Antwort bei API-Fuzzing.

Fachliche Fehler („falsche Zahl“) findet Fuzzing nur mit zusätzlichem Orakel
(Properties, metamorphe Relationen).

## 3. Vorgehen

1. Angriffsfläche bestimmen: Wo kommen nicht vertrauenswürdige Daten herein? Parser,
   Deserialisierung, Datei-Import, API-Endpunkte, Protokollhandler.
2. Fuzz-Ziel schreiben (siehe 4) oder Werkzeug auf API/Schema richten.
3. Seeds sammeln: gültige, vielfältige, kleine Beispiele.
4. Sanitizer und Assertions aktivieren.
5. Laufen lassen: lokal Minuten, in CI begrenzt (z. B. 10 min je Ziel), nächtlich oder
   dauerhaft länger (OSS-Fuzz, ClusterFuzz).
6. Korpus und gefundene Fälle versionieren; Regressionstests aus jedem Fund ableeiten.

## 4. Fuzz-Ziele schreiben

- Ein Fuzz-Ziel nimmt ein Byte-Array oder strukturierte Daten entgegen und ruft die zu
  testende Funktion auf. Es muss deterministisch, schnell und seiteneffektfrei sein.
- Keine globalen Zustände, keine Netzwerkaufrufe, keine Dateisystemabhängigkeit.
- Erwartete Ausnahmen abfangen (ungültige Eingabe darf eine definierte Exception werfen),
  alles andere durchlassen.
- Strukturierte Eingaben per Bibliothek aus Bytes ableiten (`FuzzedDataProvider`,
  Hypothesis-Strategien, Arbitrary in Rust).

## 5. Werkzeuge

| Bereich | Werkzeug |
| --- | --- |
| C/C++/Rust, nativ | AFL++, libFuzzer, honggfuzz, cargo-fuzz |
| Java/Kotlin | Jazzer |
| Python | Atheris, Hypothesis (PBT als leichtes Fuzzing) |
| Go | eingebautes `go test -fuzz` |
| .NET | SharpFuzz |
| Web/API | OWASP ZAP, Burp Intruder, RESTler, Schemathesis, ffuf, wfuzz |
| Protokolle | boofuzz, Peach (kommerziell) |
| Dauerbetrieb | OSS-Fuzz, ClusterFuzz, CI Fuzz |

## 6. Umgang mit Befunden

- Jeden Absturz minimieren (Werkzeug-Minimizer), deduplizieren (Stacktrace-Hash), als
  Regressionstest mit der auslösenden Eingabe ablegen.
- Sicherheitsrelevanz bewerten: Speicherfehler in Parsern von Fremddaten sind potenziell
  ausnutzbar; nach Prozess für Sicherheitsvorfälle behandeln.
- Hänger und Ressourcenfresser nicht als „nur Performance“ abtun; sie sind DoS-Kandidaten.

## 7. Anti-Patterns

- Fuzzing ohne Sanitizer bei nativem Code; die Hälfte der Fehler bleibt unsichtbar.
- Fuzz-Ziel mit Netzwerk- oder Dateizugriff; langsam und nicht deterministisch.
- Keine Seeds; der Fuzzer braucht lange, um gültige Strukturen zu finden.
- Korpus nicht aufheben; jeder Lauf beginnt bei null.
- API-Fuzzing gegen Produktion.

## 8. Prüfliste

- [ ] Angriffsfläche ist bestimmt, Fuzz-Ziele decken sie ab.
- [ ] Seeds sind vorhanden und vielfältig.
- [ ] Sanitizer und Assertions sind aktiv.
- [ ] Laufzeitbudget in CI und nächtlich ist festgelegt.
- [ ] Korpus und Funde sind versioniert, Regressionstests abgeleitet.
- [ ] Sicherheitsrelevante Funde laufen über den Vorfallprozess.
