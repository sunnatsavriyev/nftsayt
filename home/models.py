from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import Signal


class UserModel(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    email = models.EmailField(max_length=100)
    image = models.ImageField(upload_to='images/', default='static/images/Avatar (2).png', null=True ,blank=True)

    def __str__(self) -> str:
        return str(self.username)
    

class AddNftModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='image/', default='defult_img', null=True ,blank=True)
    price = models.CharField(max_length=50)
    Highest_Bid = models.CharField(max_length=50, default='0wETH')

    def __str__(self) -> str:
        return str(self.name)
    


def  create_profil(sender,instance, created, **kwargs):
    if created:
        UserModel.objects.create(
            username=instance
        )
    else:
        profilemodel = UserModel.objects.get(username=instance)
        profilemodel.email = instance.email
        profilemodel.name = instance.username 
        profilemodel.save()
        
Signal.connect(post_save,create_profil,sender=User)

