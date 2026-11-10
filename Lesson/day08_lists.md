# Week 2 · Day 2 — Lists

**Date:** 10 November 2026
**Week / Day:** Week 2, Day 2 (session 8)
**File:** `week-02/day02_lists.py`
**Status:** ✅ Complete

---

## Goal

Hold a whole squad in one variable, reach players by position, and add/remove
players.

---

## Concepts

### One variable, many values

```python
squad = ["Raya", "De Cuyper", "Palmer", "Haaland", "Mbuembo"]
```

Lists are ordered and written with square brackets and commas.

### Indexing starts at 0

| Access | Result |
|---|---|
| `squad[0]` | `"Raya"` |
| `squad[1]` | `"De Cuyper"` |
| `squad[-1]` | `"Mbuembo"` (last) |
| `squad[-2]` | `"Haaland"` |
| `len(squad)` | `5` |

An invalid index raises:

```
IndexError: list index out of range
```

### Slices

```python
squad[:3]   # ['Raya', 'De Cuyper', 'Palmer']
squad[1:]   # ['De Cuyper', 'Palmer', 'Haaland', 'Mbuembo']
```

A slice returns a **new list** (brackets and quotes included when printed).
The stop index is excluded.

### Adding and removing

```python
squad.append("Saka")    # add at the end
squad.remove("Raya")    # remove first matching value
```

- Lists are mutable; methods change the existing list.
- `remove` raises `ValueError` if the value is absent.
- `append` returns `None` — never assign its result:
  `squad = squad.append("Saka")` destroys the list.
- Removing index 0 shifts every later item one place left.

### Membership

```python
"Palmer" in squad     # True
"Saka" in squad       # False
```

`in` returns a Boolean and works directly with `if`.

---

## Demo

`week-02/day02_lists.py` (initial version) printed:

```
Squad: ['Raya', 'De Cuyper', 'Palmer', 'Haaland', 'Mbuembo']
First player: Raya
Last player: Mbuembo
Number of players: 5
Palmer in squad: True
First three: ['Raya', 'De Cuyper', 'Palmer']
After adding Saka: ['Raya', 'De Cuyper', 'Palmer', 'Haaland', 'Mbuembo', 'Saka']
Count now: 6
After removing Raya: ['De Cuyper', 'Palmer', 'Haaland', 'Mbuembo', 'Saka']
Count now: 5
Player at index 1: Palmer
```

---

## Practice answers

### A. Indexing and a slice

```python
players = ["Raya", "Palmer", "Haaland"]
print(players[0])    # Raya
print(players[-1])   # Haaland
print(len(players))  # 3
print(players[1:])   # ['Palmer', 'Haaland']
```

Correct, with one nuance: the slice prints as a list
(`['Palmer', 'Haaland']`), not as two bare words.

### B. Index error

```python
players = ["Raya", "Palmer"]
print(players[2])
```

`IndexError: list index out of range` — valid indices are `0` and `1`.
`players[1]` gives `Palmer`; to get a third player, append one first.

### C. Membership

```python
squad = ["Raya", "Palmer"]
print("Saka" in squad)   # False
squad.append("Saka")
print("Saka" in squad)   # True
```

Correct.

---

## Implementation

Learner's additions to the demo:

```python
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
```

### Test 1 — add Isak, remove Saka

```
Enter a player: ['De Cuyper', 'Palmer', 'Haaland', 'Mbuembo', 'Saka', 'Isak']
6
Which player to remove? Saka is removed from the squad.
True
['De Cuyper', 'Palmer', 'Haaland']
```

### Test 2 — remove a player not in the squad

```
Which player to remove? Nobody is not in the squad
True
['De Cuyper', 'Palmer', 'Haaland']
```

The `in` guard correctly prevents `ValueError` when the name is absent.

### Polish

1. The demo mutations at the top (`append("Saka")`, `remove("Raya")`) still run
   before the user's actions. Remove or comment them if the program is meant to
   start from the original five-player squad.
2. Label the membership output:
   `print("Palmer in squad:", "Palmer" in squad)`.
3. Print the updated squad after removal too, not just a message.
4. Delete the whitespace-only line before the final prints.

---

## Key takeaways

1. A list stores many ordered values under one name.
2. Indices start at 0; `-1` is the last item; slices exclude the stop index.
3. `append` / `remove` mutate the list; `append` returns `None`.
4. `in` checks membership and returns a Boolean.
5. Guard `remove` with an `in` check until error handling is taught.

## Common errors

| Error | Cause | Fix |
|---|---|---|
| `IndexError` | Index beyond the last item | Check `len()`; use a valid index |
| `ValueError` on `remove` | Value not present | Guard with `if name in squad` |
| `TypeError: 'NoneType' object is not iterable` | Assigned the result of `append` | Call `append` without assigning |
| `AttributeError` | Typo in method name (`appendd`) | Match the method spelling |

## Next

Week 2, Day 3 — loops: process the whole squad without writing one line per
player.
