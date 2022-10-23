from pathlib import Path


BASE_DIR = Path(__file__).parent.parent
DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
FILENAME = 'status_summary_{date}.csv'
RESULTS_DIR_NAME = 'results'


EN_DASH = '\u2013'  # –
STATUS_PEP_NOT_FOUND = (
    'Несовпадающие статусы: '
    '{pep_link} '
    'Статус в карточке: {card_status}'
)


EXPECTED_STATUS = ['Active', 'Accepted', 'Deferred', 'Final', 'Provisional',
                   'Rejected', 'Superseded', 'Withdrawn', 'Draft']
