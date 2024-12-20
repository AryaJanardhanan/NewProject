from django.urls import path
from .import views as v

urlpatterns = [
    path('', v.home, name='home'),
    path('about/', v.about, name='abt'),
    path('base/', v.base, name='base'),
    path('contact/', v.contact, name='contact'),
    path('sample/', v.sample, name='sample'),
    path('student/', v.student, name='student'),
    path('register/', v.register, name='register'),
    path('uslogin/', v.uslogin, name='uslogin'),
    path('logout/', v.logt, name='logout'),
    path('display/', v.disply, name='display'),
    path('item/<int:pk>/delete/', v.delt, name='delete' ),
    path('item/<int:pk>/edit/' ,v.editt, name='edit'),
    path('index/', v.index, name='index'),
]