import dropbox
from dropbox.exceptions import ApiError

# Your Dropbox access token

api_key = "4ns2gt309k2kftk"
App_secret = "viigzulo2py11mz"

TOKEN = "sl.Bw4TuGoxWvNcMrIZ_wiTEqGh0XJeZt5z32iUzaVLoc9xlSttdSjHRmPOSYKS8T3X24HBDXPkYjYwdGSEPAjtQxemjJC4EGp0jbeYnKeOXyrdRwb8TqH-ItQsq3yDPNneOthxbCQ1wxuUo3xD-bvgoVA"
# Initialize Dropbox client
dbx = dropbox.Dropbox(TOKEN)

def move_file(source_path, destination_path):
    try:
        # Move the file
        dbx.files_move_v2(source_path, destination_path)
        print(f"File '{source_path}' moved to '{destination_path}' successfully.")
    except ApiError as e:
        if e.error.is_path() and e.error.get_path().is_conflict():
            print(f"A file with the same name already exists at '{destination_path}'.")
        else:
            print(f"Error moving file '{source_path}' to '{destination_path}': {e}")

# Example usage
move_file("/Myfolder/newfolder1/Ailyze.docx", "/MyFolder/folder2/Ailyze.docx")



try:
        for i in files:
            source_path = f'/myfoder/{source}/{i}'
            destination_path= f"/myfoder/{destination}/{i}"
        
            dbx.files_move_v2(source_path,destination_path)
            print(f"File '{source}' moved to '{destination}' successfully.")
    except ApiError as e:
        if e.error.is_path() and e.error.get_path().is_conflict():
            print(f"A file with the same name already exists at '{destination}'.")
        else:
            print(f"Error moving file '{source}' to '{destination}': {e}")