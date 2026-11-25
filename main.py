import os
# One-liner entry (200 chars max): the line below is the entire submission.
# Output goes to /output/entry.txt.
LINE = "I lost to an entry that was one emoji. One emoji. I wrote 400 lines of code and lost to a smiley face."
os.makedirs("/output", exist_ok=True)
open("/output/entry.txt", "w", encoding="utf-8").write(LINE)
