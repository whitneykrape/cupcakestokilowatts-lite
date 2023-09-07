from django.db import models

class Ideas(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    
    def categoriesMatching(self):
        return 'A %s is "%s"' % (self.name, self.category)