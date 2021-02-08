API reference
=============

.. class:: events(event_list:list, interval:int, chance:int)
   The main class of the module, used for most function in the module.

   :param list event_list: list of possible events to randomize
   :param str interval_type: Interval type (seconds, minutes, hours)
   :param int interval: interval between randomize
   :param int chance: chance of the event occur every interval.
   :raises UnsupportedIntervalType: Passed interval type is unsupported

   .. method:: call(type, *args, **kwargs)
      Call certain function with @events.event decorator. 
      This function is not intended to be called except from the module itself.
      For manual on_event calling use :meth:`call_event` instead.
   
   .. decorator:: event()
      A decorator that register event. You Can't have 2 decorator with same name
      
      Example:
      
      .. code-block:: python3

         @events.event()
         def on_event(event):
            print(event)

      Current supported function name. Anything else will raise :exc:`InvalidEventType` error
      * on_event
      * on_error

      :raises EventAlreadyRegisteredError: Event (function name) already registered
      :raises InvalidEventType: Event (function) name is invalid
   
   .. method:: call_event()
      Used to call on_event manually.   
   
   .. method:: start()
      Start scheduler task to run the module every specified interval time. 
      at that time it will randomize wether the event will occur or not 
      and what event happened from the event_list parameter.

   .. method:: stop()
      stop the module task

.. exception:: BaseException
   Base exception for all exception.
   
.. exception:: EventAlreadyRegisteredError
   Indicate that the event already registered, 
   most probably caused by 2 function with the same name(if both function has @event decorator)

.. exception:: InvalidEventType
   Indicate that the function name is invalid, 
   caused by unsupported function name

.. exception:: UnsupportedIntervalType
   Raised when unsupported interval type passed