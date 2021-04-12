from django.db import models
from django.conf import settings
from django.utils import timezone
#from multiselectfield import MultiSelectField
from django.contrib.auth.models import User

OPTIONS = ((1, 'Food'),(2, 'Books'),(3, 'Mobiles'),(4, 'Laptops'),(5, 'Baby Care'))

class Browse(models.Model):
	prod_name=models.TextField()
	category=models.TextField()
	price=models.IntegerField()
	details=models.TextField()

	def __str__(self):
		return self.prod_name


class Filters(models.Model):
        category=models.TextField()#MultiSelectField(choices=OPTIONS,blank=True)
        
        def __str__(self):
                return str(self.category)

class Cart(models.Model):
	date=models.DateTimeField(default=timezone.now)
	prod_name=models.TextField()
	price=models.TextField()
	quantity=models.IntegerField(default=1)
	category=models.TextField()

	def __str__(self):
		return self.prod_name
	

# Create your models here.
