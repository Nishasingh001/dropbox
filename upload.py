import dropbox
from dropbox.exceptions import ApiError

# Your Dropbox access token

api_key = "4ns2gt309k2kftk"
App_secret = "viigzulo2py11mz"

TOKEN = "sl.Bw4TuGoxWvNcMrIZ_wiTEqGh0XJeZt5z32iUzaVLoc9xlSttdSjHRmPOSYKS8T3X24HBDXPkYjYwdGSEPAjtQxemjJC4EGp0jbeYnKeOXyrdRwb8TqH-ItQsq3yDPNneOthxbCQ1wxuUo3xD-bvgoVA"

# Initialize Dropbox client
# import folder
dbx = dropbox.Dropbox(TOKEN)

def upload_file(file_name, folder_path):
    try:
        # Read the file contents
        with open(file_name, 'rb') as f:
            file_data = f.read()
        
        # Upload the file to Dropbox
        dbx.files_upload(file_data, folder_path + '/' + file_name)
        print(f"File '{file_name}' uploaded successfully to '{folder_path}'.")
    except Exception as e:
        print(f"Error uploading file '{file_name}': {e}")


upload_file("Ailyze.docx", "/MyFolder/folder1")