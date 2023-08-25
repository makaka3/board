from django.contrib import admin
from .models import Product,Rubric
from users.models import User

admin.site.register(Product)

admin.site.register(Rubric)

admin.site.register(User)