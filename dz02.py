string1 = int(input("введите секунды >>>"))
if string1 > 86400:
    print("вы ввели значение больше суток!")
else:
    hours = (string1 // 3600)
    minutes = ((string1 - (hours * 3600)) // 60)
    sec = (string1 - (hours * 3600) - (minutes * 60))
    print("часы:", hours, "минуты:", minutes, "секунды:", sec)
