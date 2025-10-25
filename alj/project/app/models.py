from django.db import models
from django.contrib.auth.models import User

class Session(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session_date = models.DateTimeField()
    duration = models.PositiveIntegerField()  # in minutes
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return f"Session for {self.user.username} on {self.session_date}"
class Progress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    weight = models.FloatField()
    body_fat = models.FloatField()
    muscle_mass = models.FloatField()

    def __str__(self):
        return f"Progress for {self.user.username} on {self.date}"
