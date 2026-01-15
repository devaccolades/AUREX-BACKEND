from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import *
from .serializers import *

class SpaceGalleryView(APIView):
    serializer_class = SpaceGallerySerializer

    def get(self, request):
        try:
            data = SpaceGallery.objects.filter(is_deleted=False)
            serializer = self.serializer_class(data, many=True, context={"request": request})
            return Response(serializer.data)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class GalleryVideosView(APIView):
    serializer_class = GalleryVideosSerializer

    def get(self, request):
        try:
            data = GalleryVideos.objects.filter(is_deleted=False).first()
            serializer = self.serializer_class(data, context={"request": request})
            return Response(serializer.data)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class EventsView(APIView):
    serializer_class = EventsSerializer

    def get(self, request):
        try:
            data = Events.objects.filter(is_deleted=False)
            serializer = self.serializer_class(data, many=True, context={"request": request})
            return Response(serializer.data)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class EventGalleryView(APIView):
    serializer_class = EventGallerySerializer

    def get(self, request, event_id=None):
        try:
            queryset = EventGallery.objects.filter(is_deleted=False)

            if event_id:
                queryset = queryset.filter(event_id=event_id)

            serializer = self.serializer_class(queryset, many=True, context={"request": request})
            return Response(serializer.data)

        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
