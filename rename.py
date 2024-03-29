
import dropbox
from dropbox.exceptions import ApiError

# Your Dropbox access token

api_key = "4ns2gt309k2kftk"
App_secret = "viigzulo2py11mz"

TOKEN = "sl.Bw4TuGoxWvNcMrIZ_wiTEqGh0XJeZt5z32iUzaVLoc9xlSttdSjHRmPOSYKS8T3X24HBDXPkYjYwdGSEPAjtQxemjJC4EGp0jbeYnKeOXyrdRwb8TqH-ItQsq3yDPNneOthxbCQ1wxuUo3xD-bvgoVA"
# Initialize Dropbox client
dbx = dropbox.Dropbox(TOKEN)








def rename_folder(old_folder_path, new_folder_name):
    try:
        # Get the parent folder path
        parent_folder_path = old_folder_path.rsplit('/', 1)[0]
        
        # Construct the new folder path
        new_folder_path = f"{parent_folder_path}/{new_folder_name}"
        
        # Move (rename) the folder
        dbx.files_move(old_folder_path, new_folder_path)
        print(f"Folder '{old_folder_path}' renamed to '{new_folder_name}' successfully.")
    except ApiError as e:
        if e.error.is_path() and e.error.get_path().is_conflict():
            print(f"A folder with the name '{new_folder_name}' already exists.")
        else:
            print(f"Error renaming folder '{old_folder_path}' to '{new_folder_name}': {e}")

# Example usage
rename_folder("/MyFolder/folder1", "newfolder1")
















# def rename_file(folder_path, old_name, new_name):
#     try:
#         # Move (rename) the file
#         dbx.files_move(folder_path + '/' + old_name, folder_path + '/' + new_name)
#         print(f"File '{old_name}' renamed to '{new_name}' in '{folder_path}' successfully.")
#     except ApiError as e:
#         if e.error.is_path() and e.error.get_path().is_conflict():
#             print(f"File '{new_name}' already exists in '{folder_path}'.")
#         else:
#             print(f"Error renaming file '{old_name}' to '{new_name}': {e}")



