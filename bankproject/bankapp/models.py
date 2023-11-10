from django .db import models
from multiselectfield import MultiSelectField



# Create your models here
class District(models.Model):
    Name = models.CharField(max_length=200)




    def __str__(self):
        return self.Name


class Branch(models.Model):
    Name = models.CharField(max_length=200)
    District = models.ForeignKey(District, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.Name

choices=[('Female','Female'),('Male','Male'),('Other','Other')]
accounts=[('Current Account','Current Account'),('Savings','Savings'),('RD Account','RD Account'),
          ('FD Account','FD Account'),('NRI Account','NRI Account')]
materials=(('Debit Card','Debit Card'),('Credit Card','Credit Card'),('Cheque Book','Cheque Book'))

class Customer(models.Model):
    Name = models.CharField(max_length=100)
    Date_of_birth=models.DateField(null=True,blank=True)
    Age = models.IntegerField()
    Gender = models.CharField(max_length=20,choices=choices)
    Phone_number = models.IntegerField()
    Mailid = models.EmailField()
    Address = models.TextField()
    District = models.ForeignKey(District, on_delete=models.SET_NULL, null=True)
    Branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True)
    Account_type = models.CharField(max_length=100,choices=accounts)
    Materials = MultiSelectField(choices=materials,max_choices=3,max_length=100)

    def __str__(self):
        return self.Name



