# Week 1 · Day 2 — Variables and Data Types

**Date:** 9 November 2026
**Week / Day:** Week 1, Day 2
**File:** `week-01/day02_variables.py`
**Status:** ✅ Complete (one naming question still open — see Next)

---

## Goal

Store a player's details under meaningful names, and know what kind of value
each variable holds.

---

## Concepts

### Variables are labelled boxes

```python
price = 4.9
```

Read **right to left**: take the value `4.9`, then attach the name `price`.

- `=` means **store this value**, not "equals".
- Using the name later looks up the current value.
- **Reassignment** replaces the old value:

```python
price = 4.5
price = 4.9
print(price)   # 4.9 — the 4.5 is gone
```

### The four basic types

| Type | Meaning | Example | Football use |
|---|---|---|---|
| `str` | text | `"Cole Palmer"` | player name, club |
| `int` | whole number | `47` | points, matches |
| `float` | decimal number | `9.8` | price (£m), averages |
| `bool` | true / false | `True` | available, injured |

```python
"9.8"    # str  — text that looks like a number
9.8      # float — a number you can calculate with
True     # bool — capital T, no quotes
"True"   # str  — just text
```

`type()` reveals the type:

```python
print(type(9.8))   # <class 'float'>
```

### Variable naming rules

- Letters, digits, underscores only: `player_name` ✅
- Cannot start with a digit: `2nd_player` ❌
- No spaces or hyphens: `player-price` ❌
- Case-sensitive: `price` and `Price` are different variables
- Convention: `snake_case`
- Avoid reserved words (`class`, `if`, `for`) and built-ins (`print`, `type`)

### Printing labels and values

```python
print("Player:", player_name)
```

Two items separated by a comma: literal text and a variable. `print` joins
them with a space.

---

## Demo

```python
player_name = "Sam Striker"
club = "Harbour City"
price = 7.5
total_points = 63
available = True

print("Player:", player_name)
print("Club:", club)
print("Price:", price)
print("Total points:", total_points)
print("Available:", available)
```

Output:

```
Player: Sam Striker
Club: Harbour City
Price: 7.5
Total points: 63
Available: True
```

---

## Practice answers

### A. Reassignment

```python
price = 7.5
price = 8.0
print(price)
```

**Answer:** `8.0`. The second assignment overwrites the first. Only the
latest value is stored.

### B. Valid names

| Name | Valid? | Reason |
|---|---|---|
| `player_name` | ✅ | Letters and underscore; snake_case |
| `2nd_player` | ❌ | Starts with a digit |
| `player-price` | ❌ | Hyphen is not allowed (it means subtraction) |
| `PlayerName` | ✅ but avoid | Legal, but not the Python convention |
| `_price` | ✅ but avoid | Legal; leading underscore has a special meaning |
| `class` | ❌ | Reserved keyword |

---

## Implementation

The learner's program used two real players as practice data:

```python
player_name = "Maxim De Cuyper"
club = "Brighton"
price = 4.5
price = 4.9
total_points = 75
available = True

print("Player:", player_name)
print("Club:", club)
print("Price:", price)
print("Total points:", total_points)
print("Available:", available)

player_name = "Cole Palmer"
club = "Chelsea"
price = 9.5
price = 9.8
total_points = 47
available = True

print("Player:", player_name)
print("Club:", club)
print("Price:", price)
print("Total points:", total_points)
print("Available:", available)
print(type(price))
```

Output:

```
Player: Maxim De Cuyper
Club: Brighton
Price: 4.9
Total points: 75
Available: True
Player: Cole Palmer
Club: Chelsea
Price: 9.8
Total points: 47
Available: True
<class 'float'>
```

### What this demonstrates

1. **Reassignment works twice:** `price = 4.5` then `4.9` means only `4.9`
   is printed. Same for Palmer (`9.5` → `9.8`).
2. **Print order matters:** the first record prints *before* the variables are
   reused, so both players appear in the output.
3. **Reusing a variable overwrites it:** if both prints happened at the end,
   only Cole Palmer would appear. To hold two players at the same time, use
   separate names (`player1_name`, `player2_name`) or, later, a list/dictionary.
4. **`type(price)` returned `<class 'float'>`** — prices are decimals.

---

## Key takeaways

1. `=` stores a value under a name; reading the name gives the current value.
2. Reassignment replaces the old value — it does not keep history.
3. `str`, `int`, `float`, and `bool` behave differently even when they look
   similar on screen.
4. Choose clear `snake_case` names; one variable holds one current value.

## Common errors

| Error | Cause | Fix |
|---|---|---|
| `NameError: name 'pice' is not defined` | Typo in variable name | Use the exact declared name |
| `SyntaxError` on a hyphen | `player-price` is read as subtraction | Use `player_price` |
| `True` vs `"True"` | One is a bool, the other a string | Remove quotes for bool |

## Next

- Day 3: arithmetic, averages, points per match, points per £m.
- Quick open question: which of these names would you avoid, and why?
  `player_name` · `2nd_player` · `player-price` · `class`
