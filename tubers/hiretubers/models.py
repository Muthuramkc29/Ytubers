from django.db import models
from datetime import datetime
# Create your models here.

class Hiretuber(models.Model):
    # User' detail
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    interested_in = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    message = models.TextField(blank=True)

    # Tuber detail + Hidden Field
    tuber_id = models.IntegerField()
    tuber_name = models.CharField(max_length=255)
    user_id = models.IntegerField()

    created_date = models.DateTimeField(blank=True, default=datetime.now)

    def __str__(self):
        return self.email
