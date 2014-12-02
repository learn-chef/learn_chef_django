from django.db import models
from django.utils import timezone

class Impression(models.Model):
  ip_addr = models.CharField('user IP address', max_length=15)
  view_date = models.DateTimeField('date viewed', default=timezone.now, editable=False)
  image_name = models.CharField('image name', max_length=1024)
  category = models.CharField('image category', max_length=128)

  def __str__(self):
    return "ip: %s, image: %s" % (self.ip_addr, self.image_name)
