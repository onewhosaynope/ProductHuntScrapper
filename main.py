from scrapper_bot import scrap
import schedule
import time

print("started")
schedule.every().day.at("13:00").do(scrap)

while True:
    schedule.run_pending()
    time.sleep(60) # wait one minute