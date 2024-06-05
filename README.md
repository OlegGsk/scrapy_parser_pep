# scrapy_parser_pep


Этот проект использует Scrapy, фреймворк для веб-скрапинга на Python. Он сканирует главную страницу Python PEP, извлекает ссылки на страницы отдельных PEP и парсит соответствующие данные о статусе, названии и номере. затем генерирует 2 файла CSV для удобной визуализации и анализа.

## Запуск проекта
* Клонируйте репозиторий и перейдите в него в командной строке:
`git clone git@github.com:OlegGsk/scrapy_parser_pep.git`
`cd scrapy_parser_pep`

* Создайте и активируйте виртуальное окружение:
`python3 -m venv venv`
`source venv/bin/activate`

* Установите зависимости из файла requirements.txt:
`pip install -r requirements.txt`

* Запустите парсинг:
`scrapy crawl pep`