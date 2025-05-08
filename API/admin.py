from django.contrib import admin
from API.models import User,Order,OrderItem
# Register your models here.
# admin.site.register(User)
# admin.site.register(Order)

class OrderItemLine(admin.TabularInline):
    model=OrderItem


class OrderAdmin(admin.ModelAdmin):
    inlines=[
        OrderItemLine
    ]

admin.site.register(Order,OrderAdmin)
admin.site.register(User)

