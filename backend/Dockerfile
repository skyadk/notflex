FROM python:3.7-alpine

RUN /usr/local/bin/python -m pip install --upgrade pip

RUN pip3 install django

RUN pip3 install --upgrade django

WORKDIR /usr/src/app

COPY . .

RUN python manage.py makemigrations

RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

