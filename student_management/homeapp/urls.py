from django.urls import path 
from . import views

urlpatterns=[
    path('',views.index_page,name='home'),
    path('std_list/',views.std_form,name='form'),
    path('del-std/<int:id>',views.delete_std,name='del'),
    path('update-std/<int:id>',views.update_std,name='update'),
    path('update-done/<int:id>',views.update_done,name='update_done'),
]