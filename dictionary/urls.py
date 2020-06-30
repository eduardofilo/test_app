from django.urls import path

from . import views

urlpatterns = [
    path('', views.WordListView.as_view(), name='word_list'),
    path('create', views.WordCreateView.as_view(), name='word_create'),
    path('edit/<int:pk>', views.WordDetailView.as_view(), name='word_edit'),
    path('delete/<int:pk>', views.WordDeleteView.as_view(), name='word_delete')
]
