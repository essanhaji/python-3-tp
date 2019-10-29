import datetime

date = input("Entrer une date avec cette forma YYYY/MM/DD : ")

date = date.split("/")
# print(date)
date = datetime.date(int(date[0]), int(date[1]), int(date[2]))

print("The current date {date}".format(date=str(date)))

# date = date + 3day
date += datetime.timedelta(days=3)

print("The date after 3 days {date}".format(date=str(date)))