class BaseException(Exception):
    pass

class EventAlreadyRegisteredError(BaseException):
  """Exception that throwed when 2 function with @events.event decorator have the same name."""
  pass

class InvalidEventType(BaseException):
  """Exception that throwed when event function name is invalid."""
  pass

class UnsupportedIntervalType(BaseException):
    pass