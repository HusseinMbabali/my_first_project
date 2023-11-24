from rest_framework import serializers

from .models import *

class EstateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estate
        fields = ("name", "location", "description")

class LandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Land
        fields = ("estate", "size", "price")

class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = ("type", "bedroom", "toilet", "price")

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ("customer_name", "contact", "land", "house")

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ("payment_date", "customer", "amt_pd", "rec_by")

class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Title
        fields = ("county", "sub_county", "block", "plot", "title_photo")