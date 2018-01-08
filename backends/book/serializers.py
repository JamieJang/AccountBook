from rest_framework import serializers

from django.utils import timezone

from . import models


class DateTimeFieldWihTZ(serializers.DateTimeField):
    '''Class to make output of a DateTime Field timezone aware
    '''

    def to_representation(self, value):
        value = timezone.localtime(value)
        return super(DateTimeFieldWihTZ, self).to_representation(value)

class ListAccountBookSerializer(serializers.ModelSerializer):
    date = DateTimeFieldWihTZ(format='%Y-%m-%d %H:%M',
                              input_formats=['%Y-%m-%d %H:%M'])
    class Meta:
        model = models.Book
        fields = ("id","book_type","payment_type","category","amount","detail","memo","date")
