from django.db import models

# Create your models here.
class customerdetails(models.Model):
    firstname=models.CharField(max_length=200,null = False)
    lastname=models.CharField(max_length=150,null = False)
    email=models.EmailField(max_length=254,null = False)
    mobileno=models.IntegerField(null = False)
    updatedby=models.CharField(max_length=200)
    updatedon=models.DateTimeField(auto_now_add=True)



class Address(models.Model):
    customer_id = models.ForeignKey(customerdetails, on_delete=models.CASCADE)
    addr_line1=models.CharField(max_length=254)
    addr_line2=models.EmailField(max_length=254)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=200)
    pincode=models.IntegerField(null = False)
    updatedby=models.CharField(max_length=200)
    updatedon=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.addr_line1


