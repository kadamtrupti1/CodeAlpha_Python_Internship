
# CodeAlpha Python Programming Internship
# Task 3: Task Automation with Python Scripts
# Project: JPG File Organizer

import os
import shutil

# STEP 1: Define the source and destination folders.
# Source folder contains all the original files.
# Destination folder will store only JPG images.

source_folder = "MyPhotos"
destination_folder = "JPG_Images"

# STEP 2: Check whether the source folder exists.
# If it does not exist, display an error message.

if not os.path.exists(source_folder):

    print("Source folder does not exist!")
    print("Please create a folder named MyPhotos.")

else:

    # STEP 3: Create the destination folder.
    # exist_ok=True prevents an error if the folder already exists.

    os.makedirs(destination_folder, exist_ok=True)

    # This variable counts how many images are moved.

    moved_count = 0

    # STEP 4: Get all filenames from the source folder.
    # os.listdir() returns the names of files and folders.

    files = os.listdir(source_folder)

    print("Starting JPG File Organizer...")
    print("--------------------------------")

    # STEP 5: Check each file one by one.

    for filename in files:

        # Create the complete path of the current file.

        source_path = os.path.join(source_folder, filename)

        # Check whether the item is a file and has .jpg extension.
        # lower() also handles uppercase extensions like .JPG.

        if os.path.isfile(source_path) and filename.lower().endswith(".jpg"):

            # Create the destination path for this image.

            destination_path = os.path.join(
                destination_folder, filename
            )

            # STEP 6: Move the JPG image to the destination folder.
            # shutil.move() moves a file from one location to another.

            if os.path.exists(destination_path):
                print(f"Skipped {filename}: file already exists.")
                continue

            shutil.move(source_path, destination_path)

            # Increase the count after successfully moving a file.

            moved_count += 1

            print(f"Moved: {filename}")

    # STEP 7: Display the final result.

    print("--------------------------------")
    print("Task completed successfully!")
    print(f"Total JPG images moved: {moved_count}")

    print(f"Images are saved in: {destination_folder}")
