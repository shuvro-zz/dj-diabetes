# coding: utf-8
from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Meals(models.Model):

    """
        Meals
    """
    user = models.ForeignKey(User)
    food = models.TextField()
    breakfast_lunch_diner = models.CharField(max_length=2)
    date_meal = models.DateField(null=True)
    hour_meal = models.TimeField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Meal'
        verbose_name_plural = 'Meals'

    def show(self):
        return "Meals %s %s %s %s %s %s" % (self.user_id, self.food,
                                            self.breakfast_lunch_diner,
                                            self.date_meal,
                                            self.created, self.modified)

    def __str__(self):
        return "%s (date: %s)" % (self.food, self.date_meal)
