from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, render
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

from underten.forms import UserCreateForm

# index view (just redirect to login page)
def index(request):
  return HttpResponseRedirect('/login')

def hello(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))


def search_form(request):
    return render(request, 'search_form.html')

def search(request):
    if 'q' in request.GET:
        message = 'You searched for: %r' % request.GET['q']
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)
