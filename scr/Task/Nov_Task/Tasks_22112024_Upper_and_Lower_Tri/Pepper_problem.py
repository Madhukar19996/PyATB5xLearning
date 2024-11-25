#
# String = "swiss"
# l=[]
#
#
# for i in String:
#     count = 0
#     for j in String:
#         if i == j:
#             count+=1
#         if count > 1:
#             break
#
#     if count == 1:
#         print(i)

print("___________________________________________________________________________________________")
def first_non_repeatable_word (string):
    for char in string:
        if string.count(char)==1 :
            return char
    return None

print(first_non_repeatable_word("ananomyous"))








