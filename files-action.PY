# import os

# # os.mkdir("python A-Z")

# # for i in range(1,101):
# #     os.mkdir(f"python A-Z/day {i}")

# main_folder_path = r"C:\Users\lenovo\Desktop\pyhton A-Z\python A-Z"

# files= ["main.py", "tutorial.md"]

# for folder in os.listdir(main_folder_path):
#     subfolder_path = os.path.join(main_folder_path, folder)
    
#     # if os.path.isdir(subfolder_path):
#     #     print(f"📁 Found folder: {folder}")
        
#     for file_name in files:
#         file_path = os.path.join(subfolder_path, file_name)
        
#         with open(file_path, "w") as file:
#             file.write(f"# {file_name} created inside {folder}\n")


# removing file within subfolders in a folder
import os

# 🔁 Replace this with your main folder path
main_folder_path = r"C:\Users\lenovo\Desktop\pyhton A-Z\python A-Z"

# File name to delete
target_file_name = "tutorial.md"

# Walk through all folders and subfolders
for root, dirs, files in os.walk(main_folder_path):
    if target_file_name in files:
        file_path = os.path.join(root, target_file_name)
        os.remove(file_path)
        print(f"🗑️ Deleted: {file_path}")
