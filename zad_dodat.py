uczelnia = {'Jan Kowalski': 5.0, 'Mieczyslaw Waski': 2.0, 'Mariusz Pudzianowski': 3.0, 'Andrzej Duda': 4.0, 'Donald Trump': 3.5}
print(uczelnia)
print("Another list")
uczelnia2 = {k: v for (k, v) in uczelnia.items() if v > 2}
print(uczelnia2)

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
double_dict1 = {k:v*2 for (k,v) in dict1.items()}
print(double_dict1)