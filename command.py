class Command:
    def __init__(self, name, description, platforms, parameters, function):
        self.name = name
        self.description = description
        self.function = function
        self.parameters = parameters
        self.platforms = platforms
    
    def run(self, parameters):
        if len(parameters) != len(self.parameters):
            msg = "please run the command as follows: %s" % (self.description)
            return msg
        return self.function