from datetime import datetime

datetime_now = datetime.now()
current_time = datetime_now.strftime("%H:%M:%S")
print(current_time)
