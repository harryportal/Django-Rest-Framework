from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import APIView
from rest_framework.parsers import JSONParser
from .models import Snippet
from .serializers import SnippetSerializer
from rest_framework import status
from rest_framework.response import Response


class snippet_list(APIView):
    """
    List all code snippets or create a new objects
    """
    def get(self, request):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = JSONParser().parse(request) # converts the json input to a python dictionary
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class snippet_detail(APIView):
    def get_object(self,pk):
        try:
            snippet = Snippet.objects.get(pk=pk)
        except:
            return Response({'message':'Requested resource not found'}, status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        snippet = self.get_object(pk=pk)
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    def post(self, request, pk):
        snippet = self.get_object(pk=pk)
        data = JSONParser().parser(request)
        serializer = SnippetSerializer(snippet, data=data)
        if snippet.is_valid():
            snippet.save()
            return Response(snippet.data)
        else:
            return Response(snippet.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request, pk):
        snippet = self.get_object(pk=pk)
        snippet.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENTA)




