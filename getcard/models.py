from django.db import models

# Create your models here.

class form(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=225)
    phone = models.CharField(max_length=13)
    email = models.CharField(max_length=100)
    birth = models.CharField(max_length=10)
    frm = models.IntegerField(max_length=6)
    to = models.IntegerField(max_length=6)
    special_number = models.CharField(max_length=20)
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return 'Message from ' + self.name + ' - ' + self.email + ' - '+ self.special_number