import requests
from pathlib import Path

TIMEEDIT_URL = "https://cloud.timeedit.net/chalmers/web/student/ri6YQ3yZ5855ZdQ5Q6Qun538Z35050t114mXeZ95b75ZnQ36jo5Q70C40CtF8k92n5A8857137o3nBQo133D7Z0F2804l050A6002F0FB.ics"
OUT = Path("data/calendar.ics")

def update_calendar():
    resp = requests.get(TIMEEDIT_URL, timeout=10)
    resp.encoding = "latin-1"
    raw_ics = resp.text

    # v1: just store it verbatim
    # v2: parse + clean + LLM
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(raw_ics, encoding="utf-8")

if __name__ == "__main__":
    update_calendar()
