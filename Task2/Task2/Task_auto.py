import os
import shutil

source_folder = r'C:\Users\ok\OneDrive\Desktop\Apexify Intership\Source Folder'
destination_folder = r'C:\Users\ok\OneDrive\Desktop\Apexify Intership\Destination Folder'

try:
    # Checks if folder is available or not.
    if not os.path.exists(destination_folder):
        print(f'Creating Destination Folder: {destination_folder}')
        os.makedirs(destination_folder)

    # Iterate through file and folders.
    for filename in os.listdir(source_folder):
        source_path = os.path.join(source_folder, filename)
        # Checks if current item is a file.
        if os.path.isfile(source_path):
            destination_path = os.path.join(destination_folder, filename)
            # Here the actual file transfer happens.
            shutil.move(source_path, destination_path)
            
            print(f'Moved: {filename} -> {destination_path}')
# Handling exceptions: 
except FileNotFoundError:
    print(f'Error: The source folder: {source_folder} was not found.')
except Exception as e:
    print(f'An exception error occurred: {e}')
print('Task Completed!')
