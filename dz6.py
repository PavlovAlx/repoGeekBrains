start = int(input("введите км в первый день:"))
finish = int(input("введите результат в км, который нужно достичь:"))
day =1
if start>finish:
    print("спортсмен сразу может пробежать", finish, "км")
else:
    while start<finish:
        day = day+1
        start = start * 1.1
        print("спортсмен пробежал в день", day, round(start,2), "км")

print("ответ: на",day,"-й день спортсмен достиг результата не менее",finish,"км")