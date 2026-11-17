# Werkzeuge nach Einsatzgebiet

Stand der Übersicht: Ende 2026. Werkzeuglandschaften ändern sich; vor einer Entscheidung die
aktuelle Lage prüfen. Die Einordnung dient der Vorauswahl, nicht als Empfehlung ohne Kontext.

## Inhalt
1. Web-GUI
2. API und Services
3. Mobile
4. Desktop
5. Visueller Regressionstest
6. Unit- und Komponententest
7. Last und Performance
8. Reporting und Testmanagement
9. Auswahlhilfe

## 1. Web-GUI

| Werkzeug | Sprache | Stärken | Beachten |
| --- | --- | --- | --- |
| Playwright | TS/JS, Python, Java, .NET | Auto-Wait, Trace Viewer, mehrere Browser, API-Tests integriert, Parallelität | Jüngeres Ökosystem als Selenium, keine echten Geräte |
| Cypress | TS/JS | Entwicklerfreundlich, Zeitreise-Debugging, Komponententests | Läuft im Browser (Einschränkungen bei Multi-Tab, Cross-Origin), JS-only |
| Selenium WebDriver | alle gängigen | W3C-Standard, größtes Ökosystem, Grid, echte Geräte über Anbieter | Synchronisation selbst bauen, mehr Boilerplate |
| Robot Framework + Browser Library (Playwright) oder SeleniumLibrary | Schlüsselwörter, Python | Fachsprache, Fachtester einbindbar, riesige Bibliotheksauswahl, RobotCode für VS Code | Eigene Syntax, Debugging weniger komfortabel |
| WebdriverIO | TS/JS | Selenium und Devtools, Mobile über Appium | JS-only |
| TestCafe | TS/JS | Einfacher Einstieg | Kleinere Community |

## 2. API und Services

| Werkzeug | Einsatz |
| --- | --- |
| Postman/Newman, Bruno, Insomnia | Manuell, explorativ, einfache Automatisierung |
| REST Assured (Java), httpx/requests + pytest (Python), supertest (Node), RestSharp (.NET) | Codebasierte API-Tests |
| Karate | DSL für API-, Mock- und Lasttests in einem |
| Robot Framework RequestsLibrary | Schlüsselwortbasiert |
| SoapUI / ReadyAPI | SOAP, WSDL, Legacy, kommerzielle Features |
| Schemathesis, Dredd | Vertragsbasierte Generierung aus OpenAPI |
| Pact | Consumer-Driven Contracts |
| WireMock, Mockoon, Prism | Mocks und Virtualisierung |
| gRPCurl, ghz | gRPC |

## 3. Mobile

| Werkzeug | Einsatz |
| --- | --- |
| Appium | Plattformübergreifend, WebDriver-Protokoll, native und hybride Apps |
| Espresso (Android), XCUITest (iOS) | Nativ, schnell, stabil, von Entwicklern gepflegt |
| Maestro | YAML-Flows, einfacher Einstieg, Flakiness-tolerant |
| Detox | React Native |
| Gerätefarmen: BrowserStack, Sauce Labs, AWS Device Farm, Firebase Test Lab | Echte Geräte, Gerätematrix |

## 4. Desktop

| Werkzeug | Einsatz |
| --- | --- |
| WinAppDriver, FlaUI (Windows) | UI-Automation-API |
| Playwright für Electron | Electron-Anwendungen |
| SikuliX, Pywinauto | Bilderkennung, Legacy ohne Testhaken |
| Ranorex, TestComplete, Tosca, UFT | Kommerziell, breite Technologieabdeckung, Lizenzkosten |

## 5. Visueller Regressionstest

Vergleich von Screenshots gegen Referenzbilder, pixel- oder wahrnehmungsbasiert.

| Werkzeug | Einsatz |
| --- | --- |
| Playwright `toHaveScreenshot`, Cypress-Plugins, BackstopJS | Pixelvergleich, Open Source, lokal |
| Applitools Eyes, Percy, Chromatic | KI-/wahrnehmungsbasiert, Cloud, Review-Workflow, Komponentenbibliotheken (Storybook) |
| Loki, reg-suit | Storybook-Komponenten |

Regeln: Referenzbilder je Browser und Auflösung, dynamische Inhalte maskieren (Zeit, Werbung),
Schwellwerte dokumentieren, Review-Prozess für Änderungen der Referenz, Fokus auf
Komponenten statt ganzer Seiten.

## 6. Unit- und Komponententest

JUnit 5/TestNG (Java), pytest (Python), Jest/Vitest (JS), xUnit/NUnit (.NET), Go testing,
Rust cargo test; Mocking: Mockito, unittest.mock, Sinon, Moq; Komponententests für UI:
Testing Library, Storybook Interaction Tests, Cypress Component Testing, Playwright CT.

## 7. Last und Performance

k6, Gatling, JMeter, Locust; siehe Skill Spezialtests.

## 8. Reporting und Testmanagement

| Werkzeug | Einsatz |
| --- | --- |
| Allure, ReportPortal | Reporting mit Historie, Screenshots, Traces |
| Robot Framework eigene Reports, Robotmk | Robot-spezifisch |
| Xray, Zephyr, TestRail, Azure Test Plans, Testmo | Testmanagement mit CI-Anbindung |
| Pipeline-native Reports (GitLab JUnit, GitHub Checks) | Minimal, in der Pipeline sichtbar |

## 9. Auswahlhilfe

| Situation | Startpunkt |
| --- | --- |
| Web, Entwickler schreiben Tests, TS-Stack | Playwright |
| Web, Fachtester schreiben mit, Python-Umfeld, Behörde | Robot Framework + Browser Library |
| Viele Browser und Legacy-Browser, bestehendes Grid | Selenium |
| API-first, Java | REST Assured oder Karate |
| API-first, Python | pytest + httpx, Schemathesis für Vertragsprüfung |
| Mobile, beide Plattformen, ein Team | Appium oder Maestro; nativ, wenn Entwickler mitziehen |
| Komponentenbibliothek, Design System | Storybook + Chromatic oder Playwright CT |
| SOAP, Legacy-Integration | SoapUI, Migration zu REST-Werkzeugen planen |
