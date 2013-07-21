class ShabbCalendarDetails():

    def __init__(self, mon_fri, day_fri, yr_fri, mon_sat, day_sat, year_sat):
        self.mon_fri = mon_fri
        self.day_fri = day_fri
        self.yr_fri = yr_fri
        self.mon_sat = mon_sat
        self.day_sat = day_sat
        self.year_sat = year_sat

    def set_candle_time(self, time):
        self.time = time

    def set_zip_code(self, zip_code):
        self.zip_code = zip_code

    def get_candle_time(self):
        return self.time
