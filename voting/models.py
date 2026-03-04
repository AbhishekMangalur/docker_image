from django.db import models

class Vote(models.Model):
    CHOICES = (
        ('cat', 'Cat'),
        ('dog', 'Dog'),
    )

    choice = models.CharField(max_length=10, choices=CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.choice