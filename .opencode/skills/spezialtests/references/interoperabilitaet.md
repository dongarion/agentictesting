# Interoperabilitäts- und Konformitätstest

**Konformität:** Erfüllt ein System einen Standard, eine Spezifikation oder eine Vorgabe?
**Interoperabilität:** Arbeiten zwei oder mehr Systeme tatsächlich zusammen?
Konformität ist notwendig, aber nicht hinreichend: Zwei konforme Systeme können an
Interpretationsspielräumen, optionalen Teilen und Versionsunterschieden scheitern.

## Inhalt
1. Begriffe
2. Konformitätstest
3. Interoperabilitätstest
4. Typische Standards und Prüfkontexte
5. Versionen, Profile, Erweiterungen
6. Zertifizierung und Nachweis
7. Werkzeuge
8. Anti-Patterns
9. Prüfliste

## 1. Begriffe

- **Standard:** normative Spezifikation (ISO, IETF RFC, W3C, OASIS, HL7, XÖV).
- **Profil:** Einschränkung oder Konkretisierung eines Standards für einen Anwendungsbereich
  (z. B. XRechnung als Profil von EN 16931 / UBL und CII; IHE-Profile über HL7/DICOM).
- **Referenzimplementierung:** vom Standardgeber bereitgestellte Implementierung oder Validator.
- **Konformitätsklausel:** welche Teile sind Pflicht (MUSS/SHALL), optional (KANN/MAY),
  bedingt (SOLL/SHOULD).
- **Interoperabilitätsstufen** (z. B. nach EIF): technisch, syntaktisch, semantisch, organisatorisch,
  rechtlich.

## 2. Konformitätstest

Vorgehen:

1. **Anforderungen extrahieren:** Standard durchgehen, jede normative Aussage (SHALL, SHOULD,
   MAY) als Anforderung mit Referenz (Abschnitt, Nummer) listen; Konformitätsklauseln und
   gewähltes Profil festhalten.
2. **Testbarkeit prüfen:** Je Anforderung Prüfmethode: Inspektion (Dokumentation, Konfiguration),
   Test (Verhalten), Analyse (Code, Schema).
3. **Testfälle ableiten:** Positiv (konforme Eingaben werden akzeptiert, konforme Ausgaben
   erzeugt), Negativ (nicht konforme Eingaben werden abgewiesen, Fehler korrekt gemeldet),
   Grenzfälle (optionale Elemente, Maximalwerte, Zeichensätze). Black-Box-Skill, besonders
   Syntaxtest und Äquivalenzklassen.
4. **Offizielle Testsuiten und Validatoren** nutzen, wo vorhanden; Ergebnisse dokumentieren.
5. **Konformitätsmatrix:** Anforderung × Status (erfüllt, teilweise, nicht erfüllt, nicht
   anwendbar) mit Nachweis.

## 3. Interoperabilitätstest

Vorgehen:

1. **Partner und Szenarien:** Welche Systeme, welche Versionen, welche Nachrichten oder
   Interaktionen, in welcher Reihenfolge (End-to-End-Geschäftsfälle)?
2. **Testumgebung:** echte Partnerumgebungen (Abstimmung, Buchung), Referenzimplementierungen
   oder Simulatoren; gemeinsame Testdaten und Kennungen.
3. **Testfälle:** je Szenario Erfolg, jeder Fehlerfall (Ablehnung, Timeout, Teilantwort),
   Wiederholung, Reihenfolgeabweichung, Versionsmischung.
4. **Prüfung auf allen Stufen:** technisch (Verbindung, TLS, Zertifikate), syntaktisch
   (Schema gültig), semantisch (Inhalte richtig interpretiert, Codelisten, Einheiten, Zeitzonen),
   organisatorisch (Prozess, Zuständigkeiten, Fristen).
5. **Plugfests / Connectathons:** mehrere Hersteller testen gegeneinander in einem organisierten
   Rahmen; Ergebnisse protokollieren.
6. **Dauerbetrieb:** Monitoring der Schnittstelle in Produktion, Fehlerquoten je Partner.

## 4. Typische Standards und Prüfkontexte

| Bereich | Standards, Profile, Prüfmittel |
| --- | --- |
| Öffentliche Verwaltung (DE) | XÖV-Standards (XJustiz, XMeld, XInneres, XSozial), OSCI/XTA, FIT-Connect, BundID/Nutzerkonten, SAFE; XÖV-Produktionsumgebung, Validatoren der KoSIT |
| E-Rechnung | EN 16931, XRechnung, ZUGFeRD/Factur-X, Peppol BIS; KoSIT-Validator, Peppol-Testbed |
| Gesundheit | HL7 v2, FHIR, DICOM, IHE-Profile, gematik TI-Spezifikationen; Connectathons, gematik Referenzumgebung |
| Web | HTML, CSS, WCAG/EN 301 549, OAuth 2.0/OIDC; W3C-Validatoren, OpenID Conformance Suite |
| Identität | eIDAS, SAML, OIDC, FIDO2 |
| Zahlungsverkehr | ISO 20022, SEPA, PSD2/Berlin Group |
| Industrie | OPC UA, MQTT, AutomationML; OPC UA Compliance Test Tool |
| Automotive | AUTOSAR, UDS (ISO 14229), DoIP, ISO 15118 |
| Dokumente | PDF/A, PDF/UA (veraPDF, PAC), OOXML, ODF |
| APIs allgemein | OpenAPI, AsyncAPI, JSON Schema; Spectral, Schemathesis |

## 5. Versionen, Profile, Erweiterungen

- Versionsmatrix: Welche Partner sprechen welche Version; Übergangszeiträume; Abwärtskompatibilität.
- Profile und Erweiterungen (nationale Anpassungen, kundenspezifische Felder) dokumentieren;
  sie sind die häufigste Quelle von Interoperabilitätsfehlern.
- Umgang mit Unbekanntem: ignorieren oder ablehnen? Muss spezifiziert und getestet sein.
- Codelisten und Stammdaten: Versionen und Gültigkeitszeiträume synchron halten.

## 6. Zertifizierung und Nachweis

- Formale Zertifizierung durch Standardgeber oder akkreditierte Stelle (z. B. Peppol Access
  Point, gematik-Zulassung, OPC Foundation, FIDO Alliance); Prozess, Testsuite, Gültigkeit,
  Rezertifizierung bei Änderungen.
- Selbsterklärung mit Konformitätsmatrix und Testprotokollen, wo keine formale Zertifizierung existiert.
- Archivierung der Nachweise (Testsuite-Version, Ergebnisse, Umgebung, Datum).

## 7. Werkzeuge

Validatoren der Standardgeber (KoSIT, veraPDF, W3C), Schema-Validatoren (XSD, Schematron,
JSON Schema), Protokollanalysatoren (Wireshark), API-Vertragsprüfer (Spectral, Schemathesis),
Konformitäts-Testsuiten (OpenID, OPC UA CTT, FHIR Touchstone/Inferno), Simulatoren und
Referenzimplementierungen, Service-Virtualisierung für nicht verfügbare Partner.

## 8. Anti-Patterns

- „Schema-valide“ mit „konform“ gleichsetzen; Schematron-Regeln und Semantik vergessen.
- Nur gegen die eigene Interpretation des Standards testen, nie gegen Partner oder Referenz.
- Optionale Elemente ignorieren; Partner sendet sie, System stürzt ab.
- Codelisten hartkodiert, Version veraltet.
- Interoperabilitätstest erst in der Produktion mit dem ersten echten Partner.
- Zertifikat als Dauerzustand betrachten; Änderungen ohne Rezertifizierung.

## 9. Prüfliste

- [ ] Normative Anforderungen sind mit Referenz extrahiert; Profil und Konformitätsklauseln festgelegt.
- [ ] Je Anforderung existieren Positiv-, Negativ- und Grenzfalltests mit Prüfmethode.
- [ ] Offizielle Validatoren und Testsuiten sind eingesetzt; Ergebnisse dokumentiert.
- [ ] Interoperabilität mit realen Partnern oder Referenzimplementierungen auf allen Stufen getestet.
- [ ] Versionsmatrix, Profile und Umgang mit unbekannten Elementen sind spezifiziert und getestet.
- [ ] Konformitätsmatrix mit Nachweisen liegt vor; Zertifizierungsanforderungen sind geklärt.
- [ ] Monitoring der Schnittstellen im Betrieb ist eingerichtet.
