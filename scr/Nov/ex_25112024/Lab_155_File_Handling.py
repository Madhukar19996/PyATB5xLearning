f =open("abc.txt", "w" )

print("file name ",f.name)
print("file mode",f.mode)
print("file readable",f.readable())
print("file write",f.writable())
print("file closed",f.closed)

f.close()
print("file closed",f.closed)


