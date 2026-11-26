import os

LINE = "My smart fridge sends me a weekly report on my eating habits. I send it a weekly report on its humming. It never replies."
MAX_CHARS = 200

if len(LINE) > MAX_CHARS:
    raise ValueError("entry line must be 200 characters or fewer")

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE + "\n")
