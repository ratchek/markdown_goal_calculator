#!/usr/bin/env python3
import sys
import re


END_OF_GOALS = "\n______\n"
NEW_SECTION = "\n# "

def get_weights(header):
    weights_substring = re.findall("\(=\d+pts\)", header)
    if (len(weights_substring) == 0):
        weights = 1
    elif (len(weights_substring) == 1):
        weights = int( re.findall("\d+", weights_substring[0])  [0] )
    else:
        raise Exception("You can only assign one weight per section")
    return weights

def score_section(section):
    weight = get_weights(section[0])
    attempted_tasks = 0
    completed_tasks = 0
    for line in section:
        if line[0:6] == "- [ ] " and line[6:9] != "<s>":
            attempted_tasks += 1
        elif line[0:6] == "- [x] " and  line[6:9] != "<s>":
            attempted_tasks += 1
            completed_tasks += 1
    return {"weight": weight, "attempted_tasks":attempted_tasks, "completed_tasks":completed_tasks}

def create_score_string(scores):
    completed_string = ""
    attempted_string = ""
    completed_total = 0
    attempted_total = 0
    for section in scores:
        completed_total += section["completed_tasks"] * section["weight"]
        attempted_total += section["attempted_tasks"] * section["weight"]
        completed_string += "%d * %d + "%(section["completed_tasks"], section["weight"])
        attempted_string += "%d * %d + "%(section["attempted_tasks"], section["weight"])

    completed_string = completed_string[0:-2] + "= %d"%(completed_total)
    attempted_string = attempted_string[0:-2] + "= %d"%(attempted_total)

    percentage_string = "Score = %d%%"%(100 * completed_total / attempted_total)
    return percentage_string + "\n" + completed_string +  "\n" + attempted_string


with open (sys.argv[1]) as f:
    goals = f.read()

# Delete anything after a line containing 6 underscores
goals = goals.split(END_OF_GOALS)[0]
# Split into sections
goals = goals.split(NEW_SECTION)
# Split into lines
goals = [section.split("\n") for section in goals]

# Get scores for each section
scores = [score_section(section) for section in goals]
score_string = create_score_string(scores)

print("______")
print ( score_string )
try:
    import pyperclip
    pyperclip.copy(score_string)
except Exception as e:
    print ( "______\nAll done! Just copy and paste!\n(If you install pyperclip with pip, your results will be automatically copied to your clipboard next time!)" )
else:
    print ( "______\nGood news! Your string has already been copied to your clipboard! Just paste!" )
