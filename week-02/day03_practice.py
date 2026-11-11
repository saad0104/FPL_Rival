    # Week 2, Day 3 — for loops, range, enumerate, accumulators
    # Practice snapshot, Gameweek 10 (fictional data, not official)

squad = [
        "Flekken", "Raya",
        "De Cuyper", "Alexander-Arnold", "Mykolenko", "Pedro Porro",
        "Saliba",
        "Palmer", "Salah", "Mbeumo", "Andreas",  "Saka",
        "Haaland", "Watkins", "Isak",
    ]

points = [
        28, 42,
        75, 68, 44, 55, 61,
        47, 89, 51, 38, 62,
        88, 56, 71,
    ]

positions = [
        "GK", "GK",
        "DEF", "DEF", "DEF", "DEF", "DEF",
        "MID", "MID", "MID", "MID", "MID",
        "FWD", "FWD", "FWD",
    ]

    # --- 1. Print the full squad with enumerate ---
print("=== My Squad ===")
for number, player in enumerate(squad, start=1):
        print(f"{number:>2}. {player}")

    # --- 2. Total and average points (accumulator) ---
total = 0
for score in points:
        total += score

average = total / len(points)
print(f"\nTotal points:   {total}")
print(f"Average points: {average:.1f}")

    # --- 3. Full squad table with position and points ---
print("\n=== Squad Points Table ===")
for i in range(len(squad)):
        print(f"{positions[i]:<4}  {squad[i]:<22}  {points[i]} pts")

    # --- 4. Find the top scorer ---
top_name = squad[0]
top_pts  = points[0]
for i in range(1, len(squad)):
    if points[i] > top_pts:
        top_pts  = points[i]
        top_name = squad[i]

print(f"\nTop scorer: {top_name} ({top_pts} pts)")