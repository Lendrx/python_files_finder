# Python File Analyzer

Ein einfaches Python-Skript zur Analyse und Visualisierung von Python-Dateien in einem Verzeichnisbaum. Das Tool durchsucht alle Unterverzeichnisse nach `.py`-Dateien, berechnet deren Größe und bietet eine detaillierte Auswertung des Speicherverbrauchs. Darüber hinaus wird eine visuelle Darstellung der Ordnergrößen erstellt, um die Ergebnisse leicht verständlich zu machen.

## Funktionen

- **Dateien finden**: Das Skript durchsucht ein angegebenes Verzeichnis und alle Unterverzeichnisse nach Python-Dateien (.py).
- **Speicherverbrauch berechnen**: Es berechnet den Speicherverbrauch der gefundenen Python-Dateien sowie der Ordner, die diese Dateien enthalten.
- **Daten ausgeben**: Das Skript gibt eine detaillierte Liste der gefundenen Python-Dateien und deren Größen aus. Zusätzlich wird eine Analyse des gesamten Speicherverbrauchs der Ordner erstellt.
- **Visualisierung**: Eine separate Datei visualisiert die Daten und stellt die Ordnergrößen in einem übersichtlichen Balkendiagramm dar.

## Installation

### Voraussetzungen

Stelle sicher, dass du Python 3.6 oder höher installiert hast. Es wird empfohlen, eine virtuelle Umgebung zu verwenden.

1. **Python 3 installieren**:
   - Lade Python von [python.org](https://www.python.org/downloads/) herunter und installiere es, falls noch nicht geschehen.

2. **Abhängigkeiten installieren**:
   - Installiere die benötigten Bibliotheken mit `pip`:

   ```bash
   pip install -r requirements.txt
