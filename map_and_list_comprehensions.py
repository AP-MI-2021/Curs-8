# map
lst = [1,2,7,4,2,8,21,33,23,43,12,543,23,435]
lst_times_2 = list(map(lambda x: x * 2, lst))
print(lst_times_2)

# list comprehensions
lst_times_2_evens = [x * 2 for x in lst if x % 2 == 0] # {2x+1 : x ap N}
print(lst_times_2)
