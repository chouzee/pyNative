from datetime import datetime, timedelta

given_date = datetime(2020, 2, 25)
print("Given date", given_date)

subtract_days = 7
# timedelta calculates a difference betwwen 2 'times'
res_date = given_date - timedelta(days=subtract_days)
print("New date", res_date)
