# Sicherheitstest

Vom Entwurf bis zum Betrieb: **Bedrohungen modellieren, Code und Abhängigkeiten prüfen,
laufende Anwendung angreifen, Reaktion testen.** Sicherheitstests sind nur mit schriftlichem
Auftrag und klarem Scope zulässig.

## Inhalt
1. Ebenen und Verfahren
2. Threat Modeling
3. SAST, SCA, Secret-Scanning
4. DAST und IAST
5. Penetrationstest
6. Red Teaming und Purple Teaming
7. Sicherheitsanforderungen testen
8. Befunde bewerten und berichten
9. Werkzeuge
10. Prüfliste

## 1. Ebenen und Verfahren

| Phase | Verfahren | Ergebnis |
| --- | --- | --- |
| Anforderung/Entwurf | Threat Modeling, Missbrauchsfälle, Sicherheitsanforderungen (ASVS) | Bedrohungsliste, Maßnahmen, Testfälle |
| Entwicklung | SAST, Secret-Scanning, SCA, Security Unit-Tests, Code-Review | Befunde im Code, verwundbare Abhängigkeiten |
| Test | DAST, IAST, Fuzzing, Test der Sicherheitsanforderungen, Konfigurationsprüfung | Laufzeitbefunde |
| Vor Release | Penetrationstest | Bericht mit Schwachstellen und Nachweisen |
| Betrieb | Schwachstellenscans, Red Teaming, Monitoring, Bug Bounty | Reifegrad der Erkennung und Reaktion |

Kein Verfahren ersetzt ein anderes. SAST findet keine Fehlkonfiguration, DAST keine Logikfehler
ohne Hilfe, der Pentest ist eine Stichprobe zu einem Zeitpunkt.

## 2. Threat Modeling

Vorgehen (Shostack, vier Fragen):

1. **Was bauen wir?** Datenflussdiagramm: Prozesse, Datenspeicher, externe Entitäten,
   Datenflüsse, Vertrauensgrenzen.
2. **Was kann schiefgehen?** Je Element Bedrohungen nach **STRIDE**: Spoofing, Tampering,
   Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege.
   Ergänzend Missbrauchsfälle („Als Angreifer möchte ich …“) und Angriffsbäume.
3. **Was tun wir dagegen?** Maßnahme je Bedrohung: vermeiden, mindern, übertragen, akzeptieren.
4. **Haben wir es gut gemacht?** Jede Bedrohung hat einen Testfall oder eine begründete Akzeptanz.

Bewertung der Bedrohungen mit CVSS-ähnlicher Einschätzung oder DREAD-Nachfolgern
(Wahrscheinlichkeit × Auswirkung). Bei jeder Architekturänderung aktualisieren.
Für KI-Komponenten zusätzlich OWASP LLM Top 10 und MITRE ATLAS.

## 3. SAST, SCA, Secret-Scanning

- **SAST** (statische Analyse auf Sicherheit): in der Pipeline je Merge Request; Regeln auf
  die Sprache und das Framework abgestimmt; Fehlalarmrate aktiv managen (Baseline, Triage,
  Unterdrückung mit Begründung).
- **SCA** (Abhängigkeiten): bekannte Schwachstellen (CVE), Lizenzen, veraltete Pakete;
  SBOM erzeugen (CycloneDX, SPDX); Aktualisierungsprozess mit Fristen je Schwere.
- **Secret-Scanning:** Zugangsdaten, Schlüssel, Token im Repository und in der Historie;
  Pre-Commit-Hook und Pipeline.
- **Container- und IaC-Scans:** Basis-Images, Konfiguration (Trivy, Grype, Checkov).
- Befunde fließen ins Fehlermanagement mit Schwere und Frist; Quality Gate für neue kritische Befunde.

## 4. DAST und IAST

- **DAST:** Scanner gegen die laufende Anwendung (OWASP ZAP, Burp, Nuclei). Authentifiziert
  scannen (sonst bleibt der größte Teil unsichtbar), Scope begrenzen, in Testumgebung, mit
  Testdaten. Automatisiert als Baseline-Scan in der Pipeline, voller Scan nächtlich.
- **IAST:** Agent in der Anwendung beobachtet während funktionaler Tests den Datenfluss
  und meldet Schwachstellen mit Codestelle; geringe Fehlalarmrate, braucht Testabdeckung.
- **API-Sicherheit:** OWASP API Security Top 10: fehlerhafte Objektautorisierung (BOLA/IDOR),
  fehlerhafte Authentifizierung, übermäßige Datenexposition, fehlende Ratenbegrenzung,
  Massenzuweisung. Gezielt testen, Scanner finden das kaum.

## 5. Penetrationstest

Manuelle, zielgerichtete Simulation eines Angriffs durch qualifizierte Tester.

- **Vorbereitung:** Schriftlicher Auftrag (Scope, Ausschlüsse, Zeitfenster, Notfallkontakte,
  Regeln für Datenzugriff, Rechtsgrundlage), Testart (Black/Grey/White Box), Testkonten je Rolle.
- **Methodik:** OWASP Web Security Testing Guide (WSTG), OWASP Mobile (MASTG), PTES,
  BSI-Leitfaden für Penetrationstests; bei Behörden BSI-Anforderungen beachten.
- **Phasen:** Aufklärung, Enumeration, Schwachstellenanalyse, Ausnutzung (nur im Rahmen),
  Nachbereitung, Bericht.
- **Bericht:** Management-Zusammenfassung, Befunde mit Schwere (CVSS), Nachweis, Reproduktion,
  Empfehlung, Scope und Grenzen. Nachtest nach Behebung.
- Pentest ist Stichprobe: Zeitpunkt, Scope, Testerfähigkeit. Kein „sicher“-Stempel.

## 6. Red Teaming und Purple Teaming

- **Red Team:** zielorientierter Angriff auf Organisation und Technik (Phishing, physisch,
  Lieferkette), oft ohne Vorwarnung der Verteidiger; prüft Erkennung und Reaktion.
- **Purple Team:** Angreifer und Verteidiger arbeiten zusammen; Angriffstechniken nach
  MITRE ATT&CK durchspielen und Erkennungsregeln verbessern.
- **Breach and Attack Simulation:** automatisierte, wiederholbare Angriffsszenarien.
- Für KI-Systeme: AI Red Teaming (siehe [ki-systeme.md](ki-systeme.md)).

## 7. Sicherheitsanforderungen testen

Nicht alles ist Angriff; vieles ist Funktionstest von Sicherheitsfunktionen:

- Authentifizierung: Passwortregeln, MFA, Sperrung, Session-Ablauf, Logout, Token-Lebensdauer.
- Autorisierung: jede Funktion je Rolle, horizontale (fremde Objekte) und vertikale
  (höhere Rechte) Eskalation; Matrix Rolle × Funktion vollständig testen.
- Eingabevalidierung und Ausgabekodierung: serverseitig, kontextbezogen.
- Kryptografie: TLS-Konfiguration, Zertifikatsprüfung, Speicherung von Geheimnissen.
- Protokollierung: sicherheitsrelevante Ereignisse werden geloggt, ohne Geheimnisse und ohne
  unnötige Personendaten; Logs manipulationssicher.
- Fehlerbehandlung: keine internen Details nach außen.
- Konfiguration: Security-Header, CORS, Standardpasswörter, offene Ports, Debug-Modi.

OWASP ASVS liefert eine prüfbare Anforderungsliste je Stufe (L1–L3).

## 8. Befunde bewerten und berichten

- Schwere nach CVSS (Basis-Score) plus Kontext (Exponiertheit, Daten, Kompensation).
- Je Befund: Beschreibung, Beleg (Screenshot, Request/Response ohne echte Daten), Reproduktion,
  betroffene Komponente, Empfehlung, Referenz (CWE, OWASP).
- Vertraulichkeit: Berichte sind sensibel; verschlüsselt, eingeschränkter Verteiler.
- Fristen je Schwere (z. B. kritisch 7 Tage), Nachtest, Tracking bis zur Schließung.

## 9. Werkzeuge

| Zweck | Werkzeuge |
| --- | --- |
| Threat Modeling | OWASP Threat Dragon, Microsoft Threat Modeling Tool, IriusRisk, pytm |
| SAST | Semgrep, CodeQL, SonarQube, Checkmarx, Fortify, Bandit (Python), SpotBugs/FindSecBugs |
| SCA / SBOM | OWASP Dependency-Check, Dependency-Track, Trivy, Grype, Snyk, Renovate/Dependabot |
| Secrets | gitleaks, trufflehog, detect-secrets |
| DAST | OWASP ZAP, Burp Suite, Nuclei, Nikto |
| IAST | Contrast, Seeker, Datadog ASM |
| API | Postman/Newman mit Sicherheitsfällen, Schemathesis, 42Crunch |
| Pentest | Burp, Kali-Werkzeuge (nmap, sqlmap, ffuf, Metasploit), Mobile: Frida, MobSF |
| Infrastruktur | OpenVAS/Greenbone, Nessus, Checkov, kube-bench, Lynis |

## 10. Prüfliste

- [ ] Schriftlicher Auftrag mit Scope, Ausschlüssen, Zeitfenster und Notfallkontakten liegt vor.
- [ ] Threat Model existiert und ist aktuell; jede Bedrohung hat Testfall oder Akzeptanz.
- [ ] SAST, SCA, Secret-Scanning laufen je Merge Request mit Quality Gate.
- [ ] DAST authentifiziert, in Testumgebung, mit begrenztem Scope.
- [ ] Autorisierungsmatrix Rolle × Funktion vollständig getestet, inklusive fremder Objekte.
- [ ] Befunde haben CVSS, Beleg, Reproduktion, Frist; Nachtest ist geplant.
- [ ] Bericht nennt Scope, Zeitpunkt und Grenzen; vertraulicher Umgang gesichert.
