from django.db import models
from .utils import detect_moods_from_text

class Song(models.Model):
    name = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/')
    lyrics = models.TextField(blank=True, null=True)
    audio = models.FileField(upload_to='songs/')

    moods = models.CharField(max_length=150, blank=True, null=True)  # Store up to 3 moods as a comma-separated string
    
    def save(self, *args, **kwargs):
        if not self.moods and self.lyrics:  # Detect moods only if not already set
            detected_moods = detect_moods_from_text(self.lyrics)
            self.moods = ", ".join(detected_moods)  # Save as comma-separated values
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.name} by {self.artist}"
