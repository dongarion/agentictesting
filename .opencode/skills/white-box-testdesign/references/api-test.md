# API-Test

Test von Schnittstellen (REST, SOAP, GraphQL, gRPC, Messaging, Bibliotheks-APIs) direkt am
Vertrag, ohne Oberfläche. Technisch ein Strukturtest, weil er Schnittstellenstruktur und
-vertrag als Testbasis nutzt; inhaltlich kombiniert er Black-Box-Verfahren mit Kenntnis der
Implementierung.

## Inhalt
1. Testbasis
2. Testdimensionen
3. Vorgehen
4. Fehlerbehandlung und Robustheit
5. Werkzeuge
6. Anti-Patterns
7. Prüfliste
8. Beispiel

## 1. Testbasis

- Vertrag: OpenAPI/Swagger, WSDL/XSD, GraphQL-Schema, Protobuf, AsyncAPI.
- Fachliche Spezifikation des Verhaltens hinter dem Endpunkt.
- Nicht-funktionale Vorgaben: Antwortzeiten, Limits, Authentifizierung.
- Prüfe zuerst den Vertrag selbst: fehlende Fehlercodes, undefinierte Pflichtfelder,
  widersprüchliche Typen sind Befunde vor dem ersten Aufruf.

## 2. Testdimensionen

| Dimension | Prüfung |
| --- | --- |
| Vertrag | Antwort entspricht Schema (Felder, Typen, Pflicht/optional, Enums) |
| Funktion | Fachlich korrektes Ergebnis je Eingabe (Black-Box-Verfahren anwenden) |
| Statuscodes | Jeder spezifizierte Code wird erreicht; kein unspezifizierter Code tritt auf |
| Fehlerfälle | Ungültige Eingaben, fehlende Felder, falsche Typen, zu große Payloads |
| Sicherheit | Authentifizierung, Autorisierung je Rolle, Zugriff auf fremde Objekte (IDOR), Injection |
| Idempotenz | Wiederholte PUT/DELETE liefern denselben Zustand; POST mit Idempotency-Key |
| Zustand | Reihenfolgeabhängigkeit (erst anlegen, dann lesen, dann löschen, dann 404) |
| Paging/Filter/Sortierung | Grenzen, leere Seiten, ungültige Parameter |
| Nebenläufigkeit | Parallele Änderungen, optimistisches Sperren, ETags |
| Versionierung | Alte Version weiter bedienbar, Deprecation-Header |
| Nicht-funktional | Antwortzeit, Rate Limits (429), Timeouts, große Antworten |

## 3. Vorgehen

1. Endpunkte und Operationen aus dem Vertrag listen. Je Operation eine Zeile.
2. Je Operation Eingabeparameter mit Äquivalenzklassen und Grenzwerten versehen
   (Black-Box-Skill). Pfad-, Query-, Header- und Body-Parameter getrennt.
3. Erwartete Antworten (Code, Body, Header) aus Vertrag und Fachspezifikation belegen.
4. Abhängigkeiten isolieren: Fremdsysteme mocken oder virtualisieren, Testdaten je Lauf
   erzeugen und aufräumen.
5. Tests automatisieren; API-Tests sind die wirtschaftlichste Ebene für Regression.
6. Vertragsprüfung automatisiert gegen das Schema laufen lassen (Schema-Validierung je Antwort).

## 4. Fehlerbehandlung und Robustheit

- Jeder Fehlerfall liefert den spezifizierten Code **und** eine strukturierte Fehlermeldung
  ohne interne Details (Stacktrace, SQL, Pfade).
- Unbekannte Felder im Request: ignoriert oder abgewiesen? Muss spezifiziert sein.
- Zeichensatz, Null gegenüber fehlendem Feld, leere Arrays gegenüber `null`.
- Timeouts und Teilausfälle von Abhängigkeiten: definierte Reaktion statt 500.

## 5. Werkzeuge

| Zweck | Beispiele |
| --- | --- |
| Manuell und explorativ | Postman, Insomnia, Bruno, SoapUI |
| Automatisiert | REST Assured, Karate, Robot Framework RequestsLibrary, pytest + httpx, Playwright API |
| Schema-basiert | Schemathesis, Dredd, Spectral (Vertragslinting) |
| Verträge zwischen Teams | Pact (siehe Agile/DevOps-Skill, Contract Testing) |
| Mocking | WireMock, Mockoon, Prism |

## 6. Anti-Patterns

- Nur Statuscode 200 prüfen, Body ignorieren.
- Testdaten aus einer geteilten Umgebung lesen, statt sie je Test zu erzeugen.
- Tests, die von der Reihenfolge anderer Tests abhängen, ohne das zu deklarieren.
- Autorisierung nur für den Admin testen.
- Fehlermeldungen mit internen Details als „hilfreich“ akzeptieren.

## 7. Prüfliste

- [ ] Vertrag ist auf Lücken und Widersprüche geprüft.
- [ ] Jede Operation hat Tests für gültige Klassen, jede ungültige Klasse einzeln und jeden spezifizierten Statuscode.
- [ ] Autorisierung ist je Rolle und für fremde Objekte getestet.
- [ ] Antworten werden gegen das Schema validiert.
- [ ] Testdaten werden je Lauf erzeugt und entfernt.
- [ ] Idempotenz und Zustandsreihenfolge sind getestet.

## 8. Beispiel

`POST /antraege` laut OpenAPI: Pflichtfelder `antragsart` (Enum), `antragsteller` (Objekt),
Antworten 201, 400, 401, 403, 422.

| TF | Eingabe | Erwartet | Quelle |
| --- | --- | --- | --- |
| A1 | gültiger Antrag | 201, Body mit `id`, `Location`-Header | OpenAPI + Fachspez. §3.1 |
| A2 | `antragsart` fehlt | 400, Fehlerobjekt nennt Feld | OpenAPI |
| A3 | `antragsart` = „Sonstiges“ (nicht im Enum) | 400 | OpenAPI |
| A4 | ohne Token | 401 | OpenAPI |
| A5 | Rolle „Leser“ | 403 | Berechtigungskonzept |
| A6 | fachlich ungültig (Enddatum vor Startdatum) | 422 | Fachspez. §3.4 |
| A7 | unbekanntes Feld `foo` | ? | offene Frage |
| A8 | identischer POST zweimal mit gleichem Idempotency-Key | 201, dann 200 oder 201 mit gleicher `id`? | offene Frage |
