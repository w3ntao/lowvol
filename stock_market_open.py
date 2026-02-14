import datetime
import chinese_calendar

today = datetime.date.today()

if chinese_calendar.is_holiday(today) or today.weekday() >= 5:
    # weekday: 0 - 6: Mon - Sun
    exit(1)

exit(0)
