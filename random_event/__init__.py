__title__ = "random event"
__author__ = "mossyegghead01"
__license__ = 'MIT'
__copyright__ = 'Copyright 2021 mossyegghead01'
__version__ = "0.2"

from random import choice, randint
import schedule
from .errors import *

class events:
    def __init__(self, event_list:list, interval:int, interval_type:str, chance:int):
        self.event_list = event_list
        self.interval = interval
        self.chance = chance
        if interval_type.lower() == "seconds" or interval_type.lower() == "minutes" or interval_type.lower() == "hours":
          self.interval_type = interval_type.lower()
        else:
          raise UnsupportedIntervalType("interval type '"+interval_type+"' is not supported")
        self.handlers = {}
        self.event_running = False
    
    def call(self, type, *args, **kwargs):
      if type in self.handlers:
        for h in self.handlers[type]:
          h(*args, **kwargs)

    def event(self):
      def registerhandler(handler):
        type = handler.__name__
        if type in self.handlers:
          if "on_error" not in self.handlers:
            raise EventAlreadyRegisteredError("Event with name '"+type+"' Already registered")
          else:
            self.call("on_error", "Event with name '"+type+"' Already registered")
        else:
          valid_types = ["on_event", "on_error"]
          if type in valid_types:
            self.handlers[type] = [handler]
          else:
            if "on_error" not in self.handlers:
              raise InvalidEventType("Function name '" + type +"' is not a valid event")
            else:
              self.call("on_error", "Function name '" + type +"' is not a valid event")
        return handler
      return registerhandler
    
    def run_event(self):
      if randint(1, 100) <= self.chance:
        self.call("on_event", choice(self.event_list))
    
    def call_event(self):
      self.run_event()
    
    def start(self):
      if self.interval_type == "seconds":
        schedule.every(self.interval).seconds.do(self.run_event)
      elif self.interval_type == "minutes":
        schedule.every(self.interval).minutes.do(self.run_event)
      elif self.interval_type == "hours":
        schedule.every(self.interval).hours.do(self.run_event)
      self.event_running = True
      while self.event_running:
        schedule.run_pending()

    def stop(self):
      self.event_running = False