from django.urls import path

from .views import index, show_tree, save_data, delete_entity, edit_entity, export_page

urlpatterns = [
    path('', index),
    path('show-tree/', show_tree),
    path('add-data/', save_data),
    path('delete-entity/', delete_entity),
    path('edit-entity/', edit_entity),
    path('export-page/', export_page),
]
