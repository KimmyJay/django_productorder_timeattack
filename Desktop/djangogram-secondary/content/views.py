from django.shortcuts import render
from rest_framework.views import APIView
from content.models import Feed

# Create your views here.

class Main(APIView):
    def get(self, request):
        feed_list = Feed.objects.all # select * from content_feed;
        return render(request, 'main.html', context=dict(feed_list=feed_list))