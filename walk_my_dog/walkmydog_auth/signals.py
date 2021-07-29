# from django import forms
# from django.contrib.auth import authenticate, get_user_model
# from django.core.exceptions import ValidationError
# from django.db.models.signals import post_save
# from django.dispatch import receiver
#
# from walk_my_dog.walkmydog_auth.models import Profile, WalkMyDogUser


# @receiver(post_save, sender=UserModel)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#
#
# @receiver(post_save, sender=UserModel)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()
