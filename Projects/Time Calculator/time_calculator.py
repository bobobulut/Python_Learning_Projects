def add_time(start_time, duration, starting_day=None):
    # Parse start time
    start_time_parts = start_time.split()
    start_hour, start_minute = map(int, start_time_parts[0].split(':'))
    am_pm = start_time_parts[1].upper()

    # Parse duration
    duration_hour, duration_minute = map(int, duration.split(':'))

    # Convert start time to 24-hour clock
    if am_pm == 'PM':
        start_hour += 12

    # Calculate the total number of minutes
    total_minutes = start_hour * 60 + start_minute + duration_hour * 60 + duration_minute

    # Calculate the new hour and minute
    new_hour = total_minutes // 60 % 24
    new_minute = total_minutes % 60

    # Determine if it's AM or PM
    if new_hour < 12:
        new_am_pm = 'AM'
    else:
        new_am_pm = 'PM'
        if new_hour >= 13:
            new_hour -= 12

    # Format the new time
    new_time = f"{new_hour}:{new_minute:02d} {new_am_pm}"

    # Calculate the number of days later
    days_later = total_minutes // (24 * 60)

    # Determine the new day of the week if starting day is provided
    if starting_day:
        starting_day = starting_day.capitalize()
        days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        starting_index = days_of_week.index(starting_day)
        new_day_index = (starting_index + days_later) % 7
        new_day = days_of_week[new_day_index]
        new_time += f", {new_day}"

    # Add "(next day)" or "(n days later)" if necessary
    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 1:
        new_time += f" ({days_later} days later)"

    return new_time
