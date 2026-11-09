# Week 2, Day 1 - if / elif / else and a value classifier
# Practice thresholds are invented for learning, not FPL advice.

# player_name = "Maxim De Cuyper"
# price = 4.9
# total_points = 75
# matches_played = 10

player_name = input("Input Player Name: ")
price = float(input("Price: "))
total_points  = int(input("Points"))
match_played = int(input("Match Played: "))

points_per_million = total_points / price

if points_per_million >= 15:
    category = "excellent (practice threshold)"
elif points_per_million >= 10:
    category = "good (practice threshold)"
elif points_per_million >= 6:
    category = "average (practice threshold)"
else:
    category = "below average (practice threshold)"

print(f"{player_name}: {points_per_million:.2f} points per £m")
print(f"Practice category: {category}")
print("Reminder: these thresholds are invented for practice, not FPL advice.")
