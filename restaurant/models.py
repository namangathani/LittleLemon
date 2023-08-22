from django.db import models

class Booking(models.Model):
    # ID = models.IntegerField(max_length=11)
    Name = models.CharField(max_length=255)
    No_of_guests = models.IntegerField(max_length=6)
    BookingDate = models.DateTimeField()



class Menu(models.Model):
    # ID = models.IntegerField(max_lengt)
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=10,decimal_places=2)
    Inventory = models.IntegerField(max_length=5)
    def __str__(self):
        return f'{self.Title} : {str(self.Price)}'

