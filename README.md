# Python Code Finder

## 🎯 Worum geht's?
Analysewerkzeug für Python-Projekte. Durchsucht Verzeichnisse nach Python-Dateien, erstellt detaillierte Statistiken über Größe, Änderungszeitpunkte und Verteilung von Python-Code.

## 🛠️ Wie ist es gebaut?
### Tech Stack:
- Python 3.x
- os & pathlib
- datetime
- collections.defaultdict

### Architektur-Highlights:
1. Rekursive Verzeichnissuche
2. Automatische Größenanalyse
3. Detaillierte Logging-Funktionen

## 📊 Technische Features
```python
def find_python_files(start_path):
    python_files = []
    folder_sizes = defaultdict(int)
    
    for root, dirs, files in os.walk(start_path):
        for file in files:
            if file.endswith('.py'):
                full_path = os.path.join(root, file)
                file_size = os.path.getsize(full_path)
                mod_time = os.path.getmtime(full_path)
                python_files.append({
                    'path': full_path,
                    'size': file_size,
                    'modified': mod_time
                })
```

Key Features:
- Detaillierte Dateianalyse
- Größenstatistiken pro Ordner
- Automatische Report-Generierung
