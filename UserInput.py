class UserInput(object):

    def __init__(self):
        self.check = CheckingUser()

    def get_number_of_fields(self):
        number = input("Please pick number of fields from 2 to 20: ")
        if not self.check.collect_type_from_user(number, int):
            self.get_number_of_fields()
        elif not self.check.collect_input_in_range(int(number), 2, 20):
            self.get_number_of_fields()
        else:
            return int(number)

    def get_parameters(self, number_of_fields, parameter, sign):
        maximum_pick = number_of_fields - 1
        number = input("Please, enter your %s(0-%s) for %s:" % (parameter, maximum_pick, sign))
        if not self.check.collect_type_from_user(number, int):
            self.get_parameters(number_of_fields, parameter, sign)
        elif not self.check.collect_input_in_range(int(number), 0, maximum_pick):
            self.get_parameters(number_of_fields, parameter, sign)
        else:
            return int(number)


class CheckingUser(object):

    def __init__(self):
        pass

    def collect_type_from_user(self, number, types):
        try:
            types(number)
        except ValueError:
            print("You give wrong answer's type!")
            return False
        else:
            return True

    def collect_input_in_range(self, number, minimum, maximum):
        try:
            if number < minimum or number > maximum:
                raise ValueError
        except ValueError:
            print("You give wrong value!")
            return False
        else:
            return True
