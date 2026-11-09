# Week 1 · Day 6 — Review + FPL Player Analyzer v1

**Date:** 9 November 2026
**Week / Day:** Week 1, Day 6
**File:** `week-01/mini_project_player_analyzer.py`
**Status:** ✅ Complete — Week 1 finished

---

## Goal

Check Week 1 understanding, then assemble everything into a small,
working command-line program.

---

## Review quiz — 5/6 ✅

| Q | Result | Feedback |
|---|---|---|
| 1 | ✅ | `"10 + 5"` prints text; `10 + 5` prints `15` |
| 2 | ✅ | `"47"` str, `47` int, `4.7` float, `False` bool |
| 3 | ✅ | `17 // 5` = 3, `17 % 5` = 2 |
| 4 | ✅ | `int("4.5")` fails: decimal text is not a whole number. `float("4.5")` keeps `4.5`; `int(float("4.5"))` truncates to `4` |
| 5 | ✅ | Fix: `age = int(input("Age: "))` — conversion happens before arithmetic |
| 6 | ❌ half | `f"{2/3:.2f}"` is **0.67** (rounds up); `not (3 > 2 and 5 == 5)` is `False` ✅ |

Only miss: `.2f` **rounds**, it does not truncate.

---

## Mini-project requirements (met)

1. Ask for two players: name, club, price, points, matches.
2. Convert numeric input with `float()` / `int()`.
3. Calculate points per match and points per £m.
4. Print a formatted report with `:.2f`.
5. Print comparisons with Booleans (no `if`).
6. Run correctly with real input.

---

## Final code

```python
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

print("Player A has higher points per match: ", ppm_a > ppm_b)
print("Player A has higher points per million: ", ppmil_a > ppmil_b)
print("Player A is cheaper: ", price_a < price_b)
print("Both under 10 million:", price_a < 10 and price_b < 10)
```

## Output

Input: Enzo (ManCity, 7.5, 35 pts, 10 matches) and Mbuembo (ManUtd, 7, 56 pts,
10 matches).

```
Player 1:
Player Name: Enzo
Club : ManCity
Price : $7.5m
Points per match : 3.50
Points per million : 4.67

Player 2:
Player Name: Mbuembo
Club : ManUtd
Price : $7.0m
Points per match : 5.60
Points per million : 8.00

Player A has higher points per match:  False
Player A has higher points per million:  False
Player A is cheaper:  False
Both under 10 million: True
```

## Verification

- Enzo: 35 / 10 = **3.50**; 35 / 7.5 = 4.666… → **4.67** ✅
- Mbuembo: 56 / 10 = **5.60**; 56 / 7 = **8.00** ✅
- Higher per match: 3.50 > 5.60 → False ✅
- Higher per £m: 4.67 > 8.00 → False ✅
- Cheaper: 7.5 < 7.0 → False ✅
- Both under £10m → True ✅

## Feedback addressed

- Player names are now printed.
- Comparison section added.
- Accidental trailing `\` removed.
- Redundant `str()` wrappers removed.
- Input prompts are still `"Input prize"` (spelling) and prices print `$`.

## Remaining polish (non-blocking)

1. `$` → `£` in the two price lines.
2. `"Input prize"` → `"Price (£m): "`.
3. `(input(...))` works but the parentheses are unnecessary.
4. Add spaces around comparison operators (`ppm_a > ppm_b`).
5. `ppm` means points per **million** in FPL, but here it means points per
   **match**; rename to `per_match` / `per_million` later.

---

## Week 1 completion check

| Skill | Status |
|---|---|
| Explain what a program does | ✅ |
| Run a Python file | ✅ |
| `print()` and strings | ✅ |
| Variables and basic types | ✅ |
| Arithmetic and rounding | ✅ |
| Input and numeric conversion | ✅ |
| Comparisons and Boolean logic | ✅ |
| `if` / `elif` / `else` | ⏭ Week 2, Day 1 |
| Mini-project runs and is explainable | ✅ |
| Log and lesson notes kept | ✅ |

Quiz: 5/6 (target met). Branching was deliberately moved to Week 2 in the
8-week plan.

---

## Key takeaways

1. Small programs combine a handful of ideas: input → convert → calculate →
   format → compare.
2. Test one player before adding the second.
3. Booleans can report comparisons without any `if` statements.
4. Naming and formatting matter for readability, not for correctness.

## Next

Week 2, Day 1 — `if` / `elif` / `else`: a value classifier with labelled
practice thresholds.
