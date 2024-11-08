# # Dict
# # Key and Value
# # name -> "Pramod"
#
# student_infor = {
#     "name": "madhukar",
#     "age": 24,
#     "age": 25,
#     "address": "up"
# }
# #
# print(student_infor)
# print(student_infor["name"])
# print(student_infor["age"])
# print(student_infor["address"])
# #
# student_infor["age"] = 26
# print(student_infor)
# #
# student_infor1 = dict(name="Akshay", age=24, address="PB")
# print(student_infor1)
# # A dictionary is an unordered collection of data
#
#
student_information = {
     "name": "Vishwas",
   # "age": 65,
      "age": 24,
     "address":
         {
        "home_address": "PB",
        "office_address": "UP"
   }
}
#
student_infor2 = {
    "name": "Mohit",
    # "age": 65,
    "age": 23,
    "address": {
        "home_address": "GOA",
        "office_address": "KA"
    }
}
#
student_list= [student_information,student_infor2]
print(student_list)