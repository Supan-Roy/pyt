import os
# Show files in the directory
# Specify the directory path

directory_path = '/Programs and Codes'

contents = os.listdir(directory_path)
for item in contents:
 print(item)
