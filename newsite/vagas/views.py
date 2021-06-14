from django.http import JsonResponse
from .models import PostVaga
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import (ListView,
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView)

from users.models import User

import simplejson as json

from django.db.models.functions import TruncMonth,ExtractMonth
from django.db.models import Count

from rest_framework.views import APIView
from rest_framework.response import Response


from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.

def home(request):
    context = {
        'title': 'Home',
        'posts': PostVaga.objects.all()
    }
    return render(request, 'vagas/home.htm', context)

class PostListView(ListView):
    model = PostVaga
    template_name = 'vagas/home.htm'
    context_object_name = 'posts'
    ordering = ['-date_posted']



class PostDetailView(DetailView):
    model = PostVaga

class PostCreateView(UserPassesTestMixin,LoginRequiredMixin,CreateView):
    model = PostVaga
    fields = ['title','faixa_salarial','escolaridade_min','requisitos']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_staff

class PostUpdateView(UserPassesTestMixin,LoginRequiredMixin,UpdateView):
    model = PostVaga
    fields = ['title','faixa_salarial','escolaridade_min','requisitos']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    

class PostDeleteView(UserPassesTestMixin,LoginRequiredMixin,DeleteView):
    model = PostVaga
    success_url = "/"
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class chart(APIView):
    labelUser = []
    dataUser = []

    labelVagas = []
    dataVagas = []

    querySetUsuarios = (
        User.objects.
        annotate(month=ExtractMonth('date_joined'))  # Truncate to month and add to select list
        .values('month')                          # Group By month
        .annotate(UsuariosCriados=Count('id'))                  # Select the count of the grouping
        .order_by()
    )

    for entry in querySetUsuarios:
        labelUser.append(entry['month'])
        dataUser.append(entry['UsuariosCriados'])
    

    querysetPostVagas = (PostVaga
    .objects
    .annotate(month=ExtractMonth('date_posted'))  # Truncate to month and add to select list
    .values('month')                          # Group By month
    .annotate(VagasPostadas=Count('id'))                  # Select the count of the grouping
    .order_by()
    )

 

    for entry in querysetPostVagas:
        labelVagas.append(entry['month'])
        dataVagas.append(entry['VagasPostadas']) 

    data = {
        'usuarios' : {
            'labels' : labelUser,
            'data' : dataUser
        },
        'vagas' : {
            'labels' : labelVagas,
            'data' : dataVagas
        },
        
    }

    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        return Response(self.data)

def charts(request):
    labelUser = []
    dataUser = []

    labelVagas = []
    dataVagas = []

    querySetUsuarios = (
        User.objects.
        annotate(month=ExtractMonth('date_joined'))  # Truncate to month and add to select list
        .values('month')                          # Group By month
        .annotate(UsuariosCriados=Count('id'))                  # Select the count of the grouping
        .order_by()
    )

    for entry in querySetUsuarios:
        labelUser.append(entry['month'])
        dataUser.append(entry['UsuariosCriados'])
    

    querysetPostVagas = (PostVaga
    .objects
    .annotate(month=ExtractMonth('date_posted'))  # Truncate to month and add to select list
    .values('month')                          # Group By month
    .annotate(VagasPostadas=Count('id'))                  # Select the count of the grouping
    .order_by()
    )

 

    for entry in querysetPostVagas:
        labelVagas.append(entry['month'])
        dataVagas.append(entry['VagasPostadas']) 

    data = {
        'usuarios' : {
            'labels' : labelUser,
            'data' : dataUser
        },
        'vagas' : {
            'labels' : labelVagas,
            'data' : dataVagas
        },
        
    }
    return render(request, 'vagas/chart.htm',data)


def about(request):
    return render(request, 'vagas/about.htm', {'title': 'About'})