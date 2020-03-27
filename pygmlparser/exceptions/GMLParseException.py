

from pygmlparser.exceptions.GMLException import GMLException


class GMLParseException(GMLException):
    """
    Raised when the parser encounters a file format inconsistency.  The nature of
    the exception is in the message.
    """
    pass
