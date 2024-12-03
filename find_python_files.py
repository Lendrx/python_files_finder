import os
import datetime
from pathlib import Path
from collections import defaultdict

def find_python_files(start_path):
    """
    Sucht nach Python-Dateien und berechnet die Größe pro Ordner.
    Erstellt außerdem Logs mit den Ergebnissen.
    """
    python_files = []  # Liste für gefundene Python-Dateien
    folder_sizes = defaultdict(int)  # Speicher für Ordnergrößen

    # Aktuelle Zeit für die Logs
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Beginn der Analyse
    print(f"\nPython-Dateien-Scan gestartet - {current_time}\n")
    print("=" * 50)

    try:
        for root, dirs, files in os.walk(start_path):
            # Überspringt versteckte Ordner (die mit '.' beginnen)
            dirs[:] = [d for d in dirs if not d.startswith('.')]

            # Speicherplatz für den aktuellen Ordner
            folder_size = 0

            # Suche nach Python-Dateien
            for file in files:
                if file.endswith('.py'):  # Nur .py-Dateien interessieren uns
                    full_path = os.path.join(root, file)
                    file_size = os.path.getsize(full_path)  # Dateigröße in Bytes
                    mod_time = datetime.datetime.fromtimestamp(
                        os.path.getmtime(full_path)
                    ).strftime("%Y-%m-%d %H:%M:%S")  # Letzte Änderung

                    # Füge die Datei zur Liste hinzu
                    python_files.append({
                        'path': full_path,
                        'size': file_size,
                        'modified': mod_time
                    })

                    # Addiere die Dateigröße zum Ordner
                    folder_size += file_size

            # Speichere die Gesamtgröße für Ordner mit Python-Dateien
            if folder_size > 0:
                folder_sizes[root] = folder_size

        # Ausgabe der gefundenen Dateien
        if python_files:
            print(f"Gefundene Python-Dateien: {len(python_files)}\n")
            for file in python_files:
                print(f"Datei: {file['path']}")
                print(f"Größe: {file['size']} Bytes")
                print(f"Zuletzt geändert: {file['modified']}")
                print("-" * 50)
        else:
            print("Keine Python-Dateien gefunden.")

        # Log-Datei mit Details zu den Python-Dateien
        log_path = os.path.join(os.path.dirname(__file__), 'python_files_log.txt')
        with open(log_path, 'w', encoding='utf-8') as f:
            f.write(f"Python-Dateien-Scan - {current_time}\n\n")
            if python_files:
                f.write(f"Gefundene Python-Dateien: {len(python_files)}\n\n")
                for file in python_files:
                    f.write(f"Datei: {file['path']}\n")
                    f.write(f"Größe: {file['size']} Bytes\n")
                    f.write(f"Zuletzt geändert: {file['modified']}\n")
                    f.write("-" * 50 + "\n")
            else:
                f.write("Keine Python-Dateien gefunden.\n")

        # Log-Datei mit Ordnergrößen
        folder_sizes_path = os.path.join(os.path.dirname(__file__), 'folder_sizes.txt')
        with open(folder_sizes_path, 'w', encoding='utf-8') as f:
            f.write(f"Ordnergrößen-Analyse - {current_time}\n\n")
            f.write("Ordner mit Python-Dateien und deren Gesamtgröße:\n\n")

            # Gesamte Größe aller Python-Dateien
            total_size = sum(folder_sizes.values())

            # Sortiere Ordner nach ihrer Größe
            sorted_folders = sorted(folder_sizes.items(), key=lambda x: x[1], reverse=True)

            for folder, size in sorted_folders:
                # Größe in MB umrechnen
                size_mb = size / (1024 * 1024)
                percentage = (size / total_size) * 100 if total_size > 0 else 0

                f.write(f"Ordner: {folder}\n")
                f.write(f"Größe: {size_mb:.2f} MB ({size:,} Bytes)\n")
                f.write(f"Anteil am Gesamtspeicher: {percentage:.1f}%\n")
                f.write("-" * 50 + "\n")

            # Gesamtstatistik
            total_size_mb = total_size / (1024 * 1024)
            f.write(f"\nGesamtstatistik:\n")
            f.write(f"Anzahl der Ordner mit Python-Dateien: {len(folder_sizes)}\n")
            f.write(f"Gesamtgröße: {total_size_mb:.2f} MB ({total_size:,} Bytes)\n")
            f.write(f"Durchschnittliche Ordnergröße: {(total_size_mb / len(folder_sizes) if folder_sizes else 0):.2f} MB\n")

    except Exception as e:
        # Fehlerbehandlung
        print(f"Ein Fehler ist aufgetreten: {str(e)}")

if __name__ == "__main__":
    # Startverzeichnis ist das Home-Verzeichnis des Benutzers
    home_dir = str(Path.home())
    print(f"Suche Python-Dateien im Verzeichnis: {home_dir}")
    find_python_files(home_dir)
    print("\nAnalyse abgeschlossen. Ergebnisse sind in 'python_files_log.txt' und 'folder_sizes.txt' gespeichert.")
