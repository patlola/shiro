"""file which interacts with config parser, abstracted the procedure of getting values from config."""
import os
import ConfigParser

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config = ConfigParser.ConfigParser(allow_no_value=True)
config.read(BASE_DIR + '/etc/config/secrets.ini')


def get(section, key):
    """getter function to get values from config directly."""

    return config.get(section, key)


def getboolean(section, key):
    """getter function to get boolean values from config directly."""

    return config.getboolean(section, key)
