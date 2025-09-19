from django.db import models

class ChurchMission(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    start_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name