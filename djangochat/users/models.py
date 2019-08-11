from django.db import models


class Users(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=10)
    birthday = models.DateField(null=True)
    number_of_friends = models.IntegerField()
    token = models.IntegerField(null=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name