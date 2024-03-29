import dropbox
from dropbox.exceptions import ApiError

# Your Dropbox access token

api_key = "4ns2gt309k2kftk"
App_secret = "viigzulo2py11mz"

TOKEN = "sl.Bw4TuGoxWvNcMrIZ_wiTEqGh0XJeZt5z32iUzaVLoc9xlSttdSjHRmPOSYKS8T3X24HBDXPkYjYwdGSEPAjtQxemjJC4EGp0jbeYnKeOXyrdRwb8TqH-ItQsq3yDPNneOthxbCQ1wxuUo3xD-bvgoVA"
# Initialize Dropbox client
dbx = dropbox.Dropbox(TOKEN)

def create_folder(folder_name):
    try:
        # Create a folder
        dbx.files_create_folder(folder_name)
        print(f"Folder 'Users_folders/{folder_name}' created successfully.")
    except ApiError as e:
        if e.error.is_path() and e.error.get_path().is_conflict():
            print(f"Folder '{folder_name}' already exists.")
        else:
            print(f"Error creating folder '{folder_name}': {e}")

# Call the function to create a folder
            
sub_folder = ["folder1","folder2","folder3"]
create_folder("/MyFolder/")




def create_folder(folder_path):
    try:
        # Create a folder
        dbx.files_create_folder(folder_path)
        print(f"Folder '{folder_path}' created successfully.")
    except ApiError as e:
        if e.error.is_path() and e.error.get_path().is_conflict():
            print(f"Folder '{folder_path}' already exists.")
        else:
            print(f"Error creating folder '{folder_path}': {e}")

def create_folders_recursive(parent_folder, sub_folders):
    try:
        # Create the parent folder
        create_folder(parent_folder)

        # Create subfolders
        for folder in sub_folders:
            create_folder(parent_folder + '/' + folder)
    except Exception as e:
        print(f"Error creating folders: {e}")

# Call the function to create folders recursively
create_folders_recursive("/MyFolder", ["folder1", "folder2", "folder3"])