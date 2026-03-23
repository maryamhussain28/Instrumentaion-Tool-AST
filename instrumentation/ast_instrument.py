import ast

class FunctionInstrumentor(ast.NodeTransformer):
    def visit_FunctionDef(self, node):
        decorator = ast.Name(id='trace_function', ctx=ast.Load())
        node.decorator_list.append(decorator)
        return node


def instrument_code(source_code):
    tree = ast.parse(source_code)

    instrumentor = FunctionInstrumentor()
    new_tree = instrumentor.visit(tree)

    ast.fix_missing_locations(new_tree)

    return ast.unparse(new_tree)