from settings import *
import peewee as models
import datetime


class BaseModel(models.Model):
    class Meta:
        database = db


class accounts(BaseModel):
    user = models.TextField()
    pwd = models.TextField()

    def __unicode__(self):
        return '%s: %s' % (self.user, self.pwd)
