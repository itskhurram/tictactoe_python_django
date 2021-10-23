from django.db import models
from django.contrib.auth.models import User

STATUS_CHOICES = (('F', 'First Player Move'), ('S', 'Second Player Move'),
                  ('W', 'First Player Win'), ('L', 'Second Player Win'),
                  ('D', 'Draw'))


# Create your models here.
class Game(models.Model):
    first_player = models.ForeignKey(User, on_delete=models.CASCADE),
    second_player = models.ForeignKey(User, on_delete=models.CASCADE),
    start_time = models.DateTimeField(auto_now_add=True),
    last_active = models.DateTimeField(auto_now_add=True),
    status = models.CharField(max_length=1,
                              default='F',
                              choices=STATUS_CHOICES)

    def __str__(self):
        return "{0} vs {1}".format(self.first_player, self.second_player)


class Move(models.Model):
    x = models.IntegerField(),
    y = models.IntegerField(),
    comments = models.CharField(max_length=300, blank=True),
    by_first_player = models.BooleanField(),
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
