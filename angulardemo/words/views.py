from django.http import HttpResponse, JsonResponse
from words.models import Word
from words.serializers import WordSerializer
from django.core import serializers


# Create your views here.
def index(request) -> HttpResponse:
    return HttpResponse("This is the words view.")

def allWords(request) -> JsonResponse:

    words = Word.objects.all()
    serializer = WordSerializer(words, many = True)
    return JsonResponse(serializer.data, safe = False)

def singleWord(request, key) -> HttpResponse:

    try:
        word = Word.objects.get(pk = key)
    except Word.DoesNotExist:
        return HttpResponse("You fucked up!")

    serializer = WordSerializer(word)
    return JsonResponse(serializer.data)

    #return JsonResponse({'jello' : 'poop'})
    # elif request.method == 'POST':
    #     data = JSONParser().parse(request)
    #     serializer = SnippetSerializer(data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse(serializer.data, status=201)
    #     return JsonResponse(serializer.errors, status=400)
