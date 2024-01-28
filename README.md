import os
import sys
import git

def create_file(file_name):
    with open(file_name, 'w') as f:
        f.write('')

def delete_file(file_name):
    os.remove(file_name)

def move_file(file_name, new_file_name):
    os.rename(file_name, new_file_name)

def copy_file(file_name, new_file_name):
    shutil.copy(file_name, new_file_name)

def create_folder(folder_name):
    os.mkdir(folder_name)

def delete_folder(folder_name):
    shutil.rmtree(folder_name)

def move_folder(folder_name, new_folder_name):
    os.rename(folder_name, new_folder_name)

def copy_folder(folder_name, new_folder_name):
    shutil.copytree(folder_name, new_folder_name)

def main():
    print("Welcome to the Git File Manager!")
    print("Please enter a command:")
    command = input()
    if command == 'create_file':
        file_name = input("Enter the name of the file to create: ")
        create_file(file_name)
    elif command == 'delete_file':
        file_name = input("Enter the name of the file to delete: ")
        delete_file(file_name)
    elif command =='move_file':
        file_name = input("Enter the name of the file to move: ")
        new_file_name = input("Enter the new name of the file: ")
        move_file(file_name, new_file_name)
    elif command == 'copy_file':
        file_name = input("Enter the name of the file to copy: ")
        new_file_name = input("Enter the new name of the file: ")
        copy_file(file_name, new_file_name)
    elif command == 'create_folder':
        folder_name = input("Enter the name of the folder to create: ")
        create_folder(folder_name)
    elif command == 'delete_folder':
        folder_name = input("Enter the name of the folder to delete: ")
        delete_folder(folder_name)
    elif command =='move_folder':
        folder_name = input("Enter the name of the folder to move: ")
        new_folder_name = input("Enter the new name of the folder: ")
        move_folder(folder_name, new_folder_name)
    elif command == 'copy_folder':
        folder_name = input("Enter the name of the folder to copy: ")
        new_folder_name = input("Enter the new name of the folder: ")
        copy_folder(folder_name, new_folder_name)
    else:
        print("Invalid command. Please enter a valid command.")

if __name__ == '__main__':
    main()
<!---
NikitaVLG/NikitaVLG is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->
