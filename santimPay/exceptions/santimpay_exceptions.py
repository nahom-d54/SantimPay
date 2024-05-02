from httpx import RequestError as ConnectionErrorException
class SantimPayBadRequestException(Exception):
    def __init__(self, message, previous=None):
        self.msg = message
        # Make sure everything is assigned properly
        super().__init__(message, 0, previous)

    # Custom string representation of object
    def __str__(self):
        return f"{self.__class__.__name__}: {self.msg}\n"
class SantimPayException(Exception):
    def __init__(self, message, previous=None):
        self.msg = message
        # Make sure everything is assigned properly
        super().__init__(message, 0, previous)

    # Custom string representation of object
    def __str__(self):
        return f"{self.__class__.__name__}: {self.msg}\n"
class SantimPayNetworkException(ConnectionErrorException):
    def __init__(self, previous=None):
        # Make sure everything is assigned properly
        super().__init__("NetworkException", 0, previous)

    # Custom string representation of object
    def __str__(self):
        return f"{self.__class__.__name__}: NetworkException\n"

class SantimPayNotFoundException(Exception):
    def __init__(self, message, previous=None):
        self.msg = message
        # Make sure everything is assigned properly
        super().__init__(message, 0, previous)

    # Custom string representation of object
    def __str__(self):
        return f"{self.__class__.__name__}: {self.msg}\n"

class SantimPayUnAuthorizedException(Exception):
    def __init__(self, message, previous=None):
        self.msg = message
        # Make sure everything is assigned properly
        super().__init__(message, 0, previous)

    # Custom string representation of object
    def __str__(self):
        return f"{self.__class__.__name__}: {self.msg}\n"