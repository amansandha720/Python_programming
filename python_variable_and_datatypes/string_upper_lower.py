def str_upper_lower(str1):
    if len(str1)>= 10:
        print(str1.upper())
    else:
        print(str1.lower())
str1 = input("Enter the string: ")
str_len = len(str1)
print(str_len)
str_upper_lower(str1)