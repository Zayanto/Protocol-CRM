from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin  # new
from .models import Book


class BookListView(LoginRequiredMixin, ListView):  # new
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/book_list.html'
    login_url = 'account_login'  # new


class BookDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):  # new
    model = Book
    context_object_name = 'book'
    template_name = 'books/book_detail.html'
    login_url = 'account_login'  # new
    permission_required = 'books.special_status'  # new