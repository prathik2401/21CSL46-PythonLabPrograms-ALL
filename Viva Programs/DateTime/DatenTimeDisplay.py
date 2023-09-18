from datetime import date, datetime
today = date.today()
todayDate = today.strftime("%d-%m-%Y")
t = str(datetime.now())
print(t.replace("2023-09-19",''))
print(todayDate)