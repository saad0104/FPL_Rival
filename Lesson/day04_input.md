# Week 1 · Day 4 — Input, Type Conversion, f-strings

**Date:** 9 November 2026
**Week / Day:** Week 1, Day 4
**File:** `week-01/day04_input.py`
**Status:** ✅ Complete (one misconception corrected — see Practice A)

---

## Goal

Make the program ask for values instead of hard-coding them, convert the text
to numbers, and print the results neatly.

---

## Concepts

### `input()` always returns a string

```python
name = input("Player name: ")
```

- Shows the prompt, waits for Enter, returns what was typed **as text**.
- Typing `25` gives `"25"`, not `25`.

Proof:

```python
age = input("Age: ")
print(type(age))
```

If the user types `25`:

```
Age: <class 'str'>
```

So a number typed at `input()` must be converted before arithmetic.

### Conversion functions

| Function | Converts to | Example | Result |
|---|---|---|---|
| `int(...)` | whole number | `int("47")` | `47` |
| `float(...)` | decimal number | `float("9.8")` | `9.8` |
| `str(...)` | text | `str(47)` | `"47"` |

`int("4.7")` fails:

```
ValueError: invalid literal for int() with base 10: '4.7'
```

- `ValueError` = right type of input, wrong value/format.
- Use `float("4.7")`, or `int(float("4.7"))` to deliberately truncate to `4`.

### Why conversion matters

```python
print("9.8" * 2)   # 9.89.8 (text repeated)
print(9.8 * 2)     # 19.6   (number multiplied)
```

### f-strings

```python
print(f"{player_name}: {average_points:.2f} points per match")
```

- `f` before the quotes enables replacement fields.
- `{variable}` inserts the value.
- `:.2f` prints fixed-point with exactly two decimals (`4.70`, `10.00`).
- Text outside the braces prints normally.

---

## Demo

`week-01/day04_input.py`:

```python
player_name = input("Player name: ")
price = float(input("Price (£m): "))
total_points = int(input("Total points: "))
matches_played = int(input("Matches played: "))

average_points = total_points / matches_played
points_per_million = total_points / price

print(f"{player_name}: {average_points:.2f} points per match")
print(f"{player_name}: {points_per_million:.2f} points per £m")
```

Test run (answers piped in):

```
Cole Palmer: 4.70 points per match
Cole Palmer: 4.80 points per £m
```

The prompts normally appear one at a time; piping all answers at once makes them
look bunched.

---

## Practice answers

### A. Type returned by `input()`

**Question:** user types `25` at `age = input("Age: ")`. What is `type(age)`?

**Learner's answer:** `int` ❌
**Correct answer:** `str` ✅

`input()` *always* returns text. The displayed value looks like a number, but
its type is `str` until converted with `int(...)` or `float(...)`.

### B. Which line errors?

```python
print(int("7") + 3)      # 10
print(int("7.5"))        # ValueError
print(float("7.5") + 1)  # 8.5
print(f"{2/3:.2f}")      # 0.67
```

Only line 2 errors. `int()` refuses a decimal string; `float()` accepts it.

### C. Implementation

Input values:

```
Player name: David Raya
Price (£m): 6.00
Total points: 60
Matches played: 10
```

Output:

```
David Raya: 6.00 points per match
David Raya: 10.00 points per £m
```

Checks:

- `60 / 10` = `6.0` → `6.00` ✅
- `60 / 6.0` = `10.0` → `10.00` ✅
- f-string formatting correctly forced two decimals, fixing the Day 3
  "7.5 vs 7.50" issue.

---

## Key takeaways

1. `input()` returns a **string**, always.
2. Convert before calculating: `int()` for whole numbers, `float()` for decimals.
3. `ValueError` means the text could not be converted.
4. f-strings combine text and variables; `:.2f` controls decimals precisely.
5. Without conversion, `*` repeats text instead of multiplying.

## Common errors

| Error | Cause | Fix |
|---|---|---|
| `ValueError: invalid literal for int()` | Passing a decimal or letters to `int()` | Use `float()` or clean the input |
| `TypeError` on arithmetic | Using the raw `input()` string | Wrap in `int()`/`float()` |
| `"9.8" * 2` gives `9.89.8` | String repetition, not multiplication | Convert to `float` first |
| Output shows `4.7` not `4.70` | Using `round()` instead of a format spec | Use `f"{x:.2f}"` |

## Next

Day 5 — comparisons and Boolean logic: `==`, `!=`, `>`, `<`, `and`, `or`, `not`;
compare players' value.
