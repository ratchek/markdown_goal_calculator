This is a personal tool for calculating how well I followed my weekly schedule.
Basically calculates the weighted sum for total and completed tasks using markdown checkmarks and headers as syntax. 
Works specifically for the type of formatting I follow in my files and doubt it will be useful to anyone else.

## Running the calculator
`python markdown-goal-calculator.py name-of-text-file-with-goals`

## General Syntax
"______" (six underscores) denote file end. Nothing after that will be counted.

Each section starts with a "# " (a markdown heading).

## Weights
Each section can have custom weights.
To add specific weights to a section, include "(=5pts)" somewhere in the section header,
but replace the 5 with a desired weight (can use multiple digits).
The default weight, if none is included is 1.

## Scoring
Every line starting with an empty markdown checkmark "- [ ] " is counted as a task attempted
but not completed. (Notice the space before the brackets, inside the brackets, and after the brackets).

Every line starting with an filed markdown checkmark "- [x] " is counted as a task successfully completed.
(Notice the space before the brackets, no spaces inside the brackets, and space after the brackets).

If you include a html strike-through tag right after the markdown checkmark "- [ ] \<s>",
then the task will not be counted at all.

## pyperclip
If you have pyperclip installed (you can get it with pip), then the results of the calculation will be automatically
added to your system's clipboard, so you can just paste them wherever you'd like.
