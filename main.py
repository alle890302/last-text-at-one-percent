"""Last Text at One Percent — make.fun entry.

Final text (pass 1, kept): the dying phone confesses the one job it did
for its owner for years — keeping the ex blocked — and resigns from it
in its last breath. Judge criteria: (1) final text from a dying phone
at 1%, funny; (2) the turn lands on the last clause ("You're on your
own now" — the protection ends with the battery); (3) the phone's own
voice, a personality with a stake in dying; (4) short, punchy, reads
like a real text; (5) fresh — no low-battery pun, no charger goodbye,
no "1%" wordplay.

Pass 2 challenger (rejected): "I deleted your search history. That's
the last kind thing I'll ever do." (71 chars) — also a real turn, but
the search-history-deletion gag is a well-worn trope, while the ex-block
is a fresher, more phone-specific job (the phone itself did the
blocking for three years). Pass 1 wins on criterion 5 and its punch is
tighter: the protection the owner never noticed vanishes with the phone.
"""
import os

ENTRY = "I kept your ex's number blocked for three years. You're on your own now."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
    f.write(ENTRY)
