import os
import shutil
import sys
from datetime import datetime

def backup_files(source_dir, destination_dir):
    try:
        # Check if source directory exists
        if not os.path.exists(source_dir):
            raise FileNotFoundError(f"Source directory '{source_dir}' does not exist.")

        # Create destination directory if it doesn't exist
        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)

        # Get list of files in the source directory
        files = os.listdir(source_dir)

        for file in files:
            source_path = os.path.join(source_dir, file)
            destination_path = os.path.join(destination_dir, file)

            # Check if a file with the same name exists in the destination
            if os.path.exists(destination_path):
                # Append timestamp to the file name for uniqueness
                timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
                base_name, extension = os.path.splitext(file)
                new_file_name = f"{base_name}_{timestamp}{extension}"
                destination_path = os.path.join(destination_dir, new_file_name)

            # Copy the file to the destination
            shutil.copy2(source_path, destination_path)
            print(f"File '{file}' backed up to '{destination_path}'")

        print("Backup completed successfully.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python backup.py C:/Users/njalkote/Documents/AB C:/Users/njalkote/Documents/XYZ")
    else:
        source_directory = sys.argv[1]
        destination_directory = sys.argv[2]
        backup_files(source_directory, destination_directory)
