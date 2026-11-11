# FPL Rival — Learning Log

One entry per session. Newest entries at the bottom.
Format: date, topic, what was learned, commands/concepts practised, errors,
what is still confusing, next task, status.

---

## 2026-11-09 — Environment setup

**Topic:** Project setup (before Week 1 Day 1).
**Learned:** The machine already has everything needed; no installs were required.
**Environment verified:**
- Ubuntu 24.04.4 LTS, x86_64
- Python 3.12.3 (`/usr/bin/python3`), pip 24.0
- Git 2.43.0
- Editors available: VS Code (`code`), vim, nano
- Disk: 16 GB free; RAM: 7.4 GiB total, ~2.3 GiB available

**Set up:**
- Created project virtual environment in `.venv/`
- Created `.gitignore`, `README.md`, `PLAN.md`, this log
- Initialised a local Git repository (no remote, nothing pushed)

**Next task:** Continue Week 1 Day 1.

---

## 2026-11-09 — Week 1, Day 1 (part 1)

**Topic:** What a program is, why Python, editors, `print()`, strings.
**Learned:**
- A program is an ordered list of instructions.
- Python is readable and well suited to data work.
- An editor (VS Code) helps write and run code.
- `print("text")` displays text; the quotes make it a string.
- Python runs a file top to bottom.

**Practised:**
- Created and ran `week-01/day01_hello.py`.
- Command: `python3 week-01/day01_hello.py`
- Output:
  ```
  Hello, FPL Rival
  This is my first Python program.
  ```

**Errors:** None so far.
**Still confusing:** (to be filled in by the learner)
**Next task:** Add a third `print()` line with an FPL-related message, run it,
and report the line and output.
**Status:** Day 1 in progress — exercise pending. (Completed in the entry below.)

---

## 2026-11-09 — Week 1, Day 1 (completed)

**Topic:** First program; `print()` and strings.
**Learned:**
- Quotes mark text; `print()` does not display them.
- Strings are literal: case, spacing, and spelling are printed exactly.
- `print("2 + 2")` shows text, not `4`.
- A missing closing quote causes `SyntaxError: unterminated string literal`.

**Practised:**
- Predicted the output of three `print()` calls, including leading spaces.
- Added a third line to `week-01/day01_hello.py`; corrected the spelling from
  "Halland" to "Haaland".
- Ran the file successfully.

**Commands:**
- `python3 week-01/day01_hello.py`
- `source .venv/bin/activate` (optional; no packages needed yet)

**Errors:** Mentor demonstrated the unterminated-string `SyntaxError`; learner
read and explained it. No unresolved errors.
**Still confusing:** None reported.
**Next task:** Day 2 — variables and basic data types. Store a fictional player's
name, club, price, points, and availability, then print them with labels.
**Status:** ✅ Day 1 complete.

---

## 2026-11-09 — Week 1, Day 2 (completed)

**Topic:** Variables, assignment/reassignment, `str`/`int`/`float`/`bool`,
variable naming, `type()`.
**Learned:**
- `name = value` stores a value; `=` is not "equals".
- Reassignment replaces the previous value; it does not keep history.
- `type()` reveals a value's type: `str`, `int`, `float`, `bool`.
- `"9.8"` (str) and `9.8` (float) look similar when printed but behave
  differently in calculations.
- Naming: letters/digits/underscore, no leading digit, no hyphen, case-sensitive,
  `snake_case` convention.
- `print("Price:", price)` prints a label and the variable's value.

**Practised:**
- Predicted the result of reassignment (`price = 7.5` then `8.0` → `8.0`).
- Built two player records in `week-01/day02_variables.py`:
  Maxim De Cuyper (Brighton, 4.9, 75 pts) and Cole Palmer (Chelsea, 9.8, 47 pts).
- Ran the file; `type(price)` returned `<class 'float'>`.

**Key insight from the code:** both players were printed *before* the variables
were reused for the second player. Reusing `player_name`, `club`, `price`, etc.
overwrote the first record. If both prints were moved to the end, only Cole
Palmer would appear. Separate names (or, later, lists/dicts) are needed to keep
two players at once.

**Errors:** None unresolved.
**Still confusing:** The naming-rule question is still open (which of
`player_name`, `2nd_player`, `player-price`, `class` to avoid, and why).
**Next task:** Day 3 — arithmetic: points per match, points per £m, precedence,
rounding.
**Status:** ✅ Day 2 complete.

---

## Project notes (2026-11-09)

- Added `Lesson/` with one markdown note per study day:
  `day01_first_program.md`, `day02_variables.md`, and an index `README.md`.
- Updated `PLAN.md` and `README.md` so every future day also gets a lesson note.
- Day 2 output verified; no errors.

---

## 2026-11-09 — Week 1, Day 3 (completed)

**Topic:** Arithmetic, order of operations, derived metrics.
**Learned:**
- Operators `+`, `-`, `*`, `/`, `//`, `%`, `**`.
- `/` returns a decimal; `//` returns the whole part; `%` returns the remainder.
- Parentheses override the normal order (`2 + 3 * 4` vs `(2 + 3) * 4`).
- `round(value, 2)` limits decimals but does not force trailing zeros.
- Points per match = points / matches; points per £m = points / price.

**Practised:**
- Predicted all five operator outputs correctly: 16, 36, 2.5, 2, 2.
- Hand formulas: 63/9 = 7.0 points per match; 63/7.5 = 8.4 points per £m.
- Built `week-01/day03_calculator.py` for Cole Palmer (47 pts, £9.8m, 10 matches).

**Output:**
```
Player: Cole Palmer
Average points per match: 4.7
Points per £m: 4.8
Rounded average: 4.7
Rounded points per £m: 4.8
```

**Notes:** The two "rounded" print lines duplicate the two lines above them.
The optional floor-division (`//`) line was not added; revisit in the Day 6
review.

**Errors:** None unresolved.
**Still confusing:** None reported.
**Next task:** Day 4 — `input()`, converting text to numbers, `ValueError`,
and f-strings.
**Status:** ✅ Day 3 complete.

---

## 2026-11-09 — Week 1, Day 4 (completed)

**Topic:** `input()`, type conversion, `ValueError`, f-strings.
**Learned:**
- `input()` always returns a `str`, even when the user types digits.
- `int()` converts whole-number text; `float()` converts decimal text.
- `int("7.5")` raises `ValueError: invalid literal for int()`.
- `"9.8" * 2` repeats text (`9.89.8`); numbers must be converted first.
- f-strings: `f"{value}"`, and `{value:.2f}` forces exactly two decimals.

**Practised:**
- Answered the `input()` type question — initially said `int`, corrected to
  `str` after checking `type(age)`.
- Identified that only `int("7.5")` errors; the other lines print 10, 8.5, 0.67.
- Ran the interactive calculator with David Raya (£6.0m, 60 pts, 10 matches).

**Output:**
```
David Raya: 6.00 points per match
David Raya: 10.00 points per £m
```

**Implementation:** `week-01/day04_input.py` — four `input()` calls, `int()` /
`float()` conversion, and two f-strings. Arithmetic verified: 60/10 = 6.00 and
60/6 = 10.00.

**Errors:** No runtime errors. One conceptual error: `input()` was thought to
return `int`; corrected and demonstrated with `type()`.
**Still confusing:** None reported after correction.
**Next task:** Day 5 — comparisons and Boolean logic; compare two players.
**Status:** ✅ Day 4 complete.

---

## 2026-11-09 — Week 1, Day 5 (completed)

**Topic:** Comparison operators, Booleans, `and`/`or`/`not`.
**Learned:**
- `==`, `!=`, `>`, `<`, `>=`, `<=` return `True` or `False`.
- `=` assigns; `==` compares.
- `and` requires both sides; `or` requires one; `not` flips the result.
- Comparisons are case-sensitive for strings.
- Floats are approximate: `0.1 + 0.2 == 0.3` is `False`; compare rounded values.
- `5 == 5.0` is `True` (numeric value).

**Practised:**
- Predicted five comparison results correctly: True, True, False, False, True.
- Predicted three combined conditions correctly: True, True, False.
- Extended `week-01/day05_comparison.py` to calculate points per £m from raw
  points and price, then compare the two players.

**Output:**
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

**Notes:** Replaced hard-coded ppm with `points / price`. Added availability
checks. Minor style issues: missing spaces around `/`; trailing space in
`"Both available: "`. The label "injured" for `not available` is imprecise.

**Errors:** None unresolved.
**Still confusing:** None reported.
**Next task:** Day 6 — Week 1 review quiz and the Player Analyzer v1 mini-project.
**Status:** ✅ Day 5 complete.

---

## 2026-11-09 — Week 1, Day 6 (completed) — Week 1 finished

**Topic:** Week 1 review quiz + FPL Player Analyzer v1.
**Quiz:** 5/6 (target met).
- Missed only `f"{2/3:.2f}"`: it is `0.67`, not `0.66`; `.2f` rounds.

**Learned/revised:**
- `.2f` rounds rather than truncating.
- A small program is a pipeline: input → convert → calculate → format → compare.
- Build and test one player before duplicating the block for the second.
- Booleans can report comparisons without `if` statements.

**Implementation:** `week-01/mini_project_player_analyzer.py`
- Two players, five inputs each.
- Points per match and points per £m, formatted to two decimals.
- Four comparison outputs.
- Verified with Enzo (7.5, 35 pts, 10 matches) and Mbuembo (7.0, 56 pts,
  10 matches): 3.50 / 4.67 and 5.60 / 8.00; all comparisons correct.

**Feedback addressed:** added player names, added comparison section, removed
the stray trailing backslash, removed redundant `str()` wrappers.
**Remaining polish:** `$` → `£`, `"Input prize"` → `"Price (£m): "`,
unnecessary parentheses around `input()`, spaces around comparison operators,
and clearer metric names (`ppm` currently means points per match).

**Week 1 check:** print, strings, variables/types, arithmetic, input/conversion,
comparisons/Booleans, mini-project, notes/log all complete. `if`/`elif`/`else`
was deliberately moved to Week 2.

**Errors:** None unresolved. Quiz: one rounding error, corrected.
**Next task:** Week 2, Day 1 — `if` / `elif` / `else` and a value classifier.
**Status:** ✅ Day 6 complete. Week 1 complete (6/48 sessions).

---

## 2026-11-09 — Week 2, Day 1 (completed)

**Topic:** `if` / `elif` / `else`, indentation, order of conditions, truthiness.
**Learned:**
- Conditions are Boolean expressions; the line ends with `:` and the body is
  indented 4 spaces.
- Only the **first true branch** runs.
- Place the strictest/highest threshold first; otherwise a broad condition
  swallows the specific one.
- `elif` means "else if"; `else` is optional and catches everything remaining.
- Empty string, `0`, and `False` are falsy.
- Missing indentation raises `IndentationError`.

**Practised:**
- Converted the demo from hard-coded values to `input()` with `float()` / `int()`.
- Classified points per £m into four labelled practice bands.
- Test 1: De Cuyper (4.9, 75, 10) → 15.31 → "excellent".
- Test 2: Palmer (9.8, 47, 10) → 4.80 → "below average".
- Both outputs verified correct.

**Practice answers (not submitted; recorded in the lesson note):**
- A → `medium`; B → `average` (order bug; move `>= 15` first); C → `free?`
  (zero is falsy). These need checking in the Day 6 review.

**Errors:** None at runtime.
**Still confusing:** Nothing reported; practice-answer checking is pending.
**Next task:** Week 2, Day 2 — lists: store a squad as a collection.
**Status:** ✅ Day 7 complete (7/48 sessions).

---

## 2026-11-10 — Week 2, Day 2 (completed)

**Topic:** Lists — indexing, slicing, `append`, `remove`, membership, `len`.
**Learned:**
- A list stores many ordered values under one name.
- Indexing starts at 0; `-1` is the last item; slices exclude the stop index
  and return a new list.
- `len()` gives the count; an invalid index raises `IndexError`.
- `append` adds at the end; `remove` deletes by value and raises `ValueError`
  if absent; both mutate the list.
- `append` returns `None` — never assign its result.
- `in` checks membership and returns a Boolean, so it works with `if`.

**Practised:**
- Predicted indexing, `len`, and slice results correctly; noted that a slice
  prints as a list (`['Palmer', 'Haaland']`).
- Explained the `IndexError` and the valid index range.
- Predicted membership before and after `append`: False → True.
- Extended `week-02/day02_lists.py` to add a player from `input()` and remove
  one under an `if name in squad` guard.

**Test 1:** added Isak, removed Saka — updated squad and count printed.
**Test 2:** tried to remove "Nobody" — guard printed "not in the squad" without
crashing.

**Practised outputs:**
```
Enter a player: ['De Cuyper', 'Palmer', 'Haaland', 'Mbuembo', 'Saka', 'Isak']
6
Which player to remove? Saka is removed from the squad.
True
['De Cuyper', 'Palmer', 'Haaland']
```

**Polish:** the demo's own `append("Saka")` / `remove("Raya")` still run before
user input; label the membership print; print the squad after removal; remove a
whitespace-only line.

**Errors:** None unresolved.
**Still confusing:** None reported.
**Next task:** Week 2, Day 3 — loops (`for`, `range`, accumulators) over the
squad.
**Status:** ✅ Day 8 complete (8/48 sessions).

---

## 2026-11-11 — Week 2, Day 3 (completed)

**Topic:** `for` loops, `range`, `enumerate`, accumulators.
**Learned:**
- `for item in list` visits every element; the indented block runs once per item.
- `range(n)` → 0 to n−1; `range(a, b)` → a to b−1; stop is always **excluded**.
- `range(a, b, step)` skips by `step` (e.g. `range(2, 8, 2)` → 2, 4, 6).
- Accumulator pattern: initialise to `0` before the loop, `+=` inside, read after.
- `enumerate(seq, start=1)` yields `(counter, item)` pairs without needing `range(len(...))`.
- f-string alignment: `:<n` left-aligns, `:>n` right-aligns in an n-character field.

**Practised:**
- Predicted four loop/range outputs before running (1/4 correct).
- All four errors shared the same theme: forgot that `range` starts at 0 and
  that the stop value is excluded (same rule as list slicing).

**Implementation:** `week-02/day03_loops.py`
- 15-player GW10 practice squad across three parallel lists (squad, points, positions).
- Numbered squad with `enumerate`.
- Total (775) and average (51.7) points via accumulator.
- Formatted position/name/points table using `range(len(...))` and f-string alignment.
- Top-scorer search: seed with index 0, loop from 1, update on each new best.
- Top scorer: Salah (89 pts).

**Key insight:** Three parallel lists (`squad`, `points`, `positions`) must be
kept in sync manually — adding a player to one and forgetting the others causes
either an `IndexError` or silent wrong data. Day 4 (dictionaries) fixes this by
bundling all player data into one object.

**Errors:** None at runtime. Four prediction errors — all corrected.
**Still confusing:** Nothing reported.
**Next task:** Week 2, Day 4 — Dictionaries: player as a single bundle.
**Status:** ✅ Day 9 complete (9/48 sessions).
