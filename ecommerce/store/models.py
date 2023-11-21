from django.db import models

# Create your models here.

class Catagory(models.Model):
    
    
    name = models.CharField(max_length=250, db_index=True)
    slug = models.SlugField(max_length=250, unique=True)
    
    class Meta:
        verbose_name_plural = 'catagories'
     
    def _str__(self):
        return self.name
    
    class Product(models.Model):
        title = models.CharField(max_length=250)
        
        
        description = models.TextField(blank=True)
        
        slug = models.SlugField(max_length=255)
        
        price = models.DecimalField(max_digits=4, decimal_places=2)
    
        image = models.ImageField(upload_to='images/')
        
             
    class Meta:
        verbose_name_plural = 'products'
     
    def _str__(self):
        return self.title