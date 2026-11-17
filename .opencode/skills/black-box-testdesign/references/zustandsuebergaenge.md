# Zustandsübergangstest

Für Systeme, deren Reaktion auf ein Ereignis von der **Vorgeschichte** abhängt: Workflows,
Antragsstatus, Sitzungen, Protokolle, Geräte, Benutzerkonten.

## Inhalt
1. Modell aufstellen
2. Zustandstabelle
3. Überdeckungsziele
4. Testfälle ableiten
5. Anti-Patterns
6. Prüfliste
7. Beispiel

## 1. Modell aufstellen

Erfasse aus der Spezifikation:

- **Zustände:** unterscheidbare Situationen, in denen das System auf Ereignisse unterschiedlich reagiert.
  Startzustand und Endzustände kennzeichnen.
- **Ereignisse:** Auslöser eines Übergangs (Benutzeraktion, Nachricht, Zeitablauf).
- **Wächterbedingungen:** Bedingungen, die zusätzlich erfüllt sein müssen (`[Betrag > 0]`).
- **Aktionen:** was beim Übergang passiert (Mail senden, Zähler erhöhen).
- **Übergänge:** Zustand + Ereignis (+ Wächter) → Aktion + Folgezustand.

Stelle das Modell als Zustandsdiagramm (z. B. Mermaid `stateDiagram-v2`) **und** als Tabelle dar.
Ist das Modell nicht in der Spezifikation enthalten, sondern von dir rekonstruiert, kennzeichne
es so und lass es bestätigen.

## 2. Zustandstabelle

- Zeilen = Zustände, Spalten = Ereignisse, Zelle = Folgezustand und Aktion.
- Fülle **jede** Zelle, auch die nicht spezifizierten Kombinationen.
- Eine leere Zelle bedeutet entweder „ungültiger Übergang“ (Ereignis wird ignoriert oder
  abgewiesen) oder eine Lücke in der Spezifikation. Kläre, was gilt, und halte es als offene
  Frage fest, wenn es nicht belegt ist.

## 3. Überdeckungsziele

Wähle nach Risiko, in aufsteigender Strenge:

| Ziel | Bedeutung | Einsatz |
| --- | --- | --- |
| Alle Zustände | Jeder Zustand wird mindestens einmal erreicht | Minimum, schwach |
| Alle gültigen Übergänge (0-Switch) | Jeder spezifizierte Übergang wird mindestens einmal durchlaufen | Standard (CTFL) |
| Alle Übergänge | Zusätzlich jeder ungültige Übergang wird einzeln versucht | Bei sicherheits- oder geschäftskritischen Abläufen |
| n-Switch | Alle Folgen von n+1 aufeinanderfolgenden Übergängen | Bei hohem Risiko, z. B. Protokolle |

**Überdeckung** = abgedeckte Elemente des gewählten Ziels / alle Elemente × 100 %.

## 4. Testfälle ableiten

- Ein Testfall ist eine Folge von Ereignissen ab einem definierten Startzustand.
- Für gültige Übergänge: möglichst lange, zusammenhängende Pfade, um mit wenigen Testfällen
  alle Übergänge zu durchlaufen. Jeder Testfall prüft nach jedem Schritt den Folgezustand.
- Für **ungültige Übergänge:** je Testfall genau **ein** ungültiges Ereignis. Den Zustand davor
  über gültige Übergänge herstellen, danach prüfen, dass der Zustand unverändert ist und die
  spezifizierte Fehlerreaktion erfolgt.
- Wächterbedingungen mit [aequivalenzklassen-grenzwerte.md](aequivalenzklassen-grenzwerte.md)
  testen: Wächter knapp erfüllt, knapp nicht erfüllt.
- Zeitgesteuerte Übergänge (Timeouts) gezielt an der Zeitgrenze testen.

## 5. Anti-Patterns

- Nur den „Happy Path“ durch den Automaten testen.
- Nicht spezifizierte Zellen der Zustandstabelle stillschweigend als „ignoriert“ annehmen.
- Nach einem Übergang nur die Aktion prüfen, nicht den Folgezustand.
- Mehrere ungültige Ereignisse in einem Testfall.
- Zustände verwechseln mit Bildschirmen oder Seiten. Ein Bildschirm kann mehrere Zustände haben.

## 6. Prüfliste

- [ ] Start- und Endzustände sind gekennzeichnet.
- [ ] Die Zustandstabelle enthält jede Kombination aus Zustand und Ereignis.
- [ ] Jede nicht spezifizierte Zelle ist als ungültig belegt oder als offene Frage erfasst.
- [ ] Das Überdeckungsziel ist gewählt und begründet.
- [ ] Jeder Testfall prüft nach jedem Schritt den Zustand.
- [ ] Ungültige Übergänge sind einzeln getestet.
- [ ] Wächter und Timeouts sind an ihren Grenzen getestet.

## 7. Beispiel

Anforderung: „Ein Konto ist zunächst aktiv. Nach drei aufeinanderfolgenden Fehlanmeldungen
wird es gesperrt. Eine erfolgreiche Anmeldung setzt den Zähler zurück. Ein Administrator kann
ein gesperrtes Konto entsperren.“

| Zustand \ Ereignis | Anmeldung ok | Anmeldung falsch | Entsperren |
| --- | --- | --- | --- |
| Aktiv (0 Fehler) | Aktiv (0) | Aktiv (1) | ? |
| Aktiv (1 Fehler) | Aktiv (0) | Aktiv (2) | ? |
| Aktiv (2 Fehler) | Aktiv (0) | Gesperrt | ? |
| Gesperrt | ? | ? | Aktiv (0) |

Offene Fragen:
- Was passiert bei „Entsperren“ auf einem aktiven Konto?
- Wie reagiert das System auf eine Anmeldung mit korrektem Passwort bei gesperrtem Konto?
  Welche Meldung erhält der Benutzer? Verrät sie, dass das Passwort korrekt war?
- Erhöht eine falsche Anmeldung bei gesperrtem Konto einen Zähler?
