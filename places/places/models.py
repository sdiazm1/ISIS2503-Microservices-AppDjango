from django.db import models

class Places(models.Model):
    variable = models.IntegerField(null=False, default=None)
    name =  models.CharField(max_length=50)

    def __str__(self):
        return '%s %s' % (self.value, self.unit)