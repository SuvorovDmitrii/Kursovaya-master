import datetime

from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.views import View
from qsstats import QuerySetStats
from .models import *
from django.http import HttpResponse
from .forms import UserRegistrationForm, RequestCreate
from django.core.paginator import Paginator
from django.core.files.storage import FileSystemStorage
from django.views.generic.detail import DetailView
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.


def index(request):
    reqs = Request.objects.all()  # fetching all post objects from database
    model = Status.objects.all()
    com_ss = QuerySetStats(reqs, 'datetime')



    p = Paginator(reqs, 3)
    page_obj = p.page(1)
    return render(request, "index.html", context={'page_obj':page_obj, 'com_ss':com_ss})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)

        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()

            return render(request, 'registration/login.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/registration.html', {'user_form': user_form})

def requestUser(request):
    if request.method == 'POST':
        url = reverse('main')
        ret = HttpResponseRedirect(url)
        request_form = RequestCreate(request.POST, request.FILES)
        if request_form.is_valid():
            new_request = request_form.save(commit=False)
            new_request.person_id = request.user.id
            print(new_request.img)
            new_request.save()
            # new_request['user'] = request_form.users()
            # new_request.id = User.objects.filter(id__exact = request.user.id)
            return ret
    else:
        request_form = RequestCreate()
    return render(request, 'request_create.html', {'request_form': request_form})

# def get_request(request):
#     requests = Request.objects.all
#     return render(request, 'registration/user_room_admin.html', context={'requests':requests})


class SectionView(View):

    def get(self, request):
        #req = get_object_or_404(Request)
        sort = request.GET.getlist('sort')
        articles = Request.objects.all().order_by(*sort)
        print(request.GET.getlist('sort'))
        return render(
            request=request,
            template_name='my_orders.html',
            context={

                'articles': articles
            }
        )


class SectionViewAdmin(View):

    def get(self, request):
        #req = get_object_or_404(Request)
        sort = request.GET.getlist('sort')
        articles = Request.objects.all().order_by(*sort)
        print(request.GET.getlist('sort'))
        return render(
            request=request,
            template_name='registration/user_room_admin.html',
            context={
                'articles': articles
            }
        )


def show_orders(request):
    requests = Request.objects.all
    return render(request, 'my_orders.html', context={'requests':requests})
# class BaseUserSet(RequestCreate):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.queryset = User.objects.filter(id__exact=self.request.user.id)

def getStatistic(req):
    model = Status.objects.all()
    com_ss = QuerySetStats(model, 'request')

    return render(req, 'statistic.html', context={'com_ss':com_ss})





# User.get(user=self.request.user.id)