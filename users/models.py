from django.contrib.auth.models import AbstractUser
from django.db import models
from django_countries.fields import CountryField


# username:comerset123 email:comerset@email.com pass:ecom0987654321
# sub_username:kaycool123 email: kay123@email.com pass: kay123456789
class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.PositiveIntegerField(null=True, blank=True)
    country = CountryField(multiple=False)
    occupation = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField('email address', unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["username"]

    # def get_absolute_url(self):
    #     return reverse('edit_custom_user', args=[str(self.pk)])
