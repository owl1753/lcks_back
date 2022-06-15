from django.contrib import admin
from .models import Team, Match, Comment

admin.site.register(Match)
admin.site.register(Team)
admin.site.register(Comment)

# Register your models here.
