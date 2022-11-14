def lexify(code):
    # Lexer Action Plan
    # - Create a list of tokens

    code = code.split(" ")

    KEYWORDS = ['var', 'out']
    OPERATIONS = ['+', '-', '*', '/', '=']
    MARKS = ["'", '"', "(", ")"]

    tokens = []

    for word in code:
        if word in KEYWORDS:
            token = ["kw", word]
            tokens.append(token)
        elif word in OPERATIONS:
            token = ["op", word]
            tokens.append(token)
        elif word in MARKS:
            token = ["mk", word]
            tokens.append(token)
        elif word == "\n":
            token = ["nl"]
            tokens.append(token)
        else:
            token = ["txt", word]
            if word != " " and word != "":
                tokens.append(token)

    return tokens