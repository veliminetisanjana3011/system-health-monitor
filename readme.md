# System Health Monitor

A lightweight, beginner-friendly Python console application that monitors and reports your system's core vital metrics in real-time on Windows:

- **CPU Usage:** Overall percentage load and physical/logical core counts.
- **RAM (Memory) Usage:** Total, used, available memory, and usage percentage.
- **Disk Usage:** Total, used, free storage, and percentage utilization for your main Windows drive (e.g. `C:\`).

---

## Project Structure

```text
system_health_monitor/
├── main.py          # Main monitoring script
├── requirements.txt # Project dependencies (psutil)
└── readme.md        # Documentation and running instructions
```

---

## Prerequisites

- **Python 3.8+** installed on Windows.
- Make sure Python and `pip` are added to your Windows `PATH`. You can verify by opening PowerShell or Command Prompt and running:
  ```powershell
  python --version
  pip --version
  ```

---

## Installation & Setup on Windows

### 1. Open Terminal in the Project Folder
Open PowerShell or Command Prompt and navigate to the project directory:
```powershell
cd C:\Users\HP\.gemini\antigravity\scratch\system_health_monitor
```

### 2. (Optional but Recommended) Create a Virtual Environment
Create and activate an isolated virtual environment:
```powershell
python -m venv venv
.\venv\Scripts\activate
```
*(If you see an execution policy warning in PowerShell, you can run `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` or activate via Command Prompt).*

### 3. Install Dependencies
Install the required `psutil` library:
```powershell
pip install -r requirements.txt
```

---

## Running the Application

Execute the script with:
```powershell
python main.py
```

- The monitor refreshes every 2 seconds with clean visual ASCII bars.
- To exit the program at any time, press **`Ctrl + C`**.

---

## How to Test

1. **Idle Test:** Run `python main.py` when your PC is idle and note the baseline metrics.
2. **CPU / RAM Activity Test:** Open multiple browser tabs, launch an application, or run a video. Notice the CPU and RAM percentages dynamically increase.
3. **Graceful Exit Test:** Press `Ctrl + C` in your terminal window and verify that the script cleanly terminates with `Monitor stopped. Goodbye!`.
