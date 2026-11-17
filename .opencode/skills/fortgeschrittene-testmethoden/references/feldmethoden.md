# Feldmethoden: A/B-Test, Dogfooding, Crowdtesting

Methoden, die **echte Nutzer oder echte Umgebungen** einbeziehen. Sie liefern Erkenntnisse,
die im Labor nicht entstehen, kosten aber Kontrolle und brauchen Datenschutz und Ethik.

## Inhalt
1. A/B-Test (Online-Experiment)
2. Dogfooding
3. Crowdtesting
4. Datenschutz und Ethik
5. Prüfliste

## 1. A/B-Test (Online-Experiment)

Zwei Varianten werden parallel an zufällig zugeteilte Nutzergruppen ausgeliefert; eine
vorab definierte Metrik entscheidet. Streng genommen eine Produkt- und Datenmethode, aber
Tester entwerfen die Varianten mit, sichern die Messung ab und prüfen die Ausspielung.

Vorgehen:

1. **Hypothese** schriftlich: „Variante B erhöht Metrik M um mindestens x %, weil …“
2. **Primärmetrik** und **Leitplankenmetriken** (Fehlerrate, Ladezeit, Abbrüche, Support-Tickets)
   vorab festlegen.
3. **Stichprobengröße und Laufzeit** vorab berechnen (Effektgröße, Signifikanzniveau, Power).
   Mindestens volle Wochenzyklen laufen lassen.
4. **Zuteilung** prüfen: zufällig, stabil je Nutzer, keine Überschneidung mit anderen
   Experimenten, Sample Ratio Mismatch überwachen.
5. **A/A-Test** zur Absicherung der Messinfrastruktur.
6. **Auswertung** nach Plan; kein vorzeitiger Abbruch beim ersten „signifikanten“ Blick
   (Peeking), außer Leitplanken werden verletzt.
7. **Entscheidung** dokumentieren: ausrollen, verwerfen, weiter untersuchen.

Testaufgaben dabei: beide Varianten funktional testen, Feature-Toggle-Logik testen,
Tracking-Events auf Vollständigkeit und Korrektheit prüfen, Verhalten bei Toggle-Wechsel
während einer Sitzung prüfen.

## 2. Dogfooding

Das eigene Team oder Unternehmen nutzt das Produkt im Alltag vor der Freigabe.

- Geeignet für Produkte, die intern sinnvoll nutzbar sind; nicht für Fachverfahren, die
  nur Sachbearbeiter mit echten Fällen bedienen können.
- Rahmen setzen: Zeitraum, Zielgruppe, Feedbackkanal mit minimaler Hürde, Erwartungsmanagement
  (unfertiges Produkt).
- Feedback strukturieren: Fehler, Usability, fehlende Funktion, Idee. Triage wöchentlich.
- Verzerrung kennen: Interne Nutzer sind Experten, tolerant gegenüber Macken und nicht
  repräsentativ. Dogfooding ersetzt keine Nutzerforschung.
- Variante **Fishfooding** (Google): noch frühere, kleinere Gruppe mit dem Entwicklungsteam.

## 3. Crowdtesting

Externe, verteilte Tester prüfen über eine Plattform auf eigenen Geräten und in eigenen
Umgebungen.

Einsatz:

- Gerätevielfalt (Mobil, Browser, Betriebssysteme), reale Netze, Lokalisierung,
  Barrierefreiheit mit betroffenen Nutzern, Usability-Eindrücke, Last durch viele Standorte.
- Beta-Tests vor Veröffentlichung.

Vorgehen:

1. Ziel und Umfang: exploratives Testen, Testfallausführung, Usability-Studie, Gerätematrix.
2. Testauftrag schreiben wie einen Charter: Bereich, Fokus, Ausschlüsse, Testdaten,
   Zugangsdaten, Meldeformat.
3. Plattform und Testerprofil wählen (Land, Sprache, Geräte, Erfahrung).
4. Testumgebung und Testkonten bereitstellen, die keine Produktionsdaten enthalten.
5. Befunde triagieren: Duplikate, Nichtreproduzierbares, Umgebungsprobleme aussortieren;
   den Rest ins Fehlermanagement.
6. Qualität der Plattform bewerten: Reproduktionsquote, Duplikatrate, Reaktionszeit.

Grenzen: keine tiefen Fachkenntnisse, keine Vertraulichkeit bei sensiblen Systemen,
schwankende Qualität. Für Behördenverfahren meist nur mit anonymisierter Testumgebung und
eingeschränktem Umfang einsetzbar.

## 4. Datenschutz und Ethik

- A/B-Tests: Nutzer dürfen nicht benachteiligt oder getäuscht werden; Varianten, die
  Preise, Rechte oder Fristen betreffen, brauchen rechtliche Prüfung. Tracking nur mit
  Rechtsgrundlage (DSGVO, TTDSG), Daten minimieren.
- Dogfooding: echte Daten von Kolleginnen und Kollegen sind personenbezogen; Zugriff und
  Löschung regeln.
- Crowdtesting: keine Produktionsdaten, keine personenbezogenen Daten Dritter, NDA mit der
  Plattform, Sicherheitsfreigabe prüfen (bei Ü2-Umfeld meist ausgeschlossen).

## 5. Prüfliste

- [ ] A/B: Hypothese, Primär- und Leitplankenmetriken, Stichprobe und Laufzeit sind vorab festgelegt.
- [ ] A/B: Zuteilung, Tracking und Toggle-Logik sind getestet; A/A-Test ist gelaufen.
- [ ] Dogfooding: Rahmen, Feedbackkanal und Triage sind eingerichtet; Verzerrung ist im Bericht benannt.
- [ ] Crowd: Auftrag ist als Charter formuliert, Umgebung ohne Produktionsdaten, Triageprozess steht.
- [ ] Datenschutz und rechtliche Prüfung sind dokumentiert.
