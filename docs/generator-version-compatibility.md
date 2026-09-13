# Generatorversion und Receipt-Pruefung / Generator version and receipt validation

Die bisherige Schema-2-Allowlist endete bei 0.3.2 und wies damit neue Receipts
der eigenen 0.3.4-Vorlage zurueck. Beide Wrapper akzeptieren jetzt die bekannten
Schema-2-Generatoren einschliesslich 0.3.3/0.3.4 sowie die konkrete Version aus
der eigenen `preset.yml`. Unbekannte fremde Versionen bleiben ungueltig; die
engen Regeln fuer Schema 1.0 und 1.1 bleiben erhalten.

Die Lifecycle-Suite prueft einen vollstaendigen Receipt mit der aktuellen
Release-Version und die Ablehnung von 99.0.0. Bestehende Archiv-, Quellen-,
Transaktions- und Shell-Paritaetstests bleiben verbindlich. Die Korrektur ist
Quellcode fuer den naechsten Patch; existierende Tags und ZIPs werden nicht
nachtraeglich veraendert. Ein gezielter Verbraucher-Backport muss seine
Abweichungen und diesen kanonischen Quellcommit dokumentieren.

The prior schema-2 allowlist stopped at 0.3.2 and rejected receipts generated
from its own 0.3.4 template. Both wrappers now accept known schema-2 generators,
including 0.3.3/0.3.4, plus the exact version of their own preset metadata.
Unknown external versions remain invalid; schema-1.0/1.1 restrictions remain.
Lifecycle tests cover a complete current-version receipt and rejection of
99.0.0, alongside existing archive, source, transaction and shell-parity cases.
This correction is source for the next patch; existing tags/ZIPs are immutable.
A targeted consumer backport must record its deviations and canonical commit.

Documentation Impact: UpdateRequired. Owner: Maintainer. Leser / audience:
Preset-Maintainer und Integratoren / preset maintainers and integrators.
Kanonische Quelle / canonical source: beide Receipt-Wrapper / both receipt
wrappers. Navigation: README. Klasse / class: source-only technical evidence.
DE/EN in dieser Datei / in this file. Home-Sync: keiner / none. Re-Evaluation:
naechster Release, Schemawechsel oder neuer Generator / next release, schema
change or new generator. Validation: macOS, Bash and PowerShell parity;
native platform evidence is attached to the source PR.
