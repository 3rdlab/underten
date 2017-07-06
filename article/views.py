from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.utils import timezone

from django.contrib.auth.decorators import login_required

from article.models import Article, ArticleCategory
from article.forms import ArticleForm



# Create your views here.


class IndexView(generic.ListView):

    template_name = 'article/index.html'
    context_object_name = 'latest_article_list'

    #pagination!!
    paginate_by = 10

    def get_queryset(self):
        username = None
        if self.request.user.is_authenticated():
            username = self.request.user.username
        return Article.objects.filter(pub_date__lte = timezone.now()).order_by('-pub_date')

# filtered by Category
class CategoryIndexView(generic.ListView):

    template_name = 'article/index.html'
    context_object_name = 'latest_article_list'

    def get_queryset(self):
        slug = self.kwargs['category']
        return Article.objects.all().filter(category__name__startswith=slug)

    def get_context_data(self, **kwargs):
        slug = self.kwargs['category']
        cat_id = ArticleCategory.objects.get(name__startswith = slug)
        context = super(CategoryIndexView, self).get_context_data(**kwargs)
        context.update({'cat_id': cat_id.id})
        return context



class DetailView(generic.DetailView):
    model = Article
    template_name = 'article/detail.html'


def hello(request):
    return HttpResponse("Hello World!")

@login_required
def add_new(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.pub_date = timezone.now()
            form.save()
        return HttpResponseRedirect("/")
    else:
        if request.GET.get('cat') != None:
            cat = request.GET.get('cat')
        else:
            cat = 2
        form = ArticleForm(initial={'category':cat} )

    return render(request, 'article/add_new.html', {'form': form})
