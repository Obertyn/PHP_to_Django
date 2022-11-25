from django.db import models
import datetime

class Users(models.Model):
    id_user = models.BigAutoField(primary_key=True)
    user = models.CharField(max_length=200)
    password = models.CharField(max_length=130)
    email = models.EmailField()
    wood = models.PositiveIntegerField(default=0)
    stone = models.PositiveIntegerField(default=0)
    food = models.PositiveIntegerField(default=0)
    premium_time = models.DateTimeField(default=datetime.datetime.now()+datetime.timedelta(10))
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.user} {self.password} {self.email} {self.wood} {self.stone} {self.food} {self.premium_time}'

