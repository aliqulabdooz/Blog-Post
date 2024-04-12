from django.db import models


class Post(models.Model):
    STATUS_CHOICES = (
        ('pub', 'Published'),
        ('drf', 'Draft'),
    )

    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=False)
    title = models.CharField(max_length=50, null=False)
    text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_CHOICES, default='drf', max_length=3)

    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(max_length=50, null=False)
    email = models.EmailField(null=False)
    caption = models.TextField(null=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    post = models.ManyToManyField(Post)

    def __str__(self):
        return self.name

