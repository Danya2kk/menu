import tables as tl

meals = tl.selectMenu()

answer = ''
for meal in meals:
    answer = answer + str(meal[0]) + ' ' + str(meal[1]) + '\n'
print(answer)
