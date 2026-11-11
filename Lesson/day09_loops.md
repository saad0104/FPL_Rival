# Week 2 · Day 3 — Loops and Accumulators

**Date:** 11 November 2026
**Week / Day:** Week 2, Day 3 (session 9)
**File:** `week-02/day03_loops.py`
**Status:** ✅ Complete

---

## Goal

Process a 15-player squad without writing one line per player: total points,
average points, a formatted table, and the top scorer — all with loops.

---

## Concepts

### `for` loop — iterate over a list

```python
squad = ["Raya", "Palmer", "Haaland"]
for player in squad:
    print("-", player)
```

Each pass, `player` takes the next value. The indented block runs once per item.

### `range()` — a sequence of numbers

| Expression | Produces |
|---|---|
| `range(3)` | 0, 1, 2 |
| `range(1, 4)` | 1, 2, 3 |
| `range(2, 8, 2)` | 2, 4, 6 |

> **Important:** the stop value is always **excluded** — same rule as slicing.
> `range(3)` starts at **0**, not 1.

Use `range(len(squad))` to loop by index when you need to access two
parallel lists at once.

### Accumulator pattern

```python
points = [42, 75, 47, 88, 51]
total = 0
for score in points:
    total += score        # total = total + score
average = total / len(points)
```

Start at zero outside the loop; add inside; read the result after.

### `enumerate()` — index and item together

```python
for number, player in enumerate(squad, start=1):
    print(f"{number}. {player}")
```

Cleaner than `range(len(...))` when you only need a counter alongside items.

### f-string alignment

| Format | Effect |
|---|---|
| `{n:>2}` | right-align in 2-character field |
| `{s:<22}` | left-align in 22-character field |

Alignment keeps table columns tidy.

---

## Demo

`week-02/day03_loops.py` — 15-player GW10 practice squad:

```python
squad = [
    "Flekken", "Raya",
    "De Cuyper", "Alexander-Arnold", "Mykolenko", "Pedro Porro", "Saliba",
    "Palmer", "Salah", "Mbeumo", "Andreas",  "Saka",
    "Haaland", "Watkins", "Isak",
]
points = [28, 42, 75, 68, 44, 55, 61, 47, 89, 51, 38, 62, 88, 56, 71]
positions = ["GK","GK","DEF","DEF","DEF","DEF","DEF",
             "MID","MID","MID","MID","MID","FWD","FWD","FWD"]
```

Four sections:
1. Numbered squad list with `enumerate`
2. Total and average points with an accumulator
3. Full position/name/points table with `range(len(...))`
4. Top scorer found by looping and comparing

---

## Practice answers

### P1 — `range(3)` starts at 0
```python
for i in range(3):
    print(i * 2)
# prints: 0, 2, 4   (not 2, 4, 5)
```
Mistake: forgot range starts at 0 and miscalculated the last value.

### P2 — Accumulator ✅
```python
nums = [10, 20, 30]
total = 0
for n in nums:
    total += n
# total = 60   ✅ correct
```

### P3 — `enumerate` visits every item, including index 0
```python
words = ["GK", "DEF", "MID", "FWD"]
for i, w in enumerate(words, start=1):
    print(f"{i}: {w}")
# 1: GK  2: DEF  3: MID  4: FWD
```
Mistake: skipped "GK" (thought `start=1` skips the first list item;
it only changes the counter label).

### P4 — `range` stop is exclusive
```python
list(range(2, 8, 2))  # [2, 4, 6]  (8 excluded)
```
Mistake: included 8. Same exclusive-stop rule as slicing.

**Score: 1/4 — all errors share the same theme: `range`/sequences are
exclusive at the top and start at 0 by default.**

---

## Implementation

Full 15-player squad output:

```
=== My Squad ===
 1. Flekken
 2. Raya
 3. De Cuyper
 4. Alexander-Arnold
 5. Mykolenko
 6. Pedro Porro
 7. Saliba
 8. Palmer
 9. Salah
10. Mbeumo
11. Andreas
12. Saka
13. Haaland
14. Watkins
15. Isak

Total points:   775
Average points: 51.7

=== Squad Points Table ===
GK    Flekken                 28 pts
GK    Raya                    42 pts
DEF   De Cuyper               75 pts
DEF   Alexander-Arnold        68 pts
DEF   Mykolenko               44 pts
DEF   Pedro Porro             55 pts
DEF   Saliba                  61 pts
MID   Palmer                  47 pts
MID   Salah                   89 pts
MID   Mbeumo                  51 pts
MID   Andreas                 38 pts
MID   Saka                    62 pts
FWD   Haaland                 88 pts
FWD   Watkins                 56 pts
FWD   Isak                    71 pts

Top scorer: Salah (89 pts)
```

---

## Key takeaways

1. `for player in squad` visits every item — no index needed.
2. `range(n)` → 0 to n−1; `range(a, b)` → a to b−1; stop is always **excluded**.
3. Accumulator: initialise to 0 before the loop, add inside, read after.
4. `enumerate(seq, start=1)` gives a counter + item without `range(len(...))`.
5. Three parallel lists drift apart if you forget to update all three — Day 4
   fixes this with dictionaries.

## Common errors

| Error | Cause | Fix |
|---|---|---|
| Wrong count from `range` | Forgot stop is exclusive | Use `range(1, n+1)` to include n |
| `IndexError` in top-scorer loop | Started at index 0 and missed initialising | Seed with index 0, loop from 1 |
| Columns misaligned | No format spec | Use `:<n` / `:>n` in f-strings |

## Next

Week 2, Day 4 — Dictionaries: store all player data in one bundle so
parallel lists can't drift.
