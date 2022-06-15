from django.db import models
from accounts.models import Account

class Team(models.Model):
    name = models.CharField(max_length=200)
    rank = models.IntegerField()
    win = models.IntegerField()
    defeat = models.IntegerField()
    v_point = models.IntegerField()
    info = models.TextField()

class Match(models.Model):
    team_1_name = models.CharField(max_length=200)
    team_2_name = models.CharField(max_length=200)
    team_1_score = models.IntegerField()
    team_2_score = models.IntegerField()
    match_date = models.DateTimeField()
    match_set = models.CharField(max_length=200)

class Comment(models.Model):
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    contents = models.CharField(max_length=1000)
