# Week 2 · Day 1 — if / elif / else and a Value Classifier

**Date:** 9 November 2026
**Week / Day:** Week 2, Day 1 (session 7)
**File:** `week-02/day01_conditions.py`
**Status:** ✅ Complete

---

## Goal

Let the program choose between outcomes instead of always doing the same thing.

---

## Concepts

### The shape

```python
if condition:
    # runs only when condition is True
elif another_condition:
    # runs only when the first was False and this one is True
else:
    # runs when none of the above were True
```

Rules:

1. The condition is a Boolean expression: `ppm > 10`, `available`,
   `price < 8 and points > 50`.
2. The line ends with a colon `:`.
3. The block is indented (4 spaces). Indentation is syntax.
4. Python checks top to bottom and runs **only the first true branch**.

Missing indentation gives:

```
IndentationError: expected an indented block after 'if' statement on line 2
```

### Order matters

```python
ppm = 15.31

if ppm >= 6:
    print("average")
elif ppm >= 15:
    print("excellent")
```

This prints `average`, because `15.31 >= 6` is true and Python stops checking.
Put the strictest / highest threshold first.

### Truthiness

```python
if "Haaland":   # non-empty string → True
if "":          # empty string     → False
if 0:           # zero             → False
if available:   # Boolean value used directly
```

Prefer explicit comparisons when the meaning is not obvious.

---

## Demo

`week-02/day01_conditions.py` classifies a player's points per £m into
clearly labelled **practice** bands.

Output for Maxim De Cuyper:

```
Maxim De Cuyper: 15.31 points per £m
Practice category: excellent (practice threshold)
Reminder: these thresholds are invented for practice, not FPL advice.
```

The thresholds are invented for learning, not FPL advice, and the program says
so in its output.

---

## Practice answers

### A. Score classifier

```python
score = 7
if score > 10:
    print("big")
elif score > 5:
    print("medium")
else:
    print("small")
```

**Answer:** `medium`. `7 > 10` is false; `7 > 5` is true.

### B. Order bug

```python
ppm = 15.31
if ppm >= 6:
    print("average")
elif ppm >= 15:
    print("excellent")
```

**Answer:** `average`. The first condition is already true, so the `elif` is
never checked. Fix by putting `ppm >= 15` first.

### C. Truthiness

```python
price = 0
if price:
    print("has a price")
else:
    print("free?")
```

**Answer:** `free?`. Zero is falsy, so the `else` branch runs.

> These answers were not submitted before closing; they are recorded here for
> review and should be checked in the Day 6 review session.

---

## Implementation

Learner's program now takes input:

```python
player_name = input("Input Player Name: ")
price = float(input("Price: "))
total_points = int(input("Points"))
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
```

### Test 1 — De Cuyper

```
Maxim De Cuyper: 15.31 points per £m
Practice category: excellent (practice threshold)
```

### Test 2 — Palmer

```
Cole Palmer: 4.80 points per £m
Practice category: below average (practice threshold)
```

Both correct: 15.31 ≥ 15 and 4.80 < 6.

### Polish

- Prompt `"Points"` should be `"Points: "` for consistency.
- `total_points  =` has a double space.
- The commented-out demo values at the top can be deleted once the input
  version works.
- `input()` values are converted with `float()` / `int()` correctly.

---

## Key takeaways

1. `if` / `elif` / `else` runs only the first true branch.
2. Colons and indentation are mandatory.
3. Order conditions from most specific to least specific.
4. Truthiness exists, but explicit comparisons are clearer.
5. Always label invented thresholds as practice data.

## Common errors

| Error | Cause | Fix |
|---|---|---|
| `IndentationError` | Missing indented block | Indent 4 spaces after `:` |
| `SyntaxError` | Missing colon | Add `:` at the end of the condition |
| Wrong category | Broad condition placed first | Reorder the branches |
| `ValueError` | Comparing text to a number | Convert input first |

## Next

Week 2, Day 2 — lists: a squad as a collection of players.
