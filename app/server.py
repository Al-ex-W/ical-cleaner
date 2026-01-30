from fastapi import FastAPI, Response
from pathlib import Path

app = FastAPI()
CAL_PATH = Path("data/calendar.ics")

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
            "Cache-Control": "public, max-age=3600"
        }
    )
