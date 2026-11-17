# Subsetting von Produktionsdaten

Eine **kleine, referenziell konsistente Teilmenge** eines großen Datenbestands bilden.
Fast immer in Kombination mit Maskierung (siehe [anonymisierung.md](anonymisierung.md)).
Zweck: handhabbare Umgebungen, schnelle Rücksetzung, geringere Angriffsfläche.

## Inhalt
1. Wann Subsetting
2. Auswahlstrategien
3. Referenzielle Konsistenz
4. Vorgehen
5. Besondere Fälle
6. Werkzeuge
7. Anti-Patterns
8. Prüfliste

## 1. Wann Subsetting

- Produktionsbestand zu groß für Testumgebungen (Speicher, Ladezeit, Lizenz).
- Viele Umgebungen oder ephemere Umgebungen je Merge Request.
- Datenminimierung nach DSGVO: nur so viel, wie der Test braucht.
- Nicht ausreichend: Last- und Performancetests, Migrationstests mit Vollbestand. Dort
  Vollbestand maskiert oder synthetisch hochskaliert.

## 2. Auswahlstrategien

| Strategie | Beschreibung | Eignung |
| --- | --- | --- |
| Zufallsstichprobe | n % der Wurzelentitäten (Kunden, Fälle) | Allgemeine Funktionstests |
| Geschichtet | Stichprobe je Kategorie (Tarif, Region, Status), damit seltene Klassen vertreten sind | Abdeckung von Varianten |
| Zielgerichtet | Datensätze mit bestimmten Eigenschaften (alle Fälle mit Widerspruch, alle Mandanten) | Abnahme, Fehleranalyse |
| Zeitfenster | Alle Vorgänge eines Zeitraums | Monatsabschluss, Batchläufe |
| Kombiniert | Geschichtet plus zielgerichtete Ergänzung | Standard |

Wurzelentität festlegen (meist Person, Kunde, Akte), von dort alle abhängigen Datensätze
mitnehmen, dann referenzierte Stammdaten vollständig.

## 3. Referenzielle Konsistenz

- Fremdschlüssel in beide Richtungen verfolgen: Kinder der ausgewählten Wurzeln (Verträge,
  Buchungen) und Eltern aller ausgewählten Datensätze (Stammdaten, Kataloge).
- Stamm- und Referenzdaten vollständig übernehmen; sie sind klein und werden überall gebraucht.
- Zyklen und Selbstreferenzen (Hierarchien, Vorgänger-Nachfolger) auflösen.
- Implizite Referenzen ohne Fremdschlüssel-Constraint (Freitext-IDs, JSON-Spalten,
  anwendungsseitige Beziehungen, Referenzen über Systemgrenzen) aus dem Datenmodell und
  dem Code ermitteln; sie brechen am häufigsten.
- Datensätze in Fremdsystemen (DMS, Archiv, Schnittstellenpartner) zum selben Subset mitnehmen
  oder virtualisieren.

## 4. Vorgehen

1. Datenmodell erfassen: Tabellen, Beziehungen, explizit und implizit, Volumen je Tabelle.
2. Wurzelentität und Auswahlstrategie festlegen; Zielgröße (z. B. 2 % oder 50.000 Kunden).
3. Auswahlregeln schreiben (SQL, Werkzeugkonfiguration), inklusive Pflichtfälle.
4. Extraktion in gesicherte Zwischenumgebung.
5. Maskierung auf dem Subset (billiger als auf dem Vollbestand).
6. Konsistenzprüfung: verwaiste Fremdschlüssel zählen (muss 0 sein), Zeilenzahlen je Tabelle
   gegen Erwartung, Stichproben fachlich prüfen, Anwendung starten und Kernfunktionen durchspielen.
7. Als Snapshot oder Skript bereitstellen; Lauf versionieren und wiederholbar machen.

## 5. Besondere Fälle

- **Zeitbezug:** Ein Subset von heute ist morgen veraltet (Fristen, Status). Datumsverschiebung
  bei der Maskierung oder regelmäßige Neuerzeugung.
- **Mandanten:** Ganze Mandanten übernehmen statt Kunden quer über Mandanten; weniger
  Konsistenzprobleme.
- **Sequenzen und IDs:** Nummernkreise in der Zielumgebung so setzen, dass neue Datensätze
  nicht mit übernommenen kollidieren.
- **Große Binärdaten:** Dokumente, Bilder durch Platzhalter ersetzen, wenn Inhalt nicht relevant.
- **Historisierung und Audit-Tabellen:** Mitnehmen oder konsistent leeren; halbe Historien
  verwirren.

## 6. Werkzeuge

| Werkzeug | Hinweis |
| --- | --- |
| Jailer | Open Source, Subsetting mit Fremdschlüsselverfolgung, Java |
| Condenser | Open Source, PostgreSQL, Python |
| pg_sample | PostgreSQL |
| Datenbank-Bordmittel | Export mit Filter, Views, CTAS; bei einfachen Modellen ausreichend |
| Kommerziell | Delphix, Informatica TDM, IBM Optim, Broadcom TDM, Tonic, Redgate Data Masker + Subsetter |

## 7. Anti-Patterns

- Nur die Haupttabelle filtern, Rest voll übernehmen; Konsistenz und Datenminimierung verfehlt.
- Implizite Beziehungen übersehen; Anwendung stürzt bei Datensätzen ohne Partner ab.
- Subset ohne Maskierung, weil „nur 2 %“.
- Einmalig per Hand erzeugt, nie wiederholbar.
- Seltene, testrelevante Konstellationen fehlen, weil Zufallsstichprobe.

## 8. Prüfliste

- [ ] Datenmodell mit expliziten und impliziten Beziehungen liegt vor.
- [ ] Wurzelentität, Strategie und Zielgröße sind festgelegt; Pflichtkonstellationen enthalten.
- [ ] Stamm- und Referenzdaten sind vollständig.
- [ ] Verwaiste Referenzen: 0; Zeilenzahlen geprüft; Anwendung läuft auf dem Subset.
- [ ] Maskierung ist auf das Subset angewendet und freigegeben.
- [ ] Lauf ist skriptbasiert, versioniert und wiederholbar; Sequenzen sind angepasst.
