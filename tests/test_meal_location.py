import unittest
from shab_dates import next_weeks
from shab_dates import next_month_year
from shab_dates import this_month_year
from shab_dates import get_url

class DateTests(unittest.TestCase):

    def testCurrentMonthYear(self):
        self.failUnless(len(this_month_year())==2)

    def testNextMonthYear(self):
        self.failUnless(next_month_year(7, 2013)==(8, 2013)
                        and next_month_year(12, 2013)==(1, 2014))

    def testUpcomingShabDates(self):
        self.failUnless(next_weeks(3)[0].get_candle_time().endswith("pm")==True)

    def testUrl(self):
        self.failUnless(get_url(7,2013,90210)=="http://www.hebcal.com/hebcal/?v=1&cfg=json&c=on&month=7&year=2013&zip=90210")    
         
def main():
    unittest.main()

if __name__ == '__main__':
    main()