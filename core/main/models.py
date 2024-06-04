from django.db import models

# Create your models here.

class Logo(models.Model):
    img = models.ImageField('Logo picture', upload_to='logo')



class Info(models.Model):
    phone = models.CharField('Phone number', max_length=50)
    email = models.EmailField('Email')
    location = models.CharField('Location', max_length=60)

    def __str__(self):
        return 'Info'
    
class Background(models.Model):
    img = models.ImageField('Background picture')
    text1 = models.TextField('Text')
    text2 = models.TextField('Text2', blank=True)
    text3 = models.TextField('Text3', blank=True)
    button_name = models.CharField('Button name', max_length=20)

    def __str__(self):
        return self.text1
    


class About(models.Model):
    text = models.TextField('Text')
    img = models.ImageField('Image of boat', blank=True)

    def __str__(self):
        return self.text
    
class Track(models.Model):
    img = models.ImageField('Image', upload_to='boat')
    text1 = models.TextField('Text')
    button = models.CharField('Button', max_length=10)


class Reviws(models.Model):
    review1 = models.TextField('Text')
    review2 = models.TextField('Text2')
    review3 = models.TextField('Text3')
    review4 = models.TextField('Text4')

    def __str__(self):
        return self.review1


class ContactUs(models.Model):
    name = models.CharField('Name', max_length=50)
    phone = models.CharField('Phone number', max_length=60)
    email = models.EmailField('Email')
    message = models.TextField('Message')