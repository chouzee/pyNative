from datetime import datetime

given_date = datetime(2020, 7, 26)

day = datetime.strftime(given_date, "%A")
print(day)
