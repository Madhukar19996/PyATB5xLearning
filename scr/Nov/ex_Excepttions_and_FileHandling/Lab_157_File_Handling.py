# import os, sys
#
# file_name  =input('enter your file name :')
#
# if os.path.isfile(file_name):
#     print('File  is exist', file_name)
#     f = open(file_name, "r")
#
#     print("_________________________")
#
# else:
#     print('File does not exist', file_name)
#
#     sys.exit(5)
#
# c=f.read()
# print(c)
#
# f.close()
#

#WAP to count no of lines

import os, sys

file_name  =input('enter your file name :')
lcount=0

if os.path.isfile(file_name):
    print('File  is exist', file_name)
    f = open(file_name, "r")

    print("_________________________")

else:
    print('File does not exist', file_name)

    sys.exit(5)

for i in f:
    lcount= lcount+1



print(lcount)
f.close()


