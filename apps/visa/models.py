from django.db import models


class ContactRequest(models.Model):
    title = models.CharField(max_length=255)
    email = models.EmailField()
    text = models.TextField()

    def __str__(self):
        return self.title


class FAQ(models.Model):
    question = models.TextField()
    answer = models.TextField()
    country = models.ForeignKey('Country', on_delete=models.PROTECT, related_name='faqs')

    def __str__(self):
        return self.question


class Country(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=2)

    def __str__(self):
        return self.name


class Media(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    file = models.FileField()
    address = models.TextField()
    country = models.ForeignKey(Country, on_delete=models.PROTECT, related_name='medias')

    def __str__(self):
        return self.title


class Document(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    country = models.ForeignKey(Country, on_delete=models.PROTECT, related_name='documents')

    def __str__(self):
        return self.title


class About(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return self.title
