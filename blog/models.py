from django.db   import models
from django.conf import settings

class Comment(models.Model):
    creator      = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    content      = models.TextField()

class Tag(models.Model):
    value        = models.TextField(max_length=100)
    
    def Number_Of_Posts(self):
        ''' return the number of posts related to 
            this tag
        '''
        return self.posts.count()
    
    def __str__(self):
        return self.value
    
class Post(models.Model):
    author       = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.PROTECT)
    title        = models.TextField(max_length=100)
    slug         = models.SlugField()
    summary      = models.TextField(max_length=500)
    content      = models.TextField()
    created_at   = models.DateTimeField(auto_now_add=True)
    modified_at  = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(blank=True,null=True)
    tags         = models.ManyToManyField(Tag,related_name='posts')
    
    def __str__(self):
        return self.title
    
    