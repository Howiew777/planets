class Planets(Object):

    # constructor
    def __init__(size, type, composition):
        self.size = size
        self.type = type
        self.composition = composition

        # to string method
        def __str__(self):
            return f"Make: {self.size}"

