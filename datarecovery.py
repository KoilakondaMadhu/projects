import os
import shutil

# Define the directory from which you want to recover deleted files
directory_to_scan = '/path/to/your/directory'

# Define a destination directory to recover the files to
recovery_directory = '/path/to/recovery/directory'

# Ensure the recovery directory exists
os.makedirs(recovery_directory, exist_ok=True)

# Function to recover deleted files in the specified directory
def recover_deleted_files(directory):
    for root, dirs, files in os.walk(directory, topdown=False):
        for name in files:
            file_path = os.path.join(root, name)
            try:
                # Check if the file is accessible
                with open(file_path, 'rb') as file:
                    pass
            except IOError:
                # File is likely deleted or inaccessible, attempt to recover it
                recovery_path = os.path.join(recovery_directory, name)
                try:
                    shutil.copy2(file_path, recovery_path)
                    print(f"Recovered: {file_path} -> {recovery_path}")
                except Exception as e:
                    print(f"Failed to recover: {file_path} ({e})")

# Call the function to start the recovery process
recover_deleted_files(directory_to_scan)
