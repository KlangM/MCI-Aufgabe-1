## Project background
### Purpose of project

Die Software soll dazu dienen EKG Daten zu veranschaulichen damit Diaknostiker und Sportmediziner mit den Daten Arbeiten können 

### Scope of project

Werkzeug zur Vereinfachung und Automatisierung von Leistungstests, basierend auf EKG-Daten und Leistungswerten und Patient:innen-Daten

### Other background information

Der Auftraggeber verfügt bereits über ein EKG und ein Fahrradergometer

## Perspectives
### Who will use the system?

Diaknostiker und Sportmediziner

### Who can provide input about the system?

Proband:innen generieren zusammen mit dem EKG den Input


## Project Objectives
### Known business rules



### System information and/or diagrams

Beispiel von aufgezeichneten EKG Daten
![](ekg_example.png)

Aus diesem muss die Herzrate bestimmt werden.

### Assumptions and dependencies

Die .json Dateien enthalten Daten über Probanden und Test. Die .csv sind die unverarbeiteten EKG Daten. Die .txt Dateien sind die weiterverarbeiteten .csv Daten welche die Leistung des Probanden wiederspiegelt. Die .txt Datei kann direkt zum visualiesieren verwendet werden. 

Der Test dauert 180s. EKG misst jede ms einen Wert und speichert diesen .csv Datei ab.

*Welche Daten über Probanden und Test? Mit welcher Frequenz werden die Leistungsdaten gemessen? In welchen Einheiten könnten die Daten sein?- YS*

### Design and implementation constraints

Vorerst benutzung via Komandozeile. Die Implementierung findet in Phyton statt.

## Risks

Daten können falsch ausgegeben werden was zur Ergebnisverfälschung führen kann

## Known future enhancements

- Eine Applikation mit Nutzerinterface soll eine Diganostiker:in durch einen Leistungstest führen
- Vor der Durchführung soll eine Abfrage auf Kontraindikationen [p11](https://www.klinikum.uni-heidelberg.de/fileadmin/medizinische_klinik/Abteilung_7/pdf/ergo_bf.pdf) ausgeführt werden

## References

- [Link zur Aufgabenstellung](tbd)

## Open, unresolved or TBD issues

NONE
