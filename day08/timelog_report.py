import sys
import re
from datetime import datetime
from collections import defaultdict

def parse_log_file(filename):
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]
    
    entries = []
    for line in lines:
        match = re.match(r'(\d{2}:\d{2}) (.+)', line)
        if match:
            time_str, label = match.groups()
            time_obj = datetime.strptime(time_str, '%H:%M')
            entries.append((time_obj, label))
    return entries

def compute_durations(entries):
    sessions = []
    for i in range(len(entries) - 1):
        start_time, label = entries[i]
        end_time = entries[i + 1][0]
        duration = int((end_time - start_time).total_seconds() / 60)
        sessions.append((start_time.strftime('%H:%M'), end_time.strftime('%H:%M'), label, duration))
    return sessions

def summarize_sessions(sessions):
    summary = defaultdict(int)
    for _, _, label, duration in sessions:
        summary[label] += duration
    return summary

def print_report(sessions, summary):
    for start, end, label, _ in sessions:
        print(f"{start}–{end} {label}")
    print()

    total = sum(summary.values())
    for label in sorted(summary):
        minutes = summary[label]
        percent = round((minutes / total) * 100)
        print(f"{label:<20} {minutes:>3} minutes {percent:>2}%")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python timelog_report.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    entries = parse_log_file(filename)
    sessions = compute_durations(entries)
    summary = summarize_sessions(sessions)
    print_report(sessions, summary)
