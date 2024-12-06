# Theory-Project-2-tessa


Team Name: tessa

Team members names and netids: Tessa Berning, tberning

Overall project attempted, with sub-projects: Tracing NTM behavior

Overall success of the project: Successfully traces NTM behavior and returns proper metrics

Approximately total time (in hours) to complete: 4-5 hours

Link to github repository: you're here

List of included files (if you have many files of a certain type, such as test files of different sizes, list just the folder): (Add more rows as necessary). Add more rows as necessary.

File/folder Name
File Contents and Use
Code Files
traceTM_tessa.py
This is the actual program that traces the NTM and returns the necessary metrics
Test Files
a_plus_DTM.csv
Input file for deterministic a plus machine
a_plus.csv
Input file for nondeterministic a plus machine
abc_star_DTM.csv
Input file for deterministic a*b*c* machine
abc_star.csv
Input file for nondeterministic a*b*c* machine
equal_01s_DTM.csv
Input file for deterministic equal 0s and 1s  machine
equal_01s.csv
Input file for nondeterministic equal 0s and 1s machine

Output Files
output_tessa.csv
Stores the results of all 6 different machines and 2 different strings for the NTM ones

Plots (as needed)
N/A
N/A

Programming languages used, and associated libraries: python – csv and sys

Key data structures (for each sub-project): list of list that stores all the transitions, list of list of lists that stores the final tree

General operation of code (for each subproject): read in all of the information from the csv input file. Have an array that stores the final tree. Loop through the different levels in the tree and within the levels, loop through the different configurations. For each configuration, loop through the transitions and see which ones match the current state and input character. Create the next configuration from that transition and append it to the array that stores all of the configurations for the next level of the tree. After going through the whole current level, append that array to the final array. Once we reach q accept or the max depth or all of the states are in q reject,break and print the necessary metrics/results.

What test cases you used/added, why you used them, what did they tell you about the correctness of your code: I used the 6 machines created by another student and provided by Prof. Kogge. These machines tested both DTM and NTM and had transitions that moved both left and right. I tested all of these in my program and compared them with what I thought the output should be based off of my own assessment of the input string on the machine

How you managed the code development: I worked through the logic of each of the different sections (appending results, transitioning left, transitioning right, adding blanks to the tape when necessary) and used the VSCode python debugging function to help me a lot when I was running into unexpected results

Detailed discussion of results: For deterministic machines, the average nondeterminism was 1 meaning that it was completely deterministic. There was only one option for each transition. In the NTMs, the longer the input string was, the higher the average nondeterminism ended up being because the depth of the tree was higher, so it expanded more and had more transitions for each level.

How team was organized: I did it all by myself

What you might do differently if you did the project again: Honestly this went smoothly and I really enjoyed the coding for this project. I wouldn’t change much but I would maybe read the project description a little bit more in depth – I was confused about what Prof. Kogge meant by average nondeterminism in his canvas announcement but then realized it was in the project description all along.

Any additional material: don’t have any


