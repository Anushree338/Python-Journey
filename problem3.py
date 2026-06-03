import os

# Specify the directory path
directory = "/"

# List and print all files and folders in the directory
for item in os.listdir(directory):
    print(item)