# Week 1 · Day 5 — Comparisons and Boolean Logic

**Date:** 9 November 2026
**Week / Day:** Week 1, Day 5
**File:** `week-01/day05_comparison.py`
**Status:** ✅ Complete

---

## Goal

Ask yes/no questions about player data, and combine those questions into
useful conditions.

---

## Concepts

### Comparison operators

| Operator | Question | Example | Result |
|---|---|---|---|
| `==` | equal to? | `4.9 == 4.9` | `True` |
| `!=` | not equal? | `4.9 != 9.8` | `True` |
| `>` | greater than? | `75 > 47` | `True` |
| `<` | less than? | `4.9 < 9.8` | `True` |
| `>=` | greater or equal? | `4.9 >= 4.9` | `True` |
| `<=` | less or equal? | `4.9 <= 4.0` | `False` |

Comparisons produce a **Boolean**: `True` or `False`.

### `=` versus `==`

```python
price = 9.8      # assignment: store a value
price == 9.8     # comparison: ask whether it is equal
```

Mixing them up inside an `if` will be a syntax error next week.

### Combining conditions

| Operator | Meaning | Example |
|---|---|---|
| `and` | both true | `True and False` → `False` |
| `or` | at least one true | `True or False` → `True` |
| `not` | flips the value | `not True` → `False` |

Precedence: comparisons, then `not`, then `and`, then `or`. Parentheses remove
ambiguity: `not (a and b)` ≠ `(not a) and b`.

### Two traps

1. **Strings are case-sensitive:** `"Chelsea" == "chelsea"` → `False`.
2. **Floats are approximate:**

```python
0.1 + 0.2            # 0.30000000000000004
0.1 + 0.2 == 0.3     # False
```

Do not test calculated decimals with `==`; compare rounded values or use a
tolerance.

`5 == 5.0` is `True` because Python compares numeric value, not type.

---

## Demo

`week-01/day05_comparison.py` compares Cole Palmer and Maxim De Cuyper:

```python
ppm_a = 4.8
ppm_b = 15.31
price_a = 9.8
price_b = 4.9

print("A has better points per £m:", ppm_a > ppm_b)
print("B is cheaper:", price_b < price_a)
print("Both cost under £10m:", price_a < 10 and price_b < 10)
print("Either is above 10 points per £m:", ppm_a > 10 or ppm_b > 10)
print("They cost the same:", price_a == price_b)
print("They cost different amounts:", price_a != price_b)
print("Not both conditions:", not (price_a < 10 and ppm_a > 4))
```

Output:

```
A has better points per £m: False
B is cheaper: True
Both cost under £10m: True
Either is above 10 points per £m: True
They cost the same: False
They cost different amounts: True
Not both conditions: False
```

---

## Practice answers

### A. Predictions

```python
print(5 > 3)                   # True
print(5 == 5.0)                # True
print("Chelsea" == "chelsea")  # False
print(10 != 10)                # False
print(4 <= 4)                  # True
```

All correct.

### B. Logic

```python
price = 7.5
points = 60

print(price < 8 and points > 50)  # True
print(price > 8 or points > 50)   # True
print(not price < 8)              # False
```

All correct.

---

## Implementation

Learner's version, now calculating points per £m from raw points and price:

```python
player_a = "Cole Palmer"
price_a = 9.8
points_a = 47
available_a = True
ppm_a = points_a / price_a

player_b = "Maxim De Cuyper"
price_b = 4.9
points_b = 75
available_b = True
ppm_b = points_b / price_b

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
```

Output:

```
Cole Palmer vs Maxim De Cuyper
A has better points per £m: False
B is cheaper: True
Both cost under £10m: True
Either is above 10 points per £m: True
They cost the same: False
They cost different amounts: True
A can be afforded and is above 4 ppm: True
Not both conditions: False
Both available:  True
Is Palmer injured: False
```

Checks:

- `ppm_a` = 47 / 9.8 = 4.7959…, `ppm_b` = 75 / 4.9 = 15.306… → B higher ✅
- All Boolean results follow correctly from the data ✅
- **Label caution:** `not available_a` means *not available*, which is not
  necessarily *injured*. Use precise labels in FPL analysis.
- Style nits: `points_a/price_a` should be `points_a / price_a`; the string
  `"Both available: "` has a trailing space, producing a double space.

---

## Key takeaways

1. Comparisons return `True`/`False`; `==` is not `=`.
2. `and` needs both sides; `or` needs one; `not` flips.
3. Parentheses make combined conditions readable.
4. Never test calculated floats with `==`.
5. A Boolean variable can answer questions like "both available?" directly.

## Common errors

| Error | Cause | Fix |
|---|---|---|
| `if price = 9.8` | Used assignment instead of comparison | `if price == 9.8` |
| `NameError: true` | Lowercase Boolean | Use `True` / `False` |
| Unexpected `True` for "same" floats | Float approximation | Compare `round(...)` values |
| Wrong logic result | Missing parentheses / wrong operator | Read the condition aloud |

## Next

Day 6 — Week 1 review and mini-project: **FPL Player Analyzer v1**.
