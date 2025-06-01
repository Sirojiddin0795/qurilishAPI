from django.urls import path
from . import views

urlpatterns = [
    path('terms/', views.term_list),
    path('terms/<int:pk>/', views.term_detail),
    path('categories/', views.category_list),
    path('search/', views.term_search),
    path('topics/<int:category_id>/', views.topic_terms),
]
