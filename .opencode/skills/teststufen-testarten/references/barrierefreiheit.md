# Barrierefreiheitstest

Prüft, ob Menschen mit Behinderungen das System **wahrnehmen, bedienen, verstehen und robust
nutzen** können. Für öffentliche Stellen in Deutschland Pflicht (BITV 2.0, BGG); seit Juni 2025
für viele private Produkte und Dienstleistungen ebenfalls (Barrierefreiheitsstärkungsgesetz, BFSG).

Hinweis: Rechtliche Einordnung im Einzelfall mit Fachstelle klären; dieses Dokument gibt den
Stand der Normen als Orientierung.

## Inhalt
1. Rechtlicher und normativer Rahmen
2. Prinzipien und Konformitätsstufen
3. Prüfmethoden
4. Prüfung mit Hilfsmitteln
5. Typische Prüfpunkte
6. Barrierefreiheit im Entwicklungsprozess
7. Dokumente und Erklärung
8. Werkzeuge
9. Anti-Patterns
10. Prüfliste

## 1. Rechtlicher und normativer Rahmen

| Regelwerk | Geltung | Inhalt |
| --- | --- | --- |
| BGG, BITV 2.0 | Öffentliche Stellen des Bundes (Länder mit eigenen Gesetzen) | Verweis auf EN 301 549; Erklärung zur Barrierefreiheit, Feedbackmechanismus, Inhalte in Leichter Sprache und Gebärdensprache |
| EN 301 549 | Harmonisierte europäische Norm | Anforderungen an IKT; Kapitel 9 (Web) und 11 (Software) übernehmen WCAG 2.1 AA; weitere Kapitel für Dokumente, Hardware, Support |
| WCAG 2.1 / 2.2 (W3C) | International | Erfolgskriterien in A, AA, AAA; WCAG 2.2 ergänzt u. a. Fokus nicht verdeckt, Zielgröße, Ziehbewegungen, barrierefreie Authentifizierung |
| BFSG | Bestimmte Produkte und Dienstleistungen privater Anbieter (E-Commerce, Banken, E-Books, Verkehr) | Ab 28.06.2025; Anforderungen über Verordnung, technisch EN 301 549 |
| BIK BITV-Test | Prüfverfahren | Verbreitetes Prüfverfahren in Deutschland mit 98 Prüfschritten auf Basis WCAG/EN 301 549 |

Prüfziel im öffentlichen Sektor: Konformität mit EN 301 549 bzw. WCAG 2.1 Stufe AA,
zusätzlich BITV-spezifische Anforderungen. WCAG 2.2 AA als zukunftssicheres Ziel empfehlen.

## 2. Prinzipien und Konformitätsstufen

POUR-Prinzipien:

- **Wahrnehmbar:** Textalternativen, Untertitel, Kontraste, Anpassbarkeit, keine reine Farbinformation.
- **Bedienbar:** Tastatur vollständig, genug Zeit, keine Anfälle auslösen, Navigation, Eingabemodalitäten.
- **Verständlich:** Lesbar, vorhersehbar, Eingabehilfen und Fehlervermeidung.
- **Robust:** Kompatibel mit Hilfsmitteln (korrekte Semantik, Namen, Rollen, Werte).

Stufen: A (Minimum), AA (gesetzliches Ziel), AAA (erweitert, nicht vollständig erreichbar für alle Inhalte).

## 3. Prüfmethoden

| Methode | Findet | Grenzen |
| --- | --- | --- |
| Automatisierte Scans (axe, Lighthouse, WAVE, Pa11y) | Fehlende Alternativtexte, Kontraste, fehlende Labels, ARIA-Fehler | Nur ein Teil der Kriterien automatisch prüfbar (oft genannt: rund 30–40 %); keine Aussage zur Sinnhaftigkeit |
| Manuelle Expertenprüfung nach Prüfschritten (BITV-Test) | Alle Kriterien systematisch | Aufwand, Expertise nötig |
| Prüfung mit Hilfsmitteln (Screenreader, Vergrößerung, Sprachsteuerung, Tastatur) | Tatsächliche Nutzbarkeit | Erfahrung mit Hilfsmitteln nötig |
| Nutzertests mit Menschen mit Behinderungen | Reale Barrieren, Prioritäten | Rekrutierung, Planung |

Strategie: automatisierte Scans in der Pipeline (Shift-Left), manuelle Prüfung je Release,
Nutzertests für Kernprozesse, Konformitätsprüfung vor Abnahme.

## 4. Prüfung mit Hilfsmitteln

| Hilfsmittel | Plattform | Prüfen |
| --- | --- | --- |
| NVDA (kostenlos), JAWS | Windows + Firefox/Chrome/Edge | Lesereihenfolge, Überschriften, Landmarks, Formulare, Fehlermeldungen, dynamische Inhalte (Live Regions), Tabellen |
| VoiceOver | macOS, iOS | Wie oben, plus Mobile-Gesten |
| TalkBack | Android | Mobile |
| Tastatur allein | alle | Erreichbarkeit, Fokusreihenfolge, sichtbarer Fokus, keine Tastaturfalle, Tastenkürzel |
| Bildschirmvergrößerung, 200 %/400 % Zoom, Reflow 320 px | alle | Kein Informationsverlust, kein horizontales Scrollen |
| Hoher Kontrast, Farbsimulation | alle | Lesbarkeit, Farbe nicht alleinige Information |
| Sprachsteuerung (Dragon, Voice Control) | alle | Sichtbare Beschriftung entspricht zugänglichem Namen |

## 5. Typische Prüfpunkte

- Alle Funktionen per Tastatur erreichbar und bedienbar; Fokus sichtbar und logisch.
- Überschriftenstruktur, Landmarks, Seitentitel, Sprache der Seite.
- Bilder mit sinnvollen Alternativtexten; dekorative Bilder ausgeblendet.
- Formulare: sichtbare Labels, programmatisch verknüpft, Pflichtfelder gekennzeichnet,
  Fehlermeldungen verständlich und mit Feld verknüpft, Eingabezweck (autocomplete).
- Kontraste: Text 4,5:1 (groß 3:1), Bedienelemente und Grafiken 3:1.
- Keine Information nur über Farbe, Form oder Position.
- Videos mit Untertiteln, Audiodeskription wo nötig; Audio mit Transkript.
- Zeitbegrenzungen verlängerbar; keine automatische Bewegung ohne Pause.
- Dynamische Inhalte: Statusmeldungen per Live Region; Modale Dialoge mit Fokusführung.
- Eigene Komponenten (Dropdowns, Tabs, Datepicker) nach WAI-ARIA Authoring Practices.
- PDF und Dokumente: getaggt, Lesereihenfolge, Alternativtexte, PDF/UA.
- Authentifizierung ohne kognitiven Test (WCAG 2.2: 3.3.8).

## 6. Barrierefreiheit im Entwicklungsprozess

- Anforderungen: Konformitätsziel im Lastenheft (z. B. EN 301 549 / WCAG 2.2 AA).
- Design: Kontraste, Fokusdarstellung, Zielgrößen, Struktur im Design System festlegen und prüfen.
- Entwicklung: semantisches HTML zuerst, ARIA nur wo nötig; Komponentenbibliothek barrierefrei.
- Automatisierte Prüfung: axe-core in Unit-/Komponententests (jest-axe), E2E (Playwright + axe),
  Pipeline-Gate gegen neue Verstöße.
- Definition of Done: Tastaturtest und Scan je Story.
- Abnahme: Expertenprüfung, ggf. externer BITV-Test.

## 7. Dokumente und Erklärung

- **Erklärung zur Barrierefreiheit** (Pflicht für öffentliche Stellen): Stand der Vereinbarkeit,
  nicht barrierefreie Inhalte mit Begründung, Datum der Bewertung, Feedbackmechanismus,
  Schlichtungsstelle.
- **Prüfbericht**: Prüfgegenstand (Seiten, Prozesse, Stichprobe), Methode, Ergebnis je Kriterium,
  Befunde mit Priorität und Lösungsvorschlag.
- Stichprobe nach WCAG-EM: repräsentative Seiten, alle Seitentypen, Kernprozesse vollständig.

## 8. Werkzeuge

axe DevTools, axe-core (jest-axe, @axe-core/playwright), Lighthouse, WAVE, Pa11y, IBM Equal Access
Checker, ARC Toolkit, Accessibility Insights (Microsoft), Colour Contrast Analyser (TPGi),
NVDA, JAWS, VoiceOver, TalkBack, PAC (PDF), veraPDF, Android Accessibility Scanner,
Xcode Accessibility Inspector.

## 9. Anti-Patterns

- Nur automatisierte Scans; „100 Punkte in Lighthouse“ als Konformitätsnachweis.
- ARIA überall statt semantischem HTML.
- Barrierefreiheit als Abnahmepunkt am Ende; Umbau teuer.
- Overlay-Werkzeuge als Lösung (beheben keine Ursachen, werden von Betroffenen kritisiert).
- Screenreader-Test durch jemanden ohne Erfahrung mit dem Hilfsmittel als einzige Prüfung.
- Dokumente (PDF-Bescheide, Formulare) vergessen.

## 10. Prüfliste

- [ ] Konformitätsziel (EN 301 549 / WCAG 2.x AA, BITV) ist festgelegt und vertraglich verankert.
- [ ] Automatisierte Prüfung läuft in Komponenten- und E2E-Tests mit Gate.
- [ ] Manuelle Prüfung nach Prüfverfahren für eine repräsentative Stichprobe und alle Kernprozesse.
- [ ] Prüfung mit Tastatur, Screenreader, Zoom/Reflow durchgeführt.
- [ ] Dokumente und PDFs sind geprüft.
- [ ] Nutzertests mit Betroffenen für Kernprozesse sind geplant.
- [ ] Prüfbericht und Erklärung zur Barrierefreiheit sind erstellt.
