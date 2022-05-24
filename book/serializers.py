from rest_framework import serializers
from book.models import *


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class BookGenreSerializer(serializers.ModelSerializer):
    genre = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = '__all__'

    def get_genre(self, obj):
        return obj.get_genre_display()


class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = '__all__'


class JournalTypeSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()

    class Meta:
        model = Journal
        fields = '__all__'

    def get_type(self, obj):
        return obj.get_type_display()


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
