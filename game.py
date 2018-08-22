fields = ["O" * 5] * 5


def make_fields(x):
    board = []
    for field in x:
        board.append(field)


make_fields(fields)

fields[0][0] = "X"

make_fields(fields)

lista = [1, 2, 3]
make_fields(lista)


#def change(x, y, value, listaa):

    #for i in range(0, len(listaa)):
        #for j in range(0, len(listaa)):
            #if i == x and j == y:
                #listaa[i][j] = str(value)

#change(0,0,2,fields)
#make_fields(fields)