This part of the project raises error if the input is semantically incorrect otherwise outputs an abstract syntax tree.

To run this code firstly clone this repository and type: 
python3 projectpart3.py on terminal or open this folder in any IDE.

There are 10 inputs files:
input1.txt --> Error type 1
input2.txt --> Error type 2
input3.txt --> Error type 3
input4.txt --> Error type 4
input5.txt --> Error type 5
input6.txt --> Error type 6
input7.txt --> Error type 7

input8.txt --> semantically correct
input9.txt --> semantically correct
input10.txt --> semantically correct

This is also given as comments in the code. So choose any of the premade input file to check.

Assumptions made
1. The token stream must contain tokens according to JSON syntax and grammar.
2. If the input lies within any of the 7 error types then an error would be raised.
3. Otherwise an abstract syntax tree would be made for the input.