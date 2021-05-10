FROM python:3.5

RUN pip3 install django

WORKDIR /usr/src/app

COPY . .

CMD ["python", "manage.py", "runserver"]

EXPOSE 8000
