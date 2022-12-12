from django.http import JsonResponse

def say_hello(request):
    resp = {
        'key': 'name',
        'val': 'Anuj',
    }
    return JsonResponse(resp)

def say_hello_dop(request):
    resp = {
        'key': 'name',
        'val': 'Anuj Doppelganger',
    }
    return JsonResponse(resp)
