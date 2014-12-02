# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Impression',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip_addr', models.CharField(max_length=15, verbose_name=b'user IP address')),
                ('view_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'date viewed', editable=False)),
                ('image_name', models.CharField(max_length=1024, verbose_name=b'image name')),
                ('category', models.CharField(max_length=128, verbose_name=b'image category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
