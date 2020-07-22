# importing required modules
from zipfile import ZipFile, ZIP_DEFLATED
import os
from datetime import date
from pathlib import Path

# Variables definition
file_paths = []


def unzip(decrypt_status, path, file):
    global file_paths

    # Unzips all the files
    with ZipFile(file, "r") as zip:

        # extracting all the files
        zip.extractall(
            path=Path(f"{path}")
        )  # Inflates the zip file on the output directory
        if decrypt_status:

            from Defs.crypto import decrypt

            file_paths = get_file_to_zip(Path(f"{path}/Hidden/"))
            decrypt(file_paths, "foo")
        else:
            pass


def get_file_to_zip(directory):

    """ Returns a list of the files in the given directory"""

    global file_paths

    # crawling through directory and subdirectories
    for root, directories, files in os.walk(directory):
        for filename in files:
            # join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)

    # returning all file paths
    return file_paths


def zipall(encryption, filename, original, location, new_name):

    """ Generates a zip file with the selected files """

    global file_paths

    pic_location = Path(f"{location}/{new_name}.jpg")
    filename = Path(f"{location}/{filename}")
    file_2_list = []

    # writing files to a zipfile
    with ZipFile(filename, "w", ZIP_DEFLATED) as zip:
        # writing each file one by one
        for file in file_paths:
            if encryption:
                from Defs.crypto import encrypt

                file_2 = encrypt(file, "foo")
                zip.write(file_2, arcname=f"Hidden/{os.path.basename(file_2)}")
                file_2_list.append(Path(file_2))
            else:
                zip.write(file, arcname=f"Hidden/{os.path.basename(file)}")
                file_2_list.append(Path(file))

    # Hides the zip file into the picture, creating a duplicate of said picture with the zip file inside
    os.system(
        f'copy /b {Path(original)} + {Path(filename)} "{pic_location}" && del {Path(filename)}'
    )

    file_paths = []  # Clears the lis

    return file_2_list
