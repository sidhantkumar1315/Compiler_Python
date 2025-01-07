# Sidhant Kumar
# B00961444
# CSCI 2115 Project Part 2

import os

#importing TokenType from projectpart1.py
from projectpart1 import TokenType

#this class makes Token   
class Token:
    def __init__(self,typeA, value):
        self.type = typeA
        self.value = value

#this class reads the input text files
class InputReader:
    def __init__(self, input_path):
        self.tokens = []
        with open(input_path, 'r') as input:
            for line in input:

                #strip() referred from w3cschools to remove all brackets<>(strip) before the tokens and split the token and values into two different objects
                #URL: https://www.w3schools.com/python/ref_string_strip.asp
                token_type, value = line.strip('<>\n').split(", ", 1)
                token_type = token_type.strip()
                value = value.strip("'")
                
                #reading token one by one(its type and value)
                self.tokens.append(Token(token_type, value))
        self.current_index = 0

    #this gets the next token
    def get_next_token(self):
        if self.current_index < len(self.tokens):
            token = self.tokens[self.current_index]
            self.current_index += 1
            return token
        return Token(TokenType.EOF, None)
    
#node class to make parse trees
class Node:
    def __init__(self, label=None, is_leaf=False):
        self.label = label
        self.children = []
        self.is_leaf = is_leaf

    def add_child(self, child):
        self.children.append(child)

    def outputprint_tree(self,file, depth=0):
        indent = "    " * depth
        file.write(f"{indent}{self.label}\n")
        for child in self.children:
            child.outputprint_tree(file,depth + 1)

#this is the parser
class Parser:
    def __init__(self, scanner):
        self.scanner = scanner
        self.current_token = self.scanner.get_next_token()

    def parse(self):
        try:
            return self.value()
        except Exception as e:
            print(f"Parsing error: {e}")
            raise

#defining values according to the given grammar
    def value(self):

        value = Node(label="value")

        #each child is added according to their token types
        if self.current_token.type == TokenType.LBRAC:
            value.add_child(self.list())
        elif self.current_token.type == TokenType.LPAREN:
            value.add_child(self.dict())  
        elif self.current_token.type == TokenType.STRING:
            value.add_child(self.string())
        elif self.current_token.type == TokenType.NUMBER:
            value.add_child(self.number())
        elif self.current_token.type == TokenType.BOOL:
            value.add_child(self.boolean())
        elif self.current_token.type == TokenType.NULL:
            value.add_child(self.null())
        else:
            raise Exception(f"Unexpected token: {self.current_token}")
        return value

# if the input starts with '[' then the parser will take it as a list
# if anything comes from scanner that does not match to the provided grammar for list then it raises an exception
    def list(self):
        self.eat(TokenType.LBRAC)
        node = Node(label="list")
        node.add_child(Node(label='['))

        commaPos = True
        while self.current_token.type != TokenType.RBRAC:
            if not commaPos:
                #throwing an exception if after comma there is no value
                raise Exception("Comma should be followed by a value")
            child_node = self.value()
            node.add_child(child_node)
            commaPos = False

            if self.current_token.type == TokenType.COMMA:
                self.eat(TokenType.COMMA)
                node.add_child(Node(label=','))
                commaPos = True

        if commaPos:
            #throwing an error is comma is at the end of the list
            raise Exception("Comma at the end of the list")
        self.eat(TokenType.RBRAC)
        node.add_child(Node(label=']'))
        return node

# # if the input starts with '{' then the parser will take it as a dict
# if anything comes from scanner that does not match to the provided grammar for dict then it raises an exception
    def dict(self):
        self.eat(TokenType.LPAREN)
        node = Node(label="dict")
        node.add_child(Node(label='{'))

        pair1 = True
        while self.current_token.type != TokenType.RPAREN:
            if not pair1:
                self.eat(TokenType.COMMA)
                node.add_child(Node(label=','))
            pair_node = self.pair()
            node.add_child(pair_node)
            pair1 = False
        self.eat(TokenType.RPAREN)
        node.add_child(Node(label='}')) 

        if self.current_token.type != TokenType.EOF and self.current_token.type == TokenType.COMMA:
            #throwing error if comma is at the end of the dict
            raise Exception(f"Unexpected token at the end of the dict: {self.current_token.value}")
        return node

    def pair(self):
        key = self.string()
        self.eat(TokenType.COLON)
        if self.current_token.type not in [
            TokenType.STRING, TokenType.NUMBER, TokenType.BOOL,
            TokenType.NULL, TokenType.LPAREN, TokenType.LBRAC
        ]:
            #thrwoiing an exception if after : there is not value key
            raise Exception(f"Expected a value after ':', but got {self.current_token.type}")
        
        valueP = self.value()
        if self.current_token.type == TokenType.COMMA:
            pair = Node(label="Pair")
            pair.add_child(key)
            pair.add_child(Node(label=":"))
            pair.add_child(valueP)
            return pair
        elif self.current_token.type == TokenType.RPAREN:
            pair = Node(label="Pair")
            pair.add_child(key)
            pair.add_child(Node(label=":"))
            pair.add_child(valueP)
            return pair
        else:
            #throwing an exception
            raise Exception(f"Expected ',' or RBRAC after pair, got {self.current_token.type}")

    def string(self):
        token = self.current_token
        self.eat(TokenType.STRING)
        node = Node(label=f'STRING: {token.value}', is_leaf=True)
        return node

    def number(self):
        token = self.current_token
        self.eat(TokenType.NUMBER)
        node = Node(label=f'NUMBER: {token.value}', is_leaf=True)
        return node

    def boolean(self):
        token = self.current_token
        self.eat(TokenType.BOOL)
        node = Node(label=f'BOOL: {token.value}', is_leaf=True)
        return node

    def null(self):
        token = self.current_token
        self.eat(TokenType.NULL)
        node = Node(label='NULL', is_leaf=True)
        return node

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.scanner.get_next_token()
        else:
            #throwing an exception if during eating some unexpected token is encountered
            raise Exception(f"Expected token {token_type}, got {self.current_token.type}")

#the main method
if __name__ == "__main__":

    #reading the input file
    # can change the input file here
    scanner = InputReader("Inputs/input5.txt")

    #writing the output in output.txt
    #can change the output file here
    with open("Outputs/output1.txt", "w") as outputFile:
        try:
            parser = Parser(scanner)
            parse_tree = parser.parse()
            if parse_tree:
                parse_tree.outputprint_tree(outputFile)
                print("Output has been written to output.txt")

        except Exception as e:
            #writing the error in the output.txt
            outputFile.write(f"Error detected during parsing: {e}\n")
            print("Error detected during parsing. Check output.txt for details.")