import re  # Biblioteca que maneja regex de Python


class Scanner:

    def __init__(self, program):

        # Contiene el programa leido del programa.txt
        self.program = program

        # Contiene los identificadores de las palabras clave del Java Tropicalizado al Español.
        self.integer_token = r'[0-9]+'
        self.print_token = r'imprime'
        self.id_token = r'[a-z]+'
        self.Left_parenthesis_token = r'\('
        self.Right_parenthesis_token = r'\)'
        self.semi_colon_token = r';'
        self.operator_token = r'-|\+|/|\*|\+|='
        self.error_token = r'[\S]+'

        # Se crea un regex con todos los posibles tokens para formar la gramatica
        self.grammar = r'(' + self.integer_token + ')|(' + self.print_token + ')|(' \
                       + self.Left_parenthesis_token + ')|(' + self.Right_parenthesis_token + ')|(' \
                       + self.semi_colon_token + ')|(' + self.operator_token + ')|(' \
                       + self.id_token + ')|(' + self.error_token + ')'

        self.founded_tokens = []
        self.wrong_token = []
        self.error = False

        self.find_tokens()
        self.show_tokens()

    def find_tokens(self):

        # Imprime el programa ingresado.
        print(self.program)
        # Prepara la gramatica para hacer match
        self.grammar = re.compile(self.grammar)

        lines = re.split(r'\n', self.program)

        # Recorre los matches encontrados para asignarles su respectivo tipo.
        for line in lines:

            words = re.split(r' ', line)
            for word in words:
                if re.fullmatch(self.integer_token, word):
                    self.founded_tokens += [["INTEGER", word]]
                elif re.fullmatch(self.print_token, word):
                    self.founded_tokens += [["PRINT", word]]
                elif re.fullmatch(self.Left_parenthesis_token, word):
                    self.founded_tokens += [["LEFT_PARENTHESIS", word]]
                elif re.fullmatch(self.Right_parenthesis_token, word):
                    self.founded_tokens += [["RIGHT_PARENTHESIS", word]]
                elif re.fullmatch(self.semi_colon_token, word):
                    self.founded_tokens += [["SEMI_COLON", word]]
                elif re.fullmatch(self.operator_token, word):
                    self.founded_tokens += [["OPERATOR", word]]
                elif re.fullmatch(self.id_token, word):
                    self.founded_tokens += [["IDENTIFIER", word]]
                elif re.fullmatch(self.error_token, word):
                    self.founded_tokens += [["ERROR", word]]
                    raise Exception(
                        "ERROR: Token " + word + " in line " + str(lines.index(line) + 1) + " not recognized.")
                else:
                    print("ERROR: Token not recognized. \t '" + word + "'")
                    self.error = True

    def show_tokens(self):

        count = 0
        print("Founded tokens: \n")

        for token in self.founded_tokens:
            print(str(count) + " " + str(token))
            count += 1
        print()
