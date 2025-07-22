from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer

# Health check endpoint
class HealthView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({"status": "ok"})

# Book CRUD endpoint via ViewSet
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
