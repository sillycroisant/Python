import random

months = ('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec')

def birthday_paradox():
    birthdays = []

    count = 0

    while True:
        month = random.choice(months)
        if(month in ('Jan','Mar','May','Jul','Aug','Oct','Dec')):
            date = str(random.randint(1,31))
        elif(month in ('Apr','Jun','Nov','Sep')):
            date = str(random.randint(1,30))
        else:
            date = str(random.randint(1,29))
        birthday = month + " " + date

        if(birthday not in birthdays):
            birthdays.append(birthday)
            count += 1
        else:
            print("You need atleast {} people in a room to have two people with a same birthday.".format(count+1))
            break

num = int(input("Number of simulation : "))


for sim in range(num):
    birthday_paradox()
    

    
    
    

    

    
