import os
import shutil

# Set the folder to monitor
source_folder = r"C:\Users\faeln\Downloads"

# File type mappings
file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documents': ['.pdf', '.docx', '.txt'],
    'Videos': ['.mp4', '.mov', '.avi'],
    'Music': ['.mp3', '.wav'],
    'Archives': ['.zip', '.rar', '.7z'],
    'Code': ['.py', '.js', '.html', '.css'],
}


def organize_files():
    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)

        if os.path.isfile(file_path):
            ext = os.path.splitext(filename)[1].lower()
            moved = False

            for folder, extensions in file_types.items():
                if ext in extensions:
                    dest_folder = os.path.join(source_folder, folder)
                    os.makedirs(dest_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(dest_folder, filename))
                    moved = True
                    break

            # Unmatched files go to 'Others'
            if not moved:
                others_folder = os.path.join(source_folder, 'Others')
                os.makedirs(others_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(others_folder, filename))


organize_files()
