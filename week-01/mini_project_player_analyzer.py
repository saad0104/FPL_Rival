name_a = (input("Input Player A: "))
club_a = (input("Input Club Player A: "))
price_a = float(input("Input prize: "))
pts_a = int(input("Total points: "))
match_a = int(input("Total Match played: "))

ppm_a = pts_a / match_a
ppmil_a = pts_a / price_a

name_b = (input("Input Player B: "))
club_b = (input("Input Club Player B: "))
price_b = float(input("Input prize: "))
pts_b = int(input("Total points: "))
match_b = int(input("Total Match played: "))

ppm_b = pts_b / match_b
ppmil_b = pts_b / price_b


print("Player 1: ")
print(f"Player Name: {name_a}")
print(f"Club : {club_a}")
print(f"Price : ${price_a}m")
print(f"Points per match : {ppm_a:.2f}")
print(f"Points per million : {ppmil_a:.2f}")

print("Player 2: ")
print(f"Player Name: {name_b}")
print(f"Club : {club_b}")
print(f"Price : ${price_b}m")
print(f"Points per match : {ppm_b:.2f}")
print(f"Points per million : {ppmil_b:.2f}")


print("Player A has higher points per match: ", ppm_a>ppm_b)
print("Player A has higher points per million: ", ppmil_a>ppmil_b)
print("Player A is cheaper: ", price_a<price_b)
print("Both under 10 million:", price_a< 10 and price_b<10)