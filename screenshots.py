import os
import shutil
from datetime import datetime
from config import project_name  # Import project name from config file


def organize_screenshots():
    desktop_folder = os.path.join(os.path.expanduser('~'), 'Desktop')
    screenshot_folder = os.path.join(os.path.expanduser('~'), 'Documents', 'Screenshots')

    if not os.path.exists(screenshot_folder):
        os.makedirs(screenshot_folder)
        print(f'Created screenshot folder: {screenshot_folder}')

    screenshot_extensions = ('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')

    for filename in os.listdir(desktop_folder):
        if filename.lower().endswith(screenshot_extensions):
            src_path = os.path.join(desktop_folder, filename)

            # Extract date from screenshot filename
            try:
                date_str = filename.split('Screenshot ')[1].split(' at ')[0]
                date_created = datetime.strptime(date_str, "%Y-%m-%d").strftime("%d-%m-%Y")
            except IndexError:
                print(f"Skipping file {filename} as it doesn't match the expected format.")
                continue
            except ValueError:
                print(f"Skipping file {filename} due to invalid date format.")
                continue

            dest_folder = os.path.join(screenshot_folder, date_created + " : " + project_name)

            if not os.path.exists(dest_folder):
                os.makedirs(dest_folder)
                print(f'Created folder: {dest_folder}')

            dest_path = os.path.join(dest_folder, filename)
            shutil.move(src_path, dest_path)
            print(f'Moved: {src_path} to {dest_path}')

    print('Organizing screenshots completed.')


if __name__ == "__main__":
    organize_screenshots()
