def add_time(start_time, duration, opt_day="not"):
    week_days = ["saturday", "sunday", "monday", "tuesday", "wednesday", "thursday", "friday"]
    start = {
        "start_hour": int(start_time.split(":")[0]),
        "start_minutes": int(start_time.split(":")[1][0:2]),
        "time_zone": start_time.split(" ")[1]
    }
    dur = {
        "hour": int(duration.split(":")[0]),
        "minutes": int(duration.split(":")[1])
    }

    def calculate_time(start, dur):
        days = 0
        start_hour = start["start_hour"]
        end_hour = dur["hour"]
        zone = start["time_zone"]
        hour_time = start_hour + end_hour
        if hour_time / 12 > 1:
            for i in range((start_hour + end_hour) // 12):
                hour_time -= 12
                if zone == "AM":
                    zone = "PM"
                else:
                    days += 1
                    zone = "AM"
        start_minutes = start["start_minutes"]
        dur_minutes = dur["minutes"]
        minutes_time = start_minutes + dur_minutes
        if minutes_time / 60 > 1:
            for i in range((start_minutes + dur_minutes) // 60):
                minutes_time -= 60
                if hour_time == 11:
                    if zone == "AM":
                        zone = "PM"
                    else:
                        days += 1
                        zone = "AM"
                hour_time += 1

        return {
            "result_hour": str(hour_time),
            "result_minutes": str(f'{minutes_time:02}'),
            "days_passed": days,
            "zone": zone
        }

    result = calculate_time(start, dur)
    days_passed = ""
    if result["days_passed"] == 1:
        days_passed = " (next day)"
    elif result["days_passed"] > 1:
        days_passed = f" ({result['days_passed']} days later)"
    if not opt_day.lower() in week_days:
        print(f'{result["result_hour"]}:{result["result_minutes"]} {result["zone"]}{days_passed}')
    else:
        if week_days.index(opt_day.lower()) + result["days_passed"] + 1 > len(week_days):
            week_passed = week_days.index(opt_day.lower()) + result["days_passed"] + 1
            for i in range((week_days.index(opt_day.lower()) + result["days_passed"]) // len(week_days)):
                week_passed -= 6
            current_day = week_days[week_passed - 2]
        else:
            current_day = week_days[week_days.index(opt_day.lower()) + result["days_passed"]]
        print(f'{result["result_hour"]}:{result["result_minutes"]} {result["zone"]}, {current_day.title()}{days_passed}')


add_time("3:00 PM", "3:10")
# Returns: 6:10 PM

add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday

add_time("11:43 AM", "00:20")
# Returns: 12:03 PM

add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)

add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)

add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)