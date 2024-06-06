BOT_NAME = 'pep_parse'
# Список модулей, в которых Scrapy будет искать пауков
SPIDER_MODULES = ['pep_parse.spiders']
# Модуль для создания новых пауков с помощью команды genspider.
NEWSPIDER_MODULE = 'pep_parse.spiders'

ROBOTSTXT_OBEY = True

FEEDS = {
    'results/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    },
}

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300
}
