moon_phases = [
    "New Moon",        # 1
    "Waxing Crescent", # 2
    "First Quarter",   # 3
    "Waxing Gibbous",  # 4
    "Full Moon",       # 5
    "Waning Gibbous",  # 6
    "Last Quarter",    # 7
    "Waning Crescent"  # 8
]
print("Moon Phases:")
for i, phase in enumerate(moon_phases):
    print(f"{i+1}. {phase}")
current_phase = int(input("Enter today's moon phase (1=New Moon, 8=Waning Crescent): "))
if current_phase < 1 or current_phase > 8:
    print("Invalid input! Please enter a number between 1 and 8.")
    exit()
days_later = int(input("How many days later do you want to check?: "))
phase_length = 29.53 / 8
phases_passed = int(days_later / phase_length)
future_phase_index = (current_phase - 1 + phases_passed) % 8
print(f"{days_later} days later, the moon phase will be: {moon_phases[future_phase_index]}")
