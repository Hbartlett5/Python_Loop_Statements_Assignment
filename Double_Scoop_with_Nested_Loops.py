# Question 2: Double Scoop with Nested Loops

# Task 1: Your Mood Tracker

import random

moods = ["Happy", "Sad", "Energetic", "Calm"]

week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

time_of_day = ["Morning", "Afternoon", "Evening"]

for days in week:
    for time in time_of_day:
        mood = random.choice(moods)
        print(f"On {days} {time}, you were feeling {mood}.")