from rest_framework import serializers
from notes import models as notes_models


class NotesSerialiser(serializers.ModelSerializer):

    class Meta:
        model = notes_models.Notes
        fields = '__all__'