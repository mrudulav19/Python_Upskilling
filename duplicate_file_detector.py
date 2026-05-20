# Sample files for testing
sample_files = ["cat.jpg", "dog.jpg", "cat.jpg"]

seen_files = set()

# Detect duplicate files
for file in sample_files:
    if file in seen_files:
        print(f"Duplicate file detected: {file}")
    else:
        seen_files.add(file)
        print(f"Added: {file}")
