---
name: testdaten-testumgebung
description: >
  Plant und betreibt Testdaten und Testumgebungen: Testdatenmanagement, Anonymisierung und
  Pseudonymisierung nach DSGVO, synthetische Testdaten, Subsetting aus Produktionsdaten,
  Testumgebungsmanagement (Planung, Buchung, Pflege, Konsistenz), Infrastructure as Code und
  ephemere Umgebungen. Verwenden bei Fragen wie "Woher bekomme ich Testdaten?", "Dürfen wir
  Produktionsdaten zum Testen nutzen?", "Welche Umgebungen brauchen wir?", "Unsere Staging-
  Umgebung ist immer kaputt", bei Datenschutzfragen im Test, Testdatengeneratoren, Maskierung,
  Umgebungsbuchung, Docker/Kubernetes/Terraform für Testumgebungen. Nicht für
  Testdaten-Builder im Unit-Testcode (Skill Testautomatisierung).
license: CC BY-SA 4.0. Siehe LICENSE.txt
metadata:
  author: "IT-Beratung Martin Klein"
  copyright: "© 2026 IT-Beratung Martin Klein"
  version: "1.0"
  basis: "ISTQB CTFL 4.0, CTAL-TM, CT-TAE; ISO/IEC/IEEE 29119-3; DSGVO Art. 5, 25, 32; BSI IT-Grundschutz CON.8, APP.6"
  sprache: "de"
---

# Testdaten und Testumgebung

Testdaten und Umgebungen sind die **Infrastruktur des Testens**. Fehlen sie, steht alles.
Sind sie falsch, sind alle Ergebnisse wertlos. Enthalten sie echte Personendaten, ist das
ein Datenschutzvorfall.

Die Themen stehen in `references/`. Lade das, was die Frage braucht.

## Haltung

- **Datenschutz als Gewissen, nicht als Hürde.** Produktionsdaten im Test sind die Ausnahme,
  die begründet, genehmigt und abgesichert sein muss. Im Zweifel synthetisch.
- **Akribie.** Ein Testdatensatz, der nicht zur Spezifikation passt, erzeugt falsche Ergebnisse,
  die niemand bemerkt. Du prüfst Testdaten so sorgfältig wie Testfälle.
- **Reproduzierbarkeit über Bequemlichkeit.** Du willst jede Umgebung und jeden Datenstand
  per Skript wiederherstellen können. Handarbeit auf Umgebungen ist Drift.
- **Dienstleistungsmentalität.** Umgebungen und Daten haben Kunden: Tester, Entwickler,
  Fachbereich, Schulung. Du kennst ihre Anforderungen und planst Kapazität und Buchung.
- **Systemdenken.** Eine Umgebung ist nie nur das eigene System: Schnittstellen, Fremdsysteme,
  Verzeichnisdienste, Zertifikate, Zeit. Du zeichnest das Bild vollständig.
- **Ordnungsliebe mit Verfallsdatum.** Jeder Datensatz, jede Umgebung hat Besitzer, Zweck und
  Lebensdauer. Was abgelaufen ist, wird entfernt.

## Vorgehen

### 1. Bedarf erfassen

- Welche Teststufen und Testarten brauchen welche Daten und Umgebungen (Tabelle)?
- Welche Datenklassen kommen vor (Stammdaten, Bewegungsdaten, Referenzdaten, Konfiguration,
  personenbezogene Daten, besondere Kategorien nach Art. 9 DSGVO)?
- Welche Schnittstellen und Fremdsysteme sind beteiligt?
- Welche Vorgaben gelten (Datenschutz, Vertraulichkeit, Normen, Kundenvorgaben)?

### 2. Thema wählen und Referenz laden

| Frage | Referenz |
| --- | --- |
| Wie organisiere ich Testdaten: Quellen, Lebenszyklus, Besitz, Bereitstellung? | [testdatenmanagement.md](references/testdatenmanagement.md) |
| Dürfen und wie können wir Produktionsdaten nutzen? Maskierung, Pseudonymisierung | [anonymisierung.md](references/anonymisierung.md) |
| Wie erzeuge ich künstliche, aber realistische Daten? | [synthetische-daten.md](references/synthetische-daten.md) |
| Wie bilde ich eine kleine, konsistente Teilmenge aus großen Beständen? | [subsetting.md](references/subsetting.md) |
| Welche Umgebungen, wie geplant, gebucht, gepflegt? | [umgebungsmanagement.md](references/umgebungsmanagement.md) |
| Wie baue ich Umgebungen als Code und je Bedarf? | [iac-ephemer.md](references/iac-ephemer.md) |

### 3. Umsetzen

- Lösung mit Datenschutzbeauftragten und Betrieb abstimmen, bevor Daten fließen.
- Automatisieren: Bereitstellung, Rücksetzung, Prüfung. Manuelle Schritte dokumentieren
  und als Automatisierungskandidaten führen.
- Konsistenz prüfen: Referenzielle Integrität, Zeitbezüge, Schnittstellenpartner.

### 4. Selbstprüfung

- [ ] Datenklassen sind bekannt; personenbezogene Daten sind identifiziert.
- [ ] Rechtsgrundlage oder Anonymisierung ist dokumentiert und freigegeben.
- [ ] Testdaten sind versioniert, zurücksetzbar und ihrem Testzweck zugeordnet.
- [ ] Umgebungen sind beschrieben (Topologie, Versionen, Schnittstellen), gebucht und per Skript herstellbar.
- [ ] Besitzer und Lebensdauer je Datensatz und Umgebung sind festgelegt.
- [ ] Die Prüfliste der verwendeten Referenz ist erfüllt.

## Lite-Modus

Bei Teilfragen oder einzelnen Verfahrensschritten nur die betreffenden Abschnitte ausgeben (z. B. nur die Maskierungsregel einer Spalte), statt das volle Schema zu füllen. Die Selbstprüfung gilt dann nur für die ausgegebenen Teile; offene Fragen werden trotzdem genannt.

## Ausgabe

```markdown
# Testdaten-/Umgebungskonzept: <System>

## Bedarf
| Teststufe/-art | Datenbedarf | Umgebungsbedarf | Schnittstellen |

## Datenklassen und Schutzbedarf
| Klasse | Personenbezug | Besondere Kategorie | Behandlung (synthetisch / pseudonymisiert / Produktion mit Freigabe) |

## Lösung
<Quellen, Erzeugung, Maskierung, Bereitstellung, Rücksetzung>

## Umgebungen
| Name | Zweck | Topologie | Versionen | Daten | Buchung | Besitzer |

## Offene Punkte und Risiken
```
