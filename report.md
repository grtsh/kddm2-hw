# KDDM 2 Homework
**Author: Alex Ghiriti - aghiriti@student.tugraz.at - 11904833**

### Task 1: Causality 
_TODO: Please provide an own example for a Simpson’s paradox (i.e., not an example from the slides, Wikipedia,etc.). Add the code and the result to the submitted zip file._

**(a)** My generated data can be found in [results/1a_simpsons_paradox.csv](results/1a_simpsons_paradox.csv)

**(b)** Graph and Table of the Results:

#graph

#table

**(c)** This is a personal example of me encountering a Simpson's Paradox. The data shows the following: 
- [0]: Switch Manufacturer: Cisco/Aruba
- [1]: Enviroment: 1 (Server Room) / 0 (Industrial Grounds)
- [2]: RMA Cycle / Life Expentancy in Days


My goal was to create a report for a colleague to determine which manufacturer had a better life expectancy for a particular customer. In the initial report, it appeared that Aruba switches had a longer life expectancy than Cisco. However, after discussing with another colleague, I learned that many RMAs were related to the environment in which the switches operated—specifically, an industrial environment where the air is "oily," causing devices to break down more often. He was interested in seeing how much the oily environment impacted the life expectancy compared to server environments, so I created a separate report for that comparison.

In this report, I noticed that most switches in the harsh (bad) environment were from Cisco, while most switches in the good environment were from Aruba. I then reintroduced this environmental variable into the initial report and discovered that, in fact, Cisco was performing better in both environments.

**Interpretation**: In the long run we sshould go with Cisco instead of Aruba as it better archieves our goal of having less RMAs

