# main.py created inside day 46
# os module(built-in library that provide function for intrecting with operating system)
import os
os.mkdir(f"secret code")   # create folder secret code

for i in range(1,7):
    os.mkdir(f"secret code/code{i}")   # create 6 new folder code within secret code folder
    os.rename(f"secret code/code{i}",f"secret code/code {i}") # rename the folder

folders=os.listdir("secret code")     # show all folder in list
print(folders)

for folder in folders:
    print(folder)  # again show all folder but not in list
    print(os.listdir(f"secret code/{folder}")) # show all folder or file within secret code folder

os.remove("file or folder name")  # remove file or folder)