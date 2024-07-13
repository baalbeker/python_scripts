import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

def clean_name(name):
    return re.sub(r'[\[_\(].*$', '', name)

def collect_unique_file_names(directory):
    file_names = set()

    for root, dirs, files in os.walk(directory):
        for file in files:
            if any(ext in file for ext in [".nsp", ".xcl", ".nsz"]):
                clean_file = clean_name(file).strip().lower()
                file_names.add(clean_file)
    return file_names

def save_unique_file_names(directory, output_file):
    unique_file_names = collect_unique_file_names(directory)
    sorted_file_names = sorted(unique_file_names)
    with open(output_file, 'w', encoding='utf-8') as f:
        for name in sorted_file_names:
            f.write(f"{name}\n")
    # for name in sorted_file_names: print(name)
    print("Done")
    print(f"There are {len(sorted_file_names)} games on the monstrous USB")


directory_path = 'G:/nintendont'
output_file_path = 'C:/Users/DOOMSLAYER/Desktop/usb_games.txt'

save_unique_file_names(directory_path, output_file_path)
