from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=200)
    logo_url = models.CharField(max_length=200)
    rank = models.IntegerField()
    win = models.IntegerField()
    defeat = models.IntegerField()
    v_point = models.IntegerField()
    info = models.TextField()

class Match(models.Model):
    team_1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="team_1")
    team_2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="team_2")
    team_1_score = models.IntegerField()
    team_2_score = models.IntegerField()
    match_date = models.DateTimeField()
    match_set = models.IntegerField()