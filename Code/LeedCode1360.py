class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        # solution one: datetime
        import datetime
        year1, month1, day1 = date1[0:4], date1[5:7], date1[8:10]
        year2, month2, day2 = date2[0:4], date2[5:7], date2[8:10]

        d1 = datetime.datetime(int(year1), int(month1) , int(day1))   # date1
        d2 = datetime.datetime(int(year2), int(month2) , int(day2))   # date2
        print(d1, type(d1), d2)
        print(d1-d2)
        print(type(d1-d2))
        return abs((d1 - d2).days)


class Solution2:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        # solution two: manual calculation
        y1, m1, d1 = map(int, date1.split('-'))
        y2, m2, d2 = map(int, date2.split('-'))
        months = [0,31,28,31,30,31,30,31,31,30,31,30,31]
        
        # get days from 1971
        def getDays(y, m, d):
            ans = 0
            # calculate years
            for i in range(1971, y):
                #四年一闰；百年不闰，四百年再闰
                if (i % 4 == 0 and i % 100 != 0) or i % 400 == 0:  # leap year
                    ans += 366
                else:
                    ans += 365
            # calculate months
            for i in range(1, m):
                if i == 2:  # February
                    ans += 29 if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0 else 28
                else:
                    ans += months[i]
            return ans + d  # calculate days
        
        days1 = getDays(y1, m1, d1)
        days2 = getDays(y2, m2, d2)
        return abs(days1 - days2)



date1 = "2020-01-15"
date2 = "2019-12-31"

s = Solution()
print(s.daysBetweenDates(date1, date2))
