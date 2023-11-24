from django.db   import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation


class Comment(models.Model):
    creator        = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    content        = models.TextField()
    created_at     = models.DateTimeField(auto_now_add=True)
    modified_at    = models.DateTimeField(auto_now=True)
    
    ##1) defines a foreign key with ContentType. that can be any model
    ##2) we need an id as a foreign key for this content type
    ##3) we made this a foreign key with content_type with the object_id
    content_type   = models.ForeignKey(ContentType,on_delete=models.CASCADE)
    object_id      = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type','object_id')

class Tag(models.Model):
    value        = models.TextField(max_length=100)
    
    def Number_Of_Posts(self):
        ''' return the number of posts related to 
            this tag
        '''
        return self.posts.count()
    
    def __str__(self):
        return self.value

## if you use the comment with post very often you can add GenericRelation
## but  adding with user is not so easy
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
    comments     = GenericRelation(Comment)
    
    def __str__(self):
        return self.title
    
    