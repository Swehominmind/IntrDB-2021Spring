from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^publisher_list/', views.publisher_list),
    re_path(r'^add_publisher/', views.add_publisher),
    re_path(r'^drop_publisher/', views.drop_publisher),
    re_path(r'^edit_publisher/', views.edit_publisher),
    re_path(r'^book_list/', views.book_list),
    re_path(r'^add_book/', views.add_book),
    re_path(r'^drop_book/', views.drop_book),
    re_path(r'^edit_book/', views.edit_book),
    re_path(r'^author_list/', views.author_list),
    re_path(r'^add_author/', views.add_author),
    re_path(r'^drop_author/', views.drop_author),
    re_path(r'^edit_author/', views.edit_author),
    re_path(r'^$', views.publisher_list),
]
