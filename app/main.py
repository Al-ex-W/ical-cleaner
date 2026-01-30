# app/main.py
import threading
import time
from pathlib import Path
from fastapi import FastAPI, Response
from app.updater import *

app = FastAPI()

CAL_PATH = Path("data/calendar.ics")

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

@app.get("/calendar.ics")
def get_calendar():
    if not CAL_PATH.exists():
        return Response(
            "BEGIN:VCALENDAR\nVERSION:2.0\nEND:VCALENDAR",
            media_type="text/calendar"
        )

    return Response(
        CAL_PATH.read_bytes(),
        media_type="text/calendar",
        headers={
            "Cache-Control": "public, max-age=600"
        }
    )
