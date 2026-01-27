class InvalidKeyError(Exception):

    def __init__(self, message='Invalid key'):
        super().__init__(message)
