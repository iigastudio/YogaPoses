from pyexpat import model
from django.db import models
# Import user model
from django.contrib.auth.models import User


# Create your models here.
LEVEL_CHOICES = [
    ('beginner', 'Beginner'),
    ('advanced', 'Advanced'),
    ('intermediate', 'Intermediate'),
]

# Create Yoga model
class Yoga(models.Model):
    # Attribute to store Yoga Pose name as charfield
    name = models.CharField(max_length=300)
    # Attribute to store Yoga pose description as text allowing null and blank
    description = models.TextField(max_length=3000, null=True, blank=True)
    # Attribute to store Yoga level as charater choice
    level = models.CharField (max_length=13, choices=LEVEL_CHOICES)
    # Attribute to store Yoga pose image as imagefield
    image = models.ImageField(upload_to='upload/', default="")
    # Attribute to store rating as int, use validators for min and max values
    posted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # Attribute to store when yoga was last updated, automatically updates time when changed
    updated_at = models.DateTimeField(auto_now=True)
    # Attribute to store when yoga was created, update only once when created
    created_at = models.DateTimeField(auto_now_add=True)

    # Override string representation of object
    def __str__(self):
        # Return yoga pose name when printing yoga model
        return self.name

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url