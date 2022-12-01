from django.db import models
# from django.books import Book

class User(models.Model): # use Django Model object to create fields
    name = models.CharField(max_length = 250) # max_length required
    username = models.CharField(max_length = 250, unique = True)
    email = models.EmailField(max_length = 250, unique = True)
    password = models.CharField(max_length = 250)
    # books = models.OneToMany(Book) (check doccumentation for correct syntax)

    def __str__(self): # prints name instead of Object with all attributes
        return self.name
