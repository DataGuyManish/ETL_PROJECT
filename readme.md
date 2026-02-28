# 🐍 ETL Pipeline with Structured Python Logging

This project was built while learning **Python Data Engineering** from scratch. It is a complete Extract → Transform → Load pipeline that reads raw student data, cleans it by removing invalid records, and saves the output — with every step logged to both the terminal and a persistent log file using Python's built-in `logging` module.

The focus was not just making the pipeline work, but building it the way it would be built in a real job — modular, observable, and debuggable.

---

## 🧰 Tools Used

| Tool         | Purpose 
|------        |--------
| Python 3.13  | Core language 
| pandas       | Reading, filtering, and saving CSV data 
| pathlib      | Cross-platform file path handling 
| logging      | Structured pipeline logging to terminal and file 
| venv         | Isolated Python environment 

---

## 📊 Dataset

The dataset **Student_details.csv** contains 20 records and includes:

- Student name, age, grade, subject, score, and email
- Intentionally dirty data — missing names, invalid ages, empty grades
- Used to simulate real-world messy input data in a pipeline

---

## 🧹 Data Cleaning Summary (Transform Step)

- Dropped rows where **name** was missing or empty
- Dropped rows where **age** was not a valid number (e.g. `"abc"`, `"twenty"`, `"xyz"`)
- Dropped rows where **grade** was missing or empty
- Used `pd.to_numeric(errors="coerce")` to safely catch invalid age values without crashing
- Logged every dropped row with count and reason at `WARNING` level

---

## 🔄 Pipeline Stages

**1. Extract — `extract.py`**
- Reads raw CSV using `pandas`
- Builds file path dynamically using `pathlib` so it works on any machine
- Logs rows loaded and returns the DataFrame to the next stage
- Catches `FileNotFoundError` and stops the pipeline with a full traceback if file is missing

**2. Transform — `transform.py`**
- Applies three cleaning rules in sequence
- Tracks row count before and after each rule to calculate rows dropped
- Logs a `WARNING` for every rule that drops rows, with exact count and reason
- Returns the cleaned DataFrame

**3. Load — `load.py`**
- Creates the output folder automatically if it does not exist
- Saves cleaned DataFrame to `data/cleaned_data/cleaned_students.csv`
- Logs the number of rows saved and the full output path
- Catches and logs any save errors with full traceback

**4. Orchestration — `main.py`**
- Calls extract → transform → load in order
- Wraps full pipeline in `try/except`
- Logs `PIPELINE STARTED` and `PIPELINE COMPLETED` at `INFO` level
- Logs `PIPELINE FAILED` at `CRITICAL` level if anything goes wrong

---

## 📋 Logging Architecture

A single reusable function `get_logger(__name__)` is defined once in `utils/logger_setup.py` and imported by every file. Logs are written to two destinations simultaneously:

- **Terminal** → `INFO` and above (important milestones only)
- **pipeline.log** → `DEBUG` and above (captures everything including debug detail)

Every log line includes a timestamp, the module name, the severity level, and the message — so it is always clear when something happened, where it came from, and how serious it was.

---

## 🗂️ Folder Structure

```
ETL_PROJECT/
├── src/
│   ├── utils/
│   │   └── logger_setup.py
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── main.py
├── data/
│   ├── raw/
│   │   └── Student_details.csv
│   └── cleaned_data/
│       └── cleaned_students.csv
├── pipeline.log
├── requirements.txt
└── README.md ✅
```

---

## 💡 Key Things I Implemented

- **No `print()` anywhere** — every message goes through the logging system with proper levels and timestamps
- **Named loggers** — each module calls `get_logger(__name__)` so logs show exactly which file produced each message
- **Dual output** — terminal shows `INFO+`, log file captures everything including `DEBUG`
- **`logger.exception()`** — used inside every `except` block to capture full tracebacks automatically
- **`pathlib`** — all file paths are built relative to the script so the project runs on any machine
- **`mkdir(exist_ok=True)`** — output folder is created automatically, no manual setup needed
- **`if __name__ == "__main__"`** — each file can be run and tested independently

---

## 👨‍💻 Author

**Manish**
📧 **ms1717265@gmail.com**
