.. Random Event documentation master file, created by
   sphinx-quickstart on Sat Feb  6 17:30:34 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Random Event's documentation!
========================================

A python module made to make random event at almost random time based on interval and chance

Basic example:
.. code-block:: python
   from random_event import events

   possible_event_list = ["asteroid", "volcano", "earthquake"]

   randomevent = events(event_list=possible_event_list, interval=20, chance=50) # pick one event from the list every 20 seconds with chance of 50% the event will occur

   @randomevent.event()
   def recevie(event): # currently the only event name accepted, more will added soon
      print(event)
   
   randomevent.start() # start the random event

.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
