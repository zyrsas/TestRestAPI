from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class Answer(models.Model):
    answer1 = models.TextField(default=None)
    answer2 = models.TextField(default=None)
    answer3 = models.TextField(default=None)
    answer4 = models.TextField(default=None)
    is_correct = models.IntegerField(default=1)

    def __str__(self):
        return u"A: %s; B: %s; C: %s; D: %s;" % (self.answer1, self.answer2, self.answer3, self.answer4)


class Question(models.Model):
    question = models.TextField(verbose_name="Question")
    answer = models.ForeignKey(Answer)

    class Meta:
        ordering = ("question",)

    def __str__(self):
        return self.question


class UserInfo(models.Model):
    name = models.CharField(max_length=50)
    rezult = models.IntegerField(default=0)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class Test(models.Model):
    title = models.CharField(max_length=100)
    questions = models.ManyToManyField(Question)
    date_publisher = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(UserInfo)

    class Meta:
        ordering = ("title",)

    def __str__(self):
        return self.title


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)




