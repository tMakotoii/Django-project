from django.db import models
from django.db.models import CASCADE

from string import punctuation

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    in_menu= models.BooleanField(default=True)
    order = models.IntegerField(default=1)

    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Author(models.Model):
    name = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to='avatars')
    bio = models.CharField(max_length=255)

    objects = models.Manager()

    def __str__(self):
        return self.name


class Article(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    content = models.TextField()
    content_words_count = models.IntegerField(null=True, blank=True)
    short_description = models.TextField()
    main_image = models.ImageField(upload_to='images')
    pub_date = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category)
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)

    objects = models.Manager()

    def __str__(self):
        return self.name

    def count_unique_words(self):
        text = self.content.replace('<p>', '').replace('</p>', '')
        for symbol in punctuation:
            text = text.replace(symbol, '')
        words = text.split()
        return len(set(words))


class Comment(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    comment = models.TextField()
    article = models.ForeignKey(Article, on_delete=CASCADE, related_name='comments')
    pub_date = models.DateTimeField(auto_now_add=True)
    is_moderated = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    articles = models.ManyToManyField(Article)
    # in_menu= models.BooleanField(default=True)
    # order = models.IntegerField(default=1)

    def __str__(self):
        return self.name
