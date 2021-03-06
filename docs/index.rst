.. Random Event documentation master file, created by
   sphinx-quickstart on Sun Feb  7 15:23:25 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Random Event's documentation!
========================================

Random event is a python module made to make random event at almost random time based on interval and chance

please always refer to stable unless you use version before release

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
   
   rand_event.start() # start generating random event every specified interval time

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   API
   Get_started

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
