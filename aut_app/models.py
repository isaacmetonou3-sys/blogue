from django.db import models

class Article(models.Model):
    titre=models.CharField(max_length=50)
    auteur=models.CharField(max_length=50)
    contenu=models.TextField()
    
    date_publication=models.DateField(auto_now_add=True)
    class Meta:
        ordering= ['-date_publication']
    images = models.URLField(max_length=1000, blank=True, null=True)
    
    def __str__(self):
        return self.titre


