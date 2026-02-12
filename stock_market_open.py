import datetime
import chinese_calendar as calendar

today = datetime.date.today()

if calendar.is_holiday(today):
    exit(1)

exit(0)
