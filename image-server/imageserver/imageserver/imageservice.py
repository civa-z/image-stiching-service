from django.http import HttpResponse
 
def on_request(request):
    return HttpResponse("Hello world ! ")