class FileOperator(object):
    def __init__(self, path_to_file, operation='r'):
        self.file = open(path_to_file, operation)
        self.operation = operation
        self.path_to_file = path_to_file

    def read_file(self):
        if self.check_operation('r') or self.check_operation('r+'):
            self.read_file = self.file.read()
            self.file.close()
            return self.read_file
        else:
            raise Exception("ERROR! You can read file only on operator which is reader")

    def get_data_splitted_by_separator(self, separator=None):
        return self.read_file().split(separator)

    def check_operation(self, operation):
        return operation == self.operation

    def write_file(self, words):
        if self.check_operation('a'):
            self.appender = self.file.write("\n" + words)
            self.file.close()
            return self.appender
        else:
            raise Exception("ERROR! You can add write file only on operator which is writer")

    def change_to_integer(self):

        splitted_data = self.get_data_splitted_by_separator()
        splitted_data = [int(i) for i in splitted_data]
        return splitted_data

    def change_to_float(self):
        splitted_data = self.get_data_splitted_by_separator()
        splitted_data = [float(i) for i in splitted_data]
        return splitted_data