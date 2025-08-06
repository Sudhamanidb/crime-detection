from django.db import models
from django.contrib.auth.models import User

# Emergency Alert model
class EmergencyAlert(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    video_file = models.FileField(upload_to='emergency_videos/', null=True, blank=True)  # Handle video upload
    timestamp = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    def __str__(self):
        return f"Alert by {self.user.username} at {self.timestamp}"

# User profile model
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username
