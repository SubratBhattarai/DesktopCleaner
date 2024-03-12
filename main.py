import Undo
import os
import shutil

print("Welcome! To Desktop Cleaner.")
print('1. Clean Path.')
print('2. Undo.')
print('3. Exit.')


Files = ['png', 'jpg', 'jpeg', 'txt', 'mov', 'mp4', 'mkv', 'pdf', 'docx'] ## FIle Extensions. Add more if you want


def menu():
    userInput = int(input("Enter your choice: ")) ## Main Menu Stuff
    if userInput == 1:
        pathName = input('Enter the path: ')
        directories = os.listdir(pathName) ## Lists directories
        
        def splitting():
            name, extension = dirs.split('.') ## Splits on . (dot)
            print(name, extension)
            return name, extension

        def pathLocation(name, extension):
            sourceLocation = pathName+ '\\'+name+'.'+ extension ## Source Location
            folderName = pathName+ '\\' + extension ## Foldername
            checkingStatus = folderName + '\\'+name+'.'+ extension ## Checking if prev location has the same file
            return sourceLocation, folderName, checkingStatus 

        def movingFolders(extension, folderName, checkingStatus, sourceLocation):
            if extension.lower() in Files:
                if os.path.exists(folderName):
                    if(os.path.exists(checkingStatus)):
                        os.remove(checkingStatus) ## Removes the prev file if there is any.
                    shutil.move(sourceLocation, folderName) ## Moves the new Files
                else:
                    os.mkdir(folderName) ## Makes directory is not present
                    if(os.path.exists(checkingStatus)):
                        os.remove(checkingStatus)
                    shutil.move(sourceLocation, folderName)
        for dirs in directories:
            if(dirs.find('.') != -1): ## If folder then dont move it. Can't find the .(dot) in folder. Gives error if not used.
                name, extension = splitting()  
                sourceLocation, folderName, checkingStatus = pathLocation(name, extension)
                movingFolders(extension, folderName, checkingStatus, sourceLocation)
            else:
                print("Folder")
            
            for i in range(10):
                print('-', end="") ## Drawing Image
            print()
            print("DONE.")
    elif userInput == 2:
        Undo.undoing()
    elif userInput == 3:
        exit()
    else:
        print("Enter a real Number:")
        

menu()


