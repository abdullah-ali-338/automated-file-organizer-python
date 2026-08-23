import os
import shutil
import logging
from datetime import datetime

# Configure activity logging
logging.basicConfig(
    filename='organizer_audit.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# File Category Mappings
FILE_CATEGORIES = {
    'Documents': ['.pdf', '.docx', '.doc', '.txt', '.pptx', '.xlsx', '.csv'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.svg', '.webp'],
    'Videos': ['.mp4', '.mkv', '.avi', '.mov'],
    'Audio': ['.mp3', '.wav', '.flac'],
    'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
    'Code': ['.cpp', '.py', '.java', '.html', '.css', '.js', '.json', '.sql'],
    'Executables': ['.exe', '.msi', '.apk', '.bat']
}

def organize_directory(target_path):
    """
    Scans, classifies, and moves files into organized category directories.
    Logs execution metrics and skipped exceptions.
    """
    if not os.path.exists(target_path):
        print(f"[Error] Directory not found: {target_path}")
        return

    processed_count = 0
    skipped_count = 0

    print(f"\n[*] Scanning and organizing directory: {target_path}")

    for item in os.listdir(target_path):
        item_path = os.path.join(target_path, item)

        # Skip directories and the log file itself
        if os.path.isdir(item_path) or item in ['organizer_audit.log', 'file_organizer.py']:
            continue

        _, extension = os.path.splitext(item)
        extension = extension.lower()

        category_folder = 'Others'
        for category, extensions in FILE_CATEGORIES.items():
            if extension in extensions:
                category_folder = category
                break

        destination_dir = os.path.join(target_path, category_folder)
        os.makedirs(destination_dir, exist_ok=True)

        destination_path = os.path.join(destination_dir, item)

        try:
            shutil.move(item_path, destination_path)
            logging.info(f"Moved: {item} -> {category_folder}/")
            processed_count += 1
        except Exception as e:
            logging.error(f"Failed to move {item}: {str(e)}")
            skipped_count += 1

    print(f"[+] Organizing Complete.")
    print(f"    - Files Processed: {processed_count}")
    print(f"    - Files Skipped/Errors: {skipped_count}")
    print(f"    - Audit Log saved to: organizer_audit.log\n")

if __name__ == "__main__":
    folder_input = input("Enter full path of folder to organize (or press Enter for current folder): ").strip()
    target_directory = folder_input if folder_input else os.getcwd()
    organize_directory(target_directory)