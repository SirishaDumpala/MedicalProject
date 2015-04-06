from django.db import models

from .events import Event
from .calendars import Calendar

COLOR_TYPE = (
    ('blue', '#1EB2DE'),
    ('red', '#EF4023'),
    ('yellow' , '#FFD52F'),
)
class MyCalendar(Calendar):
    color = models.CharField(max_length=6, choices=COLOR_TYPE)
    nb_slot = models.PositiveIntegerField()

class MyEvent(Event):
    pass

