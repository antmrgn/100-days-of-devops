import time
import datetime 

#from datetime import date

#from datetime import datetime

gigasecond = 1000000000
def add(moment):
    unix = time.mktime(moment.timetuple())
    res = int(unix + gigasecond)
    return datetime.datetime.fromtimestamp(res)

#moment = (2011, 4, 25, 0, 0)
#moment = datetime.datetime(2011, 4, 25, 0, 0)
#moment = datetime.datetime(2011, 4, 25, 0, 0).timestamp()
#unix = time.mktime(moment.timetuple())
#print(unix)
#res = int(unix + gigasecond)
#print(res)

#from datetime import datetime
#nice = datetime.utcfromtimestamp(res)
#nice = datetime.datetime.fromtimestamp(res)
#nice = time.mktime(res.timetuple())
#print(nice)

#(dt).total_seconds()

#today = date.today()
#print(today)

#print(add((2011, 4, 25, 0, 0)))