from FileOperator import FileOperator
numbers = FileOperator("data/data8.txt").change_to_integer()

#sorted_numbers = sorted(numbers)
#print(sorted_numbers)
#def sorted_numbers(numbers):
index = 1
string_of_mediana = ""
for i in range(0, numbers[0]):
    three_numbers = []
    three_numbers += numbers[index:index+3]
    three_numbers = sorted(three_numbers)
    print("three: ", three_numbers)
    median = three_numbers[1]
    string_of_mediana += " " + str(median)
    index += 3
print(string_of_mediana)


#print("Mediana: ", end=" ")
#print(sorted(numbers))