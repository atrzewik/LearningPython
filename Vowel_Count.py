from FileOperator import FileOperator

data = FileOperator("data/data6.txt").get_data_splitted_by_separator("\n")
index = 1
for string in data[1:]:
    result = 0
    for letter in string:
        if letter == "a":
            result += 1
        elif letter == "o":
            result += 1
        elif letter == "u":
            result += 1
        elif letter == "i":
            result += 1
        elif letter == "e":
            result += 1
        elif letter == "y":
            result += 1
    print(result, end=" ")

# or: letter == "a" or letter == "e"...
