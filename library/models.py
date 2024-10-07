from django.db import models
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    issue_date = models.DateField(auto_now_add=True)
    return_date = models.DateField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Member(models.Model):
    name = models.CharField(max_length=100)
    membership_type = models.CharField(max_length=50, choices=[('6 months', '6 months'), ('1 year', '1 year'), ('2 years', '2 years')], default='6 months')
    membership_start = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


# Create your models here.
# library/models.py
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Member(models.Model):
    name = models.CharField(max_length=200)
    membership_type = models.CharField(max_length=20, choices=[('6 Months', '6 Months'), ('1 Year', '1 Year'), ('2 Years', '2 Years')])

    def __str__(self):
        return self.name

class Transaction(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    issue_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.book.title} - {self.member.name}"
