nums = [1,2,3,4,5]

counted = [
    (1,2),
    (2,4),
    (3,7),
    (4,1),
    (5,3)
]

arr1 = list(map(lambda x : x*2,nums))

arr2 = list(filter(lambda x: x%2 == 0,nums))

arr3 = sorted(counted,key = lambda x: x[1])

print(arr1)

print(arr2)

print(arr3)