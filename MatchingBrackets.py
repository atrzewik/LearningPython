from FileOperator import FileOperator
characters = FileOperator("data/data20.txt").get_data_splitted_by_separator("\n")


def characters_into_string(characters):
    characters_list = []
    for character in characters:
        characters_string = ""
        for ch in character:
            if ch == "(" or ch == ")" or ch == "[" or ch == "]" or ch == "{" or ch == "}" or ch == ">" or ch == "<" :
                characters_string += ch
            else:
                continue
        characters_list.append(characters_string)
    return characters_list

characters_list = characters_into_string(characters)

openList = ["[","{","(","<"]
closeList = ["]","}",")",">"]
def balance(myStr):
    all_answer = ""
    for j in myStr:
        stack= []
        for i in j:
            if i in openList:
                stack.append(i)
            elif i in closeList:
                pos = closeList.index(i)
                if len(stack) == 0 :
                    stack.append("i")
                    answer = 0
                elif (len(stack) > 0) and (openList[pos] == stack[len(stack)-1]):
                    stack.pop()
                    answer = 0
                else:
                    stack.append("i")
                    answer = 0
        if len(stack) == 0:
            answer = 1

        all_answer += " " + str(answer)
    return all_answer


print(balance(characters_list))