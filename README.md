This repository contains a CDCL SAT solver with VeriPB proof logging. The SAT solver is based on https://kienyew.github.io/CDCL-SAT-Solver-from-Scratch/. 

Run the cdcl.py script with input a SAT question in DIMACS cnf format and write the printed output to a new file to get a VeriPB proof:
```
python3 cdcl.py input.cnf > output.pbp
```
Some examples with results are given in the examples folder.
