# List
# List - Collection of Items( Duplicate is allowed)
my_list = [1, 2, 3]  # Same type of data (int)
my_list2 = [1, True, "madhukar", 12.34]

print(my_list)
print(len(my_list))

print(my_list[0])
print(my_list2[1])
# print(my_list[10])  # list index out of range - exception
#
my_list[0] = "madhukar"
my_list[1] = "kumar"
my_list[2] = "pandey"
print(my_list[0])
print(my_list[1])
print(my_list[2])
# my_list[10] = "Dutta44" # list assignment index out of range

# # Indexing
print("element at the index 0 - ", my_list[0])
print("element at the index 1 - ", my_list[1])
print("element at the index 2 - ", my_list[2])

print(my_list)
for element in my_list:
    print(element)
#
for i in range(1, 10):  # [1,2,3,4,5,6,7,8,9]
    print(i)

    # range(1,10,1) -> list -> [1,2,3,4,5,6,7,8,9]
#
# print(" - -------------")
my_list = [1, 2, 3]

# append()
my_list.append(4)  # Append object to the end of the list.
my_list.append(6)
print(my_list)
#
# extend()
my_list.extend([7, 8, 9])
my_list.extend([10])
my_list.extend(["madhukar"])
print(my_list)
print(len(my_list))
#
# # insert()
my_list.insert(1, "pandey")
print(my_list)
print(len(my_list))

my_list[1] = "Rahul"
print(my_list)
#
my_list.insert(0, 0)
print(my_list)
my_list.insert(-1,"Lucky")
print(my_list)
#
# remove()
my_list.remove("Rahul")
print(my_list)

# my_list.replace()
print(" --------------------------")
print(" --------------------------")
#
my_copy_list = my_list.copy()
print(my_list)
print(my_copy_list)

my_list.clear()
print(my_list)
print(my_copy_list)
#
 # my_copy_list.remove("madhukar")
my_copy_list.sort()
my_copy_list.sort(reverse=False)
print(my_copy_list)
#
my_copy_list.reverse()
print(my_copy_list)
#
# name = "Pramod"
# name = name.upper()
# print(name)
#
# # for - loop
#
# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# l3 = l1 + l2
# print(l3)