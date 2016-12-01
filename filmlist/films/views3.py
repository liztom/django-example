from films.models import Film
from films.serializers import FilmSerializer
from rest_framework import generics
from rest_framework.response import Response

class FilmList(generics.ListCreateAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

class FilmDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer





yourawesomeapi.com/films?year_prod=2012