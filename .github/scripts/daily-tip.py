import json
import re
import datetime
import pathlib

TIPS_PATH = pathlib.Path(".github/scripts/tips.json")
README_PATH = pathlib.Path("README.md")

with open(TIPS_PATH, encoding="utf-8") as f:
    tips = json.load(f)

# Deterministic pick from the day-of-year so the same day always shows the same tip.
idx = datetime.date.today().timetuple().tm_yday % len(tips)
tip = tips[idx]

text = README_PATH.read_text(encoding="utf-8")
new_text = re.sub(
    r"<!-- DAILY-TIP:START -->.*?<!-- DAILY-TIP:END -->",
    f"<!-- DAILY-TIP:START -->\n> 💡 {tip}\n<!-- DAILY-TIP:END -->",
    text,
    flags=re.S,
)
README_PATH.write_text(new_text, encoding="utf-8")
print("daily tip:", tip)
