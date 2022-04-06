from django.db import models

class Profile(models.Model):
    # As mentioned, there is an inherent relationship between the Profile and
    # User models. By creating a one-to-one relationship between the two, we
    # are formalizing this relationship. Every user will have one -- and only
    # one -- related Profile model.
    user = models.OneToOneField(
        'auth.User', on_delete=models.CASCADE
    )


    def __str__(self):
        return self.user.username
