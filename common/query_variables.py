class QueryVariables:
    def __init__(self, **kwargs):
        self.variables = kwargs

    def set_variable(self, key, value):
        self.variables[key] = value

    def get_variables(self):
        return self.variables
