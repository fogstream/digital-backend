# digital_backend

## Переменные окружения

Весь проект настраивается через переменные окружения. Т.к. на проекте используются pipenv, то достаточно указать их в файле `.env`

> Кроме перечисленных ниже переменных требуется указать PYTHONPATH - абсолютный путь до каталога с проектом (не требуется для запуска в Docker)

#### Параметры приложения
|       Ключ        |     Значение     |   По умолчанию   |
|-------------------|------------------|------------------|
|`DJANGO_SETTINGS_MODULE`| Файл с конфигурацией приложения|`digital_backend.settings.prod`|
|`SECRET_KEY`| Секретный ключ. Должен иметь уникальное непредсказуемое значение. |`sosecret`|
|`DEBUG`| Режим отладки |`True`|
|`ALLOWED_HOSTS`| Список разрешенных хостов. Указывается через запятую |`*`|

#### Параметры подключения к БД

По умолчанию в проекте в качестве СУБД используется PostgreSQL.

|       Ключ        |     Значение     |   По умолчанию   |
|-------------------|------------------|------------------|
|`POSTGRES_DB`| Имя БД | `digital_backend` |
|`POSTGRES_USER`| Пользователь БД | `digital_backend` |
|`POSTGRES_PASSWORD`| Пароль пользователя БД | `digital_backend` |
|`POSTGRES_HOST`| Адрес СУБД | `postgres` |
|`POSTGRES_PORT`| Порт СУБД | `5432` |

#### Параметры отправки email
|       Ключ        |     Значение     |   По умолчанию   |
|-------------------|------------------|------------------|
|`EMAIL_HOST`| Хост, используемый для отправки электронной почты ||
|`EMAIL_PORT`| Порт, используемый для отправки электронной почты ||
|`EMAIL_HOST_USER`| Имя пользователя для использования на SMTP-сервере ||
|`EMAIL_HOST_PASSWORD`| Пароль для использования на SMTP-сервере ||
|`EMAIL_USE_TLS`| Использовать ли TLS соединение при общении с SMTP-сервером. ||
|`DEFAULT_FROM_EMAIL`| Адрес электронной почты по умолчанию ||
 

## Используемые технологии

### pipenv

Для создания и управления виртуальным окружением используется `pipenv` 
* [github](https://github.com/pypa/pipenv)  
* [habr.com](https://habr.com/post/413009/)

### Docker

### Docker-compose

### pytest

### django

### pylint, isort

### gitlab-ci