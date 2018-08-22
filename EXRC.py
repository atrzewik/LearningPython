def sums(x,y):
    result = x + y
    return result
print (sums(8871, 14933))

numbers = input("Enter the number of items to sum\n")
numbers = numbers.split()
sum = 0
x = 0
for i in range(0, len(numbers)):
    sum += int(numbers[x])
    x += 1
print ("The sum is: " + str(sum))

numbers = input("Enter the number of items to sum\n")
pairs = numbers.split(

)
print(pairs)
pair = " ".join(pairs)
print(pair)
numbers = pair.split()
print(numbers)
sum = 0
x = 0
for p in range(0, len(pairs)):
    for i in range(0, 2):
        sum += int(numbers[x])
    x += 1
    print ("The sum is: " + str(sum)),

numbers = input("Enter the number of items to sum\n")
numbers = numbers.split()
sum = 0
x = 0
for i in range(0, len(numbers)):
    sum += int(numbers[x])
    x += 1
print ("The sum is: " + str(sum))