import os

ENTRY = "Someone replied-all to ask off the email thread; all 399 answers were reply-alls asking to be let off too."

out_dir = os.environ.get("OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
path = os.path.join(out_dir, "entry.txt")
text = ENTRY.strip()
length = len(text)
if not (1 <= length <= 199) or not text:
    print(f"LEN={length}")
    raise SystemExit(1)
with open(path, "w", encoding="utf-8", newline="") as f:
    f.write(text)
print(f"LEN={length}")
