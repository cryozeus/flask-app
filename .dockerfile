FROM python:3.8.6

RUN pip install pipenv

ADD . /flask-app

WORKDIR /flask-app

RUN pip install --system --skip-lock

RUN pip install gunicorn[event]

EXPOSE 5000

CMD gunicorn --worker-class gevent --workers 8 --bind 0.0.0.0:5000 wsgi:app --max-requests 10000 --timeout 5 --keep-alive 5 --log-level info
