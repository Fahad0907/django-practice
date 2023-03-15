from datetime import datetime

from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import schedule_api

def start():
    sch = BackgroundScheduler()
    #sch.add_job(schedule_api,'corn',['now ok'],seconds=5)
    sch.add_job(schedule_api, 'cron',['now ok'], second='*/5', day=datetime.utcnow().day)
    sch.start()