from django.db import models


class Image(models.Model):
    Image = models.CharField(max_length=255)
    Label = models.CharField(db_index=True , max_length=100)
    Date = models.DateField()
    user = models.OneToOneField(
        'auth.User', on_delete=models.CASCADE
    )

    def __str__(self):
        return self.Image

