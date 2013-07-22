import unittest
import shab_dates

class DateTests(unittest.TestCase):

    def testCurrentMonthYear(self):
        self.failUnless(len(shab_dates.this_month_year())==2)

    def testNextMonthYear(self):
        self.failUnless(shab_dates.next_month_year(7, 2013)==(8, 2013)
                        and shab_dates.next_month_year(12, 2013)==(1, 2014))

    def testUrl(self):
        self.failUnless(shab_dates.get_url(7,2013,90210)=="http://www.hebcal.com/hebcal/?v=1&cfg=json&c=on&month=7&year=2013&zip=90210")    

    def testUpcomingShabDates(self):
        friday_dict = {u'category': u'candles', u'date': u'2013-07-05T19:52:00-07:00', u'title': u'Candle lighting: 7:52pm'}
        saturday_dict = {u'category': u'havdalah', u'date': u'2013-07-06T21:21:00-07:00', u'title': u'Havdalah (72 min): 9:21pm'}
        shab_obj = shab_dates.convert2shab_obj(friday_dict, saturday_dict)
        this_mo, this_yr = shab_dates.this_month_year()
        next_mo, next_yr = shab_dates.next_month_year(this_mo, this_yr)
        self.failUnless(len(shab_dates.get_all_upcoming_shabs(90210))>=16
            and shab_obj.fri_mon == 7
            and shab_obj.fri_day == 5
            and shab_obj.fri_yr  == 2013
            and shab_obj.sat_mon == 7
            and shab_obj.sat_day == 6
            and shab_obj.sat_yr == 2013
            and shab_obj.get_candle_time() == " 7:52pm"
            and shab_obj.get_havdalah_time() == " 9:21pm"
        )

    def testCount(self):
        self.failUnless(len(shab_dates.next_weeks(90210)) >= 4
            and len(shab_dates.next_weeks_ltd(90210,3))==3)

         
def main():
    unittest.main()

if __name__ == '__main__':
    main()