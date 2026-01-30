# app/main.py
import threading
import time
from fastapi import FastAPI
from updater import *

app = FastAPI()

def updater_loop():
    while True:
        try:
            update_calendar()   # fetch TimeEdit + clean + write file
        except Exception as e:
            print("Updater error:", e)
        time.sleep(3600)  # every hour

@app.on_event("startup")
def start_updater():
    t = threading.Thread(target=updater_loop, daemon=True)
    t.start()
