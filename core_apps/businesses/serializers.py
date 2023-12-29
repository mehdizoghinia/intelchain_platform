from rest_framework import serializers
from .models import Business,Product  # Import the Business model

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["pkid",'id', 'name']

class BusinessSerializer(serializers.ModelSerializer):
    owner = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Business
        fields = ['id','pkid', 'business_name','owner', 'projects', 'website', 'location', 'phone']

    def get_owner(self, obj):
        first_name = obj.user.first_name.title()
        last_name = obj.user.last_name.title()
        return f"{first_name}  {last_name}"
    
    def update(self, instance, validated_data):
        # Remove 'projects' from validated_data to handle it separately
        projects = validated_data.pop('projects', None)

        # Update other fields as usual
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        # Save the instance with updated fields
        instance.save()

        # Handle 'projects' field update if provided
        if projects is not None:
            instance.projects.set(projects)  # Use set() method for many-to-many

        return instance
