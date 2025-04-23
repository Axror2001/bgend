from django.db import models

class AboutUs(models.Model):
    our_history1 = models.TextField(blank=True, null=True)
    our_history2 = models.TextField(blank=True, null=True)


    def __str__(self):
        return "Bizning tarix sahifasi"