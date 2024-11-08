a, b, c = (103, 121, 142)

print(a)
print(b)
print(c)

# Search in Tuple
cities = ("Dubai", "china", "Los Angeles", "Tokyo")
print("Paris" in cities)
print("New Delhi" in cities)


t = (12, 34, 56)
# t.append(12) # r: 'tuple' object has no attribute 'append'
my_list = list(t)
my_list.append(4)
t = tuple(my_list)
print(t)