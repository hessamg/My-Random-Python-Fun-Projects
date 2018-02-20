import os

def rename_files():
    file_list = os.listdir(r"/Users/macbook/Desktop/prank")
    print(file_list)
    saved_path = os.getcwd()
    os.chdir(r"/Users/macbook/Desktop/prank")
    for file_name in file_list:
        os.rename(file_name,file_name.translate(None,"1234567890"))
        print(file_name)
    os.chdir = saved_path

rename_files()
