from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.utils import timezone

from product.forms import ReviewForm

from product.models import Product, Review



class IndexView(generic.ListView):

    template_name = 'product/index.html'
    context_object_name = 'latest_product_list'

    def get_queryset(self):
        return Product.objects.all()

# filtered by BRAND
class BrandIndexView(generic.ListView):
    #model = Product
    template_name = 'product/index.html'
    context_object_name = 'latest_product_list'

    def get_queryset(self):
        slug = self.kwargs['brand']
        return Product.objects.all().filter(brand__brand_name__startswith=slug)


class DetailView(generic.DetailView):
    model = Product
    template_name = 'product/detail.html'


class ReviewIndexView(generic.ListView):
    template_name = 'product/review.html'
    context_object_name = 'latest_review_list'

    def get_queryset(self):
        return Review.objects.all().order_by('-pub_date')


class ReviewDetailView(generic.DetailView):
    model = Review
    template_name = 'product/review_detail.html'


def review_add(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.pub_date = timezone.now()
            form.save()
        return HttpResponseRedirect("/product/reviews")
    else:
        form = ReviewForm()
    return render(request, 'product/review_add.html', {'form': form})

