from django.db import models
from stdimage import StdImageField


class SimpleModel(models.Model):
    """works as ImageField"""
    image = StdImageField(upload_to='img')


class AdminDeleteModel(models.Model):
    """can be deleted through admin"""
    image = StdImageField(upload_to='img', blank=True)


class ResizeModel(models.Model):
    """resizes image to maximum size to fit a 640x480 area"""
    image = StdImageField(upload_to='img', variations={'medium': (640, 480)})


class ResizeCropModel(models.Model):
    """resizes image to 640x480 cropping if necessary"""
    image = StdImageField(upload_to='img', variations={'medium': (640, 480, True)})


class ThumbnailModel(models.Model):
    """creates a thumbnail resized to maximum size to fit a 100x75 area"""
    image = StdImageField(upload_to='img', blank=True, variations={'thumbnail': (100, 75)})


class ThumbnailCropModel(models.Model):
    """creates a thumbnail resized to 100x100 croping if necessary"""
    image = StdImageField(upload_to='img', variations={'thumbnail': (100, 100, True)})


class MultipleFieldsModel(models.Model):
    """creates a thumbnail resized to 100x100 croping if necessary"""
    image1 = StdImageField(upload_to='img', variations={'thumbnail': (100, 100, True)})
    image2 = StdImageField(upload_to='img')
    image3 = StdImageField('Some label', upload_to='img')
    text = models.CharField('Some label', max_length=10)


class AllModel(models.Model):
    """all previous features in one declaration"""
    image = StdImageField(upload_to='img', blank=True, variations={'size': (640, 480), 'thumbnail': (100, 100, True)})
