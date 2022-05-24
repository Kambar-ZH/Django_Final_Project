import datetime

from django.db import models
from book.utils import *
from django.contrib.auth.models import AbstractBaseUser


class UserProfile(AbstractBaseUser):
    roles = models.PositiveSmallIntegerField(choices=USER_CATEGORIES, default=GUEST)


class BookJournalBase(models.Model):
    name = models.CharField(max_length=200, blank=False)
    price = models.FloatField(blank=False)
    description = models.CharField(max_length=500, blank=True, null=True)
    created_at = models.DateField(editable=True, default=datetime.date.today)

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ('id',)

    def __str__(self):
        return f'{self.id}: {self.name}'


class Book(BookJournalBase):
    num_pages = models.IntegerField(blank=False)
    genre = models.PositiveSmallIntegerField(choices=BOOK_CATEGORIES, default=FANTASY)

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ('id',)

    def __str__(self):
        return f'{self.id}: {self.name}'


class Journal(BookJournalBase):
    publisher = models.CharField(max_length=100, blank=False)
    type = models.PositiveSmallIntegerField(choices=JOURNAL_CATEGORIES, default=SPORT)

    class Meta:
        verbose_name = 'Журнал'
        verbose_name_plural = 'Журналы'
        ordering = ('id',)

    def __str__(self):
        return f'{self.id}: {self.name}'
