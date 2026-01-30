import os
import requests
from pathlib import Path

from app.llm import LLM
from app.prompts import get_prompt

TIMEEDIT_URL = "https://cloud.timeedit.net/chalmers/web/student/ri6YQ3yZ5855ZdQ5Q6Qun538Z35050t114mXeZ95b75ZnQ36jo5Q70C40CtF8k92n5A8857137o3nBQo133D7Z0F2804l050A6002F0FB.ics"
OUT = Path("data/calendar.ics")

def update_calendar():
    print("[updater] Fetching calendar from TimeEdit...")
    resp = requests.get(TIMEEDIT_URL, timeout=10)
    resp.encoding = "latin-1"
    raw_ics = resp.text
    print(f"[updater] Fetched {len(raw_ics)} chars from TimeEdit")

    print("[updater] Sending to LLM...")
    llm = LLM(model="gpt-5.2", api_key=os.environ["OPENAI_API_KEY"])
    prompt = get_prompt("restructure_ical", ical_content=raw_ics)
    result = llm.request(prompt)
    print(f"[updater] LLM response ({len(result.ical)} chars): {result.ical[:200]}...")

    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(result.ical, encoding="utf-8")
    print(f"[updater] Wrote calendar to {OUT}")

if __name__ == "__main__":
    update_calendar()
