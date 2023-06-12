from django.db import models
from django.shortcuts import reverse
from unidecode import unidecode
from django.template.defaultfilters import slugify, title
import os
from uuid import uuid4


def upload_to(instance,filename):
    extension = filename.split('.')[-1]
    new_name = "%s.%s" % (str(uuid4()), extension)
    unique_id = instance.unique_id
    return os.path.join('post', unique_id, new_name)


class Category(models.Model):
    name = models.CharField(max_length=20, verbose_name='Category name')
    
    class Meta:
        verbose_name_plural = 'Categories'
        
    def __str__(self):
        return self.name

class Post(models.Model):
    title         = models.CharField(max_length=100, blank=False, null=True, verbose_name = 'Enter Title', 
                                    help_text = 'Title information is entered here')
    content       = models.TextField(max_length=1000, blank=False, verbose_name = 'Enter Content', null=True)
    created_date  = models.DateField(auto_now_add=True, auto_now=False)

    slug       = models.SlugField(null=True, unique=True, editable=False)

    docfile = models.FileField(verbose_name='file', null='True', upload_to='upload_to', help_text='Upload your document')
    
    unique_id = models.CharField(max_length=100, editable=True, null=True)
    categories = models.ManyToManyField(blank=True, to=Category, related_name='post')

    class Meta:
        verbose_name_plural = 'Posts'
        ordering = ['-id']

    def __str__(self):
        return "%s" %  (self.title)

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'slug':self.slug})

    def get_docfile(self):
        if self.docfile:
            return self.docfile.url
        else:
            return None

   

    def get_unique_slug(self):
        sayi = 0
        slug = slugify(unidecode(self.title))
        new_slug = slug
        while Post.objects.filter(slug=new_slug).exists():
            sayi += 1
            new_slug = "%s-%s" % (slug, sayi)
        slug = new_slug
        return slug

    def save(self, *args, **kwargs):
        if self.id is None:
            new_unique_id = str(uuid4())
            self.unique_id = new_unique_id 
            self.slug = self.get_unique_slug()
        else:
            post = Post.objects.get(slug=self.slug)
            if post.title != self.title:
                self.slug = self.get_unique_slug()
        super(Post, self).save(*args, **kwargs)

    