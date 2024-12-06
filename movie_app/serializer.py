from rest_framework import serializers
from.models import Movie, Director, Review

# MovieSerializer
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = 'id title description duration director '.split()

class MovieDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'.split()


# DirectorSerializer
class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'id name'.split()

class DirectorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'.split()


# ReviewSerializer
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text movie'.split()

class ReviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'.split()


