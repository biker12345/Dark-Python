''' script to permanently delete folders and files from a computer
    caution:- handle this script with carefully ,one execution of script can
    clear all data of a path

'''

#import required modules 
import os
import shutil

#method to remove folders/files using shutil module
def removDirectory(path):
    if os.path.exists(path):
        try:

            if os.path.isdir(path):
                shutil.rmtree(path)

            else :
                os.remove(path)

        except :
                print("exception")
    else:
        print("path not found")


if __name__ == '__main__':
    path = input("enter the path")
    removDirectory(str(path))
