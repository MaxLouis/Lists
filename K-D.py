#Max Louis and Ferhat
#XxOPT1Cz_C0DxX MLG!!! NOOOBS!!!
#06/01/2015
full_list = [
    ["K1llmAchine",51,49],
    ["bob7424",5,99],
    ["hAxOr12",72,30],
]

row = print("|")
align = ("{0:<15}{1:^1}{2:<8}{3:^1}{4:<5}")
print(align.format("NAME",row,"KILLS",row,"DEATHS"))
print("_"*50)

for player in full_list:
    print(align.format(player[0],row,player[1],row,player[2]))




