from django.db import models

from paste.utils import short_hash


class SnippetManager(models.Manager):
    def create_snippet(self, content, theme):
        snippet = self.create(url_hash=short_hash(),
                              delete_hash=short_hash(),
                              content=content,
                              theme=theme)
        return snippet


class Snippet(models.Model):
    url_hash = models.CharField(max_length=8)
    delete_hash = models.CharField(max_length=8)
    content = models.TextField()

    objects = SnippetManager()


class Theme(models.Model):
    name = models.CharField(max_length=32)


class SnippetTheme(models.Model):

    class Meta:
        unique_together = ('snippet', 'theme')

    snippet = models.ForeignKey(Snippet)
    theme = models.ForeignKey(Theme)
    content = models.TextField()
