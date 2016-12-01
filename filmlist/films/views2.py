from films.models import Film
from films.serializers import FilmSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class FilmList(APIView):
    """
    List all films, or create a new film.
    """
    def get(self, request, format=None):
        films = Film.objects.all()
        serialized_films = FilmSerializer(films, many=True)
        return Response(serialized_films.data)

    def post(self, request, format=None):
        film = FilmSerializer(data=request.data)
        if film.is_valid():
            film.save()
            return Response(film.data, status=status.HTTP_201_CREATED)
        return Response(film.errors, status=status.HTTP_400_BAD_REQUEST)


class FilmDetail(APIView):
    """
    Retrieve, update or delete a film instance.
    """
    def get_object(self, pk):
        try:
            return Film.objects.get(pk=pk)
        except Film.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        film = self.get_object(pk)
        serialized_film = FilmSerializer(film)
        return Response(serialized_film.data)

    def put(self, request, pk, format=None):
        film = self.get_object(pk)
        serialized_film = FilmSerializer(film, data=request.data)
        if serialized_film.is_valid():
            serialized_film.save()
            return Response(serialized_film.data)
        return Response(serialized_film.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        film = self.get_object(pk)
        film.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)