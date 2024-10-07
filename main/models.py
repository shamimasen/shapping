import uuid
from django.db import models
from django.contrib.auth.models import User

class MoodEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    rating = models.IntegerField()

    @property
    def is_mood_strong(self):
        return self.rating > 5
    
    