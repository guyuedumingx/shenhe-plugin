from datetime import datetime, timedelta

def create_ics_event(start, end, summary, description, location, alarm_minutes):
    """
    Creates a calendar event in ICS format with an alarm.
    """
    dt_format = '%Y%m%dT%H%M%S'
    event = [
        "BEGIN:VEVENT",
        f"DTSTART:{start.strftime(dt_format)}",
        f"DTEND:{end.strftime(dt_format)}",
        f"SUMMARY:{summary}",
        f"DESCRIPTION:{description}",
        f"LOCATION:{location}",
    ]

    if alarm_minutes:  # Add an alarm if alarm_minutes is provided
        alarm = [
            "BEGIN:VALARM",
            "TRIGGER:-PT{}M".format(alarm_minutes),
            "REPEAT:1",
            "DURATION:PT15M",
            "ACTION:DISPLAY",
            "DESCRIPTION:Reminder",
            "END:VALARM"
        ]
        event.extend(alarm)

    event.append("END:VEVENT")
    return '\n'.join(event)

def create_ics_calendar(events):
    """
    Wraps events in ICS calendar format.
    """
    calendar = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:-//Your Organisation//Your Product//EN",
        "CALSCALE:GREGORIAN",
        "METHOD:PUBLISH",
    ]
    calendar.extend(events)
    calendar.append("END:VCALENDAR")
    return '\n'.join(calendar)

# 设置事件属性
event_start = datetime.now()
event_end = event_start + timedelta(hours=1)
event_summary = "My New Event"
event_description = "This is a description of the event."
event_location = "My Location"
alarm_minutes = 40  # 设置提前10分钟提醒

# 创建事件
event_ics = create_ics_event(event_start, event_end, event_summary, event_description, event_location, alarm_minutes)

# 创建日历
calendar_ics = create_ics_calendar([event_ics])

# 写入到文件
ics_file_path = 'my_calendar.ics'
with open(ics_file_path, 'w') as my_file:
    my_file.write(calendar_ics)

print(f'ICS file created: {ics_file_path}')
