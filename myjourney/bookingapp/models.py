from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns

# Create your models here.
class Tourist(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    mobile = models.IntegerField()
    email = models.EmailField(max_length=20)
    address = models.CharField(max_length=100)

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('tourist-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'

class Pack_details(models.Model):
    pack_name = models.CharField(max_length=100)
    pack_type = models.CharField(max_length=100)
    pack_price = models.IntegerField()
    pack_summary = models.TextField(max_length=1000)

    def __str__(self):
        """String for representing the Model object."""
        return self.pack_name

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('pack-detail', args=[str(self.id)])

class Booking(models.Model):
    full_name = models.CharField(max_length=100)
    pack_name = models.ForeignKey('Pack_details', on_delete=models.SET_NULL, null=True)
    from_date = models.DateField(null=True, blank=True)
    user_email = models.EmailField(max_length=30)
    phone = models.IntegerField()
    adhaar_number = models.CharField('ISBN', max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">Adhaar number number</a>')

    def __str__(self):
        """String for representing the Model object."""
        return self.full_name

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('booking-detail', args=[str(self.id)])

class Thankyou(models.Model):
    enquiry = models.TextField(max_length=100)
    cust_satisfied = (
        ('Y', 'Yes'),
        ('N', 'No')
    )

    satisfied = models.CharField(
        max_length=1,
        choices=cust_satisfied,
        blank=True,
        help_text= 'If your satisfied with our service select yes')

    def __str__(self):
        """String for representing the Model object."""
        return self.satisfied

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('thankyou', args=[str(self.id)])
