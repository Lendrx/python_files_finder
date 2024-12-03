# 📂 Python File Analyzer

**Möchtest du wissen, welche Python-Dateien in deinem Projekt am meisten Speicher verbrauchen?**  
Dieses Tool hilft dir dabei, Python-Dateien zu finden, deren Speicherverbrauch zu analysieren und eine detaillierte Visualisierung der Verzeichnisstrukturen zu erstellen. Es ist ideal für Entwickler, die ihre Projekte effizienter managen und tiefere Einblicke in ihre Dateigrößen gewinnen möchten.

### Was macht dieses Tool? 🤔

Dieses Python-Skript untersucht ein Verzeichnis und alle Unterverzeichnisse und sucht nach **Python-Dateien (.py)**. Es berechnet deren Größe und gibt dir eine detaillierte Übersicht darüber, wie viel Speicherplatz in deinem Projekt durch Python-Code beansprucht wird. Aber das ist noch nicht alles!

- **Dateien analysieren**: Alle Python-Dateien werden nach Größe und Änderungsdatum aufgelistet.
- **Speicherverbrauch anzeigen**: Ermittelt den Speicherverbrauch von Ordnern, die Python-Dateien enthalten.
- **Daten visualisieren**: Mit einem praktischen Balkendiagramm kannst du die größten Ordner auf einen Blick erkennen.

### 🔧 Funktionen

- **Scannen von Python-Dateien**: Durchsuche Verzeichnisse und deren Unterverzeichnisse nach `.py`-Dateien und finde heraus, welche den meisten Speicher verbrauchen.
- **Ordnerspeicheranalyse**: Berechne den gesamten Speicherverbrauch eines Ordners basierend auf den enthaltenen Python-Dateien.
- **Visualisierung**: Erstelle ein interaktives Balkendiagramm, das zeigt, welche Ordner den meisten Platz beanspruchen.
- **Einfache Ausgaben**: Speichere die Analyseergebnisse als `.txt`-Dateien für eine einfache Weiterverarbeitung.

### 🚀 Wie kannst du das Tool nutzen?

#### 1. Installation und Setup

Stelle sicher, dass Python 3.x auf deinem Rechner installiert ist. Wenn noch nicht geschehen, lade es von [python.org](https://www.python.org/downloads/) herunter.

Lade das Projekt runter und installiere alle notwendigen Abhängigkeiten mit:

```requirements.txt: 
matplotlib
numpy
pandas
pathlib
collections
```
