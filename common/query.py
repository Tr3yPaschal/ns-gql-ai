class Query:
    def __init__(self, name, operation_name, query, variables):
        self.name = name
        self.operation_name = operation_name
        self.query = query
        self.variables = variables
