from django.contrib import admin
from blog.models import Tag,Post

class TagAdmin(admin.ModelAdmin):
    list_display = ['value','Number_Of_Posts']
    
    class Meta:
        model = Tag
    
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":('title',)}
    list_display = ["title",'author','created_at']
    
    class Meta:
        model = Post
     

admin.site.register(Tag,TagAdmin)
admin.site.register(Post,PostAdmin)