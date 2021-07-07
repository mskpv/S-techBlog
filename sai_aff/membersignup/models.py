from django.db import models

# Create your models here.

class Visitor_Infos(models.Model):
    ip_address = models.GenericIPAddressField()
    page_visited = models.TextField()
    event_date = models.DateTimeField(auto_now= True)