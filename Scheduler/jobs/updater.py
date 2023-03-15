from datetime import datetime, timedelta
from apscheduler.schedulers.background import BackgroundScheduler
import time
import pytz
def randomFunction():
    print('hello from before')
    time.sleep(30)
    print('hello from after')
def call_ticker_and_data():
    print('ticker')
def start():
    my_scheduler = BackgroundScheduler()
    my_scheduler.add_job(call_ticker_and_data,run_date = datetime.now()+timedelta(seconds=15))
    my_scheduler.add_job(randomFunction, 'interval', seconds=50)
    my_scheduler.start()