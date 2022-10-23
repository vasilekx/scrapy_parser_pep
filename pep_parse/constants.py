from pathlib import Path


BASE_DIR = Path(__file__).parent.parent
DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
FILENAME = 'status_summary_{date}.csv'
RESULTS_DIR_NAME = 'results'


PATTERN = r'PEP (?P<number>\d+) *– *(?P<name>.+)'


EXPECTED_STATUS = ['Active', 'Accepted', 'Deferred', 'Final', 'Provisional',
                   'Rejected', 'Superseded', 'Withdrawn', 'Draft']
