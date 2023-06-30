from django.db import models

class Entry(models.Model):
    value = models.IntegerField()  # Field to store the value of the entry
    created_at = models.DateTimeField(auto_now_add=True)  # Field to store the creation timestamp of the entry

    def __str__(self):
        return f'Entry: {self.value} ({self.created_at})'  # String representation of the Entry model
