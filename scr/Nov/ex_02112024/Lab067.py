def print_arguments(*args):
    # *args = multiple argument with no limit, -> list
    # print(args[0])
    for i in args:
        print(i)

# list = ["pramod", "amit", "lucky"]

print_arguments("madhukar", "amit", "lucky")
print_arguments("amit", "lucky")
print_arguments("amit", 10)
print_arguments("amit", 10, True)
print_arguments("amit", 10, True, False)
print_arguments("amit", 10, True, False, "PIYUSH")
print_arguments("lucky")
# print_arguments() -minimum 1 arguement is importa


print("amit")
print("madhukar", "amit")
print("madhukar", "amit", True)
print("madhukar"
      "", "amit", True, False)