from django.db import models


class Users(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=10)
    birthday = models.DateField(null=True)
    number_of_friends = models.IntegerField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name