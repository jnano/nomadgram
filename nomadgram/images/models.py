from django.db import models
from nomadgram.users import models as user_models

class TimeStempedModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True



class Image(TimeStempedModel):

    file = models.ImageField()
    location = models.CharField(max_length=140)
    caption = models.TextField()



class Comment(TimeStempedModel):

    message = models.TextField()



class Like(TimeStempedModel):
    creator = models.ForeignKey(user_models.User)