import os
import shutil


def undoing():
    
    Files = ['png', 'jpg', 'jpeg', 'txt', 'mov', 'mp4', 'mkv', 'pdf', 'docx'] ## Lists of Entensions. 
    
    pathName = input("Enter path: ")
    directories = os.listdir(pathName)

    for dir in directories:
        listDir = os.listdir(pathName + '\\' + dir)
        for files in listDir:
            name, extension = os.path.splitext(pathName + '\\' + dir + '\\' + files)
            if extension.lower()[1:] in Files: 
                    shutil.move(name+extension, pathName) ## Undos the whole file move
                
