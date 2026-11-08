# Week 1, Day 3 - arithmetic and derived metrics
# Practice snapshot, Gameweek 10 (not official/current data)

player_name = "Cole Palmer"
price = 9.8          # in millions of pounds
total_points = 47
matches_played = 10

average_points = total_points / matches_played
points_per_million = total_points / price

print("Player:", player_name)
print("Average points per match:", round(average_points, 2))
print("Points per £m:", round(points_per_million, 2))
print("Rounded average:", round(average_points, 2))
print("Rounded points per £m:", round(points_per_million, 2))
