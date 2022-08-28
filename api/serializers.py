from rest_framework import serializers

class PredictSerializer(serializers.Serializer):
    result = serializers.CharField()
    # result = serializers.CharField()