"""Manages the configuration file"""
import configparser


CONFIG_PATH = 'config.ini'

config = configparser.ConfigParser()
config.read(CONFIG_PATH)
