from rest_framework import serializers

class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    Name = serializers.CharField(max_length=100)
    Company = serializers.CharField(max_length=100)
    Cost = serializers.CharField(max_length=100)
    Color = serializers.CharField(max_length=50)
    Top_Speed = serializers.CharField(max_length=100)