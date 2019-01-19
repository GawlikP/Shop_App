from django.contrib import admin

# Register your models here.

from .models import User
from .models import Product_Type
from .models import Image
from .models import Product


admin.site.register(User)
admin.site.register(Product_Type)
admin.site.register(Image)
admin.site.register(Product)
