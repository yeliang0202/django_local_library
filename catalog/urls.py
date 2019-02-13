from django.urls import path
from catalog import views
from django.views.generic import RedirectView

urlpatterns = [
 #path('', RedirectView.as_view(url='../admin/')),
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),

]