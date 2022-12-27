# Проект асинхронного парсера PEP на Scrapy

## Описание
Парсер документов PEP, основанный на фреймворке Scrapy. Парсер создает два файла отчета. Файл, содержащий список PEP с номером документа, заголовком и статусом, а также файл сводной статистики по количеству документов в различных статусах.

### Функции парсера:
* Сброр всех PEP (номер, название и статус);
* Подсчёт количества статусов документов;
* Сохранение результатов работы парсинга в csv-формате.

## Применяемые технологи

[![Python](https://img.shields.io/badge/Python-3.9-blue?style=flat-square&logo=Python&logoColor=3776AB&labelColor=d0d0d0)](https://www.python.org/)
[![Scrapy](https://img.shields.io/badge/Scrapy-2.5.1-blue?style=flat-square&logoColor=3776AB&labelColor=d0d0d0)](https://scrapy.org/)

---

## Порядок действия для запуска парсера

Клонировать репозиторий и перейти в папку в проектом:

```bash
git clone https://github.com/vasilekx/scrapy_parser_pep.git
```

```bash
cd cat_charity_fund
```

Создать и активировать виртуальное окружение:

```bash
python3 -m venv venv
```

* Если у вас Linux/MacOS

    ```bash
    source venv/bin/activate
    ```

* Если у вас windows

    ```bash
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```bash
python3 -m pip install --upgrade pip
```

```bash
pip install -r requirements.txt
```

Запуск парсера:

```bash
scrapy crawl pep 
```

### Директория для файлов с результатами парсинга
* _results_ - для результатов парсинга;

### Примеры работы парсинга:

Содержимое файла **pep_2022-10-23T00-56-51.csv**:

|number    |name|status    |
|----------|----|----------|
|1         |PEP Purpose and Guidelines|Active    |
|243       |Module Repository Upload Mechanism|Withdrawn |
|247       |API for Cryptographic Hash Functions|Final     |
|248       |Python Database API Specification v1.0|Final     |
|249       |Python Database API Specification v2.0|Final     |
|246       |Object Adaptation|Rejected  |
|244       |The |Rejected  |
|245       |Python Interface Syntax|Rejected  |
|242       |Numeric Kinds|Rejected  |
|237       |Unifying Long Integers and Integers|Final     |
|240       |Adding a Rational Literal to Python|Rejected  |
|239       |Adding a Rational Type to Python|Rejected  |
|238       |Changing the Division Operator|Final     |
|241       |Metadata for Python Software Packages|Superseded|
|235       |Import on Case-Insensitive Platforms|Final     |
|236       |Back to the __future__|Final     |
|8103      |2022 Term steering council election|Active    |
|...       |...|...|


Содержимое файла **status_summary_2022-10-23_03-57-14.csv**:

|Статус    |Количество|
|----------|----------|
|Superseded|19        |
|Final     |261       |
|Active    |35        |
|Withdrawn |54        |
|Rejected  |119       |
|Deferred  |36        |
|Accepted  |41        |
|Draft     |32        |
|Total     |597       |


### Автор
[Владислав Василенко](https://github.com/vasilekx)
