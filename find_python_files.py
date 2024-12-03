#!/usr/bin/env python3
import os
import datetime
from pathlib import Path
from collections import defaultdict

def find_python_files(start_path):
    """
    Findet alle Python-Dateien und berechnet den Speicherverbrauch pro Ordner
    """
    python_files = []
    folder_sizes = defaultdict(int)  # Speicher für Ordnergrößen
    
    # Aktuelle Zeit für den Report
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    print(f"\nPython-Dateien Scan - {current_time}\n")
    print("=" * 50)
    
    try:
        for root, dirs, files in os.walk(start_path):
            # Überspringe versteckte Verzeichnisse
            dirs[:] = [d for d in dirs if not d.startswith('.')]
            
            folder_size = 0  # Größe für aktuellen Ordner
            for file in files:
                if file.endswith('.py'):
                    full_path = os.path.join(root, file)
                    file_size = os.path.getsize(full_path)
                    mod_time = datetime.datetime.fromtimestamp(
                        os.path.getmtime(full_path)
                    ).strftime("%Y-%m-%d %H:%M:%S")
                    
                    python_files.append({
                        'path': full_path,
                        'size': file_size,
                        'modified': mod_time
                    })
                    
                    # Addiere Dateigröße zum aktuellen Ordner
                    folder_size += file_size
            
            # Wenn Python-Dateien im Ordner gefunden wurden
            if folder_size > 0:
                folder_sizes[root] = folder_size
    
        # Ausgabe der Datei-Ergebnisse
        if python_files:
            print(f"Gefundene Python-Dateien: {len(python_files)}\n")
            for file in python_files:
                print(f"Datei: {file['path']}")
                print(f"Größe: {file['size']} Bytes")
                print(f"Zuletzt geändert: {file['modified']}")
                print("-" * 50)
        else:
            print("Keine Python-Dateien gefunden.")
            
        # Speichere die Datei-Ergebnisse in eine Log-Datei
        log_path = os.path.join(os.path.dirname(__file__), 'python_files_log.txt')
        with open(log_path, 'w', encoding='utf-8') as f:
            f.write(f"Python-Dateien Scan - {current_time}\n\n")
            if python_files:
                f.write(f"Gefundene Python-Dateien: {len(python_files)}\n\n")
                for file in python_files:
                    f.write(f"Datei: {file['path']}\n")
                    f.write(f"Größe: {file['size']} Bytes\n")
                    f.write(f"Zuletzt geändert: {file['modified']}\n")
                    f.write("-" * 50 + "\n")
            else:
                f.write("Keine Python-Dateien gefunden.\n")
        
        # Speichere die Ordnergrößen in eine separate Datei
        folder_sizes_path = os.path.join(os.path.dirname(__file__), 'folder_sizes.txt')
        with open(folder_sizes_path, 'w', encoding='utf-8') as f:
            f.write(f"Ordner-Speicherverbrauch Analyse - {current_time}\n\n")
            f.write("Ordner mit Python-Dateien und deren Gesamtgröße:\n\n")
            
            # Gesamtgröße aller Python-Dateien
            total_size = sum(folder_sizes.values())
            
            # Sortiere Ordner nach Größe (absteigend)
            sorted_folders = sorted(folder_sizes.items(), key=lambda x: x[1], reverse=True)
            
            for folder, size in sorted_folders:
                # Konvertiere Bytes in lesbares Format
                size_mb = size / (1024 * 1024)  # Konvertiere zu MB
                percentage = (size / total_size) * 100 if total_size > 0 else 0
                
                f.write(f"Ordner: {folder}\n")
                f.write(f"Größe: {size_mb:.2f} MB ({size:,} Bytes)\n")
                f.write(f"Anteil am Gesamtspeicher: {percentage:.1f}%\n")
                f.write("-" * 50 + "\n")
            
            # Schreibe Gesamtstatistik
            total_size_mb = total_size / (1024 * 1024)
            f.write(f"\nGesamtstatistik:\n")
            f.write(f"Anzahl Python-Ordner: {len(folder_sizes)}\n")
            f.write(f"Gesamtgröße aller Python-Dateien: {total_size_mb:.2f} MB ({total_size:,} Bytes)\n")
            f.write(f"Durchschnittliche Ordnergröße: {(total_size_mb/len(folder_sizes) if folder_sizes else 0):.2f} MB\n")
                
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {str(e)}")

if __name__ == "__main__":
    # Startverzeichnis ist das Home-Verzeichnis des Benutzers
    home_dir = str(Path.home())
    print(f"Suche Python-Dateien in: {home_dir}")
    find_python_files(home_dir)
    print("\nAnalyse abgeschlossen. Bitte prüfen Sie die Dateien 'python_files_log.txt' und 'folder_sizes.txt' für detaillierte Informationen.")
