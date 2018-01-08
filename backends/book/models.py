from django.db import models

class Book(models.Model):

    BOOK_CHOICES = (
        ('deposit','Deposit'),
        ('withdraw','Withdraw'),
    )

    PAYMENT_CHOICES = (
        ('cash','Cash'),
        ('debit','Debit'),
        ('credit','Credit'),
    )

    book_type = models.CharField(max_length=8, choices=BOOK_CHOICES, default="deposit")
    amount = models.PositiveIntegerField(default=0)
    payment_type = models.CharField(max_length=6, choices=PAYMENT_CHOICES, default="cash")
    detail = models.CharField(max_length=128, null=True, blank=True)
    category = models.ForeignKey("Category",on_delete=models.CASCADE)
    memo = models.TextField(null=True,blank=True)
    date = models.DateTimeField()

    def __str__(self):
        return "{} - {}".format(self.book_type, self.amount)

    class Meta:
        ordering = ['-id']

class Category(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


