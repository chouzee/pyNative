from datetime import datetime

given_date = datetime(2020, 2, 25)

new = datetime.strftime(given_date, "%A %d %B %Y")
print(new)
