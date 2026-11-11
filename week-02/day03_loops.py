 # Week 2, Day 3 - loops and accumulators
# Practice snapshot, Gameweek 10 (not official/current data)

squad = ["Raya", "De Cuyper", "Palmer", "Haaland", "Mbuembo"]
points = [42, 75, 47, 88, 51]

print("Squad:")
for player in squad:
    print("-", player)

total = 0
for score in points:
    total += score

print(f"Total points: {total}")
print(f"Average points: {total / len(points):.2f}")

print("Players and points:")
for index in range(len(squad)):
    print(f"{index + 1}. {squad[index]}: {points[index]}")

best_player = squad[0]
best_points = points[0]
for index in range(1, len(squad)):
    if points[index] > best_points:
        best_points = points[index]
        best_player = squad[index]

print(f"Top scorer: {best_player} with {best_points} points")

print("Numbered with enumerate:")
for number, player in enumerate(squad, start=1):
    print(f"{number}. {player}")
