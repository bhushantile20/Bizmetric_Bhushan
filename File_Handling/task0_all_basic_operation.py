import os
import shutil

with open("file.txt", "w") as f:
    f.write("Hello World\nLine 2")

open("newfile.txt", "w").close()
os.makedirs("new_folder")

with open("file.txt", "r") as f:
    print(f.read())

with open("file.txt", "w") as f:
    f.write("Hello World")

with open("file.txt", "a") as f:
    f.write("\nNew line")

shutil.copy("file.txt", "source.txt")

shutil.move("source.txt", "new_folder/")
os.remove("file.txt")
os.rmdir("new_folder")
