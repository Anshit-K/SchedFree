from icalendar import Calendar, Event, vCalAddress, vText
from datetime import datetime, timedelta, time
import pathlib




def workweek():

    workhour_start=time(9,0)
    workhour_end = time(17,0)
    datetime_min=datetime.now()
    datetime_max=0
    weekday_start = datetime.now().weekday

    if datetime.now().weekday == 5:     #if it's a saturday
        daytime_min = datetime.now() + timedelta(days=2)
        weekday_start = weekday_start+2
    if datetime.now().weekday == 6:      #if it's a sunday
        daytime_min = datetime.now() + timedelta(days=1)
        weekday_start = weekday_start +1 

    datetime_max = datetime_min
    weekday_end = weekday_start + 4

    if datetime.now().weekday == 5:     #to skip over if it's a saturday
        weekday_end = weekday_end +2

    if datetime.now().weekday == 6:     #to skip over if it's a sunday
        weekday_end = weekday_end +1

    
    datetime_max = datetime_max + timedelta(days=weekday_end)
    
    
    print(f"datetime_min: {datetime_min}")




workweek()
#print(f"end time: {workhour_end}")
def extract_ics_data(file_path):
    busy_times=[]
    with open(file_path, 'rb') as f:
        calendar = Calendar.from_ical(f.read())

        for component in calendar.walk():
            if component.name=="VEVENT":
                busy_start_time = component.get('dtstart').dt
                busy_end_time = component.get('dtend').dt

                busy_times.append(f"{busy_start_time.strftime('%-m-%d-%Y %I:%M %p')} - {busy_end_time.strftime('%I:%M %p')}")
        ##duration= busy_end_time- busy_start_time
       ## print(f"start time: {busy_times}; Duration: {duration}"
    return busy_times

unavailable_times = extract_ics_data(input("Enter ics file path: "))



def find_free_times(busy_times):
    free_times=[]
    free_start_time=0
    free_end_time=0
    for start,end in busy_times:
        free_times.append(f"{free_start_time.strftime('%-m-%d-%Y %I:%M %p')} - {free_end_time.strftime('%I:%M %p')}")

    
        if (end-start) >30:
            free_start_time=end
            
        free_end_time=start
    print(f"free time: {free_times}")

find_free_times(unavailable_times)
























                                                                                                                                                                                                                      