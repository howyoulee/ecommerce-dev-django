from django.db import models

# Create your models here.

class Category(models.Model):

    name = models.CharField(max_length=250, db_index=True)

    slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        
        # 显示复数情况时, 自动变成categories
        verbose_name_plural = 'categories'

    def __str__(self):
        
        return self.name

class Product(models.Model):

    title = models.CharField(max_length=250)

    brand = models.CharField(max_length=250, default='un-branded')

    description = models.TextField(blank=True)

    slug = models.SlugField(max_length=250)

    price = models.DecimalField(max_digits=4, decimal_places=2)

    # 先创建images的文件夹, 再设置所有图片存储到images里面
    image = models.ImageField(upload_to='images/')

    class Meta:

        verbose_name_plural = 'products'

    
    def __str__(self):
        
        return self.title