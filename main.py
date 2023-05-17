__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

#-----------------------------------------------------
import os
import shutil

main_location = __file__
parent_dir = main_location.replace("main.py","")
data_dir = main_location.replace("main.py","data.zip")
cache_dir = main_location.replace("main.py","cache")
files_dir = main_location.replace("main.py","cache\*")


def clean_cache():
    if os.path.exists(cache_dir):
        shutil.rmtree(cache_dir)
        os.mkdir(cache_dir)
    else:
        os.mkdir(cache_dir)
    return


def cache_zip(zip_dir,destination_dir): #Wincpy does not allow me to use a preset value :( .
#def cache_zip(zip_dir=data_dir,destination_dir=cache_dir): 
    clean_cache()
    shutil.unpack_archive(zip_dir,destination_dir)
    return


def cached_files():
    cache_zip(data_dir,cache_dir)
    file_list = []
    for F in os.listdir(cache_dir):
        file_list.append(f"{cache_dir}\{F}") 
    return file_list


def find_password(files = cached_files()): # Opens the files line by line. Then removes the front and and of the line and chekcs to see if it is a digit. If not, it wil return the line (password).
    for file in files:
        f = open(file, 'r')
        line = f.readline()
        while line:
            line_no_dot = line[2:-3]
            if not line_no_dot.isdigit():
                print(line[:-1])
                password = line[10:-1]
            line = f.readline()
        f.close()
    return password



print(find_password())