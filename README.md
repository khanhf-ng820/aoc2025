# aoc2025
My solutions **(and explanations, if possible)** for Advent of Code 2025. The solutions use **Python** and **C++**.

**Notes:**
- For Part 2 of Day 10, install the external package ```PuLP``` by typing the following in the Terminal:
```bash
pip install pulp
```
- For Part 1 of Day 12 *(even though there's no problem to solve in Part 2)*, ```part1.py``` contains the alternate solution for the problem (using the area trick), which works for your puzzle input. But ***IT IS NOT GUARANTEED TO WORK*** for any arbitrary input of the problem, or the [example input](https://adventofcode.com/2025/day/12).

I was working on a solution that solves any arbitrary input (file ```part1alt.py```, but after some further digging, it turned out this problem is **NP-hard**, so such a solution (that doesn't use approximations, heuristics) has a huge runtime complexity. You can safely ignore the file ```part1alt.py```.

*IMO, I don't really like Day 12, but because the generalized problem is NP-hard, it's interesting to think outside the box and guess interesting properties of the puzzle input instead of brute-forcing everything.*
