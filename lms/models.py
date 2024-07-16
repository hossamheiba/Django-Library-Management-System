from django.db import models
# from django.utils.text import slugify


class Books(models.Model):
    
    STATUS = [
    ("متاح", "متاح"),
    ("غير متاح" , "غير متاح"),
    ("تأجير", "تأجير"),
    ]

    author_name=models.CharField( max_length=50)
    title_book=models.CharField( max_length=50)
    image_author=models.ImageField( null=True , blank=True ,upload_to='img/')
    image_book=models.ImageField( null=True , blank=True ,upload_to='img/')
    pages=models.IntegerField( default=100)
    price = models.DecimalField(null=True , blank=True,max_digits=5, decimal_places=2)
    retal_price_day = models.DecimalField( null=True , blank=True ,max_digits=5, decimal_places=2)
    retal_period = models.DecimalField( null=True , blank=True ,max_digits=5, decimal_places=2)
    active=models.BooleanField( default=True)
    status=models.CharField( max_length=50 , choices=STATUS)
    cateogry=models.ForeignKey("Cateogry", on_delete=models.PROTECT)
    # slug=models.SlugField(blank=True ,null=True)

    
    class Meta:
        verbose_name = ("Books")
        verbose_name_plural = ("Books")
    
    def __str__(self):
        return self.author_name
    
    # def save(self,*args,**kwargs):
    #     self.slug=slugify(self.author_name)
    #     super(Books,self).save(*args,**kwargs)
    
    
    
class Cateogry(models.Model):
    name = models.CharField(max_length=25)
    
    class Meta:
        verbose_name = ("Cateogry")
        verbose_name_plural = ("Cateogry")

    def __str__(self):
        return self.name.capitalize()
        