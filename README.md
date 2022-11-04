# matjongwon
맛집 종합원

## Scrapers

이 브랜치는 네이버, 카카오, 트립어드바이저 그리고 구글 맵(아직 없음) 등의 데이터를 크롤링 하기 위해서 생성하였다.
크롤링한 데이터는 [data](https://github.com/ComTalk/matjongwon/tree/scrapers/data)에 json 파일로 저장되며,
json format 은 [여기](https://github.com/ComTalk/matjongwon/wiki/json-format) 에서 확인 가능하다.

### Prerequisite

* Python 3.7+
* Selenium 3.141.0
* Webdriver_manager 3.8.3
* urllib3 1.26.9
* requests 2.28.0