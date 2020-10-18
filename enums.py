from enum import Enum


class GitHubActionsInput(str, Enum):
    DATA_FILE = 'INPUT_DATA_FILE'
    DATA_FORMAT = 'INPUT_DATA_FORMAT'
    OUTPUT_FILE = 'INPUT_OUTPUT_FILE'
    STRICT = 'INPUT_STRICT'
    TEMPLATE = 'INPUT_TEMPLATE'
    VARIABLES = 'INPUT_VARIABLES'

    def __str__(self):
        return self.value
