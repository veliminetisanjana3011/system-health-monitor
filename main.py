"""
Simple System Health Monitor
Monitors and displays CPU, RAM, and Disk usage in real time.
"""

import os
import sys
import time
import psutil


def format_bytes(bytes_value: int) -> str:
    """Convert raw byte count into a human-readable string (GB, MB, etc.)."""
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if bytes_value < 1024.0:
            return f"{bytes_value:.2f} {unit}"
        bytes_value /= 1024.0
    return f"{bytes_value:.2f} PB"


def render_bar(percentage: float, length: int = 25) -> str:
    """Generate an ASCII progress bar for metric percentages."""
    filled_length = int(length * (percentage / 100.0))
    bar = "#" * filled_length + "-" * (length - filled_length)
    return f"[{bar}] {percentage:5.1f}%"


def display_health_metrics():
    """Fetch and print system resource usage metrics."""
    # 1. CPU Usage
    cpu_percent = psutil.cpu_percent(interval=1)
    cpu_cores_physical = psutil.cpu_count(logical=False) or 1
    cpu_cores_logical = psutil.cpu_count(logical=True) or 1

    # 2. RAM (Memory) Usage
    memory = psutil.virtual_memory()

    # 3. Disk Usage (Determining root drive on Windows, e.g., C:\)
    current_drive = os.path.splitdrive(os.path.abspath("."))[0] + "\\"
    if not current_drive.strip("\\"):
        current_drive = "C:\\"
    disk = psutil.disk_usage(current_drive)

    # Clear terminal screen if running in an interactive terminal
    if sys.stdout.isatty():
        os.system("cls" if os.name == "nt" else "clear")

    print("=" * 60)
    print("               SYSTEM HEALTH MONITOR")
    print("=" * 60)
    print(f"Timestamp: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")

    # CPU Section
    print("--- CPU USAGE ---")
    print(f"Cores       : {cpu_cores_physical} Physical / {cpu_cores_logical} Logical")
    print(f"Usage       : {render_bar(cpu_percent)}\n")

    # RAM Section
    print("--- RAM (MEMORY) USAGE ---")
    print(f"Total       : {format_bytes(memory.total)}")
    print(f"Used        : {format_bytes(memory.used)}")
    print(f"Available   : {format_bytes(memory.available)}")
    print(f"Usage       : {render_bar(memory.percent)}\n")

    # Disk Section
    print(f"--- DISK USAGE ({current_drive}) ---")
    print(f"Total       : {format_bytes(disk.total)}")
    print(f"Used        : {format_bytes(disk.used)}")
    print(f"Free        : {format_bytes(disk.free)}")
    print(f"Usage       : {render_bar(disk.percent)}")

    print("\n" + "=" * 60)
    print("Press Ctrl+C to exit.")
    sys.stdout.flush()


def main():
    print("Starting System Health Monitor... (Press Ctrl+C to quit)")
    try:
        while True:
            display_health_metrics()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\nMonitor stopped. Goodbye!")
        sys.exit(0)


if __name__ == "__main__":
    main()
