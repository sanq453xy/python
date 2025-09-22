from django.db import models

class TrafficData(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    current_density = models.IntegerField(default=0)
    accident_detected = models.BooleanField(default=False)

    def __str__(self):
        return f"Data from {self.timestamp}"
