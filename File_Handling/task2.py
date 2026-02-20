import os
import shutil

source = "backup"
small = "small_files"
medium = "medium_files"
large = "large_files"

os.makedirs(small, exist_ok=True)
os.makedirs(medium, exist_ok=True)
os.makedirs(large, exist_ok=True)

for file in os.listdir(source):
    path = source + "/" + file
    if os.path.isfile(path):
        size = os.path.getsize(path) / 1024

        if size < 500:
            shutil.move(path, small + "/" + file)
            print(file, "small")
        elif size < 2000:
            shutil.move(path, medium + "/" + file)
            print(file, "medium")
        else:
            shutil.move(path, large + "/" + file)
            print(file, " large")

print("all sorted ")
