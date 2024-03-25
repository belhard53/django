from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
from django.urls import reverse_lazy
from django.views.decorators.cache import cache_page


# Create your views here.


from django.contrib.auth.mixins import LoginRequiredMixin 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login

from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView

def index(request):
    # return HttpResponse('Hello')
    return render(request, '1.html', {'data':'Hello'}) 

#@cache_page(60 * 15)
def persons(r, id):
    if id:
        person = Person.objects.get(id=id)
        return render(r, 'person.html', {'student':person})
    data = Person.objects.all()
    return render(r, 'persons.html', {'students':data, })



class PersonAdd(LoginRequiredMixin, CreateView):
    form_class = AddUserForm
    template_name = 'form_add_user.html'
    success_url = reverse_lazy('persons')
    login_url = '/admin/'



class Courses(ListView):
    model = Course
    template_name = 'courses.html'
    context_object_name = 'courses' # или #object_list

    # def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
    #     context =  super().get_context_data(**kwargs)
    #     context['menu'] = ['menu1', 'menu2']
    #     return context
    
    # def get_queryset(self) -> QuerySet[Any]:
    #     return Course.objects.filter(id=56)
    
class Show_course(DetailView):
    model = Course
    template_name = 'course.html'
    pk_url_kwarg = 'id'

@login_required(login_url='/login/')
def course_add_view(r):
    # без модели
    
    print(r.method)
    if r.method == 'POST':
        form = AddCourseForm2(r.POST)
        if form.is_valid():
            
            # если с моделью
            form.save() 
            return redirect('courses')

            # если без модели
            # print(form.cleaned_data)
            # try:
            #     Course.objects.create(**form.cleaned_data) #без можели
                
            #     return redirect('courses')
            # except Exception as e:
            #     print(111111,e)
            #     form.add_error(None, "Ошибка....")
    else:
        form = AddCourseForm2()
        # print(1111111, type(form))
    return render(r, 'form_add_course.html', {'form':form})



def course_edit_view(r,id):
    course = get_object_or_404(Course, id=id)
    # print(course)
    if r.method=='GET':
        return render(
                    r, 
                    'form_add_course.html', 
                    {'form':AddCourseForm2(instance=course), 'id':id}
                )
    

class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'form_reg_user.html'
    # success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')
    

class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'form_login_user.html'

    def get_success_url(self) -> str:
        return reverse_lazy('index')

def logout_user(r):
    logout(r)
    return redirect('login')