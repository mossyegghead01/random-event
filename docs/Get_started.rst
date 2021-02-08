Get started
===========

Installation
------------

```pip install random-event```

Basic example:

.. code-block:: python
    :linenos:

    from random_event import events

    possible_event_list = ["Earthquake", "Tornado", "Tsunami"]

    rand_event = random_event(event_list=possible_event_list, interval=15, chance=50) 
    # every 15 second, it will decide wether it will generate an event or no, if yes it will pick random item from possible_event_list list

    @rand_event.event()
    def on_event(event):
        print(event)
    
    @rand_event.event()
    def on_error(error):
        raise error
   
    rand_event.start() # start generating random event every specified interval time
