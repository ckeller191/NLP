remainder = lambda num: num % 2

#print(remainder(5))
#gives remainder of 1

product = lambda x, y: x * y

#print(product(2, 3))
#gives product of 6

def testfunc(num):
    return lambda x : x * num

result1 = testfunc(10)
result2 = testfunc(100)

#print(result1(9))
##gives result of 90; taking 10 from result1 * 9 from print statement
#print(result2(9))


#Filter function; filter(object, iterable)

numbers_list = [2, 6, 8, 10, 11, 4, 12, 7, 13, 17, 0, 3, 21]

filtered_list = list(filter(lambda num: (num > 7), numbers_list))

#print(filtered_list)


def addition(n):
    return n + n
#doubles input number

numbers = [1, 2, 3, 4]
result = map(addition, numbers)
print(list(result))
#creates list of each number doubled

numbers = [1, 2, 3, 4]
result = map(lambda n: n + n, numbers)
print(list(result))

numbers2 = [5, 6, 7, 8]

result2 = map(lambda x, y: x + y, numbers, numbers2)

print(list(result2))
