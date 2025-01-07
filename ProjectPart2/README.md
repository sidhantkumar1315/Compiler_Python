JSON Parser Readme
For this part of the project I have implemented a Parser for JSON like langauge which processes a token stream and converts it into meaningful parse trees.

The key components of Parser are:
1. Token - which have type and value of the token.
2. InputReader- which reads the input file containing token stream.
3. Node- which makes the parse trees.
4. Parser- which is the most important, dividing and recognizing token into different categories provided by the grammar(like list, dict, pairs).

How to run the code:
Just clone this repository and run the code (projectpart2.py) in some IDE environment or directly on terminal. There is a choice of input files in Inputs folder which would output different results in Outputs folder. You can also create your own input files but it should follow the grammar, else exceptions will be raised. The output is not shown on the console it is directly writing the output in Outputs/output.txt.

Assumptions made:
1. The token stream must contain tokens according to JSON syntax and grammar.
2. If the syntax of the token stream doesnt match the grammar then exceptions will be raised.
3. The environment in which the code is run has a necessary permissions to read from and write to files.


The current Inputs/input1.txt is correct and Inputs/input2.txt is incorrect according to the grammar so their outputs are in Outputs/output1.txt and output2.txt respectively.
