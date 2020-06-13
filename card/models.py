from django.db import models
import datetime as dt
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class FlashCard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')
    subject=models.CharField(max_length=40)
    title=models.CharField(max_length=40)
    text=models.CharField(max_length=40)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save_card(self):
        self.save()

    def update_card(self,name,field,value):
        obj = FlashCard.objects.get(title=name)
        obj.field = value
        obj.save()

    def delete_card(self):
        self.delete()

    @classmethod
    def search_by_name(cls,search_term):
        cards = cls.objects.filter(name__icontains=search_term)
        return cards