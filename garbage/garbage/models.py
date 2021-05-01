from django.db import models

class UserDB(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    openId = models.CharField(max_length=100, null=True)
    openId2 = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=15, null=True)
    score = models.IntegerField(default=0)
    auth = models.IntegerField(default=0)
    # face = models.ImageField(upload_to='img', null=True)

class MachDB(models.Model):
    name = models.CharField(max_length=20)
    number = models.IntegerField(default=0)
    locate = models.CharField(max_length=100)


# from garbage import models
# models.UserDB.objects.create(username="admin", password="password", openId="")
