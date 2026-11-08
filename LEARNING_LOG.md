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
