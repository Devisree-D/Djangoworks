from django.db import models

# Create your models here.
class Book(models.Model):
    book_name=models.CharField(max_length=120, unique=True)
    author=models.CharField(max_length=120)
    price=models.IntegerField(default=50)
    pages=models.IntegerField()
    category=models.CharField(max_length=120)

    def __str__(self):
        return self.book_name



    # book = Book(book_name="test1",author="mt",price=100,pages=150,category="fiction")
    #book.save()
    #book1=Book(book_name="test2",author="user",price=120,pages=150,category="romance")
    #book1.save()
