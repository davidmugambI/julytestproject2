from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    manager = models.ForeignKey(User,on_delete=False)
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    phone = models.IntegerField()
    info = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=(
        ('M', 'Male'),
        ('F', 'Female')
    ))
    image = models.ImageField(upload_to='images/',blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date_added'] # order by the latest