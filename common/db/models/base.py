from django.db import models as dj_models
from .manager import Manager

class Model(dj_models.Model):
    objects = Manager()
    class Meta:
        abstract = True
