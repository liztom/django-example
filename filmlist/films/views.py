from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from films.models import *
from films.serializers import *


@api_view(['GET', 'POST'])
def film_list(request, format=None):
    """
    List all films, or create a new film.
    """
    if request.method == 'GET':
        films = Film.objects.all()
        serializedFilm = FilmSerializer(films, many=True)
        return Response(serializedFilm.data)

    elif request.method == 'POST':
        serializedFilm = FilmWriteSerializer(data=request.data)
        if serializedFilm.is_valid():
            serializedFilm.save()
            return Response(serializedFilm.data, status=status.HTTP_201_CREATED)
        return Response(serializedFilm.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def film_detail(request, pk, format=None):
    """
    Retrieve, update or delete a film instance.
    """
    try:
        film = Film.objects.get(pk=pk) #Django ORM method, retrieves specific film
    except Film.DoesNotExist: 
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializedFilm = FilmSerializer(instance=film) # serialize film to JSON
        return Response(serializedFilm.data) # return serialized film

    elif request.method == 'PUT':
        serializedFilm = FilmSerializer(film, data=request.data) # takes data in and serializes to python
        if serializedFilm.is_valid():
            serializedFilm.save() # save the updated film
            return Response(serializedFilm.data)
        return Response(serializedFilm.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        film.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET', 'POST'])
# def theater_list(request, format=None):
#     """
#     List all theaters, or create a new theater.
#     """
#     if request.method == 'GET':
#         theaters = Theater.objects.all()
#         serializer = TheaterSerializer(theaters, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = TheaterSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# def theater_detail(request, pk, format=None):
#     """
#     Retrieve, update or delete a theater instance.
#     """
#     try:
#         theater = Theater.objects.get(pk=pk)
#     except Theater.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = TheaterSerializer(theater)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = TheaterSerializer(theater, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         theater.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET', 'POST'])
# def genre_list(request, format=None):
#     """
#     List all snippets, or create a new film.
#     """
#     if request.method == 'GET':
#         genres = Genre.objects.all()
#         serializer = GenreSerializer(genres, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = GenreSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# def genre_detail(request, pk, format=None):
#     """
#     Retrieve, update or delete a film instance.
#     """
#     try:
#         genre = Genre.objects.get(pk=pk)
#     except Genre.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = GenreSerializer(genre)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = GenreSerializer(film, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         genre.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
