from django.dispatch import receiver
from django.db.models.signals import post_save, m2m_changed
from .models import Blog
from user_profile.models import Follow
from notification.models import Notification





@receiver(post_save, sender = Blog)
def send_notification_to_followers_when_blog_created(instance, created, *args, **kwargs):
    if created:
        followers = instance.user.followers.all()

        for data in followers:
            follower = data.followed_by
            if not data.muted:
                Notification.objects.create(
                    content_object = instance,
                    user = follower,
                    text = f"{instance.user.username} Post a new blog.",
                    notification_types = 'Blog'
                )








@receiver(post_save, sender = Follow)
def send_notification_to_user_when_someone_followed(instance, created, *args, **kwargs):
    if created:
        followed = instance.followed
        if not instance.muted:
            Notification.objects.create(
                content_object = instance,
                user = followed ,
                text = f"{instance.followed_by.username} Started Following you.",
                notification_types = 'Follow',
            )
                

      
            
