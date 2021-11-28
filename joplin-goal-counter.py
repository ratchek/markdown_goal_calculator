#!/usr/bin/env python3
import sys


def count_totals(file):
    total = 0
    completed = 0
    while (True):
        line = f.readline()
        if line == "\n":
            pass
        elif line[0:6] == "- [ ] ":
            total += 1
        elif line[0:6] == "- [x] ":
            total += 1
            completed += 1
        else:
            return (completed, total)

def create_score_string(lc, la, sc, sa,):
    score_string = '''Score = %d%%
%d*3 + %d*1 = %d
%d*3 + %d*1 = %d'''
    total_completed = 3 * lc + 1 * sc
    total_attempted = 3 * la + 1 * sa
    percentage = 100 * total_completed / total_attempted
    return score_string%(percentage, lc, sc, total_completed, la, sa, total_attempted)


with open (sys.argv[1]) as f:
    while (f.readline()[:7] != "## Long"):
        pass
    (completed_long, total_long) = count_totals(f)
    (completed_short, total_short) = count_totals(f)

score_string = create_score_string(completed_long, total_long, completed_short, total_short)
print("--------------")
print ( score_string )
try:
    import pyperclip
    pyperclip.copy(score_string)
except Exception as e:
    print ( "--------------\nAll done! Just copy and paste!\n(If you install pyperclip with pip, your results will be automatically copied to your clipboard next time!)" )
else:
    print ( "--------------\nGood news! Your string has already been copied to your clipboard! Just paste!" )


