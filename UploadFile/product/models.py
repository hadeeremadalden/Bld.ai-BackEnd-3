from django.db import models

# Create your models here.



class File(models.Model):
  file = models.FileField(blank=False, null=False)

  class Meta:
    db_table = "File"
  
  