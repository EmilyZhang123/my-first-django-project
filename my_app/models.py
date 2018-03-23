# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Article(models.Model):
    tittle = models.CharField(max_length=32,default='Tittle')
    content = models.TextField(null=True)
    pub_time = models.DateTimeField(null=True)

    def __unicode__(self):
        return self.tittle
