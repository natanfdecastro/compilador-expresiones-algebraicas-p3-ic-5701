class AbstractSyntaxTree:

    node_type = 0
    node_value = 0
    children_nodes = []

    def __init__(self, node_type, node_value, children_nodes):
        self.node_type = node_type
        self.node_value = node_value
        self.children_nodes = children_nodes

    def add_node(self, new_node):
        self.children_nodes += [new_node]


class ValueNode(AbstractSyntaxTree):

    def init(self, node_type, node_value, children_nodes):
        AbstractSyntaxTree.__init__(self, node_type, node_value, children_nodes)

    def visit(self, semantic_checker):
        return semantic_checker.visit_value_node(self)


class ProgramRootNode(AbstractSyntaxTree):

    def init(self, node_type, node_value, children_nodes):
        AbstractSyntaxTree.__init__(self, node_type, node_value, children_nodes)

    def visit(self, semantic_checker):
        return semantic_checker.visit_program_root_node(self)


class DeclarationNode(AbstractSyntaxTree):

    def init(self, node_type, node_value, children_nodes):
        AbstractSyntaxTree.__init__(self, node_type, node_value, children_nodes)

    def visit(self, semantic_checker):
        return semantic_checker.visit_declaration_node(self)


class AssignationNode(AbstractSyntaxTree):

    def init(self, node_type, node_value, children_nodes):
        AbstractSyntaxTree.__init__(self, node_type, node_value, children_nodes)

    def visit(self, semantic_checker):
        return semantic_checker.visit_assignation_node(self)


class ExpressionNode(AbstractSyntaxTree):

    def init(self, node_type, node_value, children_nodes):
        AbstractSyntaxTree.__init__(self, node_type, node_value, children_nodes)

    def visit(self, semantic_checker):
        return semantic_checker.visit_expression_node(self)


class FactorNode(AbstractSyntaxTree):

    def init(self, node_type, node_value, children_nodes):
        AbstractSyntaxTree.__init__(self, node_type, node_value, children_nodes)

    def visit(self, semantic_checker):
        return semantic_checker.visit_factor_node(self)


class IdentifierNode(AbstractSyntaxTree):

    def init(self, node_type, node_value, children_nodes):
        AbstractSyntaxTree.__init__(self, node_type, node_value, children_nodes)

    def visit(self, semantic_checker):
        return semantic_checker.visit_identifier_node(self)


class EqualAssignationNode(AbstractSyntaxTree):

    def init(self, node_type, node_value, children_nodes):
        AbstractSyntaxTree.__init__(self, node_type, node_value, children_nodes)

    def visit(self, semantic_checker):
        return semantic_checker.visit_equal_assignation_node(self)


class SemiColonNode(AbstractSyntaxTree):

    def init(self, node_type, node_value, children_nodes):
        AbstractSyntaxTree.__init__(self, node_type, node_value, children_nodes)

    def visit(self, semantic_checker):
        return semantic_checker.visit_semi_colon_node(self)


class IntegerNode(AbstractSyntaxTree):

    def init(self, node_type, node_value, children_nodes):
        AbstractSyntaxTree.__init__(self, node_type, node_value, children_nodes)

    def visit(self, semantic_checker):
        return semantic_checker.visit_integer_node(self)


class OperatorNode(AbstractSyntaxTree):

    def init(self, node_type, node_value, children_nodes):
        AbstractSyntaxTree.__init__(self, node_type, node_value, children_nodes)

    def visit(self, semantic_checker):
        return semantic_checker.visit_operator_node(self)


class LeftParenthesisNode(AbstractSyntaxTree):

    def init(self, node_type, node_value, children_nodes):
        AbstractSyntaxTree.__init__(self, node_type, node_value, children_nodes)

    def visit(self, semantic_checker):
        return semantic_checker.visit_left_parenthesis_node(self)


class RightParenthesisNode(AbstractSyntaxTree):

    def init(self, node_type, node_value, children_nodes):
        AbstractSyntaxTree.__init__(self, node_type, node_value, children_nodes)

    def visit(self, semantic_checker):
        return semantic_checker.visit_right_parenthesis_node(self)


class PrintProductionNode(AbstractSyntaxTree):

    def init(self, node_type, node_value, children_nodes):
        AbstractSyntaxTree.__init__(self, node_type, node_value, children_nodes)

    def visit(self, semantic_checker):
        return semantic_checker.visit_print_production_node(self)


class PrintNode(AbstractSyntaxTree):

    def init(self, node_type, node_value, children_nodes):
        AbstractSyntaxTree.__init__(self, node_type, node_value, children_nodes)

    def visit(self, semantic_checker):
        return semantic_checker.visit_print_node(self)



