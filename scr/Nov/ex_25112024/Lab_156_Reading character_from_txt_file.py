# f=open("abc1.txt","r")
# data=f.read()
# print(data)
# f.close()
print("_________________________________________________________")

f=open("studentname.txt","w")
l=["Madhukar\n","Pushkar\n","Piyush\n","Himanshu\n"]
f.writelines(l)
f.close()
print("____________________________________________________________________")
f=open("studentname.txt","r")
print(f.read(6))
print(f.readlines())
f.close()