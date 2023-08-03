from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Post

@receiver(post_save, sender=Post)
def post_saved(sender, instance, created, **kwargs):
    if created:
        # Perform any necessary actions when a new post is created
        # For example, you can send an email notification to the author
        # or perform any other actions needed for new posts.
        # Example: send_new_post_notification(instance.author, instance.title)
        pass
    else:
        # Perform any necessary actions when an existing post is saved
        # For example, you can update some other related models
        # or trigger other tasks based on changes to the post.
        # Example: update_related_models(instance)
        pass
