Calenfree

Are you a manager that needs to schedule an interview with a candidate and offer them multiple time slots? do you do that by manually looking at your calendar and copying each free timeslot?
this is an easier way to do that
just generate an ics file of your calendar and this script will look at the file and generate a list of free timeslots for you for the next week.

CURRENT STATE: only be able to look at one week ahead (5 working days)
INPUT: ics file path
OUTPUT: a text based list of available time slots with date, day
FORMAT: "I have the following time slots available:
    1.   MM-DD-YYYY HH:MM am/pm- HH:MM am/pm
    2.   MM-DD-YYYY HH:MM am/pm- HH:MM am/pm"


Filters:
1. Starting time (immediately? from tomorrow?)
2. how long to look for? (available times for a week? 3 days?)
3. length of the time slot (15mins? 30 mins?)
4. any buffer time before/after the meeting? (how long if so- 5mins?)
5. 


Future additions:
1. mutiple collaborators? (two calendars from two managers?)
2. support for multiple calendars (google, outlook etc)
3. easy to send email with available time slots? 