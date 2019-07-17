from datetime import datetime
import calendar

class MeetupDayException(Exception):
    def __init__(self, expression, message):
        self.expression, self.message = expression, message

def meetup(year, month, week, day_of_week):
    days_map={"Monday":0,"Tuesday":1,"Wednesday":2,"Thursday":3,"Friday":4,"Saturday":5,"Sunday":6}
    week_map={'1st' : 0,'2nd' : 1,'3rd' : 2,'4th' : 3,'5th' : 4,'last' : -1}
    original_date=datetime(year=year,month=month,day=1)
    num_days=calendar.monthrange(year,month)[1]
    dates_in_month=[ datetime(year=year,month=month,day=day) for day in range(1,num_days+1)]
    filter_dates=[ date for date in dates_in_month if date.weekday()==days_map[day_of_week]]

    if week in week_map.keys():
        return filter_dates[week_map[week]].date()
    elif week=='teenth':
        return [date for date in filter_dates if date.day <= 19 and date.day >= 13][0].date()
    else:
        try:
            return filter_dates[int(week[0])-1].date()
        except IndexError as err:
            raise MeetupDayException(err, "Invalid\'{}\'".format(week))

