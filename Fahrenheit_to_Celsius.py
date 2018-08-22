from FileOperator import FileOperator
numbers =  FileOperator("data/data5.txt").change_to_integer()
index = 1
result = ""
for i in range(0, numbers[0]):
    rounded = round(((numbers[index]+40)/1.8)-40)
    result += " " + str(rounded)
    index += 1
print(result)