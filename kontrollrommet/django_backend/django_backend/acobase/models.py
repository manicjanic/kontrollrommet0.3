from django.db import models
import uuid as uuid_field

class Action(models.Model):
    #Unique non sequential identification
    uuid = models.UUIDField(default=uuid_field.uuid4, unique=True, editable=False)

    def __str__(self):
        return self.uuid

class Object(models.Model):
    #Unique non sequential identification
    uuid = models.UUIDField(default=uuid_field.uuid4, unique=True, editable=False)

    def __str__(self):
        return self.uuid


class Concept(models.Model):
    #Unique non sequential identification
    uuid = models.UUIDField(default=uuid_field.uuid4, unique=True, editable=False)

    def __str__(self):
        return self.uuid

