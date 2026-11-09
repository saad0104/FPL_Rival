#!/usr/bin/env python3
"""FPL Rival lesson tracker.

A deliberately small Tkinter app: 48 sessions, one checkbox each, saved to
progress.json. No third-party packages.

Run from the project root:
    python3 tracker.py
"""

from __future__ import annotations

import json
import tkinter as tk
from datetime import date
from pathlib import Path
from tkinter import ttk

ROOT = Path(__file__).resolve().parent
DATA_FILE = ROOT / "progress.json"

WEEK_TITLES = {
    1: "Python foundations",
    2: "Control flow, collections, functions",
    3: "Files, JSON, errors, HTTP",
    4: "FPL API and data collection",
    5: "pandas analysis",
    6: "Visualization, SQL, SQLite",
    7: "Statistics and ML",
    8: "App and deployment",
}

# (week, day, title) — the 8 x 6 plan from PLAN.md
LESSONS = [
    (1, 1, "First program, print(), strings"),
    (1, 2, "Variables and data types"),
    (1, 3, "Arithmetic and derived metrics"),
    (1, 4, "Input, conversion, f-strings"),
    (1, 5, "Comparisons and Boolean logic"),
    (1, 6, "Review + Player Analyzer v1"),
    (2, 1, "Conditional statements"),
    (2, 2, "Lists"),
    (2, 3, "Loops and accumulators"),
    (2, 4, "Dictionaries"),
    (2, 5, "Functions"),
    (2, 6, "Review + Squad Summary v1"),
    (3, 1, "Files and CSV"),
    (3, 2, "JSON and nested data"),
    (3, 3, "Errors and validation"),
    (3, 4, "Modules and project layout"),
    (3, 5, "HTTP and the first API call"),
    (3, 6, "Review + cache bootstrap JSON"),
    (4, 1, "Bootstrap endpoints"),
    (4, 2, "Player fields and prices"),
    (4, 3, "Fixtures and difficulty"),
    (4, 4, "Entry, history, picks"),
    (4, 5, "League standings and rivals"),
    (4, 6, "Review + full dataset cache"),
    (5, 1, "DataFrames"),
    (5, 2, "Filtering and sorting"),
    (5, 3, "Groupby and merge"),
    (5, 4, "Derived metrics"),
    (5, 5, "Squad comparison"),
    (5, 6, "Review + league report"),
    (6, 1, "Line and bar charts"),
    (6, 2, "Scatter and saving figures"),
    (6, 3, "SQL basics"),
    (6, 4, "SQLite in Python"),
    (6, 5, "Joins and aggregates"),
    (6, 6, "Review + database CLI"),
    (7, 1, "Descriptive statistics"),
    (7, 2, "Baselines and train/test"),
    (7, 3, "Linear regression"),
    (7, 4, "Evaluation metrics"),
    (7, 5, "Uncertainty and backtesting"),
    (7, 6, "Review + prediction report"),
    (8, 1, "Streamlit basics"),
    (8, 2, "Data wiring and caching"),
    (8, 3, "Rival comparison UI"),
    (8, 4, "Insight cards"),
    (8, 5, "Deployment and secrets"),
    (8, 6, "Review + final demo"),
]

# Already completed before the tracker existed (see LEARNING_LOG.md).
DONE_AT_START = {"W1D1", "W1D2", "W1D3", "W1D4"}
START_DATE = "2026-11-09"


def lesson_id(week: int, day: int) -> str:
    return f"W{week}D{day}"


def default_data() -> dict:
    lessons = []
    for week, day, title in LESSONS:
        lid = lesson_id(week, day)
        done = lid in DONE_AT_START
        lessons.append(
            {
                "id": lid,
                "week": week,
                "day": day,
                "title": title,
                "status": "done" if done else "todo",
                "completed": START_DATE if done else "",
            }
        )
    return {"project": "FPL Rival", "updated": START_DATE, "lessons": lessons}


def load_data() -> dict:
    """Load progress.json, falling back to defaults if missing or invalid."""
    if DATA_FILE.exists():
        try:
            data = json.loads(DATA_FILE.read_text(encoding="utf-8"))
            if isinstance(data, dict) and isinstance(data.get("lessons"), list):
                return data
        except (OSError, json.JSONDecodeError):
            pass
    data = default_data()
    save_data(data)
    return data


def save_data(data: dict) -> None:
    data["updated"] = date.today().isoformat()
    temp = DATA_FILE.with_suffix(".json.tmp")
    temp.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    temp.replace(DATA_FILE)


class TrackerApp(tk.Tk):
    BG = "#f6f5f1"
    CARD = "#ffffff"
    INK = "#22302a"
    MUTED = "#7b857f"
    ACCENT = "#1f6f4a"

    def __init__(self) -> None:
        super().__init__()
        self.title("FPL Rival — Lesson Tracker")
        self.geometry("780x660")
        self.minsize(600, 440)
        self.configure(bg=self.BG)
        self.data = load_data()
        self.vars: dict[str, tk.BooleanVar] = {}
        self.date_labels: dict[str, tk.Label] = {}
        self.week_labels: dict[int, tk.Label] = {}
        self._style()
        self._build()
        self._refresh()

    def _style(self) -> None:
        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure(
            "Lesson.TCheckbutton",
            background=self.CARD,
            foreground=self.INK,
            font=("DejaVu Sans", 10),
            padding=(6, 3),
        )
        style.map("Lesson.TCheckbutton", background=[("active", self.CARD)])
        style.configure(
            "Bar.Horizontal.TProgressbar",
            troughcolor="#e3e1d9",
            background=self.ACCENT,
            bordercolor="#e3e1d9",
            lightcolor=self.ACCENT,
            darkcolor=self.ACCENT,
        )
        style.configure("Vertical.TScrollbar", background="#d8d6ce", troughcolor=self.BG)

    def _build(self) -> None:
        header = tk.Frame(self, bg=self.BG)
        header.pack(fill="x", padx=18, pady=(16, 6))

        tk.Label(
            header,
            text="FPL Rival",
            bg=self.BG,
            fg=self.INK,
            font=("DejaVu Sans", 18, "bold"),
            anchor="w",
        ).pack(side="left")

        tk.Label(
            header,
            text="8 weeks · 48 sessions · 1 hour a day",
            bg=self.BG,
            fg=self.MUTED,
            font=("DejaVu Sans", 9),
            anchor="w",
        ).pack(side="left", padx=(12, 0), pady=(6, 0))

        progress = tk.Frame(self, bg=self.BG)
        progress.pack(fill="x", padx=18, pady=(0, 10))

        self.progress_label = tk.Label(
            progress,
            text="",
            bg=self.BG,
            fg=self.INK,
            font=("DejaVu Sans", 10, "bold"),
            anchor="w",
        )
        self.progress_label.pack(fill="x")

        self.progress_var = tk.DoubleVar(value=0)
        self.bar = ttk.Progressbar(
            progress,
            style="Bar.Horizontal.TProgressbar",
            variable=self.progress_var,
            maximum=len(LESSONS),
            length=100,
        )
        self.bar.pack(fill="x", pady=(4, 0))

        body = tk.Frame(self, bg=self.BG)
        body.pack(fill="both", expand=True, padx=(18, 8), pady=(0, 0))

        self.canvas = tk.Canvas(body, bg=self.BG, highlightthickness=0)
        scroll = ttk.Scrollbar(body, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=scroll.set)
        self.canvas.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y", padx=(0, 6))

        self.inner = tk.Frame(self.canvas, bg=self.BG)
        window = self.canvas.create_window((0, 0), window=self.inner, anchor="nw")
        self.inner.bind(
            "<Configure>", lambda _e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        self.canvas.bind(
            "<Configure>", lambda e: self.canvas.itemconfigure(window, width=e.width)
        )

        self._build_cards()

        footer = tk.Frame(self, bg=self.BG)
        footer.pack(fill="x", padx=18, pady=(4, 12))
        tk.Label(
            footer,
            text=f"Saved automatically to {DATA_FILE.name}",
            bg=self.BG,
            fg=self.MUTED,
            font=("DejaVu Sans", 8),
            anchor="w",
        ).pack(side="left")

        self.bind_all("<MouseWheel>", self._on_mousewheel)
        self.bind_all("<Button-4>", self._on_mousewheel)
        self.bind_all("<Button-5>", self._on_mousewheel)

    def _build_cards(self) -> None:
        current_week = None
        card = rows = None
        row_index = 0

        for lesson in self.data["lessons"]:
            week = lesson["week"]
            if week != current_week:
                current_week = week
                card, rows, row_index = self._new_week_card(week)

            lid = lesson["id"]
            var = tk.BooleanVar(value=lesson.get("status") == "done")
            self.vars[lid] = var

            line = tk.Frame(rows, bg=self.CARD)
            line.pack(fill="x", padx=8, pady=1)

            check = ttk.Checkbutton(
                line,
                text=f"Day {lesson['day']}  ·  {lesson['title']}",
                variable=var,
                style="Lesson.TCheckbutton",
                command=lambda item=lesson, value=var: self._toggle(item, value),
            )
            check.pack(side="left", fill="x", expand=True)

            date_label = tk.Label(
                line,
                text="",
                bg=self.CARD,
                fg=self.MUTED,
                font=("DejaVu Sans", 8),
                width=12,
                anchor="e",
            )
            date_label.pack(side="right", padx=(0, 6))
            self.date_labels[lid] = date_label
            row_index += 1

    def _new_week_card(self, week: int):
        card = tk.Frame(
            self.inner,
            bg=self.CARD,
            highlightbackground="#dedcd3",
            highlightthickness=1,
        )
        card.pack(fill="x", padx=4, pady=(0, 8))

        head = tk.Frame(card, bg=self.CARD)
        head.pack(fill="x", padx=10, pady=(8, 2))

        title = tk.Label(
            head,
            text="",
            bg=self.CARD,
            fg=self.INK,
            font=("DejaVu Sans", 11, "bold"),
            anchor="w",
        )
        title.pack(side="left")
        self.week_labels[week] = title

        tk.Frame(card, bg="#eceae3", height=1).pack(fill="x", padx=10, pady=(0, 3))

        rows = tk.Frame(card, bg=self.CARD)
        rows.pack(fill="x", pady=(0, 6))
        return card, rows, 0

    def _toggle(self, lesson: dict, var: tk.BooleanVar) -> None:
        done = var.get()
        lesson["status"] = "done" if done else "todo"
        lesson["completed"] = date.today().isoformat() if done else ""
        save_data(self.data)
        self._refresh()

    def _refresh(self) -> None:
        done = sum(1 for item in self.data["lessons"] if item.get("status") == "done")
        total = len(self.data["lessons"])
        percent = round(done * 100 / total) if total else 0
        self.progress_label.config(text=f"{done} / {total} sessions complete  ·  {percent}%")
        self.progress_var.set(done)

        for week in sorted(WEEK_TITLES):
            week_lessons = [i for i in self.data["lessons"] if i["week"] == week]
            week_done = sum(1 for i in week_lessons if i.get("status") == "done")
            self.week_labels[week].config(
                text=f"Week {week}  ·  {WEEK_TITLES[week]}    {week_done}/{len(week_lessons)}"
            )

        for item in self.data["lessons"]:
            label = self.date_labels.get(item["id"])
            if label is None:
                continue
            label.config(text=f"✓ {item['completed']}" if item.get("completed") else "")

    def _on_mousewheel(self, event) -> None:
        if getattr(event, "num", None) == 4:
            self.canvas.yview_scroll(-1, "units")
        elif getattr(event, "num", None) == 5:
            self.canvas.yview_scroll(1, "units")
        else:
            self.canvas.yview_scroll(int(-event.delta / 120), "units")


def main() -> None:
    app = TrackerApp()
    app.mainloop()


if __name__ == "__main__":
    main()
