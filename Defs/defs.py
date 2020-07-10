# importing required modules
from zipfile import ZipFile
import os
from os import system as sys
from datetime import date
from pathlib import Path

# Variables definition
fecha_actual = date.today()
dia = fecha_actual.strftime("%d")
mes = fecha_actual.strftime("%m")
año = fecha_actual.strftime("%y")

hoy = f"{dia}_{mes}_{año}"

global file_paths
file_paths = []


def unzip(path):  # Not usable for now
    with ZipFile("zip.zip", "r") as zip:

        # extracting all the files
        zip.extractall(path=path)


def get_file_to_zip(directory):

    # initializing empty file paths list

    # crawling through directory and subdirectories
    for root, directories, files in os.walk(directory):
        for filename in files:
            # join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)

    # returning all file paths
    return file_paths


def get_file_names(directory):

    files = [file for file in file_paths]

    return files


def zipall(original, location, new_name):
    filename = f"{hoy}.zip"
    location = f"{location}/{new_name}"
    # writing files to a zipfile
    while True:
        with ZipFile(filename, "w") as zip:
            # writing each file one by one
            print(file_paths)
            for file in file_paths:
                zip.write(file)

            break

    print(
        f"copy /b {Path(original)} + {filename} {Path(location)}.jpg && del {filename}"
    )
    sys(f"copy /b {Path(original)} + {filename} {Path(location)}.jpg && del {filename}")
