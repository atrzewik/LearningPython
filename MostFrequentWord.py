from FileOperator import FileOperator
numbers = FileOperator("data/data30.txt").change_to_integer()


class WordsGenerator(object):

    def __init__(self, data):
        self.number_of_words = data[0]
        self.data_X0 = data[1]
        self.data = data[2]
        self.list_of_data = self.making_data()
        self.consonant = self.list_of_consonant()
        self.vowels = self.list_of_vowels()
        self.words = self.generating_words()

    def making_data(self):
        list_of_data = []
        for i in range(0, self.number_of_words):
            list_of_data.append(self.data)
        return list_of_data

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

    def generating_words(self):
        words = []
        X0 = self.data_X0
        for i in range(0, self.number_of_words):
            word = ""
            for j in range(0, self.list_of_data[i]):
                random_value = ((445 * X0) + 700001) % 2097152
                X0 = random_value
                if j % 2 == 0:
                    number_of_letter = random_value % 19
                    letter = self.consonant[number_of_letter]
                else:
                    number_of_letter = random_value % 5
                    letter = self.vowels[number_of_letter]
                word += letter
            words.append(word)
        return words


class MostFrequentWords(object):

    def __init__(self, data):
        self.words = WordsGenerator(data).generating_words()
        self.list_of_words = self.list_of_words_frequency()

    def list_of_words_frequency(self):
        frequency_of_word = []
        frequency = 1
        words = self.words
        while len(words) > 0:
            word = words[0]
            del words[0]
            while word in words:
                if word in words:
                    frequency += 1
                    words.remove(word)
            tuples = (word, frequency)
            frequency_of_word.append(tuples)
            frequency = 1
        return frequency_of_word

    def list_of_frequency_values(self):
        list_of_values = []
        for element in self.list_of_words:
            list_of_values.append(element[1])
        return list_of_values

    def most_frequent_word(self):
        values = self.list_of_frequency_values()
        max_value = max(values)
        index = values.index(max_value)
        key = self.list_of_words[index][0]
        return key


print(MostFrequentWords(numbers).most_frequent_word())