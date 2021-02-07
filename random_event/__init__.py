__title__ = "random event"
__author__ = "mossyegghead01"
__license__ = 'MIT'
__copyright__ = 'Copyright 2021 mossyegghead01'
__version__ = "0.1"

from random import choice, randint
import schedule

class EventAlreadyRegisteredError(Exception):
  """Exception that throwed when 2 function with @events.event decorator have the same name."""
  pass

class InvalidEventType(Exception):
  """Exception that throwed when event function name is invalid."""
  pass

class events:
    """The main class of the module, used for most function in the module.

    :param list event_list: list of possible events to randomize
    :param int interval: interval between randomize
    :param ini chance: chance of the event occur every interval.
    """
    def __init__(self, event_list:list, interval:int, chance:int):
        self.event_list = event_list
        self.interval = interval
        self.chance = chance
        self.handlers = {}
    
    def call(self, type, *args, **kwargs):
      """Call certain function with @events.event decorator. This function is not intended to be called except from the module itself.
      use :meth:`random_event.events.call_event` instead.
      """
      if type in self.handlers:
        for h in self.handlers[type]:
          h(*args, **kwargs)

    def event(self):
      """A decorator that register event.
      You Can't have 2 decorator with same name
      
      Example:
      
      .. code-block:: python3

        @events.event()
        def recevier(event):
          print(event)

      :raises EventAlreadyRegisteredError: Event (function name) already registered
      :raises InvalidEvent: Event (function) name is invalid
      """
      def registerhandler(handler):
        type = handler.__name__
        if type in self.handlers:
          raise EventAlreadyRegisteredError("Event with name "+type+" Already registered")
        else:
          valid_types = ["recevier"]
          if type in valid_types:
            self.handlers[type] = [handler]
          else:
            raise InvalidEventType("Function name is not a valid event")
        return handler
      return registerhandler
    
    def run_event(self):
      if randint(1, 100) <= self.chance:
        self.call("recevier", choice(self.event_list))
    
    def call_event(self):
      """Used to call event manually."""
      self.run_event()
    
    def start(self):
      """Start scheduler task to run the module every specified interval time. at that time it will randomize wether the event will occur or not and what event happened from the event_list param"""
      schedule.every(self.interval).seconds.do(self.run_event)
      while True:
        schedule.run_pending()