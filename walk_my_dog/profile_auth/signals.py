from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from walk_my_dog.profile_auth.models import Profile

UserModel = get_user_model()


#
@receiver(post_save, sender=UserModel)
def user_created(sender, instance, created, **kwargs):
    if created:
        profile = Profile(
            user=instance,

        )
        profile.first_name = instance.first_name
        profile.last_name = instance.last_name
        profile.city = instance.city
        profile.category = instance.category
        # profile.age = instance.age
        # profile.phone_number = instance.phone_number

        profile.save()
