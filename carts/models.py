from django.db import models
from store.models import Product,Variation
from accounts.models import Account
# Create your models here.
class Cart(models.Model):
  cart_id =models.CharField(max_length=250,blank=True)
  date_added=models.DateField(auto_now_add=True)

  def __str__(self):
    return self.cart_id
  

class CartItem(models.Model):
  user=models.ForeignKey(Account,on_delete=models.CASCADE, null=True)
  product = models.ForeignKey(Product,on_delete=models.CASCADE)
  variations=models.ManyToManyField(Variation, blank=True)
  cart =models.ForeignKey(Cart,on_delete=models.CASCADE,null=True)
  quantity =models.IntegerField()
  is_active=models.BooleanField(default=True)

  
  def sub_total(self):
    return self.product.price * self.quantity

  def __str__(self):
    return self.product.product_name
  
  from django.db import models
from django.utils import timezone

class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True)
    discount = models.PositiveIntegerField(help_text="Discount in percentage")
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    active = models.BooleanField(default=True)
    used = models.BooleanField(default=False)  # 🔐 one-time use

    def is_valid(self):
        now = timezone.now()
        return (
            self.active and
            not self.used and
            self.valid_from <= now <= self.valid_to
        )

    def __str__(self):
        return self.code

