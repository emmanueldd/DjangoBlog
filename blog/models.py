from django.db import models
from django.core.urlresolvers import reverse
from django_markdown.models import MarkdownField
from django.contrib.auth.models import User

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    def __str__(self):
        return self.user.username

class EntryQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)
class Tag(models.Model):
    slug = models.SlugField(max_length=200, unique=True)
    def __str__(self):
        return self.slug

class Entry(models.Model):
    title = models.CharField(max_length=200)
    body = MarkdownField()
    slug = models.SlugField(max_length=200, unique=True)
    publish = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag)
    objects = EntryQuerySet.as_manager()

    def get_absolute_url(self):
        return reverse("entry_detail", kwargs={"slug": self.slug})


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Blog Entry"
        verbose_name_plural = "Blog Entries"
        ordering = ["-created"]
