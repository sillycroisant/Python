import random

months = ('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec')

num = int(input("Input number of birthday you want to generate : "))

birthdays = []

for i in range(num):
    month = random.choice(months)
    if(month in ('Jan','Mar','May','Jul','Aug','Oct','Dec')):
        date = str(random.randint(1,31))
    elif(month in ('Apr','Jun','Nov','Sep')):
        date = str(random.randint(1,30))
    else:
        date = str(random.randint(1,29))
    birthday = month + " " + date
    birthdays.append(birthday)

for bd in birthdays:
    print(bd)