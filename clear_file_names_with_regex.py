import os
import re

def clean_filename(filename):
    cleaned = re.sub(r'\s*[\(\[].*?[\)\]]', '', filename).strip()
    return cleaned

def rename_files_in_directory(directory):

    for filename in os.listdir(directory):
        full_path = os.path.join(directory, filename)
        
        if os.path.isfile(full_path):
            base_name, ext = os.path.splitext(filename)
            cleaned_base_name = clean_filename(base_name)
            new_filename = cleaned_base_name + ext
            new_full_path = os.path.join(directory, new_filename)
            
            if os.path.exists(new_full_path): # If a file with the new name already exists, prepend "AAA" to the name,so file goes the top so I can see it
                cleaned_base_name = "AAA" + cleaned_base_name
                new_filename = cleaned_base_name + ext
                new_full_path = os.path.join(directory, new_filename)
            
            os.rename(full_path, new_full_path)
            print(f'Renamed: {filename} -> {new_filename}')

directory = 'C:\\Users\\DOOMSLAYER\\Desktop\\gb\\Megapack'
rename_files_in_directory(directory)
