# list1 = ["index", "insert", "pop"]

# list1.insert(3, "append")
# print(list1)

# def tri_recursion(minusing_one):
#   if(minusing_one > 0):
#     result = minusing_one + tri_recursion(minusing_one - 1)
#     print(result)
#   else:
#     result = 0
#   return result

# print("\n\nRecursion Example Results")
# tri_recursion(6)

# a = 3.0
# b = 4.0
# c = (a ** 2 + b ** 2)** 0.5
# print(c)

# str1 = "Coding is"
# str2 = " Good for the world"
# print(str1 + str2)


# fruit_colors = {"apple": "red", "banana": "yellow", "grapes": "purple"}

# key_to_check = "apple"

# if key_to_check in fruit_colors:
#     print(f"The key {key_to_check} exists in the dictionary.", key_to_check)
# else:
#     print(f"The key {key_to_check} does not exist in the dictionary.")


# Global and local scope

# def myfunc():
#     x = 300
#     print(x)

# myfunc()

# Global scope
# x = 700

# if x >= 300:
#     print("haaa")
# else:
#     print("MMMMMM")

# # global keyword
# x = 30

# def myfunc():
#     global x

#     x = x + 40
#     print(x)

# myfunc()

# list = ["a", "b", "c", "d", "e",]
# newLists = []

# for i in list:
#     if "a" in i:
#         newLists.append(i)

# print(newLists)

# nesting conditional statements
# check a letter



# lst = [i for i in range(-1, -2)]
# print(lst)

# dit = {}
# dit['1'] = (1,2)
# dit['2'] = (2,1)

# for x in dit.keys():
#     print(dit[x][1], end="")

# nums = [1,2,3]
# vals = nums
# print(nums)
# print(vals)

# x = 1
# y = 2
# x, y, z = x, x, y
# z, y, z, = x, y, z
# print(x, y, z)
# print("a","b","c", sep="sep")
# my_list = [x * x for x in range(5)]
# def fun(lst):
#     del lst[lst[2]]
#     return lst


# y = input()
# x = input()
# print(x + y)

# try:
#     result = 10 / 0
# except ZeroDivisionError:
#     print("Error: Division by zero")


# my_list = [1, 2]

# for v in range(2):
#     my_list.insert(-1, my_list[v])

# print(my_list)

# tup = (1, 2, 4, 8)
# tup = tup[-2:-1]
# tup = tup[-1]
# print(tup)

# dd = {"1": "0", "0": "1"}
# for x in dd.vals():
#     print(x, end="")

    # mytuple[1] = mytuple[1] + mytuple[0]

# print(mytuple)

# x = int(input())
# y = int(input())
# x = x % y
# x = x % y
# y = y % x
# print(y)


# def fun(inp=2, out=494949):
#     return inp * out

# print(fun(out=2))

# x = float(input())
# y = float(input())
# print(y ** (1 / x))

# i = 0
# while i < i + 2:
#     i += 1
#     print("*")
# else :
#     print("*")

# def fun(x, y):
#     if x == y:
#         return x
#     else:
#         return fun(x, y-1)

# print(fun(0,3)) 


# def function_1(a):
#     return None

# def function_2(a):
#     return function_1(a) * function_1(a)

# print(function_2(2))



    # def fun(x):
    #     if x % 2 == 0:
    #         return 1
    #     else:
    #         return 2
        
    # print(fun(fun(2)))

# x = 1 // 5 + 1 / 5
# print(x)

# foo = (1,2,3)
# foo.index(0)

# print(foo)

# z = 0
# y = 10
# x = y < z and z > y or y > z and z < y
# print(x)

# lst = [[x for x in range(3)] for y in range(3)]

# for r in range(3):
#     for c in range(3):
#         if lst[r][c] % 2 !=  0:
#             print("#")

# def add(a, b):
#     return a - b

# result = add(5, 3)
# print(result)



