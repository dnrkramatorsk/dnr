# coding: utf-8

from django.db import models
from django import forms
from django.contrib.auth.models import User

# Create your models here.

class Call(models.Model):
    date   = models.DateTimeField(auto_now=True, verbose_name=u"Дата")
    phone  = models.CharField(max_length=20, blank=True, null=True, verbose_name=u"Конт.телефон")
    author = models.CharField(max_length=70, verbose_name=u"Конт.лицо")
    title  = models.CharField(max_length=70, verbose_name=u"Заголовок")
    message= models.TextField(verbose_name=u"Сообщение")
    closed = models.BooleanField(default=0, verbose_name=u"Закрыто?")
    user   = models.ForeignKey(User, blank=True, null=True)

    def __unicode__(self):
        return "%s: %s (%s)" % (self.date, self.title, self.author)

    class Meta:
        verbose_name = "Обращение"
        verbose_name_plural = "Обращения"

class CallForm(forms.ModelForm):
    class Meta:
        model = Call
        fields = ["phone", "author", "title", "message", "user"]
