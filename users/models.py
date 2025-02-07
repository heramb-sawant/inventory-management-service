import uuid
from django.db import models


# TODO: We should probably make this singular. Reasons:
# - Seems like python automatically makes it plural
# - When defining objects its nice to User() vs Users()
class Users(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.first_name

    def get_name(self) -> str:
        return f"{self.first_name} {self.last_name}"
