from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Authors,Genres,Books
from .serializers import AuthorSerializer,GenresSerializer,BooksSerializer
from django.db.models import Q

@api_view(['GET','POST'])
def get_authors(req:Request):
    
    if req.method=='GET':
       authors = Authors.objects.all()
       data = AuthorSerializer(authors,many=True)
       return Response(data.data)
    if req.method=='POST':
        body = req.data
        serializer = AuthorSerializer(data=body)
        if not serializer.is_valid():
           return Response({"details":serializer.errors},status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
   

@api_view(['GET','PUT','DELETE'])
def get_update_authors(req:Request,id):
    try:
        pk = int(id)
    except ValueError:
        return Response({'detail': 'ID should be an integer.'}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        author = Authors.objects.get(pk=pk)
        # getting author by id 
        if req.method == 'GET':
            data = AuthorSerializer(author)
            return Response(data.data, status=status.HTTP_200_OK)

        # update name of author 
        if req.method == 'PUT':
            body = req.data.get('name')
            if body is None:
                return Response('Name field is required', status.HTTP_400_BAD_REQUEST)
            serializer = AuthorSerializer(author,data=req.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        #  deleting author    
        if req.method=='DELETE':
            author.delete()
            return Response({"msg":'Author deleted'}, status.HTTP_200_OK)            
            
             
    except Authors.DoesNotExist:
        return Response({'detail': 'Author not found'}, status=status.HTTP_404_NOT_FOUND)        


# genres functions 
@api_view(['GET','POST'])
def get_genres(req:Request):
    
    if req.method=='GET':
       authors = Genres.objects.all()
       data = GenresSerializer(authors,many=True)
       return Response(data.data)
    if req.method=='POST':
        body = req.data
        serializer = GenresSerializer(data=body)
        if not serializer.is_valid():
           return Response({"details":serializer.errors},status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
   

@api_view(['GET','PUT','DELETE'])
def get_update_genres(req:Request,id):
    try:
        pk = int(id)
    except ValueError:
        return Response({'detail': 'ID should be an integer.'}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        author = Genres.objects.get(pk=pk)
        # getting author by id 
        if req.method == 'GET':
            data = GenresSerializer(author)
            return Response(data.data, status=status.HTTP_200_OK)

        # update name of author 
        if req.method == 'PUT':
            body = req.data.get('name')
            if body is None:
                return Response('Name field is required', status.HTTP_400_BAD_REQUEST)
            serializer = GenresSerializer(author,data=req.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        #  deleting author    
        if req.method=='DELETE':
            author.delete()
            return Response({"msg":'Genres deleted'}, status.HTTP_200_OK)            
            
             
    except Genres.DoesNotExist:
        return Response({'detail': 'Genre not found'}, status=status.HTTP_404_NOT_FOUND)        
    
  
   
# books functions 
@api_view(['GET','POST'])
def get_books(req:Request):
    
    if req.method=='GET':
        title = req.query_params.get('title',None)
        genre_id = req.query_params.get('genre_id',None)
        author_id = req.query_params.get('author_id',None)
        books = Books.objects.all()
        filters = Q()
        # Genres.objects.values('id')
        # category_ids = Genres.objects.values_list('id', flat=True)
        # products = Books.objects.filter(id__in=category_ids).all()
        # res = BooksSerializer(products,many=True)
        # print(res)
        if title is not None:
            filters &= Q(title__icontains=title)
            
        if genre_id is not None:
            filters &= Q(genre_id=genre_id)
              
        if author_id is not None:
            filters &= Q(author_id=author_id)
            
        books = books.filter(filters).all()     
        data = BooksSerializer(books,many=True)
        return Response(data.data,status.HTTP_200_OK)
    
    if req.method=='POST':
        body = req.data
        serializer = BooksSerializer(data=body)
        if not serializer.is_valid():
           return Response({"details":serializer.errors},status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
   

@api_view(['GET','PUT','DELETE'])
def get_update_books(req:Request,id):
    try:
        pk = int(id)
    except ValueError:
        return Response({'detail': 'ID should be an integer.'}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        book = Books.objects.get(pk=pk)
        # getting book by id 
        if req.method == 'GET':
            data = BooksSerializer(book)
            return Response(data.data, status=status.HTTP_200_OK)

        # update name of book 
        if req.method == 'PUT':
            body = req.data.get('title')
            if body is None:
                return Response('title field is required', status.HTTP_400_BAD_REQUEST)
            serializer = BooksSerializer(book,data=req.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        #  deleting book    
        if req.method=='DELETE':
            book.delete()
            return Response({"msg":'book deleted'}, status.HTTP_200_OK)            
            
             
    except Books.DoesNotExist:
        return Response({'detail': 'book not found'}, status=status.HTTP_404_NOT_FOUND)         
    
        
            
    