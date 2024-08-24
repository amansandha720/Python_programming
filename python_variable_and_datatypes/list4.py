x = [1, 2, 3, 4]
del x[1:2]
print(x)

def reverse_from_index(my_list, index):
    first_part = my_list[:index]
    second_part = my_list[index:]
    second_part.reverse()
    reversed_list = first_part + second_part
    return reversed_list
my_list = [1, 2, 3, 4]
index = 3
result = reverse_from_index(my_list, index)
print(result)    


    
