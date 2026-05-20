import os
import shutil

# Sample files for testing
sample_files = ["resume.pdf", "Word.doc", "Image.jpg"]

for file in sample_files:
    open(file, "w").close()

# Folder mapping based on file extensions
FOLDERS = {
    "pdf": "PDFs",
    "doc": "DOCs",
    "jpg": "IMGs"
}

# Organize files into their respective folders
for file in sample_files:
    extension = file.split(".")[-1].lower()

    if extension in FOLDERS:
        folder_name = FOLDERS[extension]

        # Create folder if it doesn't exist
        os.makedirs(folder_name, exist_ok=True)

        # Move file to the correct folder
        shutil.move(file, os.path.join(folder_name, file))

        print(f"Moved {file} → {folder_name}")

# Display final folder contents
print("\nFolder contents:")
for folder in FOLDERS.values():
    if os.path.exists(folder):
        print(f"{folder}: {os.listdir(folder)}")
