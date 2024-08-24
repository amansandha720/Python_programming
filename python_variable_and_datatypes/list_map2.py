def square_element(num):
    return num**2
lst = [1,2,3,4,5]
squared_num = map(square_element, lst)
result = list(squared_num)
print(result)
