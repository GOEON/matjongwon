# API backend server

- Django 
- Python 3.9.13
- Poetry 1.2.1

## Usage

```bash
$ poetry shell
$ cd backend
$ python manage.py runserver {8000}
```

- [http://127.0.0.1:8000/](http://127.0.0.1:8000/) 통해 Django 개발 서버 접속
- `{8000}` optional port number

## Test

1. Run Server
  ```bash
  $ python manage.py runserver
  ```
2. Request API
  - http://127.0.0.1:8000/v1/place?query=강남구&page=1&size=10

