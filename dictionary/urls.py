from django.urls import path

from . import views

urlpatterns = [
    path('', views.WordListView.as_view(), name='word_list'),
    path('<int:pk>/edit', views.WordDetailView.as_view(), name='word_detail'),
    path('<int:pk>/delete', views.WordDeleteView.as_view(), name='word_delete')
]
