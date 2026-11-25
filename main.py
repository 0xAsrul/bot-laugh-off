import os

LINE = "My phone died mid-apology, so now my ex thinks I ghosted her on purpose."

# Gate (competition.yaml): /output/entry.txt must be UTF-8 text of
# 1 to 200 characters, not only white space, exactly one line.
assert "\n" not in LINE and "\r" not in LINE, "entry must be a single line"
assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
assert LINE.strip() != "", "entry must not be only white space"

print(LINE)

# The sealed scorer reads /output/entry.txt, not stdout, so write the
# exact same line there. A failed write must never break stdout.
try:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
except OSError:
    pass
