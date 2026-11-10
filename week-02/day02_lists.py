# Week 2, Day 2 - lists: one variable holds a whole squad

squad = ["Raya", "De Cuyper", "Palmer", "Haaland", "Mbuembo"]

print("Squad:", squad)
print("First player:", squad[0])
print("Last player:", squad[-1])
print("Number of players:", len(squad))
print("Palmer in squad:", "Palmer" in squad)
print("First three:", squad[:3])

squad.append("Saka")
print("After adding Saka:", squad)
print("Count now:", len(squad))

squad.remove("Raya")
print("After removing Raya:", squad)
print("Count now:", len(squad))
print("Player at index 1:", squad[1])


squad.append(input("Enter a player: "))
print(squad)
print(len(squad))


rmv_player = input("Which player to remove? ")

if rmv_player in squad:
    squad.remove(rmv_player)
    print(f"{rmv_player} is removed from the squad.")
else:
    print(f"{rmv_player} is not in the squad")


    
print("Palmer" in squad)

print(squad[:3])

