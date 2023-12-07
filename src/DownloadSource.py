import os
import zipfile

import requests

SOURCE_FOLDER_NAME: str = 'automation_tool'
SOURCE_FOLDER = os.path.join(os.path.expanduser("~"), SOURCE_FOLDER_NAME)

def download_source():
    if os.path.exists(SOURCE_FOLDER):
        print('Already containing the source code')
        return

    download_url = f"https://github.com/HuyGiaMsk/automation-tool/archive/main.zip"
    print("Start download source")
    response = requests.get(download_url, verify=False)

    if response.status_code == 200:
        destination_directory = os.path.expanduser("~")
        file_name = os.path.join(destination_directory, "automated_task.zip")
        with open(file_name, 'wb') as downloaded_zip_file:
            downloaded_zip_file.write(response.content)
        print("Download source successfully")

        with zipfile.ZipFile(file_name, 'r') as zip_ref:
            zip_ref.extractall(destination_directory)

        os.rename(os.path.join(destination_directory, 'automation-tool-main'),
                  os.path.join(destination_directory, SOURCE_FOLDER_NAME))
        os.remove(file_name)
        print(f"Extracted source code and placed it in {destination_directory}")
    else:
        print("Failed to download the source")


if __name__ == '__main__':
    download_source()
