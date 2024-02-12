from django.db import models

# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    year = models.PositiveSmallIntegerField()
    actors = models.CharField(max_length=200)
    review = models.TextField()
    # "s" or "ss" is stored is db & 1 o 2 is displayed to the user
    STARS = (
        ("s", 1),
        ("ss", 2),
        ("sss", 3),
        ("ssss", 4),
    )
    # "choices" will show predefined choices to the user i.e STARS
    stars = models.CharField(
        max_length=4,
        choices=STARS,
        default=1,
    )

    def __str__(self):
        return self.title
