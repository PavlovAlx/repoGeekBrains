string1 = int(input("введите выручку"))
string2 = int(input("введите издержки"))
if string1 >= string2:
    print ("вы работаете с прибылью:", string1-string2)
    print ("рентабельность:", string1/string2)
    string3 = int(input("численность сотрудников:"))
    print ("прибыль на сотрудника:", (string1-string2)/string3)
else:
    print("вы работаете с убытком:", string1 - string2)