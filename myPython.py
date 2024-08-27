numbers = list(range(1,101))


result = [ n for n in numbers if n % 5 == 0]
print(result)

#x= []
#for i in range(5):
    #for j in range(4):
         #x[i][j] = 8
         # print(x)

x = list(range(5))
z = []
for i in x:
    z.append(x)
print(z)
score = (1, 2, 2,3, "bimbola")
list2 = [1,2,3, "bimbola",2.5]
print(list2)
list2[3] = "timothy"
print(list2)
single_tuple = (1,)
print(score)
score = list(score)
score[4] = "chidinma"
score = tuple(score)
#print(score)
print(type(score))

tuple2 = (1,2,3,[2,4,6], "priest", "10.3")
print(tuple2)
tuple2[3].extend([8, 10])
print(tuple2)




numbers = [1,2,3,4,5]
print(6 in numbers)
print(6 not in numbers)
print(6 in range(len(numbers)))


