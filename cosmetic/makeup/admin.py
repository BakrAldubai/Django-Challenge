from django.contrib import admin
from .models import Brand , Product , Customer ,Order
# Register your models here.




class BrandAdmin(admin.ModelAdmin):
    list_display = ('id','name','origin','image')
    list_editable = ('name','origin','image')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name','kind','price','expir_date','brand','description', 'image')
    list_editable = ('name','kind','price','expir_date','brand','description', 'image')

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'email', 'date_created')
    list_editable = ('name', 'phone', 'email')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'product', 'date_created', 'status', 'pieces')
    list_editable = ('status',)


admin.site.register(Customer,CustomerAdmin)
admin.site.register(Brand,BrandAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Order,OrderAdmin)