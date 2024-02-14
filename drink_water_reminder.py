'''
Created on Jan 27, 2024

@author: Abk
'''
from datetime import datetime
import time
from plyer import notification

import win32com.client


print("Drink water reminder")

speaker = win32com.client.Dispatch("SAPI.SpVoice")

now = datetime.now()

time_string = now.strftime("%I:%M:%S %p")
date_string  = now.strftime("%d-%b-%y")

print(time_string)
print(date_string)

def drink_water():
    message = "Drink your water now!"
    now = datetime.now()
    time_string = now.strftime("%I:%M:%S %p" )
    print(time_string)
    speaker.speak(message)

def notify_me():
    notification.notify(
    title="Drink water Reminder",
    message="Drink you water!",
    app_name="Notication app",
    timeout=5  # Optional timeout in seconds
)

def reminder():
    interval = 4 #seconds
    while True:
        notify_me()
        drink_water()
        time.sleep(interval)
    
# reminder()
