# Contract Testing, Service-Virtualisierung, Mocks und Stubs

Bei verteilten Systemen scheitern Integrationstests oft an **Verfügbarkeit, Instabilität und
Testdaten der Abhängigkeiten**. Zwei Antworten: Abhängigkeiten simulieren (Virtualisierung,
Mocks, Stubs) und Schnittstellenverträge unabhängig prüfen (Contract Testing).

## Inhalt
1. Begriffe und Ebenen
2. Mocks und Stubs im Komponententest
3. Service-Virtualisierung
4. Consumer-Driven Contract Testing
5. Werkzeuge
6. Anti-Patterns
7. Prüfliste

## 1. Begriffe und Ebenen

| Ebene | Mittel | Ersetzt |
| --- | --- | --- |
| Komponententest | Stub, Mock, Fake (im Code) | Klassen, Module |
| Integrationstest | Service-Virtualisierung, HTTP-Mock-Server | Fremde Services, Legacy, Drittanbieter |
| Teamübergreifend | Contract Testing | Den gemeinsamen Integrationstest zwischen Consumer und Provider |

## 2. Mocks und Stubs im Komponententest

- **Stub:** liefert vorbereitete Antworten; Test prüft den Zustand danach.
- **Mock:** erwartet bestimmte Aufrufe; Test prüft die Interaktion.
- **Fake:** lauffähige Vereinfachung (In-Memory-Datenbank, lokaler Mailserver).
- Regel: Zustand prüfen, wo möglich; Interaktion nur, wenn sie selbst die Anforderung ist
  (z. B. „Mail wird genau einmal versendet“).
- Nicht mocken, was man besitzt und schnell testen kann. Mocken, was langsam, fremd,
  nicht deterministisch oder teuer ist.

## 3. Service-Virtualisierung

Simuliert das Verhalten eines Services über HTTP, Messaging oder Datenbank, inklusive
Antwortzeiten, Fehlern und Zustand.

Einsatz:

- Abhängigkeit nicht verfügbar, kostenpflichtig, mit Rate Limits oder ohne Testumgebung
  (Bankschnittstellen, Behördenregister, Drittanbieter-APIs).
- Fehlerfälle provozieren, die das echte System nicht liefert: Timeout, 500, defekte Payload,
  langsame Antwort.
- Parallelentwicklung: Consumer baut gegen den virtuellen Provider, bevor der echte existiert.

Vorgehen:

1. Schnittstellenvertrag (OpenAPI, WSDL) als Grundlage; aufgezeichnete Antworten
   (Record/Replay) nur als Startpunkt, dann bereinigen.
2. Antworten je Szenario definieren: Erfolg, jeder Fehlercode, Timeout, langsame Antwort.
3. Zustand simulieren, wo nötig (erst anlegen, dann lesen).
4. Virtualisierung versionieren, zusammen mit den Tests.
5. Regelmäßig gegen den echten Service abgleichen (Contract Test oder nächtlicher Lauf),
   sonst driftet die Simulation.

## 4. Consumer-Driven Contract Testing

Der **Consumer** beschreibt, welche Anfragen er stellt und welche Antworten er braucht.
Dieser Vertrag wird gegen den **Provider** verifiziert. Beide Seiten testen isoliert; kein
gemeinsamer Integrationstest nötig, um Kompatibilität nachzuweisen.

Ablauf mit Pact:

1. Consumer-Test läuft gegen einen Pact-Mock-Server und erzeugt die Pact-Datei (Vertrag).
2. Vertrag wird im Pact Broker veröffentlicht, mit Consumer-Version und Branch.
3. Provider holt den Vertrag, spielt die Anfragen gegen sich ab, prüft die Antworten
   (Provider States stellen die nötigen Daten bereit).
4. Ergebnis geht an den Broker. `can-i-deploy` prüft vor jedem Deployment, ob die
   Versionen kompatibel sind.

Regeln:

- Consumer fordert nur, was er wirklich nutzt (Postel: Felder, die er liest, nicht die ganze Antwort).
- Keine Fachlogik im Vertrag testen; der Vertrag prüft Struktur und Semantik der Schnittstelle,
  nicht die Richtigkeit der Berechnung.
- Provider States sind Teil des Provider-Codes und werden gepflegt wie Tests.
- Bei Messaging: Nachrichtenverträge (Message Pacts) analog.
- Bidirektional (PactFlow) oder Schema-basiert (OpenAPI-Vergleich mit Spectral, Optic) als
  leichtere Alternative, wenn Consumer-Tests nicht möglich sind.

## 5. Werkzeuge

| Zweck | Werkzeuge |
| --- | --- |
| HTTP-Mock-Server | WireMock, Mockoon, Prism (aus OpenAPI), MockServer, Hoverfly |
| Messaging | Embedded Kafka, LocalStack (AWS), Testcontainers |
| Service-Virtualisierung (kommerziell) | Broadcom Service Virtualization, Parasoft Virtualize, Tricentis |
| Contract Testing | Pact (viele Sprachen), Pact Broker/PactFlow, Spring Cloud Contract |
| Echte Abhängigkeiten in Containern | Testcontainers (Datenbanken, Broker, Browser) |

Testcontainers verdient Vorrang vor Mocks, wenn die Abhängigkeit als Container verfügbar ist:
echte Datenbank in Sekunden, keine Drift.

## 6. Anti-Patterns

- Mock, der die Implementierung nachbildet; Test ist grün, Integration kaputt.
- Aufgezeichnete Antworten mit Produktionsdaten, nie bereinigt.
- Virtualisierung ohne Abgleich mit dem echten Service; Drift bleibt unbemerkt.
- Contract Test, der die ganze Antwort fixiert; jeder Provider-Zusatz bricht den Vertrag.
- Pact ohne Broker und ohne `can-i-deploy`; Verträge werden per Mail verschickt.
- Contract Testing als Ersatz für jeden E2E-Test; ein dünner E2E-Smoke bleibt nötig.

## 7. Prüfliste

- [ ] Je Abhängigkeit ist entschieden: echt (Container), virtualisiert oder gemockt, mit Begründung.
- [ ] Virtualisierte Antworten decken Erfolg, jeden Fehlercode, Timeout und langsame Antwort ab.
- [ ] Virtualisierungen sind versioniert und werden gegen den echten Service abgeglichen.
- [ ] Consumer-Verträge enthalten nur genutzte Felder.
- [ ] Provider verifiziert Verträge in seiner Pipeline; `can-i-deploy` ist Teil des Deployments.
- [ ] Keine Produktionsdaten in Aufzeichnungen und Verträgen.
