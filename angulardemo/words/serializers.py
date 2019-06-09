from rest_framework import serializers
from words.models import PartOfSpeech, Word


class PartOfSpeechSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartOfSpeech
        fields = ["definition"]


class WordSerializer(serializers.ModelSerializer):

    partOfSpeech = PartOfSpeechSerializer(many = False, read_only = True)

    class Meta:
        model = Word
        fields = "__all__"
