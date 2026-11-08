# Week 1, Day 4 - input, type conversion and f-strings
# Run with: python3 week-01/day04_input.py

player_name = input("Player name: ")
price = float(input("Price (£m): "))
total_points = int(input("Total points: "))
matches_played = int(input("Matches played: "))

average_points = total_points / matches_played
points_per_million = total_points / price

print(f"{player_name}: {average_points:.2f} points per match")
print(f"{player_name}: {points_per_million:.2f} points per £m")
