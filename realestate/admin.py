from django.contrib import admin

from .models import*

class EstateAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'description')
admin.site.register(Estate, EstateAdmin)

class LandAdmin(admin.ModelAdmin):
    list_display = ('estate', 'size', 'price', 'statu')
admin.site.register(Land, LandAdmin)

class HouseAdmin(admin.ModelAdmin):
    list_display = ('type', 'bedroom', 'toilet', 'size', 'price', 'statu')
admin.site.register(House, HouseAdmin)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'address', 'contact', 'land', 'house', 'amount_to_be_paid')
admin.site.register(Customer, CustomerAdmin)

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('payment_date', 'customer', 'amt_pd', 'rec_by')
admin.site.register(Payment, PaymentAdmin)

class TitleAdmin(admin.ModelAdmin):
    list_display = ('county', 'sub_county', 'block', 'plot', 'acrage', 'title_photo')
admin.site.register(Title, TitleAdmin)