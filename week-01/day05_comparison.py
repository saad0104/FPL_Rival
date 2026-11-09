# Week 1, Day 5 - comparisons and Boolean logic
# Practice snapshot, Gameweek 10 (not official/current data)

player_a = "Cole Palmer"
price_a = 9.8
points_a = 47
available_a = True
ppm_a = points_a/price_a         # points per million


player_b = "Maxim De Cuyper"
price_b = 4.9
points_b = 75
available_b = True
ppm_b = points_b / price_b      # points per million



print(f"{player_a} vs {player_b}")
print("A has better points per £m:", ppm_a > ppm_b)
print("B is cheaper:", price_b < price_a)
print("Both cost under £10m:", price_a < 10 and price_b < 10)
print("Either is above 10 points per £m:", ppm_a > 10 or ppm_b > 10)
print("They cost the same:", price_a == price_b)
print("They cost different amounts:", price_a != price_b)

print("A can be afforded and is above 4 ppm:", price_a < 10 and ppm_a > 4)
print("Not both conditions:", not (price_a < 10 and ppm_a > 4))
print("Both available: ", available_a and available_b)
print("Is Palmer injured:", not available_a)