# importing required modules
from zipfile import ZipFile
import os
from datetime import date
from pathlib import Path

# Variables definition
file_paths = []


def unzip(path, file):  # Unzips all the files
    with ZipFile(file, "r") as zip:

        # extracting all the files
        zip.extractall(path=Path(path))  # Inflates the zip file on the output directory


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


def zipall(filename, original, location, new_name):

    """ Generates a zip file with the selected files """

    global file_paths

    location = f'"{location}/{new_name}.jpg"'

    # writing files to a zipfile
    while True:
        with ZipFile(filename, "w") as zip:
            # writing each file one by one
            for file in file_paths:
                zip.write(file, arcname=f"Hidden/{os.path.basename(file)}")

            break

    # Hides the zip file into the picture, creating a duplicate of said picture with the zip file inside
    os.system(f"copy /b {Path(original)} + {filename} {Path(location)}")
    file_paths = []  # Clears the list
