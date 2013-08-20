class ShabbCalendarDetails():

    def __init__(self, fri_mon, fri_day, fri_yr, sat_mon, sat_day, sat_yr):
        self.fri_mon = fri_mon
        self.fri_day = fri_day
        self.fri_yr = fri_yr
        self.sat_mon = sat_mon
        self.sat_day = sat_day
        self.sat_yr = sat_yr

    def set_candle_time(self, candle_time):
        self.candle_time = candle_time

    def get_candle_time(self):
        return self.candle_time

    def set_havdalah_time(self, havdalah_time):
        self.havdalah_time = havdalah_time

    def get_havdalah_time(self):
        return self.havdalah_time    