from django.urls import path

from . import views

urlpatterns = [
    path('', views.WordListView.as_view(), name='word_list'),
    path('create', views.WordCreateView.as_view(), name='word_create'),
    path('update/<int:pk>', views.WordUpdateView.as_view(), name='word_update'),
    path('delete/<int:pk>', views.WordDeleteView.as_view(), name='word_delete')
]
