from .json import format_json
from .plain import format_plain
from .stylish import format_stylish

FORMATTERS = {
    'stylish': format_stylish,
    'plain': format_plain,
    'json': format_json,
}


def get_formatter(format_name):
    return FORMATTERS[format_name]