def sum(list):
    if len(list) == 0:
        return 0
    else:
        return list[0] + sum(list[1:])


print(sum([3, 5, 7, 5]))


def count(list):
    if list == []:
        return 0
    else:
        return 1 + count(list[1:])


print(count([3, 5, 7, 5]))


def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x - 1)


print(fact(5))
