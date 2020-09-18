from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title + '||' + str(self.author)

    def get_absolute_url(self):
        return reverse('press')
        # return reverse('post_detail', kwargs={'pk':self.pk})

        """
        Thoughts
        
        It can be done this way above also and it will display the post in the post_detail template
        but i prefer it, in my way to display straight to the press page
        """
        