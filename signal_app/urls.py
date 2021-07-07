from django.urls import path

from .views import index, show_tree, save_data

urlpatterns = [
    path('', index),
    path('show-tree/', show_tree),
    path('add-data/', save_data),
]
