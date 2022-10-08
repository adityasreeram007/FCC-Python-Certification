from datetime import date
import datetime
daysOfWeek=["monday", "tuesday", "wednesday", "thursday", "friday","satureday","sunday"]
def getDay(currDay,days):
    currDay=currDay.lower()
    days=days%7
    currindex=daysOfWeek.index(currDay)
    while True:
        if days==0:
            return daysOfWeek[currindex]

        if currindex==6:
            currindex=0
        else:
            currindex+=1
        days-=1
def add_time(curr,adder,day=None):
    topm=0
    if curr[-2:]=="PM":
        topm=12
    time=curr[:-2]
    time=time.split(':')
    currdate=str(date.today()).split('-')
    adder=adder.split(":")
    currdateandtime=datetime.datetime(int(currdate[0]),int(currdate[1]),int(currdate[2]),int(time[0])+topm,int(time[1]))
    time_change = datetime.timedelta(hours=int(adder[0]),minutes=int(adder[1]))
    new_time=currdateandtime+time_change
    delta=datetime.datetime(new_time.year,new_time.month,new_time.day)-datetime.datetime(int(currdate[0]),int(currdate[1]),int(currdate[2]))
    res=""
    hour=str(new_time.hour%12)
    if new_time.hour==12 or new_time.hour==0:
        hour=str(12)
    minutes=str(new_time.minute)
    if len(hour)==1:
        hour="0"+hour
    if len(minutes)==1:
        minutes="0"+minutes
    res+=hour+":"+minutes
    if new_time.hour>12:
        res+=" PM"
    else:
        res+=" AM"
    
    if day!=None:
        res+=", "+getDay(day,delta.days).capitalize()
    if delta.days>=1:
        if delta.days==1:
            res+=" (next day)"
        else:
            res+=" ("+str(delta.days)+" days later)"
    return res






