# coding: utf-8

from django.db import models

SEX_CHOICES = (
        (0, u'Ж'),
        (1, u'М'),
)

class Person(models.Model):
    f = models.CharField(max_length=30, verbose_name=u'Фамилия')
    i = models.CharField(max_length=30, verbose_name=u'Имя')
    o = models.CharField(null=True, blank=True, max_length=30, verbose_name=u'Отчество')
    pas = models.CharField(null=True, blank=True, max_length=15, verbose_name=u'Паспорт')
    sex = models.IntegerField(choices=SEX_CHOICES, verbose_name=u'Пол', default=1)

    addr1 = models.CharField(null=True, blank=True, max_length=150, verbose_name=u'Адрес 1')
    addr2 = models.CharField(null=True, blank=True, max_length=150, verbose_name=u'Адрес 2')

    tel1 = models.CharField(max_length=20, verbose_name=u'Телефон 1')
    tel2 = models.CharField(null=True, blank=True, max_length=20, verbose_name=u'Телефон 2')
    tel3 = models.CharField(null=True, blank=True, max_length=20, verbose_name=u'Телефон 3')

    prim = models.TextField(blank=True, null=True, max_length=250, verbose_name=u'Примечание')

    def __unicode__(self):
        return '%s %s %s' % (self.f, self.i, self.o)

    class Meta:
        verbose_name = "Человек"
        verbose_name_plural = "Люди"

class Org(models.Model):
    nam = models.CharField(max_length=30, verbose_name=u'Название')

    addr1 = models.CharField(null=True, blank=True, max_length=150, verbose_name=u'Адрес 1')
    addr2 = models.CharField(null=True, blank=True, max_length=150, verbose_name=u'Адрес 2')

    prim = models.TextField(blank=True, null=True, max_length=250, verbose_name=u'Примечание')

    main = models.ManyToManyField("self", blank=True, null=True, verbose_name=u'Подчиняется', symmetrical=False)

    members     = models.ManyToManyField(Person, through="Membership")

    def __unicode__(self):
        return self.nam

    class Meta:
        verbose_name = "Организация"
        verbose_name_plural = "Организации"

class Membership(models.Model):
    person = models.ForeignKey(Person, related_name="+", on_delete=models.SET_NULL, blank=True, null=True, verbose_name=u"Сотрудник")
    org = models.ForeignKey(Org, on_delete=models.SET_NULL, blank=True, null=True, verbose_name=u"Организация")
    role = models.CharField(null=True, blank=True, max_length=200, verbose_name=u'Должность')

