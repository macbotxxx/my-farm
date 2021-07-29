from django.contrib import admin
from .models import ClientTestimonies

@admin.register(ClientTestimonies)
class ClientTestimoniesAdmin (admin.ModelAdmin):
    list_display = ('client_full_name', 'client_comment', 'client_position', 'client_image')
    list_display_links = ('client_full_name', 'client_comment', 'client_position', 'client_image')
