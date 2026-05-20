import os

# Sample files for testing
sample_files = ["hi.jpg", "welcome.jpg", "hi2.jpg"]

for file in sample_files:
    open(file, "w").close()

# Rename files sequentially
counter = 1

for file in sample_files:
    extension = file.split(".")[-1].lower()
    new_name = f"photo_{counter}.{extension}"

    os.rename(file, new_name)
    print(f"Renamed {file} → {new_name}")

    counter += 1
