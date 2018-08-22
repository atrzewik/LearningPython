from FileOperator import FileOperator
numbers = FileOperator("data3.txt").change_to_integer()

print(max(numbers), min(numbers))