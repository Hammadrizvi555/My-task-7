from django.db import models
from django.contrib.auth.models import  AbstractUser
from django.utils import timezone





class User(AbstractUser):
    # Add your custom fields here if needed
    
    class Meta:
        # Add these to resolve the conflicts
        db_table = 'custom_user'  # Optional: custom table name
        
    # These are the critical fixes:
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='blog_api_users',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='blog_api_users',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author  = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f'Comment by {self.author.username} on {self.post.title}'
   