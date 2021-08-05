from django.contrib import admin
from .models import ClientTestimonies, FAQ

@admin.register(ClientTestimonies)
class ClientTestimoniesAdmin (admin.ModelAdmin):
    list_display = ('client_full_name', 'client_comment', 'client_position', 'client_image')
    list_display_links = ('client_full_name', 'client_comment', 'client_position', 'client_image')
    


@admin.register(FAQ)
class FAQadmin(admin.ModelAdmin):
    list_display_links = ('questions','answers')
    list_display = ('questions','answers')

