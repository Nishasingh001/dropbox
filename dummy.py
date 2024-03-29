# # return file_path
# import os
# from django.db import models
# from django.utils.translation import gettext_lazy as _
# import dropbox

# def create_path(instance, filename):
#     # Initialize Dropbox client
#     oauth2_token = "sl.Bw4TuGoxWvNcMrIZ_wiTEqGh0XJeZt5z32iUzaVLoc9xlSttdSjHRmPOSYKS8T3X24HBDXPkYjYwdGSEPAjtQxemjJC4EGp0jbeYnKeOXyrdRwb8TqH-ItQsq3yDPNneOthxbCQ1wxuUo3xD-bvgoVA"
#     dbx = dropbox.Dropbox(oauth2_token)

#     # Create parent folder if it doesn't exist
#     parent_folder_path = f"/{instance.email}"
#     if not folder_exists(dbx, parent_folder_path):
#         dbx.files_create_folder(parent_folder_path)

#     # Create subfolder 'default'
#     subfolder_path = f"{parent_folder_path}/default"
#     if not folder_exists(dbx, subfolder_path):
#         dbx.files_create_folder(subfolder_path)

#     # Replace spaces with underscores in the filename
#     filename = filename.replace(" ", "_")

#     # Upload the file to the subfolder
#     with open(filename, "rb") as file:
#         dbx.files_upload(file.read(), f"{subfolder_path}/{filename}")

#     return f"{subfolder_path}/{filename}"

# def folder_exists(dbx, folder_path):
#     try:
#         dbx.files_get_metadata(folder_path)
#         return True
#     except dropbox.exceptions.ApiError as e:
#         if e.error.is_path() and e.error.get_path().is_not_found():
#             return False
#         else:
#             raise



