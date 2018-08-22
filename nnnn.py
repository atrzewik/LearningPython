# a = 0, 2, 5, 0, 6
# print(a)
#
# a = a.split()
# print(a)

from FileOperator import FileOperator
numbers = FileOperator("data/data14.txt").change_to_integer()

print(numbers)

# class Average(object):
#     def __init__(self, value):
#         self.value = value
#         self.value_mode = value[1:]
#
#     def sth(self):
#         value = self.value_mode
#         result = []
#         index = 0
#         for i in range(0, int(self.value[0])):
#             result.append([value[index]])
#             index += 1
#         return result
#
#     def sthh(self):
#     #for i in range(0, int(self.value[0])):
#         alls = self.sth()
#         part = alls[0]
#         part = [i for i in part]
#         return part



            # value = [int(v) for v in value[index]]
            # for i in value:
            #     if i != 0:
            #         sum += int(i)
            #     else:
            #         break
            # sum /= (len(value)-1)
            # avr += " " + str(sum)
            # index += 1
            # return avr
# if value[i] == 0:
# sum += value
# else:
# sum / i

print(Average(numbers).sth())
print(Average(numbers).sthh())