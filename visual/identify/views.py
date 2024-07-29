from django.http import HttpResponse

def index(request):
    return HttpResponse("The \"identify\" route lets you identify an animal species. Go to \"\\single\" to post a single image of an pet or \"\\bulk\" to post images by bulk.")

def single(request):
    return HttpResponse("Send an image here via a POST request to submit a singular image of a pet.")

def bulk(request):
    return HttpResponse("Send a list or array of images here via a POST request to submit bulk images of pets.")
