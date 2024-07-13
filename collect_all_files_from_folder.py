import os
import shutil

def move_files_to_top_folder(top_folder):
    for root, dirs, files in os.walk(top_folder): # Iterate through all directories and subdirectories
        if root == top_folder: # Skip the top-level folder to avoid moving files from it
            continue
        for file in files: # Construct full file path
            file_path = os.path.join(root, file) # Construct the destination path
            dest_path = os.path.join(top_folder, file) # Move the file to the top-level folder
            shutil.move(file_path, dest_path) # Remove the empty directory after moving its files
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            os.rmdir(dir_path)
print("done")

top_folder_path = "C:\\Users\\DOOMSLAYER\\Downloads\\SCREENSHOT" 
move_files_to_top_folder(top_folder_path)
