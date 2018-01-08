from django.contrib import admin

from . import models

@admin.register(models.Book)
class AdminBooks(admin.ModelAdmin):
    list_display = ("id", "book_type", "amount",
                    "payment_type", "category", "date")
    list_display_links = ('id','book_type',"amount")
    list_filter = ['book_type', 'payment_type','category']

    fieldsets = (
        (None,{
            "fields": ("book_type","payment_type","category")
        }),
        (None,{
            "fields": ("amount","detail","memo")
        }),
        ("Time",{
            "fields": ("date",)
        })
    )

admin.site.register(models.Category)
