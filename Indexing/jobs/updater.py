from datetime import datetime, timedelta
from apscheduler.schedulers.background import BackgroundScheduler
from App.insert import yahoo_history_data_insert
def insert():
    print('start')

def start():
    my_scheduler = BackgroundScheduler()
    my_scheduler.add_job(yahoo_history_data_insert,run_date = datetime.now()+timedelta(seconds=5))
    my_scheduler.start()