from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import JobSerializer
from .models import Result


class JobsView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        return (request.data)

    def post(self, request):
        return (request.data)
        serializer = JobSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(worker=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
