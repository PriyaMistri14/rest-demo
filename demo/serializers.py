from rest_framework import serializers
from .models import Demo
from django.contrib.auth.models import User

# ..........................simple serializer............................
class DemoSeriallizer(serializers.Serializer):
     title= serializers.CharField(max_length=50, allow_blank=True)
     owner = serializers.ReadOnlyField(source='owner.username' , read_only=True)


     def create(self,validated_data):
         return Demo.objects.create(**validated_data)



     def update(self, instance, validated_data):
         instance.title= validated_data.get("title",instance.title)

         instance.save()
         return instance


class UserSerializer(serializers.ModelSerializer):
    # title_user = serializers.PrimaryKeyRelatedField(many=True, queryset= Demo.objects.all())
    class Meta:
        model=Demo
        fields=['title']




# ...............................model serializer.........................

# class DemoModelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Demo
#         fields=['title']







