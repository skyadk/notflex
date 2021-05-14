FROM python:3.8

RUN /usr/local/bin/python -m pip install --upgrade pip

RUN /usr/local/bin/python -m pip install --upgrade pillow

RUN pip3 install --upgrade django

RUN pip install drf_yasg

WORKDIR /usr/src/app

COPY . .

RUN python manage.py makemigrations

RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
