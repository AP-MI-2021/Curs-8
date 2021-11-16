lst = [1,2,7,4,2,8,21,33,23,43,12,543,23,435]
odds = list(filter(lambda x: x % 2 == 1, lst))
print(odds)

odds_LC = [x for x in lst if x % 2 == 1]
print(odds_LC)