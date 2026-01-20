from icalendar import Calendar
from datetime import datetime, timedelta, time
from dateutil.rrule import rrulestr


def workweek():
    today = datetime.now()
    if today.weekday() == 5:
        week_start = today + timedelta(days=2)
    elif today.weekday() == 6:
        week_start = today + timedelta(days=1)
    else:
        week_start = today
    
    week_start = week_start.replace(hour=0, minute=0, second=0, microsecond=0)
    week_end = week_start + timedelta(days=4)
    print(f"Workweek: {week_start.date()} to {week_end.date()}")
    return week_start, week_end, time(9, 0), time(17, 0)


def extract_ics_data(file_path, week_start, week_end):
    busy_times = []
    with open(file_path, 'rb') as f:
        calendar = Calendar.from_ical(f.read())
        for component in calendar.walk():
            if component.name == "VEVENT":
                dtstart = component.get('dtstart').dt
                dtend = component.get('dtend').dt
                rrule = component.get('rrule')
                
                if hasattr(dtstart, 'tzinfo') and dtstart.tzinfo:
                    dtstart = dtstart.replace(tzinfo=None)
                    dtend = dtend.replace(tzinfo=None)
                
                if rrule:
                    rule = rrulestr(str(rrule.to_ical(), 'utf-8'), dtstart=dtstart)
                    for ev_start in rule.between(week_start, week_end + timedelta(days=1), inc=True):
                        ev_end = ev_start + (dtend - dtstart)
                        busy_times.append((ev_start, ev_end))
                elif isinstance(dtstart, datetime) and isinstance(dtend, datetime):
                    if week_start <= dtstart <= week_end:
                        busy_times.append((dtstart, dtend))
    
    return busy_times


def find_free_times(busy_times, week_start, week_end, workhour_start, workhour_end):
    free_times = []
    busy_times = sorted(busy_times, key=lambda x: x[0])
    
    for day in range(5):
        day_start = datetime.combine((week_start + timedelta(days=day)).date(), workhour_start)
        day_end = datetime.combine((week_start + timedelta(days=day)).date(), workhour_end)
        day_busy = []
        
        for b_start, b_end in busy_times:
            if b_start.date() == day_start.date():
                b_start = max(b_start, day_start)
                b_end = min(b_end, day_end)
                day_busy.append((b_start, b_end))
        
        merged = []
        for b in sorted(day_busy):
            if not merged or b[0] > merged[-1][1]:
                merged.append(list(b))
            else:
                merged[-1][1] = max(merged[-1][1], b[1])
        
        prev_end = day_start
        for b in merged:
            if b[0] > prev_end:
                free_start = max(prev_end, day_start)
                free_end = min(b[0], day_end)
                if free_start < free_end:
                    free_times.append((free_start, free_end))
            prev_end = max(prev_end, b[1])
        
        if prev_end < day_end:
            free_start = max(prev_end, day_start)
            free_end = min(day_end, day_end)
            if free_start < free_end:
                free_times.append((free_start, free_end))
    
    print("Free times:")
    for start, end in free_times:
        print(f"{start.strftime('%A %-m-%d-%Y %I:%M %p')} - {end.strftime('%I:%M %p')}")


ics_path = input("Enter ics file path: ")
week_start, week_end, workhour_start, workhour_end = workweek()
unavailable_times = extract_ics_data(ics_path, week_start, week_end)
find_free_times(unavailable_times, week_start, week_end, workhour_start, workhour_end)