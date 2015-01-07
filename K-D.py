#Max Louis
#Table Generator v0.1
#07/01/2015
def inputs():
    columns = int(input("How many columns?"))
    column_list = []
    for count in range(columns):
        column_names = input("Please enter the column names.")
        column_list.append(column_names)
    return column_list

def columns(column_list,width):
    select = -1
    for each in column_list:
        select += 1
        print("{0:<{width}}".format(column_list[select],width = width[select]),end="")

def width()
    
#MAIN
column_list = inputs()
columns(column_list)
