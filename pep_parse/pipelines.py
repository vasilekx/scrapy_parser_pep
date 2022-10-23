import csv
import datetime as dt
from collections import defaultdict

from scrapy.exceptions import DropItem

from pep_parse.constants import (BASE_DIR, DATETIME_FORMAT, FILENAME,
                                 RESULTS_DIR_NAME)


# BASE_DIR = Path(__file__).parent.parent
# DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
# FILENAME = 'status_summary_{date}.csv'


class PepParsePipeline:
    def __init__(self):
        self.result_dir = BASE_DIR / RESULTS_DIR_NAME
        self.result_dir.mkdir(exist_ok=True)

    def open_spider(self, spider):
        self.count_statuses = defaultdict(int)

    def process_item(self, item, spider):
        self.count_statuses[item['status']] += 1
        return item

    def close_spider(self, spider):
        # filename = format(dt.datetime.now().strftime(DATETIME_FORMAT))
        with open(
                self.result_dir / FILENAME.format(
                    date=dt.datetime.now().strftime(DATETIME_FORMAT)
                ),
                mode='w',
                encoding='utf-8'
        ) as csvfile:
            # Записываем строки в csv-файл. Колонки разделяются запятой, без пробелов.
            # csvfile.write('Статус,Количество\n')
            # Здесь цикл с записью данных в файл.
            # csvfile.write(f'Total,{total}\n')

            writer = csv.writer(
                csvfile,
                # dialect=csv.unix_dialect,
                quoting=csv.QUOTE_MINIMAL
            )
            writer.writerows(
                [
                    ('Статус', 'Количество'),
                    *self.count_statuses.items(),
                    ('Total', sum(self.count_statuses.values()))
                ]
            )

