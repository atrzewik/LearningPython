from FileOperator import FileOperator
numbers = FileOperator("data/data17.txt").change_to_integer()

class Time(object):
    def __init__(self, data):
        self.data = data[1:]

    def differences_in_sec(self):
        index=0
        data = self.data
        sec_differences = []
        while index < len(data):
            day1=data[index]
            hour1=data[index+1]
            min1=data[index+2]
            sec1=data[index+3]
            day2=data[index+4]
            hour2=data[index+5]
            min2=data[index+6]
            sec2=data[index+7]
            sec_difference = ((((((day2 * 24) + hour2) * 60) + min2) * 60) + sec2)-((((((day1*24)+hour1)*60)+min1)*60)+sec1)
            sec_differences.append(sec_difference)
            index += 8
        return sec_differences

    def differences(self):
        data = self.differences_in_sec()
        result = ""
        for i in range(0, len(data)):
            value = data[i]
            seconds = value%60
            value = (value - seconds)/60
            value = int(value)
            minutes = value%60
            value = (value - minutes)/60
            value = int(value)
            hours = value%24
            value = (value - hours)/24
            value = int(value)
            days = value
            result += "(" + str(days) + " " + str(hours) + " " + str(minutes) + " " + str(seconds) + ") "
        return result


print(Time(numbers).differences())