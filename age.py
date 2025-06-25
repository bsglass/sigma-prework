from datetime import datetime, date
rawDate=input("What date were you born? dd-mm-yyyy")
processedDate=[int(x) for x in rawDate.split("-")[::-1]]
today=date.today()

#must be a better way to do below but idk
age=today.year-processedDate[0]
if today.month<processedDate[1]:
    age-=1
elif today.month==processedDate[1]:
    if today.day<processedDate[2]:
        age-=1
print("You are ",age," years old.")