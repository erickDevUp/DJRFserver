from rest_framework import serializers
from.models import Entry

class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = '__all__'  # Esto incluirá todos los campos del modelo en la serialización/deserialización