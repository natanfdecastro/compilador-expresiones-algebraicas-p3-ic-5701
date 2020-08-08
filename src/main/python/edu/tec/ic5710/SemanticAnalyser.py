from src.main.python.edu.tec.ic5710.AbstractSyntaxTree import *
from src.main.python.edu.tec.ic5710.SyntaxAnalyser import *


class SemanticAnalyser:

    tables = [dict()]
    tables_length = 1
    abstract_syntax_tree = []

    def __init__(self, abstract_syntax_tree):
        self.abstract_syntax_tree = abstract_syntax_tree

    def check(self):
        return self.abstract_syntax_tree.visit(self)

    def check_table(self, name):
        """
        Recibe el nombre de una variable, la busca en la lista de tablas de valores;
        en caso que la encuentre retorna un tupla la cual contiene:
        (i de la variable en la tabla, info de la variable)
        """

        search = 0
        n = 0
        for table in self.tables:
            search = table.get(name)

            if type(search) == list:
                return n, table[name]
            n += 1
        return -1, search

    def visit_program_root_node(self, node):

        # se itera visitando los hijos

        state = ""
        for child in node.children_nodes:
            state = child.visit(self)

            if type(state) == str:
                break
        return state

    def visit_declaration_node(self, node):

        # insertar el nombre con el tipo y valor del tipo de la declaracion
        node_type = node.children_nodes[0].visit(self)
        node_value = node.children_nodes[1].children_nodes[0].node_value
        table, search = self.check_table(node_value)
        if table == -1:  # no esta en la tabla
            self.tables[0][node_value] = node_type
            return node.children_nodes[1].visit(self)

        else:
            return "ERROR: The variable " + node_value + ", " + node_type + " has been declared before"

    def visit_assignation_node(self, node):

        # Buscar que el nombre exista
        node_type = node.children_nodes[0].node_type
        node_value = node.children_nodes[0].node_value
        table, search = self.check_table(node_type)

        if table != -1:

            info = node.children_nodes[1].visit(self)

        return "ERROR: The variable " + node_value + ", " + node_type + " has not been assigned"

