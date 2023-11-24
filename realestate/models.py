from django.db import models
TYPE =[
    ('B','Bunglow'),('A','Apartment')
]

class Estate(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=30)
    description = models.CharField(max_length=30)

    def __str__(self):
        return f'''{self.name}-
        {self.location}
        {self.description}'''
    
class Land(models.Model):
    estate = models.ForeignKey(Estate, on_delete=models.CASCADE)
    size = models.CharField(max_length=20)
    price = models.IntegerField()
    statu = models.CharField(max_length=30)
    def __str__(self):
        return f'''{self.estate}-
        {self.size}-{self.price}-
        {self.statu}'''

class House(models.Model):
    type = models.CharField(max_length=2, choices=TYPE)
    bedroom = models.CharField(max_length=20)
    toilet = models.CharField(max_length=10)
    size = models.CharField(max_length=20)
    price = models.CharField(max_length=20)
    statu = models.CharField(max_length=10)

    def __str__(self):
        return f'''{self.type}-
        {self.bedroom}-{self.toilet}-{self.size}-
        {self.price}-{self.statu}'''  

class Customer(models.Model):
    customer_name = models.CharField(max_length=30, verbose_name='Customer Name')
    address = models.CharField(max_length=30)
    contact = models.CharField(max_length=20)
    land = models.ForeignKey(Land, on_delete=models.CASCADE)
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    amount_to_be_paid = models.CharField(max_length=20, verbose_name='Amount to be Paid')
    def __str__(self):
        return f'''{self.customer_name}-
        {self.address}-{self.contact}-{self.land}-
        {self.house}-{self.amount_to_be_paid}'''

class Payment(models.Model):
    payment_date = models.DateField(verbose_name='Payment Date', help_text='Format: YYYY-MM-DD')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    amt_pd = models.CharField(max_length=20, verbose_name='Amount Paid')
    rec_by = models.CharField(max_length=20, verbose_name='Received By')
    def __str__(self):
        return f'''{self.payment_date}-
        {self.customer}-{self.amt_pd}-
        {self.rec_by}'''

class Title(models.Model):
    county = models.CharField(max_length = 30)
    sub_county = models.CharField(max_length = 30)
    block = models.IntegerField()
    plot = models.IntegerField()
    acrage = models.CharField(max_length = 30)
    title_photo = models.ImageField(upload_to ="images/", default="")
    def __str__(self):
        return f'''{self.county}-{self.sub_county}-
        {self.block}-{self.plot}-{self.acrage}'''