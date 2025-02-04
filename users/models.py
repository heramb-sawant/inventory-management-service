import uuid
from django.db import models


class Users(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name: models.CharField(max_length=30)
    last_name: models.CharField(max_length=30)

    def __str__(self):
        return self.id

    def get_name(self):
        return f"{self.first_name} {self.last_name}"
