"""Manages the configuration file"""
import configparser


CONFIG_PATH = 'config.ini'

config = configparser.ConfigParser()
config.read(CONFIG_PATH)


def config_fallback(value, section, key):
    return config[section][key] if value is None else value
