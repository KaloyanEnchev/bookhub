from django.db import models
from django.utils.text import slugify

from common.models import TimeStampModel


class Book(TimeStampModel):
    class GenreChoices(models.TextChoices):
        FICTION = 'Fiction', 'Fiction'
        NON_FICTION = 'Non-Fiction', 'Non-Fiction'
        FANTASY = 'Fantasy', 'Fantasy'
        SCIENCE = 'Science', 'Science'
        HISTORY = 'History', 'History'
        MYSTERY = 'Mystery', 'Mystery'
        MOSHTEN = 'Moshten', 'Moshten'
        JENA_MI = 'JENA_MI', 'JENA_MI'


    title = models.CharField(
        unique=True,
        max_length=100,
    )

    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
    )

    genre = models.CharField(
        max_length=50,
        choices=GenreChoices.choices,
    )

    publishing_date = models.DateField()

    description = models.TextField()

    image = models.ImageField(
        upload_to='post_images/',
        blank=True,
        null=True,
    )

    slug = models.SlugField(
        max_length=100,
        unique=True,
        blank=True,
    )

    pages = models.PositiveIntegerField(
        null=True,
        blank=True,
    )

    publisher = models.CharField(
        max_length=100,
    )

    # tags = models.ManyToManyField(
    #     "Tag"
    # )

    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = slugify(f"{self.title}-{self.publisher}")

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(
        max_length=50,
    )

    books = models.ManyToManyField(
        Book
    )

    def __repr__(self):
        return self.name

    def __str__(self) -> str:
        return self.name