from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .forms import *
# Create your views here.


#!Selected Movie
class MovieSelectFormView(LoginRequiredMixin,FormView):
    form_class = MovieSelectForm
    template_name = 'movies/main.html'
    success_url = reverse_lazy('movies:add-movie-view')
    
    def post(self,*args,**kwargs):
        self.request.session['movie_select'] = self.request.POST.get('movie_select').lower().capitalize()
        print('POST request select_movie ', self.request.POST.get('movie_select').lower().capitalize())
        print('Session select movie ', self.request.session.get('movie_select'))
        return super().post(*args,**kwargs)

#!AddMovieFormView
class AddMovieFormView(LoginRequiredMixin,FormView):
    template_name = 'movies/add.html'
    success_url = reverse_lazy('homeView')
    
    def get_form_class(self,*args,**kwargs):
        movie_select = self.request.session.get('movie_select')
        if(movie_select == 'Film'):
            return FilmModelForm
        else:
            return CommercialForm
    
    def form_valid(self,form):
        form.save()
        return super().form_valid(form)
