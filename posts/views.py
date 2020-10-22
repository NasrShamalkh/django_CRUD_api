from django.shortcuts import render
from django.http.response import JsonResponse

from rest_framework import status  # to handle status codes in Responses
from rest_framework.parsers import JSONParser  # parse the data coming from the request
from rest_framework.decorators import api_view

from posts.models import Post
from posts.serializers import PostSerializer

# Create your views here.
# our main functionality is in this views file

# Here we specify what HTTP request can be made to this view function
@api_view(['POST', 'GET', 'DELETE'])
def posts_list(request):

    if request.method == 'GET':
        # get all posts
        posts = Post.objects.all()

        title = request.GET.get('title', None)  # ( the title is passed as a parameter )
        # if title is in the parameters, then filter the posts with the title
        if title is not None:
            posts = posts.filter(title__icontains=title)
            # we serialize the posts and return a JsonResponse with the serialized data
        posts_serializer = PostSerializer(posts, many=True)
        return JsonResponse(posts_serializer.data, safe=False)


    elif request.method == 'POST':
        # we parse thr request to get the post data and then we serialize it
        post_data = JSONParser().parse(request)
        post_serializer = PostSerializer(data=post_data)

        # if the serializer is valid we save the serialized data (our post) and we return it with a status of 201
        if post_serializer.is_valid():
            post_serializer.save()
            return JsonResponse(post_serializer.data, status=status.HTTP_201_CREATED)
        # else we return the error raised from the serialization with a satus of 400
        return JsonResponse(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    elif request.method == 'DELETE':
        count = Post.objects.all().delete()
        return JsonResponse({'message': f"{count} posts were deleted successfully !"}, status=status.HTTP_204_NO_CONTENT)




@api_view(['PUT', 'GET', 'DELETE'])
def posts_details(request, pk):  # Here  pk corresponds to the id
    try:
        post = Post.objects.get(pk=pk)  # get the post with the matching id
    except Post.DoesNotExist:
        # if it does not exist, return the error message with 404
        return JsonResponse({'message': 'There is no post with such id'}, status=status.HTTP_404_NOT_FOUND)
    # return the post with the id if the method is get

    if request.method == 'GET':
        post_serializer = PostSerializer(post)
        return JsonResponse(post_serializer.data, status=status.HTTP_200_OK)
    # delete it if the method is DELETE

    elif request.method == 'DELETE':
        post.delete()
        return JsonResponse({'message': 'post deleted successfully !'}, status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        # we parse the data ( passed as a parameter ) and the we serialize it to the post with the matching id
        post_data = JSONParser().parse(request)
        post_serializer = PostSerializer(post, data=post_data)
        # if the serialization is valid, save it
        if post_serializer.is_valid():
            post_serializer.save()
            return JsonResponse(post_serializer.data)
        # else return a bad request status code
        return JsonResponse(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)





@api_view(['GET'])
def posts_list_published(request):
    posts = Post.objects.filter(published=True)

    if request.method == 'GET':
        posts_serializer = PostSerializer(posts, many=True)
        return JsonResponse(posts_serializer.data, safe=False)



