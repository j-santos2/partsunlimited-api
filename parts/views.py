from collections import Counter
from itertools import chain
import string

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import status
from rest_framework.viewsets import ModelViewSet

from drf_yasg.utils import swagger_auto_schema

from parts.models import Part
from parts.serializers import PartSerializer, TopWordsSerializer


def words_from_text(text):
    "Strips puntuation from text and returns lower case words."
    processed_text = text.translate(str.maketrans("", "", string.punctuation))
    return processed_text.lower().split()


class PartViewSet(ModelViewSet):
    serializer_class = PartSerializer
    queryset = Part.objects.all()

    @swagger_auto_schema(
        method="get",
        operation_description="Returns 5 most common words in our part descriptions.",
        responses={status.HTTP_200_OK: TopWordsSerializer},
    )
    @action(detail=False)
    def top_words(self, request):
        parts = Part.objects.all()
        descriptions = map(words_from_text, [p.description for p in parts])
        words_count = Counter(chain.from_iterable(descriptions))
        words_by_count = sorted(words_count, key=words_count.get, reverse=True)[:5]

        serializer = TopWordsSerializer({"words": words_by_count})

        return Response(serializer.data)
