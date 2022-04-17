from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from api.serializers import WorkExperienceSerializer, EducationSerializer, VacancySerializer, SummarySerializer
from app.models import Vacancy, Summary
from rest_framework.generics import get_object_or_404
import json
# Create your views here.


class LogoutView(APIView):
    permission_classes = []

    def post(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            user.auth_token.delete()
        return Response({'status': 'ok'})


class WorkExperienceCreateView(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = self.request.user
        serializer = WorkExperienceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EducationCreateView(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = self.request.user
        serializer = EducationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VacancyUpdateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        vacancy = get_object_or_404(Vacancy, pk=self.kwargs.get('pk'))
        serializer = VacancySerializer(vacancy)
        return Response(serializer.data)

    def patch(self, request, *args, **kwargs):
        vacancy = get_object_or_404(Vacancy, pk=self.kwargs.get('pk'))
        data = json.loads(self.request.body)
        serializer = VacancySerializer(vacancy, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class SummaryUpdateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        summary = get_object_or_404(Summary, pk=self.kwargs.get('pk'))
        serializer = SummarySerializer(summary)
        return Response(serializer.data)

    def patch(self, request, *args, **kwargs):
        summary = get_object_or_404(Summary, pk=self.kwargs.get('pk'))
        data = json.loads(self.request.body)
        serializer = SummarySerializer(summary, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
