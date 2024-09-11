from django.db import models

class MoodEntry(models.Model):
    nama = models.CharField(max_length=200)
    kelas = models.IntegerField()
    mood = models.CharField(max_length=255)
    time = models.DateField(auto_now_add=True)
    feelings = models.TextField()
    mood_intensity = models.IntegerField()

    @property
    def is_mood_strong(self):
        return self.mood_intensity > 5