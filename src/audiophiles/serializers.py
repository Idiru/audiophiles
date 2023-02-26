from rest_framework import serializers



class ecommerceSerializer(serializers.ModelSerializer):

    class Meta:
        model = ecommerce
        fields = '__all__'