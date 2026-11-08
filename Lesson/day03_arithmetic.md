# Week 1 · Day 3 — Arithmetic and Derived Metrics

**Date:** 9 November 2026
**Week / Day:** Week 1, Day 3
**File:** `week-01/day03_calculator.py`
**Status:** ✅ Complete (optional floor-division line not added)

---

## Goal

Use Python as a calculator, then turn raw player numbers into useful FPL
metrics.

---

## Concepts

### Arithmetic operators

| Operator | Name | Example | Result |
|---|---|---|---|
| `+` | add | `75 + 10` | `85` |
| `-` | subtract | `75 - 10` | `65` |
| `*` | multiply | `75 * 2` | `150` |
| `/` | divide (decimal) | `10 / 4` | `2.5` |
| `//` | floor divide | `10 // 4` | `2` |
| `%` | remainder | `10 % 4` | `2` |
| `**` | power | `2 ** 3` | `8` |

`75 // 10` = `7` (complete matches) and `75 % 10` = `5` (points left over).

### Order of operations

1. Parentheses `( )`
2. Powers `**`
3. `*`, `/`, `//`, `%` (left to right)
4. `+`, `-` (left to right)

```python
print(2 + 3 * 4)      # 14
print((2 + 3) * 4)    # 20
```

When unsure, add parentheses.

### Derived FPL metrics

```python
average_points = total_points / matches_played
points_per_million = total_points / price
```

- **Points per match:** productivity per appearance.
- **Points per £m:** output per million spent.

Both are comparison tools, not predictions. A cheap player can rank highly on
points per £m simply because they cost little.

---

## Demo

`week-01/day03_calculator.py` (before the learner's edit):

```python
player_name = "Maxim De Cuyper"
price = 4.9
total_points = 75
matches_played = 10

average_points = total_points / matches_played
points_per_million = total_points / price

print("Player:", player_name)
print("Average points per match:", average_points)
print("Points per £m:", points_per_million)
print("Rounded average:", round(average_points, 2))
print("Rounded points per £m:", round(points_per_million, 2))
```

Output:

```
Player: Maxim De Cuyper
Average points per match: 7.5
Points per £m: 15.306122448979592
Rounded average: 7.5
Rounded points per £m: 15.31
```

`round(value, 2)` keeps two decimals, but `round(7.5, 2)` still prints `7.5`.
Trailing zeros need f-strings (Day 4).

---

## Practice answers

### A. Predictions

```python
print(10 + 2 * 3)    # 16
print((10 + 2) * 3)  # 36
print(10 / 4)        # 2.5
print(10 // 4)       # 2
print(10 % 4)        # 2
```

All correct.

### B. Hand calculation

63 points, 9 matches, £7.5m:

- Points per match = `63 / 9` = **7.0**
- Points per £m = `63 / 7.5` = **8.4**

The formulas were correct; the arithmetic needed finishing.

---

## Implementation

Learner's program using Cole Palmer (47 points, £9.8m, 10 matches):

```python
player_name = "Cole Palmer"
price = 9.8
total_points = 47
matches_played = 10

average_points = total_points / matches_played
points_per_million = total_points / price

print("Player:", player_name)
print("Average points per match:", round(average_points, 2))
print("Points per £m:", round(points_per_million, 2))
print("Rounded average:", round(average_points, 2))
print("Rounded points per £m:", round(points_per_million, 2))
```

Output:

```
Player: Cole Palmer
Average points per match: 4.7
Points per £m: 4.8
Rounded average: 4.7
Rounded points per £m: 4.8
```

Checks:

- `47 / 10` = `4.7` ✅
- `47 / 9.8` = `4.7959...` → `4.8` ✅
- Lines 3–4 and 5–6 print the same rounded values twice; the last two lines are
  redundant.
- The optional `total_points // matches_played` line was not added.

---

## Key takeaways

1. `/` gives decimals; `//` and `%` give whole-number results.
2. Parentheses override the normal order.
3. Derived metrics are just arithmetic on stored variables.
4. `round(x, 2)` controls decimals but does not force trailing zeros.

## Common errors

| Error | Cause | Fix |
|---|---|---|
| `ZeroDivisionError` | Dividing by `matches_played = 0` | Check the value; handle it in Week 3 |
| Wrong metric | Missing parentheses or using `//` when `/` is needed | Re-check the formula |
| `TypeError` | Mixing a string with a number | Convert the text first (Day 4) |

## Next

Day 4 — `input()`, type conversion, `ValueError`, and f-strings.
