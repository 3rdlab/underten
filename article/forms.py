from django.forms import ModelForm

from article.models import Article, ArticleCategory

from ckeditor.widgets import CKEditorWidget

from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

# for WYSIWYG editor

class ArticleForm(ModelForm):

	class Meta:
		model = Article
		
		#fields = "__all__" 
		fields = ['category', 'title', 'body']
		widgets = {
            'body': SummernoteInplaceWidget(),
        }
"""
	def __init__ (self, *args, **kwargs):
	    initial = kwargs.get('initial', {})
	    initial['category'] = 2
	    kwargs['initial'] = initial
	    super(ArticleForm, self).__init__(*args, **kwargs)
"""
