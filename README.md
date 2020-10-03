# movie-bag

python-flask-mongodb の学習プロジェクト。

- ref: https://dev.to/paurakhsharma/flask-rest-api-part-0-setup-basic-crud-api-4650

## 開発環境構築

``` bash
pipenv --python 3.8

pipenv install flask flask-mongoengine flask-restful flask-bcrypt flask-jwt-extended flask-mail
pipenv install --dev autopep8 flake8
```

起動。

``` bash
export ENV_FILE_LOCATION=./.env
python run.py
```

ダミーのメールサーバーを起動。

``` bash
python -m smtpd -n -c DebuggingServer localhost:1025
```

テストの実行。

``` bash
export ENV_FILE_LOCATION=./.env.test
python -m unittest tests/test_signup.py
```

## flask-restful

``` python
class MovieApi(Resource):
    def put(self, id):
        body = request.get_json()
        Movie.objects.get(id=id).update(**body)
        return '', 200

    def delete(self, id):
        movie = Movie.objects.get(id=id).delete()
        return '', 200

    def get(self, id):
        movies = Movie.objects.get(id=id).to_json()
        return Response(movies, mimetype="application/json", status=200)
```

HTTP メソッドとクラスのメソッド名が紐づくようになる。
