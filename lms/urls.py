from django.urls import path
from . import views 

app_name = 'lms'

urlpatterns = [
    path('' , views.lms , name= 'lms' ) ,
    path('books/' , views.books , name= 'books' ) ,
    path('update/<int:id>' , views.update , name= 'update' ) ,
    path('delete/<int:id>' , views.delete , name= 'delete' ) ,
]
