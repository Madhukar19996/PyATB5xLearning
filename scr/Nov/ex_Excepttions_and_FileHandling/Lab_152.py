import os

full_path=os.path.join("/scr/Nov/ex_Excepttions_and_FileHandling\Mp", "madhukar.txt")
file = open(full_path,"r")
content = file.read()
print(content)