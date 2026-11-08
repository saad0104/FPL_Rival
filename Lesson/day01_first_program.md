# Week 1 · Day 1 — Your First Program

**Date:** 9 November 2026
**Week / Day:** Week 1, Day 1
**File:** `week-01/day01_hello.py`
**Status:** ✅ Complete

---

## Goal

Understand what a program is, and get Python to print text that you wrote.

## Concepts

### A program is an ordered list of instructions

A program is like a manager's instruction sheet: steps followed in order,
top to bottom. The computer does exactly what is written — including mistakes.

### Python and the editor

- **Python** is the language we write instructions in.
- A `.py` file is a plain text file containing Python code.
- **VS Code** is an editor: it colours code, spots typos, and has a terminal
  to run programs.

### `print()` and strings

```python
print("Hello, FPL Rival")
```

| Part | Name | Job |
|---|---|---|
| `print` | function | The action: display something |
| `( ... )` | parentheses | Hold what to display |
| `"Hello, FPL Rival"` | string | The text itself |

- Quotes mark where text starts and ends; they are **not printed**.
- `print()` can show several items separated by commas, joined with a space.
- Strings are **literal**: case, spaces, and spelling pass through unchanged.

### Running a file

```bash
cd /home/saad/FPL_Rival
python3 week-01/day01_hello.py
```

Python runs the file from the first line to the last.

---

## Practice

### Part A — predict the output

```python
print("Salah")
print("  Salah")
print("2 + 2")
```

**Answer:**

```
Salah
  Salah
2 + 2
```

The two leading spaces on line 2 are inside the quotes, so they are printed.
`"2 + 2"` is text, not arithmetic — Python does not calculate inside quotes.

### Part B — add a line

Add a third `print()` line with an FPL-related message.

### Part C — break it on purpose

Delete one closing `"` and run the file. Python reports:

```
SyntaxError: unterminated string literal (detected at line 1)
```

- `SyntaxError` = Python could not understand the grammar of the line.
- `unterminated string literal` = a quote was opened but never closed.
- The `^` points at where Python became confused.

---

## Implementation

Final program:

```python
print("Hello, FPL Rival")
print("This is my first Python program.")
print("Haaland")
```

Output:

```
Hello, FPL Rival
This is my first Python program.
Haaland
```

Note: an earlier version typed `Halland`. Python printed the typo exactly —
it has no spellchecker.

---

## Key takeaways

1. A program is instructions run in order.
2. `print()` displays text; quotes are delimiters, not content.
3. Strings are literal: spaces, case, and spelling are preserved.
4. Errors are information: read the type, the message, and the `^` position.

## Common errors

| Error | Cause | Fix |
|---|---|---|
| `SyntaxError: unterminated string literal` | Missing closing quote | Close the string |
| `SyntaxError: invalid syntax` | Missing `)` or quote | Check brackets and quotes |
| `NameError` | Misspelled function/variable name | Match spelling exactly |

## Next

Day 2 — variables and basic data types.
