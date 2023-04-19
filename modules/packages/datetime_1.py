import datetime

def currTime():
    date_time = datetime.datetime.now()
    current_time = date_time.time()
    print(current_time)
    print(datetime.datetime(2023, 3, 10))
    td_object = datetime.timedelta(days=5, seconds=5, milliseconds=15)
    print(td_object) 