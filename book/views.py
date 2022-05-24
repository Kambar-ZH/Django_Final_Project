import http

from book.serializers import *
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
import logging
from rest_framework.permissions import AllowAny

logger = logging.getLogger(__name__)


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def list(self, request):
        if not request.user and request.user.is_staff:
            return Response(status=http.HTTPStatus.METHOD_NOT_ALLOWED)
        books = Book.objects.all()
        serializer = BookSerializer(instance=books, many=True)
        return Response(data=serializer.data)

    def retrieve(self, request, pk):
        if not request.user and request.user.is_staff:
            return Response(status=http.HTTPStatus.METHOD_NOT_ALLOWED)
        books = Book.objects.get(pk=pk)
        serializer = BookSerializer(instance=books)
        return Response(data=serializer.data)

    def destroy(self, request, pk):
        if not request.user and request.user.is_staff:
            return Response(status=http.HTTPStatus.METHOD_NOT_ALLOWED)
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=http.HTTPStatus.OK)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)


class JournalViewSet(viewsets.ModelViewSet):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer

    def list(self, request):
        if not request.user and request.user.is_staff:
            return Response(status=http.HTTPStatus.METHOD_NOT_ALLOWED)
        journals = Journal.objects.all()
        serializer = JournalSerializer(instance=journals, many=True)
        return Response(data=serializer.data)

    def retrieve(self, request, pk):
        if not request.user and request.user.is_staff:
            return Response(status=http.HTTPStatus.METHOD_NOT_ALLOWED)
        journals = Journal.objects.get(pk=pk)
        serializer = JournalSerializer(instance=journals)
        return Response(data=serializer.data)

    def destroy(self, request, pk):
        if not request.user and request.user.is_staff:
            return Response(status=http.HTTPStatus.METHOD_NOT_ALLOWED)
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=http.HTTPStatus.OK)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)


class RegisterViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [AllowAny]

    @action(methods='POST', detail=False)
    def register(self, request):
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=http.HTTPStatus.CREATED)
        return Response(data=serializer.errors, status=http.HTTPStatus.BAD_REQUEST)
