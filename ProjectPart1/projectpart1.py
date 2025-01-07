import os
class Token:
    def __init__(self,type,value):
        self.type = type
        self.value = value

    def __repr__(self):
        return f"<{self.type}, {repr(self.value)}>"
    

# class for any illegal or unexpected values  
class LexerError(Exception):
    def __init__(self, position, character):
        self.position = position
        self.character = character
        super().__init__(f"Invalid character '{character}' at position {position}")

 # class to define the tokentypes   
class TokenType:
     LPAREN = 'LPAREN' # '{'
     RPAREN = 'RPAREN' # '}'
     LBRAC = 'LBRAC' # '['
     RBRAC = 'RBRAC' # ']'
     LCBRAC = 'LCBRAC' # '('
     RCBRAC = 'RCBRAC' # ')'
     COMMA = 'COMMA'   # ','
     COLON = 'COLON'  # ':'
     SEMICOLON = 'SEMICOLON'  #';'
     STRING = 'STRING' # 'start with " '
     NUMBER = 'NUMBER'
     BOOL = 'BOOL'  # 'true,false'
     NULL = 'NULL'
     EOF = 'EOF' # 'end of file'


class JSONScanner:
    def __init__(self, file_path):
        with open(file_path, 'r') as file:
            self.input_string = file.read()
        self.position = 0
        self.current_char = self.input_string[self.position] if self.input_string else None
        self.symbol_table = {}

    def advance(self):
        self.position += 1
        if self.position >= len(self.input_string):
             self.current_char = None
        else:
            self.current_char = self.input_string[self.position]


# to recognize the string
    def recognize_string(self):
        result = ''
        self.advance()
        while self.current_char is not None and (self.current_char != '"'):
            result += self.current_char
            self.advance()
        self.advance()

        # self.symbol_table[result] = 'STRING'
        return Token(TokenType.STRING, result)

# to recognize the numbers
    def recognize_number(self):
        result = ''
        while self.current_char is not None and (self.current_char.isdigit() or self.current_char in ['.','e','E','-','+']):
            result += self.current_char
            self.advance()
        return Token(TokenType.NUMBER,float(result))

# to recognize booleans and null values
    def recognize_BOOL(self):
        # true, false, null
        result = ''
        while self.current_char is not None and self.current_char.isalpha():
            result += self.current_char
            self.advance()
        if result == "true":
            return Token(TokenType.BOOL, True)
        elif result == "false":
             return Token(TokenType.BOOL,False)
        elif result == "null":
            return Token(TokenType.NULL, None)
        return Token(TokenType.EOF, None)

# this is the main loop for recognizing tokens    
    def get_next_token(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                 self.advance()
                 continue
            
            elif self.current_char == '{':
                    self.advance()
                    return Token(TokenType.LPAREN, '{')
            elif self.current_char == '}':
                    self.advance()
                    return Token(TokenType.RPAREN, '}')
            elif self.current_char == '[':
                    self.advance()
                    return Token(TokenType.LBRAC, '[')
            elif self.current_char == ']':
                    self.advance()
                    return Token(TokenType.RBRAC, ']')
            elif self.current_char == '(':
                    self.advance()
                    return Token(TokenType.RCBRAC, '(')
            elif self.current_char == ')':
                    self.advance()
                    return Token(TokenType.LCBRAC, ')')
            elif self.current_char == ',':
                    self.advance()
                    return Token(TokenType.COMMA, ',')
            elif self.current_char == ':':
                    self.advance()
                    return Token(TokenType.COLON, ':')
            elif self.current_char == ';':
                    self.advance()
                    return Token(TokenType.SEMICOLON, ';')
            elif self.current_char == '"':
                    # self.advance()
                    return self.recognize_string()
            elif self.current_char.isdigit():
                return self.recognize_number()
            elif self.current_char.isalpha():
                return self.recognize_BOOL()
            
            raise LexerError(self.position,self.current_char)
        
        return Token(TokenType.EOF,None)
             

 # the following reads the input files and outputs the tokens respectively       
if __name__ == "__main__":
    scanner = JSONScanner("input.json")
    
    token = scanner.get_next_token()
    while token.type != TokenType.EOF:
        print(token)
        token = scanner.get_next_token()
