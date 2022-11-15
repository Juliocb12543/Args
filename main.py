# #args means I can use as many arguments as possible
# def sum(*args):
#   total = 0
#   for arg in args:
#     total += arg
#   return total

# print(sum(2,3,1,6))



# #kwargs means using key values(limitless)
# #a step beyond args
# #keys and values represented **
# #dictionary = key, value; items are keys and values together
# def a_sum(**kwargs):
#   total = 0
#   for key, value in kwargs.items():
#     print(f"{key} = {value}")
#     total += value
#   return total

# print(a_sum(x=3,y=5, z=22))