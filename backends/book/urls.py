from django.urls import path, re_path, include

from . import views

app_name = "book"

urlpatterns = [
    re_path(r'^$',views.Books.as_view(),name="mainpage"),
    re_path(r'^(?P<book_id>\d+)/$', views.BookDetail.as_view(), name="book_detail"),
    path('<int:year>/<int:month>/',views.BookListByMonth.as_view(),name="book_by_month"),
    path('<int:year>/<int:month>/<int:day>/',views.BookListByDate.as_view(),name="book_by_date"),
    path('category/<str:category>/',views.BookListByCategory.as_view(),name="book_by_category"),
    path('category/<str:category>/<int:year>/<int:month>',views.BookListByCategoryMonthly.as_view(), name="book_by_category_monthly"),
]
