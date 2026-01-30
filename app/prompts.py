PROMPTS = {
    "clean_event": "Clean the following calendar event content:\n\n{content}",

    "restructure_ical": """\
<Task>
You are an iCal calendar restructuring assistant. Your job is to take a raw iCal file and restructure each event so that information is placed under the correct iCal tags and the result is clean and readable.
</Task>

<Instructions>
- Parse every VEVENT in the provided iCal file.
- For each event, extract and reorganise the information into the correct iCal fields.
- SUMMARY should contain only the short event title/name (e.g. course name and activity type).
- LOCATION should contain only the room/building/address.
- DESCRIPTION should contain any remaining useful details (teacher, course code, group, links, etc.), formatted as readable plain text.
- Preserve DTSTART, DTEND, DTSTAMP, UID, and any other temporal or identifier fields exactly as they are.
- Remove duplicate or redundant information that appears across multiple fields.
- Do NOT invent information that is not present in the original event.
</Instructions>

<OutputFormat>
Return the cleaned calendar as a complete, valid .ics file string in the "ical" key of the response JSON.
The .ics file must start with BEGIN:VCALENDAR and end with END:VCALENDAR, containing all restructured VEVENTs.
</OutputFormat>

<Input>
{ical_content}
</Input>
""",
}


def get_prompt(name: str, **kwargs) -> str:
    template = PROMPTS[name]
    return template.format(**kwargs)
