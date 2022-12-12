from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers

from .models import Place
import json

def placeRequest(request):
    # Initialize params
    query = request.GET.get('query', '강남구')
    page_num = int(request.GET.get('page', 1))
    page_size = int(request.GET.get('size', 10))

    total_count = Place.objects.count()
    isLastPage = True if ((total_count // page_size) + 1) == page_num else False

    # Meta : Meta data
    meta = {
        "total_count": total_count, 
        "count": page_size,
        "is_end": isLastPage
    }

    # Document : Main Content
    start_num = (page_num - 1) * page_size
    place_object = Place.objects.all()[start_num : start_num + page_size]
    document = list(place_object.values())

    # HttpResponse : creating a dictionary
    #response = {"meta": meta, "document" : document}
    response_data = {}
    response_data['meta'] = meta
    response_data['document'] = document

    # return HttpResponse(json.dumps(response_data),
    #                    content_type="application/json")
    return JsonResponse(response_data, safe=False, json_dumps_params={'ensure_ascii': False}, status=200)
#    return HttpResponse(document, content_type="text/json-comment-filtered")
#    return HttpResponse("Hello, world. You're at the Matjongwon v1 index page. " + 
#                        query + " " + str(page_num) + " " + str(page_size) + '\n' + 
#                        json.dumps(meta))
