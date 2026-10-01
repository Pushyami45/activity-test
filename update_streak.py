import os, subprocess
from datetime import datetime, timedelta

def run(commands):
    subprocess.run(commands, check=True)

def commit_for_date(date_str):
    msg = f"Contribution: {date_str} 20:00"
    with open("README.md", "a") as f:
        f.write(msg + "\n\n")
    run(["git", "add", "."])
    
    # We need to set GIT_AUTHOR_DATE and GIT_COMMITTER_DATE to properly spoof the commit date
    env = os.environ.copy()
    env["GIT_AUTHOR_DATE"] = f"{date_str} 20:00:00"
    env["GIT_COMMITTER_DATE"] = f"{date_str} 20:00:00"
    
    # Use format that works on Windows
    # Passing the strings carefully
    subprocess.run(["git", "commit", "-m", msg], env=env, check=True)

# Generate yesterday's and today's dates based on current time (2026-10-02)
# The prompt says today is 2026-10-02.
# So yesterday is 2026-10-01.
yesterday = "2026-10-01"
today = "2026-10-02"

commit_for_date(yesterday)
commit_for_date(today)
print("Commits created! Pushing to origin main...")
run(["git", "push", "-u", "origin", "main"])
print("Pushed successfully!")
