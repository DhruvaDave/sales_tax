
class SalesException(Exception):
    """
        Sales Exception
    """

    def __init__(self, message="Error", code=5000, http_code=500):
        """
            Class initialization
        """
        self.code = code
        self.message = message
        self.http_code = http_code
        super(SalesException, self).__init__(message)