from enum import Enum


class GitHubActionsInput(Enum):
    DATA_FILE = 'INPUT_DATA_FILE'
    TEMPLATE = 'INPUT_TEMPLATE'
    STRICT = 'INPUT_STRICT'
    OUTPUT_FILE = 'INPUT_OUTPUT_FILE'
    VARIABLES = 'INPUT_VARIABLES'

    def __str__(self, *args, **kwargs):
        return str(self.value)

