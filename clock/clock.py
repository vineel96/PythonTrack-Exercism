class Clock(object):
    out_hour=0
    out_minute=0
    def __init__(self, hour, minute):
        self.hour=hour
        self.minute=minute
        self.total_minutes=hour*60+minute

        self.update()

    def __repr__(self):
        return '%02d:%02d' % (self.out_hour,self.out_minute)


    def __eq__(self, other):
        return (self.out_hour==other.out_hour) and (self.out_minute==other.out_minute)

    def __add__(self, minutes):
        self.total_minutes+=minutes
        self.update()
        return self


    def __sub__(self, minutes):
        self.total_minutes-=minutes
        self.update()
        return self

    def update(self):
        htemp = self.total_minutes // 60
        self.out_hour = htemp % 24
        self.out_minute = self.total_minutes % 60