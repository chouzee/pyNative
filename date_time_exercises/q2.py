from datetime import datetime

date_string = "Feb 25 2020 4:20PM"
date_obj = datetime.strptime(date_string, "%b %d %Y %I:%M%p")
