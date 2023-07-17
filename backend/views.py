
# Create your views here.

import json

from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.utils import timezone
from backend.models import AutoCiGp1100X, AutoCiGs4227Xgs


# @require_http_methods(["GET"])
# def add_testcase(request):
#     response = {}
#     try:
#         case_headline = request.GET.get('headline')
#         testcase = Testcase(headline=case_headline, timestamp=timezone.now())
#         testcase.save()
#         response['respMsg'] = 'success'
#         response['respCode'] = '20000'
#     except Exception as e:
#         response['respMsg'] = str(e)
#         response['respCode'] = '999999'
#     return JsonResponse(response)


@require_http_methods(["GET"])
def show_testcases_gp1100x(request):
    response = {}
    try:
        testcases_gp1100x = AutoCiGp1100X.objects.filter()
        response['list'] = json.loads(serializers.serialize("json", testcases_gp1100x))
        response['respMsg'] = 'success'
        response['respCode'] = '20000'
    except Exception as e:
        response['respMsg'] = str(e)
        response['respCode'] = '999999'
    return JsonResponse(response)

@require_http_methods(["GET"])
def show_testcases_gs4227_xgs(request):
    response = {}
    try:
        testcases_gs4227_xgs = AutoCiGs4227Xgs.objects.filter()
        response['list'] = json.loads(serializers.serialize("json", testcases_gs4227_xgs))
        response['respMsg'] = 'success'
        response['respCode'] = '20000'
    except Exception as e:
        response['respMsg'] = str(e)
        response['respCode'] = '999999'
    return JsonResponse(response)
