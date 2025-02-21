from rest_framework import viewsets

from apps.visa.models import Country, FAQ, Media, ContactRequest, Document, About
from apps.visa.serializer import CountrySerializer, MediaSerializer, FAQSerializer, ContactRequestSerializer, \
    DocumentSerializer, AboutSerializer


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    http_method_names = ['get']


class MediaViewSet(viewsets.ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer
    http_method_names = ['get']


class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
    http_method_names = ['get']


class ContactRequestViewSet(viewsets.ModelViewSet):
    queryset = ContactRequest.objects.all()
    serializer_class = ContactRequestSerializer


class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    http_method_names = ['get']


class AboutViewSet(viewsets.ModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer
    http_method_names = ['get']
