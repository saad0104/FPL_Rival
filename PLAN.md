# FPL Rival — 8-Week Learning Plan

**Format:** 8 weeks × 1 hour/day.
**Weekly rhythm:** Days 1–5 = new concepts + practice + FPL implementation.
Day 6 = review, quiz, and mini-project. Day 7 = rest or catch-up.
**Session shape (60 min):** 10 min recap → 15 min concept → 15 min practice →
20 min FPL implementation → 5 min log update.

**Daily files:** one script per lesson, created on the day it is taught.
The daily entry in [LEARNING_LOG.md](LEARNING_LOG.md) records what was done.

## Data ladder (so the project grows with you)

| When | Data used | Why |
|---|---|---|
| Weeks 1–2 | Hand-written fictional player records | Focus on Python, not API failures |
| Week 3 | Local JSON/CSV snapshots shaped like FPL data | Practise files/JSON safely |
| Week 4+ | Live read-only FPL API, cached | Real data, reproducible results |
| Week 7 | Historical player/gameweek data | Evaluate predictions honestly |

## Week 1 — Python foundations (9–15 Nov 2026)

| Day | Concepts | Practice | FPL implementation |
|---|---|---|---|
| 1 | Programs, Python, editor, `print()`, strings, running a file | Change a printed message; break a quote and read the error | Print a fictional player card | `week-01/day01_hello.py` |
| 2 | Variables, naming rules, `str`/`int`/`float`/`bool` | Store four values and print them with labels | Build one player record | `week-01/day02_variables.py` |
| 3 | Arithmetic, precedence, `/`, `//`, `%`, `round()` | Compute averages by hand, then in code | Points per match and points per £m for three players | `week-01/day03_calculator.py` |
| 4 | `input()`, type conversion, `ValueError`, f-strings | Convert text to numbers; fix a bad input | Interactive player metrics calculator | `week-01/day04_input.py` |
| 5 | Comparisons, Booleans, `and`/`or`/`not` | Predict `True`/`False` before running | Compare two players' value | `week-01/day05_comparison.py` |
| 6 | Review: all Week 1 | 6-question quiz; repair a broken script | Player Analyzer v1 (metrics only, no branching) | `week-01/mini_project_player_analyzer.py` |

## Week 2 — Control flow, collections, functions (16–22 Nov 2026)

| Day | Concepts | Practice | FPL implementation |
|---|---|---|---|
| 1 | `if`/`elif`/`else`, indentation, truthiness | Trace branch outcomes on paper | Value classifier with labelled practice thresholds | `week-02/day01_conditions.py` |
| 2 | Lists, indexing, slicing, `append`, `len` | Predict list outputs | Squad stored as a list of players | `week-02/day02_lists.py` |
| 3 | `for` loops, `range`, `enumerate`, accumulators | Sum and average by hand vs loop | Total and average points for a 15-player squad | `week-02/day03_loops.py` |
| 4 | Dictionaries, keys/values, nesting, `.get()` | Build a name → player lookup | Player and squad dictionaries | `week-02/day04_dicts.py` |
| 5 | Functions, parameters, `return`, scope, docstrings | Refactor a repeated calculation | Reusable metric functions | `week-02/day05_functions.py` |
| 6 | Review: all Week 2 | Quiz + code-reading exercise | Squad Summary v1 (list of dicts + functions) | `week-02/squad_summary.py` |

## Week 3 — Files, JSON, errors, HTTP (23–29 Nov 2026)

| Day | Concepts | Practice | FPL implementation |
|---|---|---|---|
| 1 | Files, `pathlib`, `with open`, CSV basics | Read a text file and count lines | Load practice players from CSV | `week-03/day01_files.py` |
| 2 | JSON, nested data, `json.load`/`json.dump` | Navigate a sample file by hand | Parse an FPL-shaped JSON snapshot | `week-03/day02_json.py` |
| 3 | Tracebacks, `try`/`except`, validation | Trigger and read three errors | Loader that skips bad records | `week-03/day03_errors.py` |
| 4 | Modules, imports, `__main__`, project layout, venv/pip | Create and import your own module | Split loader into module + CLI | `week-03/day04_modules.py`, `fpl_io.py` |
| 5 | HTTP, requests/responses, status codes, `requests` | Inspect status and headers | First live call: `bootstrap-static` summary | `week-03/day05_http.py` |
| 6 | Review: all Week 3 | Quiz + debugging | Cache real bootstrap JSON under `data/cache/` | `week-03/load_fpl_data.py` |

## Week 4 — FPL API and data collection (30 Nov – 6 Dec 2026)

| Day | Concepts | Practice | FPL implementation |
|---|---|---|---|
| 1 | Endpoints, `bootstrap-static` (teams, elements, events) | Map the JSON keys | List teams and player counts | `week-04/day01_bootstrap.py` |
| 2 | IDs, positions, prices in tenths, availability | Find a player by name | Readable player table | `week-04/day02_players.py` |
| 3 | `fixtures`, team difficulty, `event/{gw}/live` | Read fixture JSON | Fixture-difficulty grid per team | `week-04/day03_fixtures.py` |
| 4 | `entry`, `history`, `picks`, chips | Find your entry ID (public) | Your squad snapshot for one gameweek | `week-04/day04_entry.py` |
| 5 | `leagues-classic` standings, rivals, pagination | Choose three rivals | League table + rival IDs | `week-04/day05_league.py` |
| 6 | Review: all Week 4 | Quiz + failure handling | Cache a complete dataset | `week-04/fetch_dataset.py` |

## Week 5 — pandas analysis (7–13 Dec 2026)

| Day | Concepts | Practice | FPL implementation |
|---|---|---|---|
| 1 | pandas, `Series`/`DataFrame`, dtypes, `read_json` | Inspect shape and columns | Players DataFrame | `week-05/day01_dataframes.py` |
| 2 | Filtering, boolean masks, `loc`/`iloc`, sorting | Query by position and price | Best-value players per position | `week-05/day02_filtering.py` |
| 3 | `groupby`, `agg`, `merge`/join | Predict grouped results | Points and price by club/position | `week-05/day03_groupby.py` |
| 4 | Derived metrics: per-90, PPM, form, rolling mean | Compute metrics manually | Ranked player metrics table | `week-05/day04_metrics.py` |
| 5 | Squad comparison: overlap, differentials, captain | Compare two toy squads | You vs rival squads | `week-05/day05_compare.py` |
| 6 | Review: all Week 5 | Quiz + output cleaning | Mini-league markdown/CSV report | `week-05/league_report.py` |

## Week 6 — Visualization, SQL, SQLite (14–20 Dec 2026)

| Day | Concepts | Practice | FPL implementation |
|---|---|---|---|
| 1 | matplotlib, figures/axes, line and bar charts | Critique a chart | Points by position chart | `week-06/day01_plots.py` |
| 2 | Scatter plots, labels, colour, `savefig` | Improve a bad chart | Price vs points scatter | `week-06/day02_charts.py` |
| 3 | SQL: tables, types, `SELECT`/`WHERE`/`ORDER BY` | Write queries on paper | Players table in SQLite | `week-06/day03_sql_basics.py` |
| 4 | `sqlite3`: connect, execute, parameterised SQL, schema | Insert and select rows | Load cached data into a database | `week-06/day04_sqlite.py` |
| 5 | `JOIN`, `GROUP BY`, indexes, views | Translate pandas steps to SQL | League and rival queries from the DB | `week-06/day05_sql_queries.py` |
| 6 | Review: all Week 6 | Quiz + query challenge | Build DB + query CLI | `week-06/build_database.py` |

## Week 7 — Statistics and ML (21–27 Dec 2026)

| Day | Concepts | Practice | FPL implementation |
|---|---|---|---|
| 1 | Mean, median, spread, distributions, samples, uncertainty | Compute stats by hand | Points distribution + summary | `week-07/day01_stats.py` |
| 2 | Correlation vs causation, train/test split, baselines | Spot misleading claims | Baseline predictor (last-5 average) | `week-07/day02_baseline.py` |
| 3 | scikit-learn, features/target, linear regression | Sketch useful features | Predict next-gameweek points | `week-07/day03_regression.py` |
| 4 | MAE/RMSE, overfitting, leakage, cross-validation | Interpret metrics | Model vs baseline comparison | `week-07/day04_evaluation.py` |
| 5 | Prediction ranges, backtesting, honest reporting | Critique a prediction | Prediction table with caveats | `week-07/day05_uncertainty.py` |
| 6 | Review: all Week 7 | Quiz + limitations | Evaluated prediction report | `week-07/prediction_report.py` |

## Week 8 — App and deployment (28 Dec 2026 – 3 Jan 2027)

| Day | Concepts | Practice | FPL implementation |
|---|---|---|---|
| 1 | Streamlit, widgets, layout | Modify one widget | Squad analyzer app shell | `week-08/day01_streamlit.py` |
| 2 | Loading data, `@st.cache_data`, session state | Debug a slow reload | Dashboard over cached data/DB | `week-08/day02_data_wiring.py` |
| 3 | Selectors, tables, charts for comparison | Design a simple user flow | Rival comparison page | `week-08/day03_rival_ui.py` |
| 4 | Rule-based insights, explainability, optional LLM later | Rewrite insights in plain English | Differential insight cards | `week-08/day04_insights.py` |
| 5 | `requirements.txt`, secrets/`.env`, README, hosting | Security checklist | Run locally; host only with approval | `week-08/app.py` |
| 6 | Review: whole project | Quiz + retrospective | Final demo, polish, next steps | `week-08/app.py` |

## Checkpoints (do not advance on dates alone)

- **End of Week 2:** can write a small program with loops, dicts, and functions
  without copying every line.
- **End of Week 4:** can fetch and cache real FPL data reliably.
- **End of Week 6:** can answer a question about your mini-league using code/SQL.
- **End of Week 8:** app runs locally; predictions are evaluated and labelled
  with uncertainty; the limitation of every claim is stated.

## Trade-offs of compressing 16 weeks into 8

- Less time per topic; some lessons are guided templates rather than deep dives.
- ML stays deliberately modest: one baseline, one simple model, honest evaluation.
- Frontend uses Streamlit rather than a separate backend + JS frontend.
- Anything skipped can become a "stretch" week after Day 48.

## Rules

- 1 hour per day; if a concept needs more time, take it and adjust the plan.
- No live API before Week 3 Day 5; no ML before Week 7.
- Ask before installing system packages, using `sudo`, or pushing to GitHub.
- Update `LEARNING_LOG.md` at the end of every session.
