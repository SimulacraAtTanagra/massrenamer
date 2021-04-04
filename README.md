## The purpose of this project is as follows:
This file renames `print`ed timesheet files using their contents, iterating over all files in a directory.
## Here's some back story on why I needed to build this:
Timesheet files, like so many output files from report writers, come across as blind (with filenames that do not betray their contents). This project uses the specifically structured contents of timesheets to name their host files into something more represnetative. 
## This project leverages the following libraries:
pandas, fuzzywuzzy, textract
## In order to use this, you'll first need do the following:
Timesheet files from a SOTA system such as PR-Assist, AEMS, or HR-Assist.
## The expected frequency for running this code is as follows:
As Needed