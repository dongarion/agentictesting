# Infrastructure as Code und ephemere Umgebungen

Umgebungen werden **aus Code erzeugt, versioniert, auf Anforderung aufgebaut und nach
Gebrauch entsorgt.** Das beseitigt Drift, Buchungskonflikte und Schneeflocken.

## Inhalt
1. Prinzipien
2. Bausteine
3. Ephemere Umgebungen je Merge Request
4. Daten in ephemeren Umgebungen
5. Testen der Infrastruktur selbst
6. Grenzen
7. Werkzeuge
8. Anti-Patterns
9. Prüfliste

## 1. Prinzipien

- **Deklarativ:** Sollzustand beschreiben, Werkzeug stellt ihn her (Terraform, Kubernetes-Manifeste).
- **Versioniert:** Umgebungsdefinition im Repository, Änderungen per Merge Request mit Review.
- **Idempotent:** Mehrfaches Anwenden ändert nichts mehr.
- **Unveränderlich (Immutable):** Keine Änderung an laufenden Instanzen; stattdessen neu bauen.
- **Parametrisiert:** Eine Definition, viele Umgebungen (Größe, Name, Datenprofil als Parameter).
- **Gleich wie Produktion:** Dieselben Definitionen mit anderen Parametern; Abweichungen explizit.

## 2. Bausteine

| Ebene | Mittel |
| --- | --- |
| Infrastruktur (Netz, VMs, Cluster, Datenbanken als Dienst) | Terraform, OpenTofu, Pulumi, Cloud-Templates (CloudFormation, Bicep) |
| Konfiguration von Hosts | Ansible, Chef, Puppet; bei Containern meist überflüssig |
| Anwendungslaufzeit | Container-Images (Dockerfile), Helm-Charts, Kustomize, Docker Compose |
| Daten | Migrationsskripte (Flyway, Liquibase), Seed-Skripte, vorgeladene Images, Snapshots |
| Geheimnisse | Vault, Sealed Secrets, External Secrets, Plattform-Variablen |
| Orchestrierung | CI/CD-Pipeline (GitLab CI, GitHub Actions, Argo CD, Flux) |

## 3. Ephemere Umgebungen je Merge Request

Ablauf:

1. Merge Request wird eröffnet → Pipeline baut Images.
2. Pipeline erzeugt Namespace oder Compose-Stack mit eindeutigem Namen (`mr-1234`).
3. Datenbank wird angelegt, migriert und mit Datenprofil befüllt (synthetisch, Subset).
4. Health-Check; URL wird im Merge Request verlinkt (GitLab Review Apps, GitHub Environments).
5. Automatisierte Tests laufen gegen diese URL; manuelles und exploratives Testen möglich.
6. Merge oder Schließen → Umgebung wird gelöscht; zusätzlich TTL als Sicherheitsnetz.

Voraussetzungen: Containerisierte Anwendung, externalisierte Konfiguration, automatisierte
Datenbereitstellung, Kapazität im Cluster, Wildcard-DNS und Zertifikate.

Vorteile: keine Buchung, keine Drift, paralleles Testen, jederzeit reproduzierbar.
Kosten: Rechenressourcen, anfänglicher Aufbau, Disziplin beim Aufräumen.

## 4. Daten in ephemeren Umgebungen

- Datenprofile als Parameter: `minimal` (Smoke), `standard` (Regression), `gross` (Performance).
- Bereitstellung in Sekunden bis wenigen Minuten: vorgeladene Datenbank-Images,
  Snapshot-Restore, Testcontainers mit Init-Skripten.
- Nur synthetische oder maskierte Daten; ephemere Umgebungen sind viele und schwer zu
  überwachen, also nie Produktionsdaten.
- Schnittstellenpartner virtualisiert (WireMock, Mockoon) als Teil des Stacks.

## 5. Testen der Infrastruktur selbst

Infrastrukturcode ist Code und wird getestet:

- Statische Prüfung: `terraform validate`, `tflint`, `checkov`/`tfsec` (Sicherheit),
  `kube-linter`, `helm lint`, Policy as Code (OPA/Conftest, Kyverno).
- Plan-Review: `terraform plan` im Merge Request lesbar; unerwartete Zerstörungen erkennen.
- Integrationstests: Terratest, Kitchen-Terraform; Stack aufbauen, prüfen, abbauen.
- Smoke nach Deployment: Health-Endpunkte, Erreichbarkeit, Versionsabfrage.
- Drift-Erkennung: regelmäßiger Plan gegen die laufende Umgebung; Abweichungen alarmieren.
- Wiederherstellungstest: Umgebung aus dem Nichts aufbauen; Dauer messen.

## 6. Grenzen

- Fremdsysteme ohne Testinstanz oder ohne Virtualisierung.
- Lizenzgebundene Software, die nicht beliebig instanziiert werden darf.
- Große Datenbestände für Performance; dort dedizierte, aber ebenfalls per Code gebaute Umgebungen.
- Hardwareabhängigkeit (Embedded, HiL); dort Simulation plus wenige physische Prüfstände.
- Behördenumfeld: Netzsegmentierung, Freigabeprozesse für Infrastrukturänderungen; IaC hilft
  gerade hier beim Nachweis, braucht aber Abstimmung mit IT-Sicherheit.

## 7. Werkzeuge

Terraform/OpenTofu, Pulumi, Ansible, Docker, Docker Compose, Kubernetes, Helm, Kustomize,
Argo CD, Flux, GitLab Review Apps, GitHub Environments, Testcontainers, LocalStack (AWS lokal),
Kind/k3d/minikube (lokale Cluster), Vagrant (VMs lokal), Terratest, Checkov, OPA/Conftest.

## 8. Anti-Patterns

- IaC für Aufbau, danach Handänderungen; Drift wie zuvor.
- Geheimnisse im IaC-Repository.
- Ephemere Umgebungen ohne TTL; Cluster voll mit Leichen.
- Eine Definition für Test, eine andere für Produktion; Tests prüfen das Falsche.
- Infrastrukturänderungen ohne Plan-Review und ohne Pipeline.
- Produktionsdaten in Review Apps.

## 9. Prüfliste

- [ ] Umgebungsdefinition ist versioniert, parametrisiert und per Pipeline anwendbar.
- [ ] Umgebung lässt sich aus dem Nichts aufbauen; Dauer ist bekannt.
- [ ] Ephemere Umgebungen haben eindeutige Namen, TTL und automatisches Aufräumen.
- [ ] Datenprofile sind definiert und in Minuten bereitgestellt; keine Produktionsdaten.
- [ ] Infrastrukturcode wird statisch geprüft, Plan wird reviewt, Drift wird erkannt.
- [ ] Geheimnisse liegen im Secret Store.
- [ ] Abweichungen zur Produktionsdefinition sind explizit und begründet.
