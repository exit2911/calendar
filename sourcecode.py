import calendar

print("team meeting date are : \n")

for m in range(1,13):
    cal = calendar.monthcalendar(2018,m) #loop 12 months
    weekone = cal[0] #week one - list index the first week
    weektwo = cal[1] #week two - list index the 2nd week
  
    if weekone[calendar.FRIDAY] != 0: #check if the first friday in the month calendar is from the current month
        meetday = weekone[calendar.FRIDAY]
    else:
        
        meetday = weektwo[calendar.FRIDAY] #if not the first friday is from the 2nd week

    print(calendar.month_name[m],meetday)
