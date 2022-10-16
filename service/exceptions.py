class WrongType(Exception):

    def __init__(self, message):
        self.message = message


class NoPass(Exception):

    def __init__(self, message):
        self.message = message


class NoKeySentence(Exception):

    def __init__(self, message):
        self.message = message


class NoTarget(Exception):

    def __init__(self, message):
        self.message = message


class NoRussian(Exception):

    def __init__(self, message):
        self.message = message
