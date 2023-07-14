from  rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.Serializer):
    # id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    age = serializers.IntegerField()
    address = serializers.CharField(max_length=100)
    marks = serializers.IntegerField()
    is_active = serializers.BooleanField()


    def create(self, validated_data):
        print("In create method", validated_data)
        # Student(name=validated_data.get("name"))
        return Student.objects.create(**validated_data)  # obj created
        
       