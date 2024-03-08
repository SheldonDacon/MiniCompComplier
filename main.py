from lexer import *


def main():
    # source = "LET foobar = 123"
    # lexer = Lexer(source)
    #
    # while lexer.peek() != '\0':
    #     breakpoint()
    #     print(lexer.curChar)
    #     lexer.nextChar()
    source = "IF+-123 foo*THEN/"
    lexer = Lexer(source)

    token = lexer.getToken()
    while token.kind != TokenType.EOF:
        print(token.kind)
        token = lexer.getToken()


main()
