from rest_framework import serializers
from .models import Users, Payer

class WelcomeMessageSerializer(serializers.Serializer):
    message = serializers.CharField()

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'username', 'total_points']

class PayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payer
        fields = ['id', 'payer_name', 'points_given', 'paid_to', 'paid_at']

class SpendPointsSerializer(serializers.Serializer):
    user_id = serializers.IntegerField() 
    points_to_spend = serializers.IntegerField(min_value=1)

class UsersBalanceSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    