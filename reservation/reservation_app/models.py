from django.db import models


class ModelHall(models.Model):
    name_room = models.CharField(max_length=255, unique=True)
    capacity_room = models.SmallIntegerField()
    projector_available = models.BooleanField(default=False)




#class ReservationRoom(models.Model):
