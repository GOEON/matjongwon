import requests
from django.http import JsonResponse
from django.views import View
from django.shortcuts import redirect


class KakaoCallBackView(View):
    def get(self, request):
        data = {
            "grant_type" : "authorization_code",
            "client_id" : "f0ad268d23009b5d12e685563fba56f8",
            "redirect_uri" : "http://localhost:8000/oauth/kakao/callback",
            "code" : request.GET["code"],
        }
        kakao_token_api = "https://kauth.kakao.com/oauth/token"
        access_token = requests.post(kakao_token_api, data=data).json()["access_token"]
        kakao_user_api = "https://kapi.kakao.com/v2/user/me"
        headers = {"Authorization" : f"Bearer ${access_token}"}
        user_info = requests.get(kakao_user_api, headers=headers).json()
        return JsonResponse(user_info)


class UserInfo(View):
    def get(self, request):
        data = {
            "name" : "goeon",
            "gender" : "male"
        }
        return JsonResponse(data)
