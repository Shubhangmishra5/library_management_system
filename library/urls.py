# library/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='user_login'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('book_categories/', views.book_category, name='book_category'),
    path('add_membership/', views.add_membership, name='add_membership'),
    path('update_membership/', views.update_membership, name='update_membership'),
    path('add_book/', views.add_book, name='add_book'),
    path('update_book/', views.update_book, name='update_book'),
    path('add_user/', views.add_user, name='add_user'),
    path('update_user/', views.update_user, name='update_user'),
    path('active_issues/', views.active_issues, name='active_issues'),
    path('master_list_membership/', views.master_list_membership, name='master_list_membership'),
    path('master_list_movies/', views.master_list_movies, name='master_list_movies'),
    path('overdue_returns/', views.overdue_returns, name='overdue_returns'),
    path('pending_issues/', views.pending_issues, name='pending_issues'),
    path('check_availability/', views.check_book_availability, name='check_availability'),
    path('issue_book/', views.issue_book, name='issue_book'),
    path('return_book/', views.return_book, name='return_book'),
    path('fine_payment/', views.fine_payment, name='fine_payment'),
]
