from datetime import datetime,timedelta
def meetup(year, month, week, day_of_week):
    dict={"Sunday":0,"Monday":1,"Tuesday":2,"Wednesday":3,"Thursday":4,"Friday":5,"Saturday":6}
    date=datetime(year=year,month=month,day=1)
    present_day=date.weekday()
    num_day_of_week=dict[day_of_week]
    if week=='1st':
        diff= num_day_of_week-present_day
        return date+timedelta(days=diff)


def MeetupDayException():
    pass

