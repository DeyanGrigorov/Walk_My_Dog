# from django import forms
# from django.contrib.auth import authenticate, get_user_model
# from django.core.exceptions import ValidationError
# from django.db.models.signals import post_save
# from django.dispatch import receiver
#
# from walk_my_dog.walkmydog_auth.models import Profile, WalkMyDogUser
#
# UserModel = get_user_model()
#
#
# #
# @receiver(post_save, sender=UserModel)
# def user_created(sender, instance, created, **kwargs):
#     if created:
#         profile = Profile(
#             user=instance,
#
#         )
#         profile.first_name = instance.first_name
#         profile.last_name = instance.last_name
#         profile.city = instance.city
#         profile.city = instance.city
#
#         profile.save()

# @receiver(post_save, sender=UserModel)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#
#
# @receiver(post_save, sender=UserModel)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()
