from rest_framework import serializers
from .models import Demo

# ..........................simple serializer............................
class DemoSeriallizer(serializers.Serializer):
     title= serializers.CharField(max_length=50, allow_blank=True)


     def create(self,validated_data):
         return Demo.objects.create(**validated_data)



     def update(self, instance, validated_data):
         instance.title= validated_data.get("title",instance.title)

         instance.save()
         return instance



# ...............................model serializer.........................

# class DemoModelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Demo
#         fields=['title']







