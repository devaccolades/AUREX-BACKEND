from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from projects import serializers as projects_serializer
from projects import models as projects_models

# Create your views here.

class ProjectsView(APIView):
    serializer_class = projects_serializer.ProjectsSerializer

    def get(self, request, slug=None):
        try:
            if slug:
                project = projects_models.Projects.objects.filter(
                    slug=slug,
                    is_deleted=False
                ).first()

                if not project:
                    return Response(
                        {"error": "Project not found"},
                        status=status.HTTP_404_NOT_FOUND
                    )

                serializer = self.serializer_class(
                    project,
                    context={"request": request}
                )
                return Response(serializer.data)

            projects = projects_models.Projects.objects.filter(is_deleted=False)

            serializer = self.serializer_class(
                projects,
                many=True,
                context={"request": request}
            )
            return Response(serializer.data)

        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        
class ProjectImagesView(APIView):
    serializer_class = projects_serializer.ProjectImagesSerializer

    def get(self, request, slug=None):
        try:
            if slug:
                project = projects_models.Projects.objects.filter(slug=slug, is_deleted=False).first()
                if not project:
                    return Response({"error": "Project not found"}, status=status.HTTP_404_NOT_FOUND)

                data = projects_models.ProjectImages.objects.filter(project=project, is_deleted=False)
            else:
                data = projects_models.ProjectImages.objects.filter(is_deleted=False)

            serializer = self.serializer_class(data, many=True, context={"request": request})
            return Response(serializer.data)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class AmenitiesView(APIView):
    serializer_class = projects_serializer.AmenitiesSerializer

    def get(self, request, slug=None):
        try:
            if slug:
                project = projects_models.Projects.objects.filter(slug=slug, is_deleted=False).first()
                if not project:
                    return Response({"error": "Project not found"}, status=status.HTTP_404_NOT_FOUND)

                data = projects_models.Amenities.objects.filter(project=project, is_deleted=False)
            else:
                data = projects_models.Amenities.objects.filter(is_deleted=False)

            serializer = self.serializer_class(data, many=True, context={"request": request})
            return Response(serializer.data)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class CommonFacilitiesView(APIView):
    serializer_class = projects_serializer.CommonFacilitiesSerializer

    def get(self, request, slug=None):
        try:
            if slug:
                project = projects_models.Projects.objects.filter(slug=slug, is_deleted=False).first()
                if not project:
                    return Response({"error": "Project not found"}, status=status.HTTP_404_NOT_FOUND)

                data = projects_models.CommonFacilities.objects.filter(project=project, is_deleted=False)
            else:
                data = projects_models.CommonFacilities.objects.filter(is_deleted=False)

            serializer = self.serializer_class(data, many=True, context={"request": request})
            return Response(serializer.data)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class FloorPlansView(APIView):
    serializer_class = projects_serializer.FloorPlansSerializer

    def get(self, request, slug=None):
        try:
            if slug:
                project = projects_models.Projects.objects.filter(slug=slug, is_deleted=False).first()
                if not project:
                    return Response({"error": "Project not found"}, status=status.HTTP_404_NOT_FOUND)

                data = projects_models.FloorPlans.objects.filter(project=project, is_deleted=False)
            else:
                data = projects_models.FloorPlans.objects.filter(is_deleted=False)

            serializer = self.serializer_class(data, many=True, context={"request": request})
            return Response(serializer.data)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class SpecificationsView(APIView):
    serializer_class = projects_serializer.SpecificationsSerializer

    def get(self, request, slug=None):
        try:
            if slug:
                project = projects_models.Projects.objects.filter(slug=slug, is_deleted=False).first()
                if not project:
                    return Response({"error": "Project not found"}, status=status.HTTP_404_NOT_FOUND)

                data = projects_models.Specifications.objects.filter(project=project, is_deleted=False)
            else:
                data = projects_models.Specifications.objects.filter(is_deleted=False)

            serializer = self.serializer_class(data, many=True, context={"request": request})
            return Response(serializer.data)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class LocationAdvantagesView(APIView):
    serializer_class = projects_serializer.LocationAdvantagesSerializer

    def get(self, request, slug=None):
        try:
            if slug:
                project = projects_models.Projects.objects.filter(slug=slug, is_deleted=False).first()
                if not project:
                    return Response({"error": "Project not found"}, status=status.HTTP_404_NOT_FOUND)

                data = projects_models.LocationAdvantages.objects.filter(project=project, is_deleted=False)
            else:
                data = projects_models.LocationAdvantages.objects.filter(is_deleted=False)

            serializer = self.serializer_class(data, many=True, context={"request": request})
            return Response(serializer.data)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class YoutubeVideosView(APIView):
    serializer_class = projects_serializer.YoutubeVideosSerializer

    def get(self, request, slug=None):
        try:
            if slug:
                project = projects_models.Projects.objects.filter(slug=slug, is_deleted=False).first()
                if not project:
                    return Response({"error": "Project not found"}, status=status.HTTP_404_NOT_FOUND)

                data = projects_models.YoutubeVideos.objects.filter(project=project, is_deleted=False)
            else:
                data = projects_models.YoutubeVideos.objects.filter(is_deleted=False)

            serializer = self.serializer_class(data, many=True, context={"request": request})
            return Response(serializer.data)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ProjectUpdatesView(APIView):
    serializer_class = projects_serializer.ProjectUpdatesSerializer

    def get(self, request, slug=None):
        try:
            if slug:
                project = projects_models.Projects.objects.filter(slug=slug, is_deleted=False).first()
                if not project:
                    return Response({"error": "Project not found"}, status=status.HTTP_404_NOT_FOUND)

                data = projects_models.ProjectUpdates.objects.filter(project=project, is_deleted=False)
            else:
                data = projects_models.ProjectUpdates.objects.filter(is_deleted=False)

            serializer = self.serializer_class(data, many=True, context={"request": request})
            return Response(serializer.data)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
