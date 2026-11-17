# Mobile-Test

Mobile Anwendungen laufen auf **fragmentierter Hardware, in wechselnden Netzen, mit
Unterbrechungen und unter Plattformregeln**. Der Test deckt App-Typ, Gerätevielfalt,
Plattformkonventionen und reale Nutzungsbedingungen ab.

## Inhalt
1. App-Typen und ihre Testschwerpunkte
2. Gerätematrix
3. Mobile-spezifische Testbereiche
4. Automatisierung und Infrastruktur
5. Plattformrichtlinien und Veröffentlichung
6. Sicherheit und Datenschutz
7. Werkzeuge
8. Anti-Patterns
9. Prüfliste

## 1. App-Typen und ihre Testschwerpunkte

| Typ | Beschreibung | Schwerpunkt |
| --- | --- | --- |
| Nativ | Swift/Kotlin, volle Plattform-APIs | Plattformkonventionen, Berechtigungen, Lebenszyklus |
| Cross-Platform | Flutter, React Native, .NET MAUI | Konsistenz zwischen Plattformen, Brücken zu nativen APIs |
| Hybrid | WebView in nativer Hülle | WebView-Versionen, Brücke, Performance |
| Progressive Web App | Web mit Offline- und Installationsfähigkeiten | Browserunterschiede, Service Worker, Offline |
| Mobile Web | Responsive Website | Viewports, Touch, Browser |

## 2. Gerätematrix

- Quellen: Nutzungsstatistik der eigenen App oder Zielgruppe, Marktanteile (Betriebssystem-
  versionen, Hersteller, Bildschirmgrößen), Vorgaben des Kunden (Behörde: oft Diensthandys
  mit MDM, definierte Modelle).
- Kriterien: OS-Version (aktuelle, minus 1, minus 2, Mindestversion), Hersteller-Anpassungen
  (Samsung One UI, Xiaomi MIUI, Energiesparmodi), Bildschirmgröße und -dichte, Notch/Faltbar,
  Tablet, Leistungsklasse (Low-End), Speicher knapp.
- Matrix mit Prioritäten: Kern (jeder Lauf), erweitert (nächtlich), Rand (vor Release);
  paarweise Kombination der Dimensionen (Skill Black-Box).
- Emulatoren/Simulatoren für Breite und Automatisierung, echte Geräte für Sensoren, Performance,
  Netz, Akku, Push, Biometrie; Gerätefarmen für Vielfalt.

## 3. Mobile-spezifische Testbereiche

| Bereich | Prüfungen |
| --- | --- |
| Installation und Update | Erstinstallation, Update mit Datenmigration, Downgrade verhindert, Deinstallation entfernt Daten, Speicherplatz knapp |
| App-Lebenszyklus | Hintergrund/Vordergrund, Beenden durch System, Wiederherstellung des Zustands, Kaltstart vs. Warmstart |
| Unterbrechungen | Anruf, SMS, Push, Wecker, Akkuwarnung, Rotation, Split-Screen, Multitasking |
| Netz | WLAN ↔ Mobilfunk, Flugmodus, schwache Verbindung (2G/3G-Profil), Latenz, Abbruch mitten im Request, Offline-Modus und Synchronisation, Captive Portal |
| Berechtigungen | Anfrage zum richtigen Zeitpunkt, Ablehnung, nachträglicher Entzug in Einstellungen, „nur dieses Mal“ |
| Sensoren und Hardware | GPS (Genauigkeit, kein Signal, Mocking), Kamera, NFC, Bluetooth, Biometrie (Fehlschlag, nicht eingerichtet) |
| Eingabe | Touch-Gesten, Tastaturtypen, Autokorrektur, Einfügen, externe Tastatur, Sprachsteuerung |
| Benachrichtigungen | Push-Zustellung, Deep Links, Aktionen, Sperrbildschirm, Nicht-stören |
| Ressourcen | Akkuverbrauch, Datenverbrauch, Speicher (Leaks), CPU, Hitze; Energiesparmodus |
| Barrierefreiheit | TalkBack/VoiceOver, Schriftgröße (Dynamic Type), Kontrast, Zielgrößen, Fokusreihenfolge |
| Lokalisierung | Sprachen, RTL, Datums-/Zahlenformate, Textlängen (Deutsch ist lang), Zeitzonen |
| Plattformkonventionen | Zurück-Navigation (Android), Gesten (iOS), Tab-Bars, Dialoge, Teilen |
| Performance | Startzeit, Bildrate, Reaktionszeit, Verhalten auf Low-End-Geräten |

## 4. Automatisierung und Infrastruktur

- Ebenen: Unit (Plattform-Frameworks), UI-Komponente, E2E (Appium, Espresso, XCUITest, Maestro,
  Detox), API-Tests für das Backend getrennt.
- Stabile Selektoren: Accessibility-IDs, mit Entwicklern vereinbart.
- Testdaten und Backend: Mock-Backend für deterministische UI-Tests, echtes Backend für Integration.
- Netzbedingungen simulieren (Charles, Proxyman, Network Link Conditioner, Android-Emulator-Profile).
- Geräteverwaltung: lokale Farm oder Cloud (BrowserStack, Sauce Labs, Firebase Test Lab,
  AWS Device Farm); Build-Verteilung an Tester (TestFlight, Firebase App Distribution, interner Store).
- Pipeline: Build je Plattform, Unit-Tests, UI-Tests auf Emulatoren, nächtlich Gerätematrix,
  Screenshot-Tests je Sprache.

## 5. Plattformrichtlinien und Veröffentlichung

- Store-Richtlinien (Apple App Review Guidelines, Google Play Policies): Datenschutzangaben
  (Privacy Labels, Data Safety), Berechtigungsbegründungen, Zahlungsregeln, Inhalte.
- Release-Prozess: Staged Rollout, Rücknahme, Hotfix-Zeit durch Review berücksichtigen.
- Enterprise-Verteilung (MDM, Managed Google Play, Apple Business Manager) für Behörden und
  Unternehmen: Konfigurationsprofile, App-Config, Einschränkungen testen.

## 6. Sicherheit und Datenschutz

- OWASP Mobile Application Security (MASVS/MASTG): Datenspeicherung (Keychain/Keystore,
  keine Geheimnisse in Prefs oder Logs), Transport (TLS, Certificate Pinning), Authentifizierung,
  Code-Härtung, Reverse Engineering, Deep-Link-Missbrauch.
- Datenschutz: Tracking-SDKs, Einwilligung, Berechtigungen minimal, Löschung bei Deinstallation,
  Backups (Cloud-Backup von sensiblen Daten ausschließen).
- Werkzeuge: MobSF, Frida, Objection, Burp mit Gerät.

## 7. Werkzeuge

Appium, Espresso, XCUITest, Maestro, Detox, Flutter integration_test · Android Studio
Emulator, Xcode Simulator · BrowserStack, Sauce Labs, Firebase Test Lab, AWS Device Farm ·
Charles, Proxyman, Network Link Conditioner · Android Profiler, Xcode Instruments, Firebase
Performance · Accessibility Scanner (Android), Accessibility Inspector (iOS) · MobSF, Frida.

## 8. Anti-Patterns

- Nur auf dem neuesten Flaggschiff im WLAN testen.
- Unterbrechungen und Berechtigungsentzug ignorieren.
- Emulator als einzige Testbasis; Sensoren, Push und Performance bleiben ungetestet.
- Cross-Platform: nur eine Plattform testen, weil „es ist ja derselbe Code“.
- Store-Review erst beim Release bedenken; Ablehnung kostet Wochen.
- Backend-Fehler als App-Fehler suchen und umgekehrt; Schichten getrennt testen.

## 9. Prüfliste

- [ ] Gerätematrix aus Nutzungsdaten und Kundenvorgaben, mit Prioritäten.
- [ ] Lebenszyklus, Unterbrechungen, Netzwechsel und Offline sind getestet.
- [ ] Berechtigungen: Anfrage, Ablehnung, Entzug.
- [ ] Barrierefreiheit mit Screenreader und Schriftgröße geprüft.
- [ ] Automatisierung auf Emulatoren in der Pipeline, Gerätematrix nächtlich, echte Geräte für Sensoren und Performance.
- [ ] Ressourcenverbrauch (Akku, Daten, Speicher) gemessen, auch auf Low-End.
- [ ] MASVS-Prüfungen zu Speicherung und Transport durchgeführt.
- [ ] Store-Richtlinien und Enterprise-Verteilung berücksichtigt.
