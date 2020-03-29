from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import User, ActivityPeriod
from api.serializers import PostSerializer

# Create your views here.

@api_view(['GET'])
def user_collection(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = PostSerializer(users, many=True)
        for odict in serializer.data:
            #inserting activity_period in ordereddict
            activity_period = ActivityPeriod.objects.filter(user=odict['id']).values('start_time','end_time')
            odict['activity_periods'] = activity_period

        response_dict = {"ok": True,
                        "members": serializer.data,
                        }
        return Response(response_dict)


@api_view(['GET'])
def user_element(request, pk):
    try:
        users = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PostSerializer(users)
        #inserting activity_period in ordereddict
        activity_period = ActivityPeriod.objects.filter(user=pk).values('start_time','end_time')
        response_dict = dict(serializer.data)
        response_dict['activity_periods'] = list(activity_period)
        return Response(response_dict)
