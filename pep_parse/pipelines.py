import csv
import datetime as dt
from collections import defaultdict

from pep_parse.constants import (BASE_DIR, DATETIME_FORMAT, FILENAME,
                                 RESULTS_DIR_NAME)


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
        with open(
            self.result_dir / FILENAME.format(
                date=dt.datetime.now().strftime(DATETIME_FORMAT)
            ),
            mode='w',
            encoding='utf-8'
        ) as csvfile:
            csv.writer(
                csvfile, dialect=csv.unix_dialect, quoting=csv.QUOTE_MINIMAL
            ).writerows(
                [
                    ('Статус', 'Количество'),
                    *self.count_statuses.items(),
                    ('Total', sum(self.count_statuses.values()))
                ]
            )
