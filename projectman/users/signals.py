from django.db.models.signals import post_save #Import a post_save signal when a user is created
from django.contrib.auth.models import User # Import the built-in User model, which is a sender
from django.dispatch import receiver # Import the receiver
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.contrib.sessions.models import Session
from django.utils import timezone
from .models import Profile, UserSession


##Profile
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
    
    
@receiver(user_logged_in)
def user_logged_in_handler(sender, request, user, **kwargs):
    # Create or update the UserSession when a user logs in
    session_key = request.session.session_key
    UserSession.objects.update_or_create(
        user=user,
        defaults={'session_key': session_key}
    )

@receiver(user_logged_out)
def user_logged_out_handler(sender, request, user, **kwargs):
    # Delete the UserSession when a user logs out
    UserSession.objects.filter(user=user).delete()

@receiver(post_save, sender=Session)
def session_update_handler(sender, instance, created, **kwargs):
    # Update the last_activity field when a session is updated (e.g., page refresh)
    if created:
        return
    user_session = UserSession.objects.filter(session_key=instance.session_key).first()
    if user_session:
        user_session.last_activity = timezone.now()
        user_session.save()