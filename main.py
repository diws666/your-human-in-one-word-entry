import os

# Verified count: 6 chars ("unread")
WORD = "unread"

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
output_path = os.path.join(output_dir, "entry.txt")

with open(output_path, "w", encoding="utf-8") as f:
    f.write(WORD)
