from django.urls import path
from . import views

app_name = 'snippets'

urlpatterns = [
    path('snippets', views.snippet_list, name='snippets_detail'),
    path('snippets/<int:pk>', views.snippet_detail, name='snippets_detail')

]