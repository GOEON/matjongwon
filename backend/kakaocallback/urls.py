from django.urls import path
from .views import KakaoCallBackView, UserInfo


urlpatterns = [
    path('oauth/kakao/callback/', KakaoCallBackView.as_view()),
    path('user_info/', UserInfo.as_view()),
]
