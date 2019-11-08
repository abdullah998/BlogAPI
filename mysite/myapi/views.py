from rest_framework import viewsets, mixins, status
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from core.models import BlogPost
from django.http import JsonResponse


class blog_post_set(viewsets.GenericViewSet,mixins.ListModelMixin,
                  mixins.CreateModelMixin):
    """Used to get all blogs or enter a newone"""

    serializer_class = serializers.BlogPostSerializer
    queryset = BlogPost.objects.all()

    def get_queryset(self):
        #return self.queryset.filter(title__contains='abc',post__contains='e')
        return self.queryset.filter().order_by('created_on')


class api(APIView):
    """used to fetch only one blog by it's id or edit a blog"""
    serializer_class = serializers.EditPostSerializer

    def get(self, request, format=None):
        b = BlogPost.objects.get(id=request.query_params['id'])
        return Response({'id':b.id,'post':b.post,'title':b.title,'created_on':b.created_on,'edited_on':b.edited_on})

    def post(self,request):
        serializer=self.serializer_class(data=request.data)
        if(serializer.is_valid()):
            b = BlogPost.objects.get(id=serializer.validated_data.get('id'))
            b.post = serializer.validated_data.get('post')
            b.title = serializer.validated_data.get('title')
            b.save()
            return Response('abcd')
        else:
            return Response(serializer.errors)


class api2(APIView):
    """Used to fetch only by different keywords for title and post"""
    serializer_class = serializers.EditPostSerializer

    queryset = BlogPost.objects.all()

    def get(self, request, format=None):
        data = list(self.queryset.filter(title__icontains=request.query_params['title'], post__icontains=request.query_params['post']).values())
        return JsonResponse(data, safe=False)

class api3(APIView):
    """used to search a blog by single search query for both title and post"""
    serializer_class = serializers.EditPostSerializer

    queryset = BlogPost.objects.all()

    def get(self, request, format=None):
        data = list(self.queryset.filter(title__contains=request.query_params['search'], post__contains=request.query_params['search']).values())
        return JsonResponse(data, safe=False)