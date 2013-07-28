#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest
import shab_dates


class DateTests(unittest.TestCase):

    def test_today(self):
        self.failUnless(shab_dates.get_current_day() <= 6
                        and shab_dates.get_current_day() >= 0)

    def test_next_fri_sat(self):
        (fri, sat) = shab_dates.get_next_fri_sat_dates()
        self.failUnless(fri.weekday() == 4 and sat.weekday() == 5)


class TimeTests(unittest.TestCase):

    def test_meal_time_slots(self):
        self.failUnless(len(shab_dates.get_times_quarters()) == 45)

    def test_deadline_time_slots(self):
        times = shab_dates.get_deadline_times()
        self.failUnless(len(times) == 24 and 'noon' in times
                        and 'midnight' in times)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
