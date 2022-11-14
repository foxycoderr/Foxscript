from Runner.lexer import lexify

def run(code):
    tokens = lexify(code)

    return tokens
