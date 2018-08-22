file = open("data.txt", "r")
reade_file = file.read()
file.close()
numbers = reade_file.split()
index = 1
result = []
for i in range(0, int(numbers[0])):
    sum = 0
    sum += int(numbers[index])
    sum += int(numbers[index + 1])
    index += 2
    result.append(str(sum))

result = " ".join(result)
print('result')
print(result)