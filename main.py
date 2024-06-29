import os
import shutil
from send2trash import send2trash
from datetime import datetime, timedelta

path = "C:/Users/KD/Downloads/"

list_files = os.listdir(path)

main_dirs = ["Images", "Videos", "Audios", "Executables", "Archives", "Documents", "Web Files", "Miscellaneous"]

extensions = {
    "Images": ['.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.svg', '.ico', '.psd', '.ai', '.eps', '.raw'],
    "Videos": ['.mp4', '.avi', '.mov', '.mkv', '.wmv', '.flv', '.webm', '.m4v', '.mpg', '.mpeg', '.3gp', '.ogv'],
    "Audios": ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma', '.m4a', '.opus', '.mid', '.amr', '.ac3', '.aiff'],
    "Executables": ['.exe', '.bat', '.sh', '.msi', '.app', '.jar', '.deb', '.apk', '.com', '.cmd', '.vb', '.ps1'],
    "Archives": ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2', '.xz', '.iso', '.cab', '.arj', '.rpm', '.dmg'],
    "Documents": ['.docx', '.pdf', '.pptx', '.txt', '.xls', '.csv', '.odt', '.rtf', '.epub', '.doc', '.odp', '.ods',
                  '.xlsx', '.ods', '.tsv', '.xlsm', '.numbers', '.xlr', '.gnumeric', '.xltx', '.xlw', '.ppt',
                  '.key', '.odp', '.pps', '.sldx', '.ppsx', '.potx', '.dps', '.otp', '.sxi', '.dotx',
                  '.dotm', '.docm', '.dot'],
    "Web Files": ['.html', '.css', '.js', '.php', '.asp', '.xml', '.json', '.jsp', '.scss', '.less', '.jsx', '.ts'],
}


def create_dir():
    for x in range(0, len(main_dirs)):
        if not os.path.exists(path + main_dirs[x]):
            os.makedirs(path + main_dirs[x])


def check_date_validity():
    for file in list_files:
        time_modified = os.path.getmtime(path + file)
        original_date = datetime.fromtimestamp(time_modified)
        x = datetime.now() - original_date
        if int(x.days) > 60:
            send2trash(path + file)


def sort_files():
    for file in list_files:
        fx = file.split(".")

        if "." + fx[-1] in extensions["Images"]:
            shutil.move(path + file, path + f"{main_dirs[0]}/" + file)
        elif "." + fx[-1] in extensions["Videos"]:
            shutil.move(path + file, path + f"{main_dirs[1]}/" + file)
        elif "." + fx[-1] in extensions["Audios"]:
            shutil.move(path + file, path + f"{main_dirs[2]}/" + file)
        elif "." + fx[-1] in extensions["Executables"]:
            shutil.move(path + file, path + f"{main_dirs[3]}/" + file)
        elif "." + fx[-1] in extensions["Archives"]:
            shutil.move(path + file, path + f"{main_dirs[4]}/" + file)
        elif "." + fx[-1] in extensions["Documents"]:
            shutil.move(path + file, path + f"{main_dirs[5]}/" + file)
        elif "." + fx[-1] in extensions["Web Files"]:
            shutil.move(path + file, path + f"{main_dirs[6]}/" + file)
        else:
            if file not in main_dirs:
                shutil.move(path + file, path + f"{main_dirs[7]}/" + file)


def check_date_validity_2():
    list_folders = os.listdir(path)

    for folder in list_folders:
        ls = os.listdir(path + folder)

        for file in ls:
            time_modified = os.path.getmtime(path + f"{folder}/" + file)
            original_date = datetime.fromtimestamp(time_modified)
            x = datetime.now() - original_date
            if int(x.days) > 60:
                send2trash(path + f"{folder}/" + file)


if __name__ == '__main__':
    create_dir()
    check_date_validity()
    sort_files()
    check_date_validity_2()
