from datetime import datetime

datetime_now = datetime.now()
millisec_time = datetime_now.strftime("%s")
print(millisec_time)
