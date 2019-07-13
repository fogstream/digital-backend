FROM python:3.7-alpine

# digital_backend - имя проекта (а также имя каталога с исходниками)
# USR_LOCAL_BIN - путь до пользовательских скриптов
# PROJECT_ROOT - путь до каталога внутри контейнера, в который будет
# копироваться приложение
ENV PROJECT_NAME='digital_backend' \
    USR_LOCAL_BIN=/usr/local/bin/  \
    PROJECT_ROOT=/application

# путь до исходников
ENV PYTHONPATH=$PYTHONPATH:$PROJECT_ROOT

# пакеты, которые необходимы для работы в runtime
ENV RUNTIME_PACKAGES \
    libev \
    pcre \
    postgresql-dev

# Пакеты, которые необходимы для установки зависимостей.
# Не останутся в итоговом образе.
ENV BUILD_PACKAGES \
    libev-dev \
    git \
    build-base \
    pcre-dev \
    gcc \
    linux-headers

# Установка пакетов в систему
RUN apk update && \
    apk upgrade && \
    pip install --upgrade pip && \
    pip install wheel pipenv
RUN apk --no-cache add --virtual build-deps $BUILD_PACKAGES && \
    apk --no-cache add $RUNTIME_PACKAGES

# Создание директорий
RUN mkdir $PROJECT_ROOT/ && \
    mkdir $PROJECT_ROOT/run && \
    mkdir $PROJECT_ROOT/wsgi && \
    mkdir $PROJECT_ROOT/logs && \
    mkdir $PROJECT_ROOT/tests && \
    mkdir $PROJECT_ROOT/static && \
    mkdir $PROJECT_ROOT/media

# копирование непосредственно проекта и тестов
ADD ./src $PROJECT_ROOT

RUN ls $PROJECT_ROOT

WORKDIR $PROJECT_ROOT

# Установка зависимостей через pipenv
RUN set -ex && pipenv install --deploy --system --dev
# Удаление ненужных пакетов
RUN apk del build-deps

COPY ./compose/app/start_uwsgi $USR_LOCAL_BIN/

RUN sed -i 's/\r//' $USR_LOCAL_BIN/start_uwsgi \
    && chmod +x $USR_LOCAL_BIN/start_uwsgi

# создание нового пользователя, от имени которого будет запускаться приложение
RUN adduser -D -u 1000 app_user -h $PROJECT_ROOT && \
    chown -hR app_user: $PROJECT_ROOT

USER app_user

EXPOSE 8000

CMD ["start_uwsgi"]