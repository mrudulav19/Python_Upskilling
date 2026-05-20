# Create sample log file
with open("log.txt", "w") as log_file:
    log_file.write("""
INFO: Server started
WARNING: Disk space low
ERROR: Connection timeout
INFO: User logged in
ERROR: Authentication failed
""")

info_count = 0
warning_count = 0
error_count = 0

# Parse log file
with open("log.txt", "r") as log_file:
    for line in log_file:
        if "INFO" in line:
            info_count += 1
        elif "WARNING" in line:
            warning_count += 1
        elif "ERROR" in line:
            error_count += 1

# Display results
print(f"INFO COUNT: {info_count}")
print(f"WARNING COUNT: {warning_count}")
print(f"ERROR COUNT: {error_count}")
