from src.main.python.edu.tec.ic5710.AbstractSyntaxTree import *
from src.main.python.edu.tec.ic5710.SyntaxAnalyser import *
from src.main.python.edu.tec.ic5710.configuration import NEW_PATH


class SemanticAnalyser:

    tables = dict()
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

        return self.tables.get(name)

    def visit_program_root_node(self, node):

        # se itera visitando los hijos

        state = ""
        for child in node.children_nodes:
            state = child.visit(self)

            if type(state) == str:
                break
        return state

    def visit_factor_node(self, node):

        for child in node.children_nodes:


            if(child.node_type == "EXPRESSION"):
                child.visit(self)

            if(child.node_type == "IDENTIFIER"):
                node_value = child.node_value
                node_type = child.node_value

                dict_value = self.check_table(node_value)

                if dict_value:
                    info = node.children_nodes[0]
                else:
                    raise Exception("ERROR: The variable " + node_value + ", " + node_type + " has not been assigned")


    def visit_expression_node(self, node):
        node.children_nodes[0].visit(self)


    def visit_assignation_node(self, node):
        # Buscar que el nombre exista
        node_type = node.children_nodes[0].node_type
        node_value = node.children_nodes[0].node_value

        dict_value = self.check_table(node_value)

        node.children_nodes[1].visit(self)
        self.tables.update({node_value : node_type})


    def visit_print_production_node(self, node):

        node_value = node.children_nodes[1].node_value
        node_type = node.children_nodes[1].node_type

        dict_value = self.check_table(node_value)

        if dict_value:
            info = node.children_nodes[1]
        else:
            raise Exception("ERROR: The variable " + node_value + ", " + node_type + " has not been assigned")



    def create_lexical_analysis_report(self):
        print("\nETAPA ANALISIS SEMANTICO: COMPLETADA CORRECTAMENTE")
        try:
            file = open(NEW_PATH + '/semantic_analysis_report.txt', 'w')
            file.close()

            file = open(NEW_PATH + '/semantic_analysis_report.txt', 'a')
            file.write("SEMANTIC TABLE: \n\n")
            count = 0
            for key in self.tables:
                file.write(str(count) + " { KEY: " + str(key) + ", VALUE: " + self.tables[key] + " }\n")
                count += 1

            file.close()

            print(">>> NUEVO REPORTE DE ANALISIS SEMANTICO CREADO")

        except Exception as e:
            print(str(e), ">>> ERROR GENERANDO REPORTE DE SEMANTICO LEXICO")



