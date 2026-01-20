# Calenfree

## Overview
Tired of manually checking your calendar to find free time slots for meetings? **Calenfree** automatically extracts your available time from a calendar file and displays them in a clean, easy-to-share format.

## What Does It Do?
- Takes your calendar file (ICS format) as input
- Scans your schedule for the current work week (Monday-Friday, 9 AM - 5 PM)
- Finds all free time slots between your meetings
- Displays results with day of week, date, and time

## How to Use
1. Export your calendar as an ICS file (most calendar apps support this)
2. Run the script: `python3 parser.py`
3. Enter the path to your ICS file when prompted
4. Get a list of all available time slots for the week

## Current Features
- Scans 5 working days ahead
- Works with timezone-aware calendar events
- Handles recurring events
- Shows availability during work hours only (9 AM - 5 PM)
- Displays day name with each time slot

## Planned Features
- [ ] Customize work hours
- [ ] Set minimum time slot duration
- [ ] Add buffer time before/after meetings
- [ ] Support multiple calendars
- [ ] Integration with Google Calendar and Outlook
- [ ] Email sharing of available slots 