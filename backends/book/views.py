from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.utils import timezone

from . import models
from . import serializers

class Books(APIView):
    """
        Show Book List monthly by default
    """

    def get(self, request, format=None):
        year = timezone.localtime().year
        month = timezone.localtime().month

        books = models.Book.objects.filter(date__year=year, date__month=month)
        
        serializer = serializers.ListAccountBookSerializer(books, many=True)

        return Response(data=serializer.data)

class BookDetail(APIView):
    def get(self, request, book_id, format=None):
        book = models.Book.objects.get(id=book_id)

        serializer = serializers.ListAccountBookSerializer(book)

        return Response(data=serializer.data)

    def put(self,request,book_id, format=None):
        book = models.Book.objects.get(id=book_id)
        serializer = serializers.ListAccountBookSerializer(book,data=request.data,partial=True)
        if serializer.is_valid():
            return Response(data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,book_id, format=None):
        book = models.Book.objects.get(id=book_id)
        book.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

class BookListByMonth(APIView):
    def get(self, request, year, month, format=None):
        books = models.Book.objects.filter(date__year=year, date__month=month)

        serializer = serializers.ListAccountBookSerializer(books,many=True)

        return Response(data=serializer.data)

class BookListByDate(APIView):
    def get(self, request, year, month, day, format=None):
        books = models.Book.objects.filter(date__year=year,date__month=month,date__day=day)
        serializer = serializers.ListAccountBookSerializer(books,many=True)

        return Response(data=serializer.data)


class BookListByCategory(APIView):
    def get(self,request,category,format=None):
        year = timezone.localtime().year
        month = timezone.localtime().month

        books = models.Book.objects.filter(category__name=category, date__year=year, date__month=month )

        serializer = serializers.ListAccountBookSerializer(books, many=True)

        return Response(data=serializer.data)

class BookListByCategoryMonthly(APIView):
    def get(self,request,category,year,month,format=None):
        books = models.Book.objects.filter(category__name=category,date__year=year,date__month=month)

        serializer = serializers.ListAccountBookSerializer(books,many=True)

        return Response(data=serializer.data)

