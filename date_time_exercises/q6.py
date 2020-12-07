from datetime import datetime, timedelta

# 2020-03-22 10:00:00
given_date = datetime(2020, 3, 22, 10, 0, 0)
print(given_date)

day_add = 7
hours_add = 12
day_addition = given_date + timedelta(days=day_add)
hours_addition = day_addition + timedelta(hours=hours_add)
print(hours_addition)
