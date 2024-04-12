FROM python:3.9.19-alpine

WORKDIR /app

COPY . /app

# RUN pip freeze > requirements.txt

RUN pip install -r requirements.txt

CMD [ "python", "./find_movie.py"]