# coding: utf-8

from __future__ import unicode_literals

from django.db import models


class Lead(models.Model):

    name = models.CharField('Nome', max_length=256)
    email = models.EmailField('E-mail')
    short_description = models.TextField(u'Descrição')

    def __unicode__(self):
        return self.name + ' | ' + self.email
