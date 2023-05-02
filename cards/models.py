from django.db import models
from django.utils.html import format_html
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
# Create your models here.

class Card(models.Model):
	cID	= models.TextField(verbose_name="卡牌编号",max_length=10)
	cName	= models.TextField(verbose_name="卡牌名称",max_length=10)
	cCost	= models.TextField(verbose_name="费用",max_length=20)
	cEffect	= models.TextField(verbose_name="卡牌效果",max_length=50)
	cStory	= models.TextField(verbose_name="卡牌趣闻",max_length=50)
	cImg	= models.ImageField(verbose_name="原画",upload_to="card/",blank=True)
	cImg_R	= ImageSpecField(
        source='cImg',
        processors=[ResizeToFill(316,316)],
        format='JPEG',
        options={'quality':95}
    ) 
        
	def image_data(self):
		if self.cImg:
			return format_html(
				'<img src="/media/card/{}" height="160px"/>',
				self.cImg,
			)
		else:
			return format_html(
				'<img src="/static/img/IMG_LOST.png" height="160px"/>',
			)
	
	def ___str___(self):
		return self.cName
	
	class Meta:
		verbose_name = "卡牌"
		verbose_name_plural = verbose_name

class Files(models.Model):
    Fdiscription = models.CharField(verbose_name="文件描述",max_length=40,default=" ")
    FField = models.FileField(verbose_name="文件",upload_to='file/')

    def __str__(self):
        return self.Fdiscription

    class Meta:
        verbose_name = '文件'
        verbose_name_plural = '文件'