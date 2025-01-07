JSON Scanner README

For this project I have implemented a JSON scanner which processes a JSON input file and returns token. Each token represents a unit in the input such as numbers, strings, booleans and structural symbols like brackets and commas.

The keys classes in this code are:r
1. Token- which represents each token and also prints them.

2. TokenType - which has different token types.

3. JSONScanner - which recognizes different token into predetermined types like STRING, BOOL etc

4. LexerError - which raises an exception when an illegal or unexpected value is encountered.

To Run the Code
There is already a input file input.txt with an example of JSON code. Just run it using some IDE or directly by terminal.
If using terminal just use
python3 <filename>

Assumptions Made
1. The input must in JSON.
2. Strings must be enclosed in "", numbers(both integers and floating), booleans(true and false) and null values.
3. Symbols are also recognized like {,},[,],(,).
4. White spaces are ignored.
5. No illegal character is assumed.

Key Part of the Code

Token Class
The token class represents individual tokens scanned by the scanner. Each token is of type (e.g. STRING, BOOL, NUMBER).

LexerError Class
This class checks if there are any invalid characters used and if there are any then outputs their value and position.

TokenType Class
The TokenType class has all the type of tokens to be recognized by.

JSONScanner Class
advance() - this is to ensure input buffering

recognize_string() - this recognizes and return string tokens.

recongize_number()  - this recognizes and return number tokens.

recognize_BOOL() - this recognizes and return (true, false, null)

get_next_token() - this is the main loop where all the token gets recognized by their specific token type.

Reference
Some parts of code was refferred by supplementary materials provided under CSCI 2115 course on Brightspace.
