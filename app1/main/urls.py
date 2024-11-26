from django.urls import path
from .views import contact_list, delete_contact, toggle_favorite 

urlpatterns = [
    path('', contact_list, name='contact_list'),
    path('delete_contact/', delete_contact, name='delete_contact'),
    path('toggle_favorite/', toggle_favorite, name='toggle_favorite'),
]
