# matjongwon
맛집 종합원

## Scraping Trip Advisor

이 브랜치는 Trip Advisor 를 파이썬의 selenium 모듈을 통해 크롤링 하기 위해서 생성하였다.
간단한 설명은 scraper.py 코드에 적혀있다.
크롤링한 데이터는 reviews.csv 에 저장되며, 저장되는 데이터는 [이름, 위치, 평가, 사진] 이다.

### Prerequisite

* Python 3.7+
* Selenium 3.141.0
* Webdriver_manager 3.8.3