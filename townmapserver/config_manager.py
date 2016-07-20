"""Manages the configuration file"""
try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import SafeConfigParser as ConfigParser

CONFIG_PATH = 'config.ini'

config = ConfigParser()
config.read(CONFIG_PATH)


def config_fallback(value, section, key):
    return config.get(section, key) if value is None else value
