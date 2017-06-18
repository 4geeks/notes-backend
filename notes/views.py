from django.shortcuts import render
from rest_framework import viewsets, views, status, permissions
from notes import models as notes_models
from notes import serializers as notes_serializers
from rest_framework.response import Response


class NotesViewSet(viewsets.ModelViewSet):

    queryset = notes_models.Notes.objects.all()
    serializer_class = notes_serializers.NotesSerialiser
