from src.main.python.edu.tec.ic5710.AbstractSyntaxTree import *
from src.main.python.edu.tec.ic5710.SemanticAnalyser import *
from src.main.python.edu.tec.ic5710.configuration import NEW_PATH


def check_parse(sub_tree):
    if not sub_tree:
        return False
    else:
        return True


class SintaxAnalyser:
    founded_tokens = []
    abstract_syntax_tree = 0
    error_pointer = 0
    founded_tokens_len = 0

    def __init__(self, founded_tokens):

        self.founded_tokens = founded_tokens
        self.founded_tokens_len = len(founded_tokens)

        self.parse()

    def parse(self):

        self.abstract_syntax_tree = ProgramRootNode("PROGRAM_ROOT_NODE", "", [])
        abstract_syntax_tree_pointer = self.abstract_syntax_tree
        founded_token_pointer = 0

        if self.parse_program_root_node(founded_token_pointer):

            #self.print_abstract_syntax_tree()
            self.create_syntax_analysis_report()

            semantic_analysis = SemanticAnalyser(self.abstract_syntax_tree)
            semantic_analysis.check()
            semantic_analysis.create_lexical_analysis_report()

        else:
            self.generate_error()

    def parse_program_root_node(self, founded_token_pointer):

        sub_tree = []
        new_pointer = founded_token_pointer
        succesful_parse = False

        sub_tree, new_pointer = self.parse_production(founded_token_pointer)

        if check_parse(sub_tree):

            self.abstract_syntax_tree.add_node(sub_tree)
            founded_token_pointer = new_pointer
            if founded_token_pointer == self.founded_tokens_len:
                return True
            else:
                return self.parse_program_root_node(founded_token_pointer)
        else:
            self.calculate_error(founded_token_pointer)
            return False

    #TODO Realizar un raise en vez de un print.
    def generate_error(self):
        tracking = ""
        syntax_error_message = "Invalid Sintax\n"
        max_tracking = 6  # Imprime 6 caracteres despues del error en el programa

        if self.error_pointer == len(self.founded_tokens):
            syntax_error_message += "Missing statement at the end\n"
        self.error_pointer -= 1

        while self.error_pointer > -1 and max_tracking > -1:
            tracking = self.founded_tokens[self.error_pointer][1] + " " + tracking
            self.error_pointer -= 1
            max_tracking -= 1
        tracking += "\x1b[1;31m <--- \x1b[1;37m"
        print(tracking)
        print(syntax_error_message)

    def parse_production(self, founded_token_pointer):

        sub_tree = []
        new_pointer = founded_token_pointer
        succesful_parse = False

        sub_tree, new_pointer = self.parse_declaration(founded_token_pointer)

        if check_parse(sub_tree):
            founded_token_pointer = new_pointer
            succesful_parse = True
        else:
            sub_tree, new_pointer = self.parse_assignation(founded_token_pointer)

            if check_parse(sub_tree):
                founded_token_pointer = new_pointer
                succesful_parse = True
            else:

                sub_tree, new_pointer = self.parse_print(founded_token_pointer)

                if check_parse(sub_tree):
                    founded_token_pointer = new_pointer
                    succesful_parse = True

        if succesful_parse:
            return sub_tree, founded_token_pointer
        else:
            self.calculate_error(founded_token_pointer)
            return [], -1

    def calculate_error(self, founded_token_pointer):
        if founded_token_pointer > self.error_pointer:
            self.error_pointer = founded_token_pointer

    def parse_declaration(self, founded_token_pointer):

        sub_tree = DeclarationNode("DECLARATION", "DECLARATION", [])
        new_founded_token_pointer = founded_token_pointer

        sub_tree.add_node(self.create_node(founded_token_pointer))
        founded_token_pointer += 1

        sub_tree_aux, new_founded_token_pointer = self.parse_assignation(founded_token_pointer)

        if check_parse(sub_tree_aux):
            puntero_token = new_founded_token_pointer
            sub_tree.add_node(sub_tree_aux)
            return sub_tree, founded_token_pointer
        self.calculate_error(founded_token_pointer)
        return [], -1

    def parse_assignation(self, founded_token_pointer):

        sub_tree = AssignationNode("ASSIGNATION", "ASSIGNATION", [])
        new_founded_token_pointer = founded_token_pointer

        if self.compare_types("IDENTIFIER", founded_token_pointer):
            sub_tree.add_node(self.create_node(founded_token_pointer))
            founded_token_pointer += 1

            if self.compare_types("EQUAL_ASSIGNATION", founded_token_pointer):
                founded_token_pointer += 1
                sub_tree_aux, new_founded_token_pointer = self.parse_expression(founded_token_pointer)

                if check_parse(sub_tree_aux):
                    founded_token_pointer = new_founded_token_pointer
                    sub_tree.add_node(sub_tree_aux)
                    if self.compare_types("SEMI_COLON", founded_token_pointer):
                        founded_token_pointer += 1

                        return sub_tree, founded_token_pointer
        self.calculate_error(founded_token_pointer)
        return [], -1

    def parse_expression(self, founded_token_pointer):

        sub_tree = ExpressionNode("EXPRESSION", "EXPRESSION", [])

        sub_tree_aux, new_founded_token_pointer = self.parse_factor(founded_token_pointer)
        if check_parse(sub_tree_aux):

            founded_token_pointer = new_founded_token_pointer
            sub_tree.add_node(sub_tree_aux)

        return sub_tree, founded_token_pointer

    def parse_factor(self, founded_token_pointer):
        sub_tree = FactorNode("FACTOR", "FACTOR", [])

        if self.compare_types("LEFT_PARENTHESIS", founded_token_pointer):
            sub_tree.add_node(self.create_node(founded_token_pointer))
            founded_token_pointer += 1

            sub_tree_aux, new_founded_token_pointer = self.parse_expression(founded_token_pointer)

            if self.compare_types("RIGHT_PARENTHESIS", founded_token_pointer):
                sub_tree.add_node(self.create_node(founded_token_pointer))
                founded_token_pointer += 1

                if check_parse(sub_tree_aux):

                    founded_token_pointer = new_founded_token_pointer
                    sub_tree.add_node(sub_tree_aux)
                return sub_tree, founded_token_pointer

        if self.compare_types("INTEGER", founded_token_pointer) or self.compare_types("IDENTIFIER",
                                                                                      founded_token_pointer):

            sub_tree.add_node(self.create_node(founded_token_pointer))
            founded_token_pointer += 1
            while self.compare_types("OPERATOR", founded_token_pointer) or (self.compare_types("RIGHT_PARENTHESIS", founded_token_pointer) and (not self.compare_types("SEMI_COLON", founded_token_pointer+1))):

                sub_tree.add_node(self.create_node(founded_token_pointer))
                founded_token_pointer += 1

                if self.compare_types("OPERATOR", founded_token_pointer):
                    sub_tree.add_node(self.create_node(founded_token_pointer))
                    founded_token_pointer += 1

                if self.compare_types("LEFT_PARENTHESIS", founded_token_pointer):
                    sub_tree.add_node(self.create_node(founded_token_pointer))
                    founded_token_pointer += 1

                    sub_tree_aux, new_founded_token_pointer = self.parse_expression(founded_token_pointer)

                    if check_parse(sub_tree_aux):
                        founded_token_pointer = new_founded_token_pointer
                        if self.compare_types("SEMI_COLON", founded_token_pointer+1):
                            founded_token_pointer += 1
                        sub_tree.add_node(sub_tree_aux)

                    return sub_tree, founded_token_pointer

                if self.compare_types("INTEGER", founded_token_pointer) or self.compare_types("IDENTIFIER",
                                                                                              founded_token_pointer):
                    sub_tree.add_node(self.create_node(founded_token_pointer))
                    founded_token_pointer += 1
                else:
                    self.calculate_error(founded_token_pointer)
                    return [], -1

            return sub_tree, founded_token_pointer

        self.calculate_error(founded_token_pointer)
        return [], -1

    def parse_print(self, founded_token_pointer):
        sub_tree = PrintProductionNode("PRINT_PRODUCTION", "PRINT_PRODUCTION", [])

        if self.compare_types("PRINT", founded_token_pointer):
            sub_tree.add_node(self.create_node(founded_token_pointer))
            founded_token_pointer += 1

            if self.compare_types("IDENTIFIER", founded_token_pointer):
                sub_tree.add_node(self.create_node(founded_token_pointer))
                founded_token_pointer += 1

                if self.compare_types("SEMI_COLON", founded_token_pointer):
                    founded_token_pointer += 1
                    return sub_tree, founded_token_pointer

        self.calculate_error(founded_token_pointer)
        return [], -1

    def compare_types(self, token_type, founded_token_pointer):

        if founded_token_pointer < self.founded_tokens_len:
            if self.founded_tokens[founded_token_pointer][0] == token_type:
                return True
        return False

    def create_node(self, founded_token_pointer):
        token_type = self.founded_tokens[founded_token_pointer][0]
        token_value = self.founded_tokens[founded_token_pointer][1]
        node = []
        if token_type == "IDENTIFIER":
            node = IdentifierNode(token_type, token_value, [])
        elif token_type == "EQUAL_ASSIGNATION":
            node = EqualAssignationNode(token_type, token_value, [])
        elif token_type == "SEMI_COLON":
            node = SemiColonNode(token_type, token_value, [])
        elif token_type == "INTEGER":
            node = IntegerNode(token_type, token_value, [])
        elif token_type == "OPERATOR":
            node = OperatorNode(token_type, token_value, [])
        elif token_type == "LEFT_PARENTHESIS":
            node = LeftParenthesisNode(token_type, token_value, [])
        elif token_type == "RIGHT_PARENTHESIS":
            node = RightParenthesisNode(token_type, token_value, [])
        elif token_type == "PRINT":
            node = PrintNode(token_type, token_value, [])
        return node

    def print_abstract_syntax_tree(self):
        # print(self.abstract_syntax_tree.children_nodes[0].children_nodes[0].type)

        abstract_syntax_tree_list = [self.abstract_syntax_tree]
        str_abstract_syntax_tree = ""
        while abstract_syntax_tree_list:

            str_abstract_syntax_tree += "[ " + abstract_syntax_tree_list[0].node_type + " ]" + "\n|---> "

            for child in abstract_syntax_tree_list[0].children_nodes:
                str_abstract_syntax_tree += "( " + child.node_type + " )" + " "
                abstract_syntax_tree_list += [child]

            str_abstract_syntax_tree += "\n\n"
            abstract_syntax_tree_list = abstract_syntax_tree_list[1:]



    def create_syntax_analysis_report(self):
        print("\nETAPA ANALISIS SINTACTICO: COMPLETADA CORRECTAMENTE")
        try:
            file = open(NEW_PATH + '/syntax_analysis_report.txt', 'w')

            abstract_syntax_tree_list = [self.abstract_syntax_tree]
            str_abstract_syntax_tree = "ABSTRACT SYNTAX TREE: \n\n"

            while abstract_syntax_tree_list:

                str_abstract_syntax_tree += "[ " + abstract_syntax_tree_list[0].node_type + " ]" + "\n|---> "

                for child in abstract_syntax_tree_list[0].children_nodes:
                    str_abstract_syntax_tree += "( " + child.node_type + " )" + " "
                    abstract_syntax_tree_list += [child]

                str_abstract_syntax_tree += "\n\n"
                abstract_syntax_tree_list = abstract_syntax_tree_list[1:]

            file.write(str_abstract_syntax_tree)

            file.close()

            print(">>> NUEVO REPORTE DE ANALISIS SINTACTICO LEXICO CREADO")

        except:
            print(">>> ERROR GENERANDO REPORTE DE ANALISIS SINTACTICO")