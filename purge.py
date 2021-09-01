import os
import time
import shutil

path = input('Enter the path of the folder/file')
no_of_days = int(input('Enter the no. of days'))

seconds = time.time()-(no_of_days * 24 * 60 * 60 )
deleted_folders = 0
deleted_files = 0

def main() : 

    if os.path.exists(path) : 
        for root_folder,folders,files in os.walk(path) : 
            if  seconds > getAge(root_folder) : 
                remove_folder(root_folder)
                deleted_folders += 1
                break
            else : 
                 for folder  in folders : 
                        if  seconds > getAge(os.path.join(root_folder , folder)) : 
                            remove_folder(os.path.join(root_folder,folder))
                            deleted_folders += 1

                 for file in files : 
                     filePath = os.path.join(root_folder , file)
                     if seconds> getAge(filePath):
                        remove_file(filePath)
                        deleted_files += 1
        
         else : 
            if seconds > getAge(path) : 
               remove_file(path)
               deleted_files += 1
    else : 
         print(f'Sorry : {path} does not exist')
           
    print(f'Deleted folders : {deleted_folders}')
    print(f'Deleted files : {deleted_files}')

def getAge(path) : 
        ctime = os.stat(path).st_ctime
        return ctime

def remove_folder(path) : 
        if not shutil.rmtree(path) : 
             print(f'{path} was removed successfully')
        else : 
             print(f'Unable to remove {path}')

def remove_file(path) : 
         if not os.remove(path) : 
              print(f'{path} was removed successfully')
         else : 
              print(f'Unable to remove {path}')

main()
getAge()
remove_folder()
remove_file()