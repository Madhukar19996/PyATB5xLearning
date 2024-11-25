import os

full_path=os.path.join("C:\Users\Madhukar Pandey\PycharmProjects\pyATB5xLearning\scr\Nov\ex_25112024\Mp", "madhukar.txt")
file = open(full_path,"r")
content = file.read()
print(content)