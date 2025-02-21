from django.contrib import admin
from apps.visa.models import (
    Country,
    Media,
    Document,
    FAQ,
    About,
    ContactRequest
)

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    pass

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    pass

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    pass

@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    pass

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    pass
