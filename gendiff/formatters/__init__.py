from .stylish import format_stylish
from .plain import format_plain
from .json import format_json

FORMATTERS = {
    'stylish': format_stylish,
    'plain': format_plain,
    'json': format_json,
}

def get_formatter(format_name):
    return FORMATTERS[format_name]