import os
import re  # Biblioteca que maneja regex de Python
from src.main.python.edu.tec.ic5710.configuration import NEW_PATH


class Scanner:

    def __init__(self, program):

        # Contiene el programa leido del programa.txt
        self.program = program

        # Contiene los identificadores de las palabras clave del Java Tropicalizado al Español.
        self.integer_token = r'[0-9]+'
        self.print_token = r'imprime'
        self.identifier_token = r'[a-z]+'
        self.left_parenthesis_token = r'\('
        self.right_parenthesis_token = r'\)'
        self.semi_colon_token = r';'
        self.equal_assignation_token = r'='
        self.operator_token = r'-|\+|/|\*'
        self.error_token = r'[\S]+'

        # Se crea un regex con todos los posibles tokens para formar la gramatica
        self.grammar = r'(' + self.integer_token + ')|(' + self.print_token + ')|(' \
                       + self.left_parenthesis_token + ')|(' + self.right_parenthesis_token + ')|(' \
                       + self.semi_colon_token + ')|(' + self.operator_token + ')|(' \
                       + self.identifier_token + ')|(' + self.error_token + ')'

        self.founded_tokens = []
        self.wrong_token = []
        self.error = False

        self.find_tokens()
        #self.show_tokens()

    # Es necesario comentar
    def find_tokens(self):

        # Prepara la gramatica para hacer match
        self.grammar = re.compile(self.grammar)

        lines = re.split(r'\n', self.program)

        # Recorre los matches encontrados para asignarles su respectivo tipo.
        for line in lines:

            words = re.split(r'\s', line)
            for word in words:
                if re.fullmatch(self.integer_token, word):
                    self.founded_tokens += [["INTEGER", word]]
                elif re.fullmatch(self.print_token, word):
                    self.founded_tokens += [["PRINT", word]]
                elif re.fullmatch(self.left_parenthesis_token, word):
                    self.founded_tokens += [["LEFT_PARENTHESIS", word]]
                elif re.fullmatch(self.right_parenthesis_token, word):
                    self.founded_tokens += [["RIGHT_PARENTHESIS", word]]
                elif re.fullmatch(self.semi_colon_token, word):
                    self.founded_tokens += [["SEMI_COLON", word]]
                elif re.fullmatch(self.equal_assignation_token, word):
                    self.founded_tokens += [["EQUAL_ASSIGNATION", word]]
                elif re.fullmatch(self.operator_token, word):
                    self.founded_tokens += [["OPERATOR", word]]
                elif re.fullmatch(self.identifier_token, word):
                    self.founded_tokens += [["IDENTIFIER", word]]
                elif re.fullmatch(self.error_token, word):
                    self.founded_tokens += [["ERROR", word]]
                    raise Exception(
                        "Lexical Error: TOKEN " + word + ", LINE " + str(lines.index(line) + 1) + ", NOT RECOGNIZED.")
                else:
                    print("LEXICAL ERROR TOKEN NOT RECOGNIZED: \t '" + word + "'")
                    self.error = True

    def show_tokens(self):

        count = 0
        print("Founded tokens: \n")

        for token in self.founded_tokens:
            print(str(count) + " " + str(token))
            count += 1

        # Useful comment
        print()

    def create_lexical_analysis_report(self):
        print("\nETAPA ANALISIS LEXICO: COMPLETADA CORRECTAMENTE")
        try:
            file = open(NEW_PATH + '/lexical_analysis_report.txt', 'w')
            file.close()

            file = open(NEW_PATH + '/lexical_analysis_report.txt', 'a')
            file.write("FOUNDED TOKENS LIST: \n\n")

            count = 0
            for token in self.founded_tokens:
                file.write(str(count) + " " + str(token) + "\n")
                count += 1

            file.close()

            print(">>> NUEVO REPORTE DE ANALISIS LEXICO CREADO")

        except:
            print(">>> ERROR GENERANDO REPORTE DE ANALISIS LEXICO")

