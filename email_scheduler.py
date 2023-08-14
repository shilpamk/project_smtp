import schedule
import time
from main import *


def job():
    send_email()

schedule.every().day.at("10:30").do(job)

while True:
   schedule.run_pending()
   time.sleep(1)
   