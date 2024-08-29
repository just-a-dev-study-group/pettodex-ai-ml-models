from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from library.PIC import classify
import json

@csrf_exempt
def index(request):
    if request.method == "GET":
        return HttpResponse("The \"identify\" route lets you identify an animal species. Go to \"\\single\" to post a single image of an pet or \"\\bulk\" to post images by bulk.")
    elif request.method == "POST":
        return HttpResponse("You have sent a POST request")

@csrf_exempt
def single(request):
    if request.method == "GET":
        return HttpResponse("Send an image here via a POST request to submit a singular image of a pet.")
    elif request.method == "POST":
        # Remove escape characters from payload
        # url = re.sub(r'\\', '', request.read())
        url = json.loads(request.body.decode("utf-8"))
        url = url.get("url")

        # Save input into variable
        out = classify(url)

        return HttpResponse(out)

@csrf_exempt
def bulk(request):
    if request.method == "GET":
        return HttpResponse("Send a list or array of images here via a POST request to submit bulk images of pets.")
    elif request.method == "POST":
        return HttpResponse("You have sent a POST request")
