#-*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.forms import ModelForm
from product.models import Review

from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
# for WYSIWYG editor

class ReviewForm(ModelForm):

	class Meta:
		model = Review
		fields = ['title', 'product','body']
		#fields = ['title', 'body']
		widgets = {
            'body': SummernoteWidget(),
        }

