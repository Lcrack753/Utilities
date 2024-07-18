from django.db import models
import uuid

# Create your models here.
class Autocomplete(models.Model):
    name = models.CharField(max_length=25)
    last = models.CharField(max_length=25)
    age = models.IntegerField()

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self) -> str:
        return f"{self.last.upper()} {self.name}"