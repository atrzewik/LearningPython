from FileOperator import FileOperator
data = FileOperator("data/data29.txt").change_to_integer()


class Generator(object):

    def __init__(self, data):
        self.number_of_words = data[0]
        self.data_X0 = data[1]
        self.data = data[2:]
        self.consonant = self.list_of_consonant()
        self.vowels = self.list_of_vowels()

    def list_of_letters(self, letters):
        list_of_letters= []
        for x in letters:
            list_of_letters.append(x)
        return list_of_letters

    def list_of_consonant(self):
        consonant = "bcdfghjklmnprstvwxz"
        return self.list_of_letters(consonant)

    def list_of_vowels(self):
        vowels = "aeiou"
        return self.list_of_letters(vowels)

    def generating(self):
        words = ""
        X0 = self.data_X0
        for i in range(0, self.number_of_words):
            word = ""
            for j in range(0, self.data[i]):
                random_value = ((445 * X0) + 700001) % 2097152
                X0 = random_value
                if j % 2 == 0:
                    number_of_letter = random_value % 19
                    letter = self.consonant[number_of_letter]
                else:
                    number_of_letter = random_value % 5
                    letter = self.vowels[number_of_letter]
                word += letter
            words += " " + word
        return words


print(Generator(data).generating())