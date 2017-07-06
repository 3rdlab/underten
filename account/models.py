# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class UserProfile(models.Model):
    # This field is required.
    user = models.OneToOneField(User)
    profile_img = models.ImageField(upload_to='profile_img/%Y/%m/%d', null=True)

    def __unicode__(self):
		return self.profile_img


"""
	def create_user_profile(sender, instance, created, **kwargs):
	    if created:
	        UserProfile.objects.create(user=instance)

	post_save.connect(create_user_profile, sender=User)
"""
