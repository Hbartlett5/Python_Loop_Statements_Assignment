# Question 1: The Range Riddle

# Task 1: Your Mood Today

import random

moods = ["Happy", "Sad", "Energetic", "Calm"]

week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

for days in range(len(week)):
    todays_mood = random.choice(moods)
    print(f"On {week[days]}, you were feeling {todays_mood}.")