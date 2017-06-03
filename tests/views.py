from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from tests.models import Test
from tests.serializers import TestSerializer


@csrf_exempt
def tests_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Test.objects.all()
        serializer = TestSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TestSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)



@csrf_exempt
def test_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        test = Test.objects.get(pk=pk)
    except Test.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TestSerializer(test)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TestSerializer(test, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        test.delete()
        return HttpResponse(status=204)

