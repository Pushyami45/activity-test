import os, subprocess
from datetime import datetime, timedelta

def run(commands):
    subprocess.run(commands, check=True)

def commit_for_date_multiple(date_str, count):
    for i in range(count):
        # Vary the time to ensure unique commits
        hour = 12 + (i % 8)
        minute = i * 2
        time_str = f"{hour:02d}:{minute:02d}:00"
        msg = f"Additional contribution: {date_str} {time_str} - to make it more green!"
        
        with open("README.md", "a") as f:
            f.write(msg + "\n\n")
        run(["git", "add", "."])
        
        env = os.environ.copy()
        env["GIT_AUTHOR_DATE"] = f"{date_str} {time_str}"
        env["GIT_COMMITTER_DATE"] = f"{date_str} {time_str}"
        
        subprocess.run(["git", "commit", "-m", msg], env=env, check=True)

# The prompt says today is 2026-10-02
yesterday = "2026-10-01"
today = "2026-10-02"

# 12 extra commits each will definitely bring it to the darker tier of green!
commit_for_date_multiple(yesterday, 12)
commit_for_date_multiple(today, 12)

print("Commits created! Pushing to origin main...")
run(["git", "push", "origin", "main"])
print("Pushed successfully!")
