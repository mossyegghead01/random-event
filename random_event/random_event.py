from random import choice, randint
import schedule

class EventAlreadyRegisteredError(Exception):
  pass

class InvalidEvent(Exception):
  pass

class events:
    def __init__(self, event_list:list, interval:int, chance:int):
        self.event_list = event_list
        self.interval = interval
        self.chance = chance
        self.handlers = {}
    
    def call(self, type, *args, **kwargs):
        if type in self.handlers:
          for h in self.handlers[type]:
            h(*args, **kwargs)

    def event(self):
      def registerhandler(handler):
        type = handler.__name__
        if type in self.handlers:
          raise EventAlreadyRegisteredError(type+" Already registered")
        else:
          valid_types = ["recevie"]
          if type in valid_types:
            self.handlers[type] = [handler]
          else:
            raise InvalidEvent("Function name is not a valid event")
        return handler
      return registerhandler
    
    def run_event(self):
      if randint(1, 100) <= self.chance:
        self.call("recevie", choice(self.event_list))
    
    def start(self):
      schedule.every(self.interval).seconds.do(self.run_event)
      while True:
        schedule.run_pending()