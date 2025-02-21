from rest_framework import serializers

from apps.visa.models import Country, FAQ, Document, Media, About, ContactRequest


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'name', 'code']


class FAQSerializer(serializers.ModelSerializer):
    country = CountrySerializer()

    class Meta:
        model = FAQ
        fields = ['id', 'question', 'answer', 'country']


class DocumentSerializer(serializers.ModelSerializer):
    country = CountrySerializer()

    class Meta:
        model = Document
        fields = ['id', 'title', 'text', 'country']


class MediaSerializer(serializers.ModelSerializer):
    country = CountrySerializer()

    class Meta:
        model = Media
        fields = ['id', 'title', 'text', 'file', 'address', 'country']


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ['id', 'title', 'text']


class ContactRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactRequest
        fields = ['id', 'title', 'text', 'email']
