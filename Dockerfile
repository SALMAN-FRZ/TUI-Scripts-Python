FROM python:3.7.3-alpine3.8

WORKDIR /usr/src/app

COPY . .

CMD [ "python", "./pip_cache_directories.py" ]
