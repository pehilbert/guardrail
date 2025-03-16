DEBUG = True
PREFIX = "[DEBUG]"

def log(*values):
    print(PREFIX, *values)

def check_value(value_name, value):
    log(value_name, "=", value)