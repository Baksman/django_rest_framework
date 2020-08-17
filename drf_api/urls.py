
from django.urls import path,include
from .views import ItemsView,ItemsCreateView

urlpatterns = [
    path('', ItemsView.as_view(), name = "blog-home"),
    path('create/', ItemsCreateView.as_view(), name = "create-home"),
    
]