import csv
import datetime
from collections import defaultdict

from pep_parse.constants import BASE_DIR


class PepParsePipeline:

    def open_spider(self, spider):
        self.status_dict = defaultdict(int)

        date_now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        filename = f'status_summary_{date_now}.csv'

        downloads_dir = BASE_DIR / 'results'
        downloads_dir.mkdir(exist_ok=True)
        self.status_summary_path = downloads_dir / filename

    def process_item(self, item, spider):
        self.status_dict[item['status']] += 1
        return item

    def close_spider(self, spider):

        total = sum(self.status_dict.values())

        with open(f'{self.status_summary_path}', 'w', newline=''
                  ) as csvfile:
            fieldnames = ['Статус', 'Количество']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for key, value in self.status_dict.items():
                writer.writerow({'Статус': key, 'Количество': value})

            writer.writerow({'Статус': 'Total', 'Количество': total})
